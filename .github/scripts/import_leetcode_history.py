#!/usr/bin/env python3
"""Import the latest accepted LeetCode submission for every previously solved problem.

This script is intentionally run only by the manual import workflow. It needs
the encrypted LEETCODE_SESSION repository secret and never prints that value.
Existing solution files are left untouched.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path.cwd()
USERNAME = os.environ.get("LEETCODE_USERNAME", "")
SESSION = os.environ.get("LEETCODE_SESSION", "")
PAGE_SIZE = 20
EXTENSION_BY_LANGUAGE = {
    "python": ".py",
    "python3": ".py",
    "c++": ".cpp",
    "cpp": ".cpp",
    "c": ".c",
    "java": ".java",
    "javascript": ".js",
    "typescript": ".ts",
    "go": ".go",
    "golang": ".go",
    "rust": ".rs",
    "c#": ".cs",
    "csharp": ".cs",
    "kotlin": ".kt",
    "swift": ".swift",
    "ruby": ".rb",
    "php": ".php",
    "scala": ".scala",
    "mysql": ".sql",
    "mssql": ".sql",
    "oraclesql": ".sql",
}


def session_cookie() -> str:
    """Accept either a cookie value or an already formatted Cookie header value."""
    if not SESSION:
        raise SystemExit(
            "LEETCODE_SESSION is not configured. Add it as a GitHub Actions secret "
            "before running this import."
        )
    return SESSION if "=" in SESSION else f"LEETCODE_SESSION={SESSION}"


def get_json(path: str) -> dict[str, object]:
    request = Request(
        f"https://leetcode.com{path}",
        headers={
            "Cookie": session_cookie(),
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
                "LeetCode rejected LEETCODE_SESSION. Replace the repository secret with "
                "a current session value, then rerun the workflow."
            ) from error
        raise SystemExit(f"LeetCode request failed with HTTP {error.code}.") from error
    except (OSError, URLError, json.JSONDecodeError) as error:
        raise SystemExit(f"Could not retrieve LeetCode data: {error}") from error

    return payload if isinstance(payload, dict) else {}


def latest_accepted_submissions() -> dict[str, dict[str, object]]:
    """Collect one latest accepted submission for every problem in the account."""
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
    submission_id = submission.get("id")
    try:
        submission_number = int(submission_id)
    except (TypeError, ValueError):
        print(f"Skipping {slug}: submission id was unavailable.")
        return False

    detail = get_json(f"/submissions/detail/{submission_number}/")
    code = detail.get("code")
    question_id = detail.get("question_id", submission.get("question_id"))
    language = str(detail.get("lang", submission.get("lang", "text"))).lower()
    try:
        question_number = int(question_id)
    except (TypeError, ValueError):
        question_number = 0
    if not isinstance(code, str) or question_number <= 0:
        print(f"Skipping {slug}: source code or problem number was unavailable.")
        return False

    extension = EXTENSION_BY_LANGUAGE.get(language, ".txt")
    directory = ROOT / f"{question_number:04d}-{slug}"
    destination = directory / f"solution{extension}"
    if destination.exists():
        print(f"Keeping existing {destination.relative_to(ROOT)}")
        return False

    directory.mkdir(parents=True, exist_ok=True)
    destination.write_text(code, encoding="utf-8")
    print(f"Imported {destination.relative_to(ROOT)}")
    return True


def main() -> None:
    if not USERNAME:
        raise SystemExit("LEETCODE_USERNAME is not configured.")

    submissions = latest_accepted_submissions()
    imported = sum(save_submission(slug, submission) for slug, submission in submissions.items())
    print(f"Imported {imported} solution(s) from {len(submissions)} accepted problem(s).")


if __name__ == "__main__":
    main()
