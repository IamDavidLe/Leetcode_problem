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
LEETCODE_ROOT = ROOT / "LeetCode"
USERNAME = os.environ.get("LEETCODE_USERNAME", "JiaPark")
PAGE_SIZE = 20
SOLVED_QUESTIONS_PAGE_SIZE = 50
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
    question { questionId difficulty }
  }
}
"""
SOLVED_QUESTIONS_QUERY = """
query userProgressQuestionList($filters: UserProgressQuestionListInput) {
  userProgressQuestionList(filters: $filters) {
    totalNum
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
    questions_by_slug: dict[str, dict[str, object]] = {}
    skip = 0
    total = None

    # LeetCode caps a single response, even when a much larger limit is
    # requested. Fetching successive pages keeps older accepted solutions from
    # being silently omitted.
    while total is None or skip < total:
        progress = graphql(
            SOLVED_QUESTIONS_QUERY,
            {"filters": {"questionStatus": "SOLVED", "skip": skip, "limit": SOLVED_QUESTIONS_PAGE_SIZE}},
            "userProgressQuestionList",
        ).get("userProgressQuestionList")
        if not isinstance(progress, dict):
            raise SystemExit("LeetCode returned an unexpected solved-questions response.")

        questions = progress.get("questions", [])
        if not isinstance(questions, list):
            raise SystemExit("LeetCode returned an unexpected solved-questions response.")
        try:
            total = int(progress.get("totalNum"))
        except (TypeError, ValueError):
            total = skip + len(questions)

        if not questions:
            break
        for question in questions:
            if isinstance(question, dict) and isinstance(question.get("titleSlug"), str):
                questions_by_slug[question["titleSlug"]] = question

        next_skip = skip + len(questions)
        if next_skip <= skip:
            break
        skip = next_skip

    for slug, question in questions_by_slug.items():
        try:
            submission_list = graphql(
                QUESTION_SUBMISSIONS_QUERY,
                {"offset": 0, "limit": 1, "lastKey": None, "questionSlug": slug, "lang": None, "status": 10},
                "submissionList",
            ).get("questionSubmissionList")
        except SystemExit as error:
            print(f"Skipping {slug}: could not read its submission list ({error}).")
            continue
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

    try:
        question_number = int(submission.get("question_id"))
    except (TypeError, ValueError):
        print(f"Skipping {slug}: problem number was unavailable.")
        return False

    folder_name = f"{question_number:04d}-{slug}"
    existing = next(
        (path for path in LEETCODE_ROOT.rglob(folder_name) if path.is_dir()), None
    )
    if existing is not None:
        print(f"Keeping existing {existing.relative_to(ROOT)}")
        return False

    try:
        detail = get_submission_detail(submission_number)
    except SystemExit as error:
        print(f"Skipping {slug}: LeetCode did not expose this historical submission ({error}).")
        return False

    code = detail.get("code")
    question = detail.get("question", {})
    if isinstance(question, dict):
        try:
            question_number = int(question.get("questionId") or question_number)
        except (TypeError, ValueError):
            pass
    if not isinstance(code, str) or question_number <= 0:
        print(f"Skipping {slug}: source code or problem number was unavailable.")
        return False

    language_data = detail.get("lang")
    language = (
        str(language_data.get("name", "text"))
        if isinstance(language_data, dict)
        else str(submission.get("lang", "text"))
    ).lower()
    difficulty = str(question.get("difficulty", "Uncategorized")) if isinstance(question, dict) else "Uncategorized"
    if difficulty not in {"Easy", "Medium", "Hard"}:
        difficulty = "Uncategorized"
    destination = LEETCODE_ROOT / difficulty / f"{question_number:04d}-{slug}" / f"solution{EXTENSION_BY_LANGUAGE.get(language, '.txt')}"
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
