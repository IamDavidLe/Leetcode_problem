#!/usr/bin/env python3
"""Import the latest accepted LeetCode submission for every solved problem.

Run this script locally on the same Mac and network where you are signed into
LeetCode. It prompts for the session value without echoing or saving it, leaves
existing files untouched, and refreshes the repository documentation.
"""

from __future__ import annotations

import getpass
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
USERNAME = os.environ.get("LEETCODE_USERNAME", "JiaPark")
PAGE_SIZE = 20
EXTENSION_BY_LANGUAGE = {
    "python": ".py", "python3": ".py", "c++": ".cpp", "cpp": ".cpp",
    "c": ".c", "java": ".java", "javascript": ".js", "typescript": ".ts",
    "go": ".go", "golang": ".go", "rust": ".rs", "c#": ".cs",
    "csharp": ".cs", "kotlin": ".kt", "swift": ".swift", "ruby": ".rb",
    "php": ".php", "scala": ".scala", "mysql": ".sql", "mssql": ".sql",
    "oraclesql": ".sql",
}


def session_cookie() -> str:
    """Prompt securely unless a user deliberately supplied an environment value."""
    session = os.environ.get("LEETCODE_SESSION")
    if not session:
        session = getpass.getpass("Paste your current LEETCODE_SESSION value (hidden): ").strip()
    if not session:
        raise SystemExit("No LeetCode session value was supplied.")
    return session if "=" in session else f"LEETCODE_SESSION={session}"


COOKIE = session_cookie()


def get_json(path: str) -> dict[str, object]:
    request = Request(
        f"https://leetcode.com{path}",
        headers={
            "Cookie": COOKIE,
            "User-Agent": "leetcode-history-importer",
            "Referer": "https://leetcode.com/",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except HTTPError as error:
        if error.code in {401, 403}:
            raise SystemExit(
                "LeetCode rejected this session. Sign in again, copy a fresh session value, "
                "and rerun this local command."
            ) from error
        raise SystemExit(f"LeetCode request failed with HTTP {error.code}.") from error
    except (OSError, URLError, json.JSONDecodeError) as error:
        raise SystemExit(f"Could not retrieve LeetCode data: {error}") from error
    return payload if isinstance(payload, dict) else {}


def latest_accepted_submissions() -> dict[str, dict[str, object]]:
    """Collect one newest accepted submission for every problem in the account."""
    accepted: dict[str, dict[str, object]] = {}
    offset = 0
    while True:
        page = get_json(f"/api/submissions/{USERNAME}/?offset={offset}&limit={PAGE_SIZE}")
        submissions = page.get("submissions_dump", [])
        if not isinstance(submissions, list):
            raise SystemExit("LeetCode returned an unexpected submissions response.")
        for submission in submissions:
            if not isinstance(submission, dict) or submission.get("status_display") != "Accepted":
                continue
            slug = submission.get("title_slug")
            if isinstance(slug, str) and slug and slug not in accepted:
                accepted[slug] = submission
        if not page.get("has_next"):
            return accepted
        offset += PAGE_SIZE
        time.sleep(0.2)


def save_submission(slug: str, submission: dict[str, object]) -> bool:
    try:
        submission_number = int(submission.get("id"))
    except (TypeError, ValueError):
        print(f"Skipping {slug}: submission id was unavailable.")
        return False

    detail = get_json(f"/submissions/detail/{submission_number}/")
    code = detail.get("code")
    try:
        question_number = int(detail.get("question_id", submission.get("question_id")))
    except (TypeError, ValueError):
        question_number = 0
    if not isinstance(code, str) or question_number <= 0:
        print(f"Skipping {slug}: source code or problem number was unavailable.")
        return False

    language = str(detail.get("lang", submission.get("lang", "text"))).lower()
    destination = ROOT / f"{question_number:04d}-{slug}" / f"solution{EXTENSION_BY_LANGUAGE.get(language, '.txt')}"
    if destination.exists():
        print(f"Keeping existing {destination.relative_to(ROOT)}")
        return False
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(code, encoding="utf-8")
    print(f"Imported {destination.relative_to(ROOT)}")
    return True


def main() -> None:
    submissions = latest_accepted_submissions()
    imported = sum(save_submission(slug, submission) for slug, submission in submissions.items())
    print(f"Imported {imported} solution(s) from {len(submissions)} accepted problem(s).")
    environment = {**os.environ, "LEETCODE_USERNAME": USERNAME}
    subprocess.run(
        [sys.executable, ".github/scripts/process_leetcode.py"],
        cwd=ROOT,
        env=environment,
        check=True,
    )


if __name__ == "__main__":
    main()
