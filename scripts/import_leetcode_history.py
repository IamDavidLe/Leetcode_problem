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
PROBLEMS_ROOT = ROOT / "Problems"
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
SUBMISSION_DETAILS_QUERY = """
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    code
    lang { name }
    question { questionId }
  }
}
"""
SOLVED_QUESTIONS_QUERY = """
query userProgressQuestionList($filters: UserProgressQuestionListInput) {
  userProgressQuestionList(filters: $filters) {
    questions { frontendId titleSlug }
  }
}
"""
QUESTION_SUBMISSIONS_QUERY = """
query submissionList($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!, $lang: Int, $status: Int) {
  questionSubmissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug, lang: $lang, status: $status) {
    submissions { id frontendId }
  }
}
"""


def session_cookie() -> str:
    """Prompt securely unless a user deliberately supplied an environment value."""
    session = os.environ.get("LEETCODE_SESSION")
    if not session:
        session = getpass.getpass("Paste your current LEETCODE_SESSION value (hidden): ").strip()
    if not session:
        raise SystemExit("No LeetCode session value was supplied.")
    return session if "=" in session else f"LEETCODE_SESSION={session}"


COOKIE = session_cookie()


def graphql(query: str, variables: dict[str, object], operation_name: str) -> dict[str, object]:
    """Call LeetCode's authenticated GraphQL endpoint."""
    request_body = json.dumps(
        {"query": query, "variables": variables, "operationName": operation_name}
    ).encode()
    request = Request(
        "https://leetcode.com/graphql/",
        data=request_body,
        headers={
            "Cookie": COOKIE,
            "Content-Type": "application/json",
            "User-Agent": "leetcode-history-importer",
            "Referer": "https://leetcode.com/",
        },
        method="POST",
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
        raise SystemExit(f"LeetCode GraphQL request failed with HTTP {error.code}.") from error
    except (OSError, URLError, json.JSONDecodeError) as error:
        raise SystemExit(f"Could not retrieve LeetCode data: {error}") from error

    if not isinstance(payload, dict):
        raise SystemExit("LeetCode returned an unexpected GraphQL response.")
    errors = payload.get("errors")
    if errors:
        raise SystemExit(f"LeetCode rejected the {operation_name} query: {errors}")
    data = payload.get("data")
    return data if isinstance(data, dict) else {}


def get_submission_detail(submission_id: int) -> dict[str, object]:
    """Retrieve source code through LeetCode's current authenticated GraphQL API."""
    detail = graphql(
        SUBMISSION_DETAILS_QUERY,
        {"submissionId": submission_id},
        "submissionDetails",
    ).get("submissionDetails")
    if not isinstance(detail, dict):
        raise SystemExit("LeetCode did not return source code for a historical submission.")
    return detail


def latest_accepted_submissions() -> dict[str, dict[str, object]]:
    """Collect the newest accepted submission for every solved question."""
    accepted: dict[str, dict[str, object]] = {}
    progress = graphql(
        SOLVED_QUESTIONS_QUERY,
        {"filters": {"questionStatus": "SOLVED", "skip": 0, "limit": 4000}},
        "userProgressQuestionList",
    ).get("userProgressQuestionList")
    questions = progress.get("questions", []) if isinstance(progress, dict) else []
    if not isinstance(questions, list):
        raise SystemExit("LeetCode returned an unexpected solved-questions response.")

    for question in questions:
        if not isinstance(question, dict) or not isinstance(question.get("titleSlug"), str):
            continue
        slug = question["titleSlug"]
        submission_list = graphql(
            QUESTION_SUBMISSIONS_QUERY,
            {"offset": 0, "limit": 1, "lastKey": None, "questionSlug": slug, "lang": None, "status": 10},
            "submissionList",
        ).get("questionSubmissionList")
        submissions = submission_list.get("submissions", []) if isinstance(submission_list, dict) else []
        if isinstance(submissions, list) and submissions and isinstance(submissions[0], dict):
            accepted[slug] = {**submissions[0], "question_id": question.get("frontendId")}
        time.sleep(0.1)
    return accepted


def save_submission(slug: str, submission: dict[str, object]) -> bool:
    try:
        submission_number = int(submission.get("id"))
    except (TypeError, ValueError):
        print(f"Skipping {slug}: submission id was unavailable.")
        return False

    detail = get_submission_detail(submission_number)
    code = detail.get("code")
    try:
        question = detail.get("question", {})
        question_id = question.get("questionId") if isinstance(question, dict) else None
        question_number = int(submission.get("question_id") or question_id)
    except (TypeError, ValueError):
        question_number = 0
    if not isinstance(code, str) or question_number <= 0:
        print(f"Skipping {slug}: source code or problem number was unavailable.")
        return False

    language_data = detail.get("lang")
    language = (
        str(language_data.get("name", "text"))
        if isinstance(language_data, dict)
        else str(submission.get("lang", "text"))
    ).lower()
    destination = PROBLEMS_ROOT / f"{question_number:04d}-{slug}" / f"solution{EXTENSION_BY_LANGUAGE.get(language, '.txt')}"
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
