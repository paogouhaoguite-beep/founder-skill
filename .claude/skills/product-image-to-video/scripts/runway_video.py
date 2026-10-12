#!/usr/bin/env python3
"""Submit one Runway image-to-video request, resume its status, or save its output.

Python 3.10+, standard library only. Submission defaults to offline validation.
The --execute flag is required for a billable request. No automatic POST retries.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener, urlopen
from urllib.parse import urlparse

API = "https://api.dev.runwayml.com/v1"
VERSION = "2024-11-06"


class HTTPSRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, url):
        if urlparse(url).scheme != "https":
            raise ValueError("Refusing output redirect away from HTTPS")
        return super().redirect_request(request, response, code, message, headers, url)


def read_json(path):
    value = json.loads(Path(path).read_text())
    if not isinstance(value, dict):
        raise ValueError("Expected a JSON object")
    return value


def save_receipt(path, value):
    path = Path(path)
    with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False) as file:
        json.dump(value, file, indent=2)
        file.write("\n")
        temporary = Path(file.name)
    temporary.replace(path)


def api_request(method, path, payload=None):
    key = os.environ.get("RUNWAYML_API_SECRET")
    if not key:
        raise ValueError("Set RUNWAYML_API_SECRET in the environment; never put it in request JSON")
    headers = {"Authorization": "Bearer " + key, "X-Runway-Version": VERSION,
               "Content-Type": "application/json"}
    data = json.dumps(payload).encode() if payload is not None else None
    request = Request(API + path, data=data, headers=headers, method=method)
    try:
        with urlopen(request, timeout=45) as response:
            return json.load(response)
    except HTTPError as error:
        raise RuntimeError(f"Provider HTTP {error.code}; inspect account/request before retrying") from None
    except (URLError, TimeoutError):
        raise RuntimeError("Provider connection failed; submission may have been accepted") from None


def validate_request(payload):
    for field in ("model", "promptText", "ratio"):
        if not isinstance(payload.get(field), str) or not payload[field].strip():
            raise ValueError(f"Missing nonempty {field}")
    if not re.fullmatch(r"[1-9]\d*:[1-9]\d*", payload["ratio"]):
        raise ValueError("ratio must use WIDTH:HEIGHT; check dimensions supported by your model")
    duration = payload.get("duration")
    if type(duration) is not int or duration <= 0:
        raise ValueError("duration must be a positive integer; check model-specific limits")
    image = payload.get("promptImage")
    if not isinstance(image, str) or not (image.startswith("https://") or image.startswith("data:image/")):
        raise ValueError("This helper accepts one promptImage: an authorized HTTPS URL or image data URI")
    return payload


def submit(args):
    payload = validate_request(read_json(args.request))
    receipt = {"state": "validated_offline", "model": payload["model"],
               "duration": payload["duration"], "ratio": payload["ratio"],
               "request_sha256": hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()}
    if not args.execute:
        print(json.dumps(receipt))
        return
    if not args.job:
        raise ValueError("--job is required with --execute")
    if not os.environ.get("RUNWAYML_API_SECRET"):
        raise ValueError("RUNWAYML_API_SECRET is missing; nothing submitted")
    job = Path(args.job)
    job.parent.mkdir(parents=True, exist_ok=True)
    receipt["state"] = "submission_unknown"
    # An existing receipt prevents accidental repeated billable submissions.
    with job.open("x") as file:
        os.chmod(job, 0o600)
        json.dump(receipt, file, indent=2)
    response = api_request("POST", "/image_to_video", payload)
    task_id = response.get("id")
    if not isinstance(task_id, str) or not re.fullmatch(r"[A-Za-z0-9-]+", task_id):
        raise RuntimeError("No usable task ID returned; preserve receipt and reconcile before resubmitting")
    receipt.update(id=task_id, state="submitted")
    save_receipt(job, receipt)
    print(json.dumps({"id": task_id, "state": "submitted", "receipt": str(job)}))


def status(args):
    receipt = read_json(args.job)
    task_id = receipt.get("id", "")
    if not isinstance(task_id, str) or not re.fullmatch(r"[A-Za-z0-9-]+", task_id):
        raise ValueError("No task ID; reconcile the unknown submission in the provider account")
    task = api_request("GET", "/tasks/" + task_id)
    if task.get("id") != task_id:
        raise ValueError("Provider task ID does not match receipt")
    receipt.update(state=task.get("status", "unknown"), output=task.get("output", []))
    save_receipt(args.job, receipt)
    print(json.dumps({"id": task_id, "state": receipt["state"], "output_count": len(receipt["output"])}))


def download(args):
    receipt = read_json(args.job)
    if receipt.get("state") != "SUCCEEDED":
        raise ValueError("Only a SUCCEEDED task may be downloaded; run status first")
    outputs = receipt.get("output", [])
    if not isinstance(outputs, list) or not 0 <= args.index < len(outputs):
        raise ValueError("Output index is missing or out of range")
    url = outputs[args.index]
    if not isinstance(url, str) or urlparse(url).scheme != "https":
        raise ValueError("Expected provider HTTPS output URL")
    target = Path(args.output)
    if target.exists():
        raise ValueError("Output already exists; choose a new path")
    target.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=target.name + ".", suffix=".part", dir=target.parent)
    partial = Path(temporary)
    size = 0
    digest = hashlib.sha256()
    # No API authorization header is forwarded to the signed output URL.
    try:
        with os.fdopen(descriptor, "wb") as file:
            with build_opener(HTTPSRedirect()).open(url, timeout=60) as response:
                length = response.headers.get("Content-Length")
                while chunk := response.read(1024 * 1024):
                    file.write(chunk)
                    digest.update(chunk)
                    size += len(chunk)
        if not size:
            raise ValueError("Empty download; not a video delivery")
        if length is not None and size != int(length):
            raise ValueError("Truncated download; no final file saved, retry download")
        # Atomic no-clobber promotion: another process may have created the target.
        os.link(partial, target)
    finally:
        partial.unlink(missing_ok=True)
    print(json.dumps({"file": str(target), "bytes": size, "sha256": digest.hexdigest(),
                      "visual_review": "not_performed", "playback_review": "not_performed"}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("submit")
    create.add_argument("--request", required=True)
    create.add_argument("--job")
    create.add_argument("--execute", action="store_true")
    inspect = commands.add_parser("status")
    inspect.add_argument("--job", required=True)
    fetch = commands.add_parser("download")
    fetch.add_argument("--job", required=True)
    fetch.add_argument("--output", required=True)
    fetch.add_argument("--index", type=int, default=0)
    args = parser.parse_args()
    try:
        {"submit": submit, "status": status, "download": download}[args.command](args)
    except (ValueError, OSError, RuntimeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
