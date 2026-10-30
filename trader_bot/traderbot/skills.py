"""Runs the trader-* skill tools exactly as Claude would: one subprocess each,
from the project folder, so every step reads and writes the same trader/ files
the skills use. The bot adds no trading logic of its own here."""

import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.normpath(os.path.join(HERE, "..", "..", "skills"))

TOOLS = {
    "scan": ("trader-scanner", "scan.py"),
    "news": ("trader-news", "news.py"),
    "entry": ("trader-entry", "entry.py"),
    "exit": ("trader-exit", "exit.py"),
    "timemachine": ("trader-timemachine", "timemachine.py"),
    "size": ("trader-budget", "size.py"),
    "risk": ("trader-risk", "check.py"),
    "ticket": ("trader-broker", "ticket.py"),
    "alerts": ("trader-alerts", "alerts.py"),
}
# tools whose first argument is a subcommand; extra_args are keyed by it ("" for the rest)
SUBCOMMANDS = {"scan", "entry", "exit", "timemachine", "ticket", "alerts"}


class Result(object):
    def __init__(self, tool, args, code, out, err):
        self.tool, self.args, self.code, self.out, self.err = tool, args, code, out, err

    @property
    def ok(self):
        return self.code == 0

    def json(self):
        return json.loads(self.out)

    def text(self):
        return (self.out + ("\n" + self.err if self.err.strip() else "")).strip()


class Skills(object):
    """workdir is the project folder that holds trader/. extra_args adds flags per
    tool (for example --offline for a replay); now pins every tool's clock."""

    def __init__(self, workdir, skills_dir=SKILLS_DIR, extra_args=None, now=None, timeout=900, python=None):
        self.workdir = os.path.abspath(workdir)
        self.skills_dir = skills_dir
        self.extra_args = extra_args or {}
        self.now = now
        self.timeout = timeout
        self.python = python or sys.executable

    def path(self, rel):
        return os.path.join(self.workdir, rel)

    def run(self, tool, *args, **kw):
        folder, script = TOOLS[tool]
        argv = [str(a) for a in args]
        sub = argv[0] if tool in SUBCOMMANDS and argv else ""
        argv += [str(a) for a in self.extra_args.get(tool, {}).get(sub, [])]
        if kw.get("now", True) and self.now:
            argv += ["--now", self.now]
        cmd = [self.python, os.path.join(self.skills_dir, folder, script)] + argv
        try:
            p = subprocess.run(cmd, cwd=self.workdir, capture_output=True, text=True, timeout=self.timeout)
        except subprocess.TimeoutExpired:
            return Result(tool, argv, 124, "", "%s timed out after %ds" % (script, self.timeout))
        return Result(tool, argv, p.returncode, p.stdout, p.stderr)

    def read(self, rel, default=None):
        try:
            with open(self.path(rel), encoding="utf-8") as fh:
                return json.load(fh)
        except (OSError, ValueError):
            return default
