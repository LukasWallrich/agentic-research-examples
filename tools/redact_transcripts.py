#!/usr/bin/env python3
"""Export the local session records of each example run into <folder>/run_records/.

The records are copied with these redactions:

- all email addresses except placeholders and no-reply
  addresses (see KEPT_EMAIL_*)                                 -> [email redacted]
- the author's ORCID iD (matched by SHA-256, see ORCID_SHA256) -> [ORCID redacted]
- the home directory /Users/<user> (also JSON-escaped, URL-encoded, relative and in
  Claude Code's encoded form -Users-<user>-)                  -> ~  (encoded form: -~-)
- secret values from ~/.claude/api_keys.env, any printed fragment of a key-like
  value (a token that is a prefix or suffix of 6 or more characters, not counting
  a public type prefix such as sk-or-v1-; see key_fragments),
  and common key formats (sk-..., ghp_..., AIza..., AKIA..., xox?-..., JWTs,
  Bearer tokens, NAME_API_KEY=value, private-key blocks)     -> [secret redacted]
- names of local project folders that are not among the examples -> [other project]

Stored tool outputs (Claude Code `tool-results/` files: fetched web pages, article texts,
search results, PDFs, page images) are not exported; each run_records/README.md lists them.
Everything else is kept, including the standing instructions the sessions loaded.

Sources (all opened read-only):
- Claude Code transcripts in ~/.claude/projects/
- Codex session files in ~/.codex/sessions/2026/09/
- OpenCode sessions in ~/.local/share/opencode/opencode.db
- T3 Code threads in ~/.t3/userdata/state.sqlite

Usage (from the repository root):
    python3 tools/redact_transcripts.py            # export, then verify
    python3 tools/redact_transcripts.py --verify   # verify existing run_records only

Each run deletes and rewrites <folder>/run_records/ for the example folders in EXAMPLES.
The same inputs give byte-identical outputs. The script writes nothing outside
those run_records folders.
"""

import argparse
import datetime as dt
import gzip
import hashlib
import io
import json
import re
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HOME = Path.home()
USER = HOME.name

CLAUDE_PROJECTS = HOME / ".claude" / "projects"
CODEX_SESSIONS = HOME / ".codex" / "sessions" / "2026" / "09"
OPENCODE_DB = HOME / ".local" / "share" / "opencode" / "opencode.db"
T3_DB = HOME / ".t3" / "userdata" / "state.sqlite"
API_KEYS_ENV = HOME / ".claude" / "api_keys.env"

MAX_PLAIN_BYTES = 50 * 1024 * 1024  # larger files are written as .gz
TEXT_SUFFIXES = {".jsonl", ".json", ".txt", ".md", ".log"}

# Run windows (UTC) bound every match, so later sessions in the same folders are not picked up.
# `marker` is a phrase from the manuscript title, used to attribute headless Claude Code
# calls that ran in /private/tmp.
EXAMPLES = {
    "anchoring-extremity-opaq": {
        "source": HOME / "Documents" / "Coding" / "ai-jdm-paper",
        "window": ("2026-09-27T19:40:00Z", "2026-09-28T03:30:00Z"),
        "marker": "anchor extremity",
        "notes": [
            "The 36 headless Claude Code calls in `claude/private-tmp/` are round-3 coarse-review calls. "
            "They ran in /private/tmp while no other example run was active, and each contains the manuscript title.",
            "Codex review calls that ran in /tmp are included because the example repository cites their session ids "
            "(`reviews/`) or because their prompt appears in the lead transcript (a one-line availability check).",
        ],
    },
    "selective-feedback-simulation": {
        "source": HOME / "Documents" / "Coding" / "ai-jdm-paper3",
        "window": ("2026-09-28T10:10:00Z", "2026-09-28T11:15:00Z"),
        "marker": "when selective feedback helps and harms",
        "notes": [
            "Thread `af0cf5ab-83e0-41b7-a442-e230777837e7` was started 28 seconds before the run thread with an "
            "earlier wording of the brief. It has no agent response.",
            "The Claude Code reviewer calls cite session ids in `reviews/manuscript/claude_r*.json`. These sessions "
            "are not stored under ~/.claude/projects, so no Claude transcript is exported for this example.",
        ],
    },
    "confidence-weighting-crowds": {
        "source": HOME / "Documents" / "Coding" / "ai-jdm-paper4",
        "window": ("2026-09-28T13:15:00Z", "2026-09-28T19:55:00Z"),
        "marker": "when does weighting by confidence help the crowd",
        "notes": [
            "Thread `3c67298c-645f-4940-9d90-e484f27d70a4` (\"Diagnose OpenCode CLI Failure\", Codex) is a setup "
            "thread. The user asked why the OpenCode CLI failed in this folder, 1 h 52 min before the run thread "
            "started. Its Codex session also records a thread-settings entry on 29 September 2026.",
            "An empty OpenCode session in this folder (no messages, created 13:23 UTC) is not exported.",
        ],
    },
}

COMMON_NOTES = [
    "Gemini (agy) review calls are not exported: their local records are not among the sources of this tool. "
    "Their prompts and answers are in the example's `reviews/` folder.",
    "T3 Code tool-activity rows (`projection_thread_activities`) and T3 Code checkpoint refs in the source "
    "repository (`refs/t3/checkpoints/...`) are not exported. They repeat what the agent transcripts record.",
]

# SHA-256 of the author's ORCID iD without hyphens. A hash keeps the identifier out of this file.
ORCID_SHA256 = {"2188531a3c3d7589af2064ebf763ca9ca83fad7d1f1716d77c9b59729252a786"}

REDACTED = {"email": "[email redacted]", "orcid": "[ORCID redacted]", "secret": "[secret redacted]",
            "other_project": "[other project]"}
COUNT_KEYS = ("email_author", "email_other", "orcid", "home_path", "secret", "other_project")

# Placeholder and no-reply addresses carry no personal data and are kept.
KEPT_EMAIL_DOMAINS = ("example.org", "example.com", "example.net", "example.invalid",
                      "users.noreply.github.com")
KEPT_EMAIL_ADDRESSES = {"noreply@anthropic.com", "git@github.com"}

# Sibling project folders are named like the example sources (<stem><number>).
# Those that are not exported here are replaced.
PROJECT_STEM = "ai-jdm-paper"
OTHER_PROJECT_RE = re.compile(re.escape(PROJECT_STEM) + r"\d+")
FRAGMENT_MIN = 6
TOKEN_RE = re.compile(r"[A-Za-z0-9_\-]{%d,}" % FRAGMENT_MIN)

# A match may start after a JSON escape such as \n; the escape itself is never consumed.
_START = r"(?:(?<![A-Za-z0-9_.%+\-\\])|(?<=\\[nrt])|(?<=\\u[0-9a-fA-F]{4}))"
EMAIL_RE = re.compile(_START + r"(?P<addr>[A-Za-z0-9_.%+\-]+(?:@|%40)[A-Za-z0-9.\-]+\.[A-Za-z]{2,})")
ORCID_RE = re.compile(r"\d{4}-?\d{4}-?\d{4}-?\d{3}[\dX]")
# In JSONL a key block sits inside one line (newlines are escaped); in plain text it spans lines.
KEY_BLOCK_LINE = re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----[^\n]*?-----END [A-Z ]*PRIVATE KEY-----")
KEY_BLOCK_MULTILINE = re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----")
SECRET_PATTERNS = [
    re.compile(_START + r"sk-[A-Za-z0-9_\-]{20,}"),
    re.compile(_START + r"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(_START + r"github_pat_[A-Za-z0-9_]{30,}"),
    re.compile(_START + r"AIza[0-9A-Za-z_\-]{35}"),
    re.compile(_START + r"AKIA[0-9A-Z]{16}"),
    re.compile(_START + r"xox[abpsr]-[A-Za-z0-9\-]{10,}"),
    re.compile(_START + r"eyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}"),
]
# Keep the prefix (group 1), replace the value (group 2).
SECRET_PREFIXED = [
    re.compile(r"(?i)(bearer\s+)([A-Za-z0-9._~+/=\-]{20,})"),
    re.compile(r"(?i)(?:(?<![A-Za-z0-9_])|(?<=\\[nrt]))([A-Z0-9_]*(?:API_KEYS?|APIKEY|_TOKEN|_SECRET|PASSWORD)\\?[\"']?[ \t]*[=:][ \t]*\\?[\"']?)"
               r"([A-Za-z0-9_\-.]{16,})(?![A-Za-z0-9_\-.(])"),  # not a function call
]


def load_secret_values():
    """Values from api_keys.env (comma-separated lists split). Never printed or logged."""
    values = set()
    if not API_KEYS_ENV.exists():
        return values
    for line in API_KEYS_ENV.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        value = line.split("=", 1)[1].strip().strip("'\"")
        for part in value.split(","):
            part = part.strip()
            if len(part) >= 8:
                values.add(part)
    return values


KNOWN_KEY_PREFIX = re.compile(r"sk-(?:or-v1-|proj-|ant-[a-z0-9]+-)?|gh[pousr]_|github_pat_|AIza|AKIA|xox[abpsr]-")


def key_fragments(secret_values):
    """Prefixes and suffixes of each key-like value (16+ characters with a digit).

    A public type prefix such as sk-or-v1- does not count towards the FRAGMENT_MIN
    characters, so text that only names the key type is kept. Short or word-like
    values (for example a bucket name) are redacted only in full.
    """
    frags = set()
    for v in secret_values:
        if len(v) < 16 or not re.search(r"\d", v):
            continue
        m = KNOWN_KEY_PREFIX.match(v)
        head = m.group(0) if m else ""
        body = v[len(head):]
        for k in range(FRAGMENT_MIN, len(body)):
            frags.update((body[:k], head + body[:k], body[-k:]))
    return frags


def replace_fragments(text, fragments, counts=None):
    """Replace whole tokens that are key fragments. A token may follow a JSON escape (\\n, \\t, \\r)."""
    out, pos = [], 0
    for m in TOKEN_RE.finditer(text):
        tok, start = m.group(0), m.start()
        if start > 0 and text[start - 1] == "\\" and tok[0] in "nrt" and tok[1:] in fragments:
            tok, start = tok[1:], start + 1
        elif tok not in fragments:
            continue
        out.append(text[pos:start])
        out.append(REDACTED["secret"])
        pos = m.end()
        if counts is not None:
            counts["secret"] += 1
    out.append(text[pos:])
    return "".join(out)


def is_kept_email(addr):
    addr = addr.lower().replace("%40", "@")
    return addr in KEPT_EMAIL_ADDRESSES or addr.split("@")[-1].endswith(KEPT_EMAIL_DOMAINS)


class Redactor:
    def __init__(self, secret_values):
        self.secret_values = sorted(secret_values, key=len, reverse=True)
        self.fragments = key_fragments(secret_values)
        self.examples = {cfg["source"].name for cfg in EXAMPLES.values()}
        home = str(HOME)
        self.home_forms = [
            (home.replace("/", "\\/"), "~"),
            (home.replace("/", "%2F"), "~"),
            (home, "~"),
            (home.lstrip("/") + "/", "~/"),  # relative form, e.g. OpenCode tool titles
            (home.replace("/", "-") + "-", "-~-"),
        ]

    def redact(self, text, counts, multiline=False):
        for value in self.secret_values:
            n = text.count(value)
            if n:
                counts["secret"] += n
                text = text.replace(value, REDACTED["secret"])
        for pat in [KEY_BLOCK_MULTILINE if multiline else KEY_BLOCK_LINE] + SECRET_PATTERNS:
            text, n = pat.subn(REDACTED["secret"], text)
            counts["secret"] += n
        for pat in SECRET_PREFIXED:
            text, n = pat.subn(lambda m: m.group(1) + REDACTED["secret"], text)
            counts["secret"] += n
        text = replace_fragments(text, self.fragments, counts)

        def email(m):
            addr = m.group("addr")
            if is_kept_email(addr):
                return m.group(0)
            counts["email_author" if "wallrich" in addr.lower() else "email_other"] += 1
            return REDACTED["email"]

        text = EMAIL_RE.sub(email, text)

        def orcid(m):
            digits = m.group(0).replace("-", "")
            if hashlib.sha256(digits.encode()).hexdigest() in ORCID_SHA256:
                counts["orcid"] += 1
                return REDACTED["orcid"]
            return m.group(0)

        text = ORCID_RE.sub(orcid, text)
        for form, repl in self.home_forms:
            n = text.count(form)
            if n:
                counts["home_path"] += n
                text = text.replace(form, repl)

        def other_project(m):
            if m.group(0) in self.examples:
                return m.group(0)
            counts["other_project"] += 1
            return REDACTED["other_project"]

        return OTHER_PROJECT_RE.sub(other_project, text)


# ---------------------------------------------------------------- helpers

def parse_ts(value):
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return dt.datetime.fromtimestamp(value / 1000, dt.timezone.utc)
    try:
        return dt.datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def fmt_ts(value):
    return value.strftime("%Y-%m-%d %H:%M:%S") + " UTC" if value else ""


def in_window(ts, window):
    lo, hi = (parse_ts(w) for w in window)
    return ts is not None and lo <= ts <= hi


def tilde(path):
    s = str(path)
    return "~" + s[len(str(HOME)):] if s.startswith(str(HOME)) else s


def claude_encode(path):
    return re.sub(r"[^A-Za-z0-9]", "-", str(path))


def jsonl_summary(path):
    """First/last timestamp and model names found in a JSONL file."""
    first = last = None
    models = set()
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            ts = parse_ts(obj.get("timestamp"))
            if ts:
                first = ts if first is None or ts < first else first
                last = ts if last is None or ts > last else last
            msg = obj.get("message")
            if isinstance(msg, dict) and msg.get("model") and msg["model"] != "<synthetic>":
                models.add(msg["model"])
            if obj.get("type") == "turn_context":
                m = obj.get("payload", {}).get("model")
                if m:
                    models.add(m)
    return first, last, sorted(models)


def cited_ids(source):
    """UUID-like strings in tracked files at HEAD of the source repository (read-only git grep)."""
    out = subprocess.run(
        ["git", "-C", str(source), "grep", "-I", "-h", "-o", "-E",
         r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", "HEAD"],
        capture_output=True, text=True)
    return {line.split(":", 1)[-1] for line in out.stdout.split()}


def ro_connect(path):
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


# ---------------------------------------------------------------- discovery

def discover_claude(name, cfg):
    source, window = cfg["source"], cfg["window"]
    enc = claude_encode(source)
    items, lead_texts = [], []
    dirs = [d for d in sorted(CLAUDE_PROJECTS.glob(enc + "*"))
            if d.is_dir() and (d.name == enc or d.name.startswith(enc + "-"))]
    for d in dirs:
        label = "project-root" if d.name == enc else "project" + d.name[len(enc):]
        for f in sorted(d.glob("*.jsonl")):
            first, last, models = jsonl_summary(f)
            if not in_window(first, window):
                continue
            items.append(claude_item(f, d, label, first, last, models,
                                     "Claude Code project folder of the example path (or a subfolder); "
                                     "session starts in the run window"))
            items.extend(claude_companions(f, d, label))
            if d.name == enc:
                lead_texts.append(f.read_text(encoding="utf-8", errors="replace"))
                lead_texts.extend(p.read_text(encoding="utf-8", errors="replace")
                                  for p in sorted((d / f.stem / "subagents").glob("*.jsonl")))
    tmp = CLAUDE_PROJECTS / "-private-tmp"
    for f in sorted(tmp.glob("*.jsonl")):
        first, last, models = jsonl_summary(f)
        if not in_window(first, window):
            continue
        if cfg["marker"] not in f.read_text(encoding="utf-8", errors="replace").lower():
            continue
        items.append(claude_item(f, tmp, "private-tmp", first, last, models,
                                 f"Claude Code session in /private/tmp, in the run window, whose text contains "
                                 f"the manuscript title phrase \"{cfg['marker']}\""))
        items.extend(claude_companions(f, tmp, "private-tmp"))
    return items, lead_texts


def claude_item(f, root, label, first, last, models, reason):
    entry = ""
    with open(f, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                entry = json.loads(line).get("entrypoint") or ""
            except json.JSONDecodeError:
                continue
            if entry:
                break
    if "/subagents/" in str(f):
        kind = f"Claude Code subagent of session {f.parent.parent.name}"
    elif entry == "sdk-cli":
        kind = "headless Claude Code call (entrypoint sdk-cli)"
    else:
        kind = f"Claude Code lead session (entrypoint {entry or 'unknown'})"
    return {"kind": kind, "src": f, "dest": Path("claude") / label / f.relative_to(root),
            "session": f.stem, "first": first, "last": last, "models": models, "reason": reason,
            "reader": "file"}


def claude_companions(f, root, label):
    """Subagent transcripts and metadata of one session; stored tool outputs are marked as skipped."""
    out = []
    comp = f.parent / f.stem
    if not comp.is_dir():
        return out
    for p in sorted(comp.rglob("*")):
        if not p.is_file():
            continue
        dest = Path("claude") / label / p.relative_to(root)
        if "tool-results" in p.relative_to(comp).parts or p.suffix not in TEXT_SUFFIXES:
            out.append({"skip": True, "src": p, "dest": dest, "size": p.stat().st_size})
            continue
        if p.suffix == ".jsonl":
            first, last, models = jsonl_summary(p)
            item = claude_item(p, root, label, first, last, models,
                               f"subagent transcript of exported session {f.stem}")
            out.append(item)
            continue
        out.append({"kind": f"subagent metadata of session {f.stem}", "src": p, "dest": dest, "session": f.stem,
                    "first": None, "last": None, "models": [], "reader": "file",
                    "reason": f"companion file of exported session {f.stem}"})
    return out


def codex_meta(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        head = fh.readline()
        try:
            meta = json.loads(head).get("payload", {})
        except json.JSONDecodeError:
            return None, None
        prompt = None
        for line in fh:
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            p = obj.get("payload", {})
            if obj.get("type") == "response_item" and p.get("type") == "message" and p.get("role") == "user":
                text = " ".join(c.get("text", "") for c in p.get("content", []) if isinstance(c, dict))
                if text and not text.lstrip().startswith("<") and not text.startswith("# AGENTS.md"):
                    prompt = text.strip().splitlines()[0].strip()
                    break
    return meta, prompt


def discover_codex(name, cfg, lead_texts):
    source, window = cfg["source"], cfg["window"]
    cites = cited_ids(source)
    items = []
    for f in sorted(CODEX_SESSIONS.glob("*/rollout-*.jsonl")):
        meta, prompt = codex_meta(f)
        if not meta:
            continue
        start = parse_ts(meta.get("timestamp"))  # session_meta payload timestamp
        if not in_window(start, window):
            continue
        cwd, sid = meta.get("cwd", ""), meta.get("id", "")
        if cwd == str(source) or cwd.startswith(str(source) + "/"):
            reason = "Codex session whose recorded cwd is the example folder (or a subfolder), in the run window"
        elif sid in cites:
            reason = "Codex session id cited in the example repository, in the run window"
        elif prompt and len(prompt) >= 20 and any(prompt in t for t in lead_texts):
            reason = "Codex session whose first prompt appears in the example's Claude Code lead transcript, " \
                     "in the run window"
        else:
            continue
        src = meta.get("source")
        if isinstance(src, dict) and "subagent" in src:
            sub = src["subagent"]
            if isinstance(sub, dict) and "thread_spawn" in sub:
                kind = f"Codex subagent ({sub['thread_spawn'].get('agent_path', '')})"
            else:
                kind = f"Codex subagent ({json.dumps(sub, sort_keys=True)})"
        elif src == "exec":
            kind = "codex exec call"
        else:
            kind = f"Codex thread session (originator {meta.get('originator', '')})"
        first, last, models = jsonl_summary(f)
        items.append({"kind": kind, "src": f, "dest": Path("codex") / f.name, "session": sid,
                      "first": first, "last": last, "models": models, "reason": reason, "reader": "file"})
    return items


def discover_opencode(name, cfg):
    items = []
    if not OPENCODE_DB.exists():
        return items
    con = ro_connect(OPENCODE_DB)
    rows = con.execute(
        "select id, parent_id, title, model, time_created from session where directory = ? order by time_created, id",
        (str(cfg["source"]),)).fetchall()
    for sid, parent, title, model, created in rows:
        n = con.execute("select count(*) from message where session_id = ?", (sid,)).fetchone()[0]
        if n == 0 or not in_window(parse_ts(created), cfg["window"]):
            continue
        times = con.execute("select min(time_created), max(time_updated) from message where session_id = ?",
                            (sid,)).fetchone()
        try:
            model_id = json.loads(model).get("providerID", "") + "/" + json.loads(model).get("id", "")
        except (TypeError, ValueError):
            model_id = model or ""
        kind = "OpenCode lead session" if not parent else f"OpenCode subagent session ({title})"
        items.append({"kind": kind, "src": OPENCODE_DB, "dest": Path("opencode") / f"{sid}.jsonl",
                      "session": sid, "first": parse_ts(times[0]), "last": parse_ts(times[1]),
                      "models": [model_id], "reader": ("opencode", sid),
                      "reason": "OpenCode session whose directory is the example folder, in the run window"})
    con.close()
    return items


def discover_t3(name, cfg):
    items = []
    con = ro_connect(T3_DB)
    rows = con.execute(
        "select t.thread_id, t.title, t.created_at, t.model_selection_json from projection_threads t "
        "join projection_projects p using(project_id) where p.workspace_root = ? order by t.created_at",
        (str(cfg["source"]),)).fetchall()
    for tid, title, created, model_json in rows:
        if not in_window(parse_ts(created), cfg["window"]):
            continue
        last = con.execute("select max(created_at) from projection_thread_messages where thread_id = ?",
                           (tid,)).fetchone()[0]
        try:
            model = json.loads(model_json).get("model", "")
        except (TypeError, ValueError):
            model = ""
        items.append({"kind": f"T3 Code thread \"{title}\"", "src": T3_DB, "dest": Path("t3") / f"thread-{tid}.jsonl",
                      "session": tid, "first": parse_ts(created), "last": parse_ts(last), "models": [model],
                      "reader": ("t3", tid),
                      "reason": "T3 Code thread of the project whose workspace root is the example folder"})
    con.close()
    return items


# ---------------------------------------------------------------- readers

def rows_as_dicts(cur):
    cols = [c[0] for c in cur.description]
    return [dict(zip(cols, r)) for r in cur.fetchall()]


def read_opencode(sid):
    con = ro_connect(OPENCODE_DB)
    out = []
    for rec in rows_as_dicts(con.execute("select * from session where id = ?", (sid,))):
        out.append({"record": "session", **rec})
    for table in ("message", "part"):
        for rec in rows_as_dicts(con.execute(
                f"select * from {table} where session_id = ? order by time_created, id", (sid,))):
            rec["data"] = json.loads(rec["data"])
            out.append({"record": table, **rec})
    con.close()
    return "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in out)


def read_t3(tid):
    con = ro_connect(T3_DB)
    out = []
    queries = [
        ("project", "select p.project_id, p.title, p.workspace_root, p.created_at from projection_projects p "
                    "join projection_threads t using(project_id) where t.thread_id = ?"),
        ("thread", "select * from projection_threads where thread_id = ?"),
        ("thread_session", "select * from projection_thread_sessions where thread_id = ?"),
        ("turn", "select * from projection_turns where thread_id = ? order by requested_at, row_id"),
        ("message", "select * from projection_thread_messages where thread_id = ? order by created_at, message_id"),
    ]
    for record, sql in queries:
        for rec in rows_as_dicts(con.execute(sql, (tid,))):
            out.append({"record": record, **rec})
    con.close()
    return "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in out)


def read_item(item):
    if item["reader"] == "file":
        return item["src"].read_text(encoding="utf-8", errors="surrogateescape")
    kind, key = item["reader"]
    return read_opencode(key) if kind == "opencode" else read_t3(key)


# ---------------------------------------------------------------- writing

def safe_target(folder):
    if folder not in EXAMPLES:
        sys.exit(f"refusing: {folder} is not an example folder")
    if not (REPO / ".git").exists():
        sys.exit(f"refusing: {REPO} is not a git repository")
    base = (REPO / folder).resolve()
    if base.parent != REPO or not base.is_dir():
        sys.exit(f"refusing: {base} is not a folder at the top of {REPO}")
    target = base / "run_records"
    if target.is_symlink():
        sys.exit(f"refusing: {target} is a symlink")
    return target


def safe_path(target, rel):
    out = (target / rel).resolve()
    if target.resolve() not in out.parents:
        sys.exit(f"refusing to write outside {target}: {rel}")
    return out


def check_jsonl(original, redacted, label):
    """Line count is unchanged, and every line that parsed before redaction still parses."""
    if len(original.splitlines()) != len(redacted.splitlines()):
        sys.exit(f"redaction changed the line count of {label}")
    for i, (a, b) in enumerate(zip(original.splitlines(), redacted.splitlines()), 1):
        try:
            json.loads(a)
        except json.JSONDecodeError:
            continue
        try:
            json.loads(b)
        except json.JSONDecodeError:
            sys.exit(f"redaction broke JSON in {label}, line {i}")


def write_output(path, text):
    data = text.encode("utf-8", errors="surrogateescape")
    path.parent.mkdir(parents=True, exist_ok=True)
    if len(data) > MAX_PLAIN_BYTES:
        path = path.with_name(path.name + ".gz")
        buf = io.BytesIO()
        with gzip.GzipFile(filename="", mode="wb", fileobj=buf, mtime=0) as gz:
            gz.write(data)
        path.write_bytes(buf.getvalue())
        return path, True
    path.write_bytes(data)
    return path, False


def human_size(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024


def export(folder, cfg, redactor):
    target = safe_target(folder)
    claude_items, lead_texts = discover_claude(folder, cfg)
    items = discover_t3(folder, cfg) + claude_items + discover_codex(folder, cfg, lead_texts) \
        + discover_opencode(folder, cfg)
    if target.exists():
        shutil.rmtree(target)
    target.mkdir()
    counts = dict.fromkeys(COUNT_KEYS, 0)
    rows, skipped = [], []
    for item in items:
        if item.get("skip"):
            skipped.append(item)
            continue
        original = read_item(item)
        is_json = item["dest"].suffix in (".jsonl", ".json")
        redacted = redactor.redact(original, counts, multiline=not is_json)
        if is_json:
            check_jsonl(original, redacted, str(item["dest"]))
        path, gz = write_output(safe_path(target, item["dest"]), redacted)
        item.update(out=path.relative_to(target), size=path.stat().st_size, gz=gz)
        rows.append(item)
    readme = render_readme(folder, cfg, rows, skipped, counts)
    (target / "README.md").write_text(redactor.redact(readme, dict.fromkeys(COUNT_KEYS, 0)))
    total = sum(r["size"] for r in rows)
    print(f"{folder}: {len(rows)} files, {human_size(total)}, not exported {len(skipped)}; "
          f"redactions {counts}")
    return rows, counts


def render_readme(folder, cfg, rows, skipped, counts):
    source = tilde(cfg["source"])
    lo, hi = cfg["window"]
    lines = [
        f"# Run records: `{folder}`",
        "",
        f"Local session records of the run that produced this example (source folder `{source}`), exported by "
        "`tools/redact_transcripts.py`. Rerun that script from the repository root to regenerate this folder.",
        "",
        "The transcripts show what the agents did, including the text that tools returned to them. They may "
        "therefore contain quoted excerpts of third-party texts, such as search results, abstracts and web pages. "
        "That text remains the property of its owners.",
        "",
        "## How records were matched",
        "",
        f"Every record starts inside the run window {lo} to {hi} (UTC) and meets one of these rules:",
        "",
    ]
    for reason in sorted({r["reason"] for r in rows}):
        n = sum(1 for r in rows if r["reason"] == reason)
        lines.append(f"- {reason} ({n} files).")
    lines += ["", "## Notes", ""]
    lines += [f"- {n}" for n in cfg["notes"] + COMMON_NOTES]
    if any(r["gz"] for r in rows):
        lines.append("- Files larger than 50 MB are gzip-compressed (`.gz`).")
    else:
        lines.append("- No file is larger than 50 MB; none is compressed.")
    lines += ["", "## Not exported", ""]
    if skipped:
        lines += [
            "Claude Code stores large tool outputs as separate files next to a session (`tool-results/`). "
            "These files are not exported, because they hold fetched third-party texts (web pages, "
            "article texts, extracted document text, search results with abstracts, PDFs and page images) "
            "together with long command outputs. The transcripts keep the reference to each file and a short "
            "preview of its content.",
            "",
            "| File (source path) | Size |",
            "|---|---|",
        ]
        lines += [f"| `{tilde(s['src'])}` | {human_size(s['size'])} |" for s in skipped]
    else:
        lines.append("No stored tool-output files exist for this run.")
    lines += [
        "",
        "## Redaction",
        "",
        "All other content is kept, including the standing instructions that the sessions loaded at start-up.",
        "",
        "| Rule | Replacement | Count |",
        "|---|---|---|",
        f"| The author's email addresses | `[email redacted]` | {counts['email_author']} |",
        "| Other email addresses (placeholder domains such as example.org and no-reply addresses are kept) "
        f"| `[email redacted]` | {counts['email_other']} |",
        f"| The author's ORCID iD | `[ORCID redacted]` | {counts['orcid']} |",
        "| Home directory path (plain, JSON-escaped, URL-encoded, without the leading slash; Claude Code's "
        f"encoded form becomes `-~-`) | `~` | {counts['home_path']} |",
        "| Secret values from the local API-key file and any printed fragment of a key (prefix or suffix of "
        "6 or more characters after the public type prefix); common key formats (`sk-`, `ghp_`, `AIza`, `AKIA`, `xox?-`, JWTs, Bearer "
        f"tokens, `NAME_API_KEY=value`, private-key blocks) | `[secret redacted]` | {counts['secret']} |",
        f"| Names of local project folders that are not part of this repository | `[other project]` "
        f"| {counts['other_project']} |",
        "",
        "## Files",
        "",
        f"{len(rows)} files, {human_size(sum(r['size'] for r in rows))} in total. Times are UTC.",
        "",
        "| File | Record | Source | Session id | First entry | Last entry | Model | Size |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        src = f"`{tilde(r['src'])}`"
        if r["reader"] != "file":
            src += f" ({'table rows' if r['reader'][0] == 't3' else 'session, message and part rows'})"
        lines.append(f"| `{r['out']}` | {r['kind']} | {src} | `{r['session']}` | {fmt_ts(r['first'])} | "
                     f"{fmt_ts(r['last'])} | {', '.join(r['models'])} | {human_size(r['size'])} |")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- verification

def verify(secret_values):
    """Count forbidden strings in all run_records. Prints counts only."""
    home = str(HOME)
    literal = {
        "lukas.wallrich (any case)": re.compile(r"lukas\.wallrich", re.I),
        "@birkbeck": re.compile(r"@birkbeck", re.I),
        "home path": re.compile(re.escape(home)),
        "home path (JSON-escaped)": re.compile(re.escape(home.replace("/", "\\/"))),
        "home path (URL-encoded)": re.compile(re.escape(home.replace("/", "%2F")), re.I),
        "home path (encoded form)": re.compile(re.escape(home.replace("/", "-") + "-")),
        "home path (relative form)": re.compile(re.escape(home.lstrip("/") + "/")),
    }
    fragments = key_fragments(secret_values)
    examples = {cfg["source"].name for cfg in EXAMPLES.values()}
    ok = True
    for folder in EXAMPLES:
        target = REPO / folder / "run_records"
        totals = {k: 0 for k in literal}
        totals.update({"ORCID": 0, "api_keys.env values": 0, "key fragments": 0, "email addresses": 0,
                       "other project names": 0, "bare username": 0})
        files = sorted(p for p in target.rglob("*") if p.is_file())
        if not files:
            print(f"verify {folder}: no run_records found")
            ok = False
        for p in files:
            raw = p.read_bytes()
            text = (gzip.decompress(raw) if p.suffix == ".gz" else raw).decode("utf-8", errors="replace")
            for k, pat in literal.items():
                totals[k] += len(pat.findall(text))
            totals["ORCID"] += sum(1 for m in ORCID_RE.finditer(text)
                                   if hashlib.sha256(m.group(0).replace("-", "").encode()).hexdigest()
                                   in ORCID_SHA256)
            totals["api_keys.env values"] += sum(text.count(v) for v in secret_values)
            counter = {"secret": 0}
            replace_fragments(text, fragments, counter)
            totals["key fragments"] += counter["secret"]
            totals["email addresses"] += sum(1 for m in EMAIL_RE.finditer(text) if not is_kept_email(m.group("addr")))
            totals["other project names"] += sum(1 for m in OTHER_PROJECT_RE.finditer(text)
                                                 if m.group(0) not in examples)
            totals["bare username"] += text.count(USER)
        hits = {k: v for k, v in totals.items() if v and k != "bare username"}
        ok &= not hits
        print(f"verify {folder}: {len(files)} files; forbidden hits {hits or 0}; "
              f"bare username '{USER}' (kept) {totals['bare username']}")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--verify", action="store_true", help="only verify existing run_records")
    args = ap.parse_args()
    secret_values = load_secret_values()
    if not args.verify:
        redactor = Redactor(secret_values)
        for folder, cfg in EXAMPLES.items():
            export(folder, cfg, redactor)
    if not verify(secret_values):
        sys.exit("verification failed")
    print("verification passed")


if __name__ == "__main__":
    main()
