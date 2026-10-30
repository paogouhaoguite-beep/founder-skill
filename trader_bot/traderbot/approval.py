"""Your yes, one order at a time (or, with "auto_approve": true, the bot's).

The bot finds, plans, replays, sizes and risk-checks a trade on its own, then
stops here. The reply goes word for word to trader-broker (ticket.py approve),
which accepts only an explicit yes for THIS order: not "ok", not "yes to all",
not a yes that names another stock or amount. No answer before the timeout is
a no, because a breakout signal goes stale."""

import select
import sys


class TerminalApprover(object):
    def __init__(self, timeout=120, stream_in=None, stream_out=None):
        self.timeout = timeout
        self.stream_in = stream_in or sys.stdin
        self.stream_out = stream_out or sys.stdout

    def ask(self, ticket_text):
        out = self.stream_out
        out.write("\n" + ticket_text.rstrip() + "\n")
        out.write("Type yes to place this one order (anything else, or %ds of silence, is a no): "
                  % self.timeout)
        out.flush()
        try:
            ready, _, _ = select.select([self.stream_in], [], [], self.timeout)
        except (ValueError, OSError):  # stdin is not selectable (Windows, a pipe that closed)
            ready = [self.stream_in]
        if not ready:
            out.write("\nNo answer in %ds: declined.\n" % self.timeout)
            return None
        line = self.stream_in.readline()
        return line.strip() if line else None


class AutoApprover(object):
    """"auto_approve": true in trader/bot.json: every ticket that reached this
    point (trader-risk PASS) gets a yes without asking. The ticket is still
    printed and the yes still goes through ticket.py approve, so trader/state/
    broker.json says who said yes."""

    REPLY = "yes (auto-approved by traderbot)"

    def __init__(self, stream_out=None):
        self.stream_out = stream_out or sys.stdout

    def ask(self, ticket_text):
        self.stream_out.write("\n" + ticket_text.rstrip() + "\nAuto-approved (auto_approve is on).\n")
        self.stream_out.flush()
        return self.REPLY


class ScriptedApprover(object):
    """For tests and dry runs: replies from a list, then None (a no)."""

    def __init__(self, replies=()):
        self.replies = list(replies)
        self.asked = []

    def ask(self, ticket_text):
        self.asked.append(ticket_text)
        return self.replies.pop(0) if self.replies else None
