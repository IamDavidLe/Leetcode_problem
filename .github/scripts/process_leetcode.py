#!/usr/bin/env python3
"""Create LeetCode documentation and keep the repository progress index current.

Use a directory named like ``0001-two-sum`` and add a Python source file inside
it. The first run creates its README and metadata file. The workflow also reads
the configured public LeetCode profile; no account cookie or password is used.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen


ROOT = Path.cwd()
README = ROOT / "README.md"
PROGRESS_START = "<!-- leetcode-progress:start -->"
PROGRESS_END = "<!-- leetcode-progress:end -->"
EXCLUDED_DIRECTORIES = {".git", ".github", ".venv", "venv", "__pycache__"}
PROBLEM_DIRECTORY = re.compile(r"^(?P<number>\d+)-(?P<slug>[a-z0-9-]+)$")
LOWERCASE_TITLE_WORDS = {"a", "an", "and", "as", "at", "by", "for", "in", "of", "on", "or", "the", "to", "via", "vs"}
PROFILE_QUERY = """
query userPublicProfile($username: String!) {
  matchedUser(username: $username) {
    username
    submitStats { acSubmissionNum { difficulty count } }
  }
}
"""


@dataclass(frozen=True)
class Solution:
    number: int
    slug: str
    directory: Path
    source_file: Path

    @property
    def title(self) -> str:
        words = self.slug.split("-")
        return " ".join(
            word.capitalize() if index == 0 or word not in LOWERCASE_TITLE_WORDS else word
            for index, word in enumerate(words)
        )

    @property
    def url(self) -> str:
        return f"https://leetcode.com/problems/{self.slug}/"

    @property
    def metadata_path(self) -> Path:
        return self.directory / "metadata.json"


def discover_solutions() -> list[Solution]:
    """Find Python sources in directories named like ``0001-two-sum``.

    This supports both a hand-written ``solution.py`` and filenames produced by
    common LeetCode sync extensions, such as ``0001-two-sum.py``.
    """
    by_directory: dict[Path, Path] = {}
    for source_file in ROOT.rglob("*.py"):
        relative_parts = source_file.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIRECTORIES for part in relative_parts):
            continue
        if PROBLEM_DIRECTORY.fullmatch(source_file.parent.name) is None:
            continue

        current = by_directory.get(source_file.parent)
        if current is None or (source_file.name != "solution.py", source_file.name) < (
            current.name != "solution.py", current.name
        ):
            by_directory[source_file.parent] = source_file

    solutions: list[Solution] = []
    for directory, source_file in by_directory.items():
        match = PROBLEM_DIRECTORY.fullmatch(directory.name)
        assert match is not None
        solutions.append(
            Solution(
                number=int(match["number"]),
                slug=match["slug"],
                directory=directory,
                source_file=source_file,
            )
        )
    return sorted(solutions, key=lambda solution: (solution.number, solution.slug))


def default_metadata(solution: Solution) -> dict[str, object]:
    return {
        "problem_number": solution.number,
        "title": solution.title,
        "slug": solution.slug,
        "difficulty": "Unknown",
        "language": "Python",
        "leetcode_url": solution.url,
    }


def load_metadata(solution: Solution) -> dict[str, object]:
    """Read user-maintained metadata, falling back safely to generated defaults."""
    defaults = default_metadata(solution)
    if not solution.metadata_path.exists():
        return defaults

    try:
        saved = json.loads(solution.metadata_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return defaults

    return {**defaults, **saved} if isinstance(saved, dict) else defaults


def write_problem_files(solution: Solution) -> None:
    """Create first-run documentation without overwriting manual additions."""
    if not solution.metadata_path.exists():
        solution.metadata_path.write_text(
            json.dumps(default_metadata(solution), indent=2) + "\n", encoding="utf-8"
        )

    problem_readme = solution.directory / "README.md"
    if not problem_readme.exists():
        problem_readme.write_text(
            f"""# {solution.number}. {solution.title}

- Difficulty: Unknown
- Language: Python
- LeetCode: [{solution.title}]({solution.url})

## Solution

See [{solution.source_file.name}]({solution.source_file.name}).

## Complexity

Add the time and space complexity for this solution here.
""",
            encoding="utf-8",
        )


def fetch_public_profile(username: str | None) -> dict[str, int | str] | None:
    """Return public accepted-solution counts without authenticating to LeetCode."""
    if not username:
        return None

    payload = json.dumps({"query": PROFILE_QUERY, "variables": {"username": username}}).encode()
    request = Request(
        "https://leetcode.com/graphql/",
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "leetcode-progress-bot"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=20) as response:
            data = json.load(response)
    except (OSError, URLError, json.JSONDecodeError) as error:
        print(f"Warning: could not retrieve public LeetCode stats: {error}")
        return None

    user = data.get("data", {}).get("matchedUser")
    if not isinstance(user, dict):
        print(f"Warning: public LeetCode profile not found for {username}.")
        return None

    counts = {
        entry.get("difficulty"): entry.get("count", 0)
        for entry in user.get("submitStats", {}).get("acSubmissionNum", [])
        if isinstance(entry, dict)
    }
    return {
        "username": str(user.get("username", username)),
        "All": int(counts.get("All", 0)),
        "Easy": int(counts.get("Easy", 0)),
        "Medium": int(counts.get("Medium", 0)),
        "Hard": int(counts.get("Hard", 0)),
    }


def progress_block(
    solutions: list[Solution], profile: dict[str, int | str] | None
) -> str:
    rows = [PROGRESS_START]
    if profile is not None:
        username = str(profile["username"])
        rows.extend(
            [
                "## LeetCode Profile",
                "",
                f"[{username}](https://leetcode.com/u/{username}/)",
                f"**Public stats:** {profile['All']} solved — {profile['Easy']} Easy · "
                f"{profile['Medium']} Medium · {profile['Hard']} Hard",
                "",
            ]
        )

    rows.extend(
        [
            "## Repository Progress",
            "",
            f"**Solutions in this repository: {len(solutions)}**",
            "",
            "| # | Problem | Difficulty | Language |",
            "| ---: | --- | --- | --- |",
        ]
    )
    for solution in solutions:
        metadata = load_metadata(solution)
        difficulty = str(metadata.get("difficulty", "Unknown"))
        language = str(metadata.get("language", "Python"))
        title = str(metadata.get("title", solution.title))
        path = solution.directory.relative_to(ROOT).as_posix()
        rows.append(f"| {solution.number} | [{title}]({path}/) | {difficulty} | {language} |")

    rows.extend(["", PROGRESS_END])
    return "\n".join(rows)


def update_root_readme(
    solutions: list[Solution], profile: dict[str, int | str] | None
) -> None:
    """Replace only the marked generated section, retaining all other README text."""
    current = README.read_text(encoding="utf-8") if README.exists() else "# LeetCode Solutions\n"
    block = progress_block(solutions, profile)
    section = re.compile(
        rf"{re.escape(PROGRESS_START)}.*?{re.escape(PROGRESS_END)}", re.DOTALL
    )
    updated = section.sub(block, current) if section.search(current) else current.rstrip() + "\n\n" + block + "\n"
    README.write_text(updated, encoding="utf-8")


def main() -> None:
    solutions = discover_solutions()
    for solution in solutions:
        write_problem_files(solution)
    update_root_readme(solutions, fetch_public_profile(os.environ.get("LEETCODE_USERNAME")))
    print(f"Processed {len(solutions)} Python solution(s).")


if __name__ == "__main__":
    main()
