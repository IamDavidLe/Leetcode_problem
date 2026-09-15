#!/usr/bin/env python3
"""Create LeetCode documentation and keep the repository progress index current.

Use a directory name such as ``0001-two-sum`` and add ``solution.py`` inside
it. The first workflow run creates its README and metadata file. Later manual
edits to those files are preserved; the root progress table reads their values.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path.cwd()
README = ROOT / "README.md"
PROGRESS_START = "<!-- leetcode-progress:start -->"
PROGRESS_END = "<!-- leetcode-progress:end -->"
EXCLUDED_DIRECTORIES = {".git", ".github", ".venv", "venv", "__pycache__"}
PROBLEM_DIRECTORY = re.compile(r"^(?P<number>\d+)-(?P<slug>[a-z0-9-]+)$")
LOWERCASE_TITLE_WORDS = {"a", "an", "and", "as", "at", "by", "for", "in", "of", "on", "or", "the", "to", "via", "vs"}


@dataclass(frozen=True)
class Solution:
    number: int
    slug: str
    directory: Path

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
    """Find ``solution.py`` files in directories named like ``0001-two-sum``."""
    solutions: list[Solution] = []
    for solution_file in ROOT.rglob("solution.py"):
        relative_parts = solution_file.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIRECTORIES for part in relative_parts):
            continue

        match = PROBLEM_DIRECTORY.fullmatch(solution_file.parent.name)
        if match is None:
            continue

        solutions.append(
            Solution(
                number=int(match["number"]),
                slug=match["slug"],
                directory=solution_file.parent,
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

See [solution.py](solution.py).

## Complexity

Add the time and space complexity for this solution here.
""",
            encoding="utf-8",
        )


def progress_block(solutions: list[Solution]) -> str:
    rows = [
        PROGRESS_START,
        "## LeetCode Progress",
        "",
        f"**Solved: {len(solutions)}**",
        "",
        "| # | Problem | Difficulty | Language |",
        "| ---: | --- | --- | --- |",
    ]
    for solution in solutions:
        metadata = load_metadata(solution)
        difficulty = str(metadata.get("difficulty", "Unknown"))
        language = str(metadata.get("language", "Python"))
        title = str(metadata.get("title", solution.title))
        path = solution.directory.relative_to(ROOT).as_posix()
        rows.append(f"| {solution.number} | [{title}]({path}/) | {difficulty} | {language} |")

    rows.extend(["", PROGRESS_END])
    return "\n".join(rows)


def update_root_readme(solutions: list[Solution]) -> None:
    """Replace only the marked generated section, retaining all other README text."""
    current = README.read_text(encoding="utf-8") if README.exists() else "# LeetCode Solutions\n"
    block = progress_block(solutions)
    section = re.compile(
        rf"{re.escape(PROGRESS_START)}.*?{re.escape(PROGRESS_END)}", re.DOTALL
    )
    updated = section.sub(block, current) if section.search(current) else current.rstrip() + "\n\n" + block + "\n"
    README.write_text(updated, encoding="utf-8")


def main() -> None:
    solutions = discover_solutions()
    for solution in solutions:
        write_problem_files(solution)
    update_root_readme(solutions)
    print(f"Processed {len(solutions)} Python solution(s).")


if __name__ == "__main__":
    main()
