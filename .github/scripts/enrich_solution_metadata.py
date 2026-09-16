#!/usr/bin/env python3
"""Add verified difficulty plus implementation-specific complexity notes."""

from __future__ import annotations

import json
import time
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path.cwd()
LEETCODE_ROOT = ROOT / "LeetCode"
QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) { difficulty }
}
"""

# Complexity is for the submitted implementation. "Auxiliary" excludes the
# result returned by LeetCode, but includes arrays/maps created by the solution.
COMPLEXITIES = {
    "0001-two-sum": ("O(n²)", "O(1)"),
    "0002-add-two-numbers": ("O(max(m, n))", "O(max(m, n)) for the returned list"),
    "0003-longest-substring-without-repeating-characters": ("O(n)", "O(n)"),
    "0004-median-of-two-sorted-arrays": ("O((m + n) log(m + n))", "O(m + n) for the merged copy"),
    "0005-longest-palindromic-substring": ("O(n²)", "O(1) auxiliary"),
    "0012-integer-to-roman": ("O(1)", "O(1)"),
    "0013-roman-to-integer": ("O(n)", "O(1)"),
    "0015-3sum": ("O(n²)", "O(n) auxiliary; output excluded"),
    "0016-3sum-closest": ("O(n²)", "O(n) for the sorted copy"),
    "0017-letter-combinations-of-a-phone-number": ("O(4ⁿ · n)", "O(n) auxiliary; output excluded"),
    "0018-4sum": ("O(n³)", "O(n) for the sorted copy; output excluded"),
    "0019-remove-nth-node-from-end-of-list": ("O(n)", "O(1)"),
    "0021-merge-two-sorted-lists": ("O(m + n)", "O(1)"),
    "0024-swap-nodes-in-pairs": ("O(n)", "O(1)"),
    "0045-jump-game-ii": ("O(n)", "O(1)"),
    "0047-permutations-ii": ("O(n · n!)", "O(n) auxiliary; output excluded"),
    "0053-maximum-subarray": ("O(n)", "O(1)"),
    "0055-jump-game": ("O(n)", "O(1)"),
    "0061-rotate-list": ("O(n)", "O(1)"),
    "0062-unique-paths": ("O(m · n)", "O(m · n)"),
    "0079-word-search": ("O(m · n · 4ˡ)", "O(l) auxiliary"),
    "0082-remove-duplicates-from-sorted-list-ii": ("O(n)", "O(1)"),
    "0094-binary-tree-inorder-traversal": ("O(n)", "O(h) auxiliary"),
    "0091-decode-ways": ("O(n)", "O(n) for memoization"),
    "0098-validate-binary-search-tree": ("O(n)", "O(h) auxiliary"),
    "0100-same-tree": ("O(n)", "O(h) auxiliary"),
    "0101-symmetric-tree": ("O(n)", "O(h) auxiliary"),
    "0102-binary-tree-level-order-traversal": ("O(n)", "O(n)"),
    "0103-binary-tree-zigzag-level-order-traversal": ("O(n)", "O(n)"),
    "0104-maximum-depth-of-binary-tree": ("O(n)", "O(h) auxiliary"),
    "0107-binary-tree-level-order-traversal-ii": ("O(n)", "O(n)"),
    "0111-minimum-depth-of-binary-tree": ("O(n)", "O(h) auxiliary"),
    "0112-path-sum": ("O(n)", "O(h) auxiliary"),
    "0113-path-sum-ii": ("O(n · h)", "O(h) auxiliary; output excluded"),
    "0115-distinct-subsequences": ("O(m · n)", "O(m · n)"),
    "0116-populating-next-right-pointers-in-each-node": ("O(n)", "O(h) auxiliary"),
    "0118-pascals-triangle": ("O(n²)", "O(n²) for the returned triangle"),
    "0128-longest-consecutive-sequence": ("O(n α(n))", "O(n)"),
    "0129-sum-root-to-leaf-numbers": ("O(n)", "O(h) auxiliary"),
    "0136-single-number": ("O(n)", "O(1)"),
    "0144-binary-tree-preorder-traversal": ("O(n)", "O(h) auxiliary"),
    "0145-binary-tree-postorder-traversal": ("O(n)", "O(h) auxiliary"),
    "0152-maximum-product-subarray": ("O(n)", "O(1)"),
    "0191-number-of-1-bits": ("O(log n)", "O(1)"),
    "0198-house-robber": ("O(n)", "O(1) auxiliary; mutates the input"),
    "0199-binary-tree-right-side-view": ("O(n)", "O(h) auxiliary"),
    "0200-number-of-islands": ("O(rows · cols)", "O(rows · cols) worst case call stack"),
    "0209-minimum-size-subarray-sum": ("O(n)", "O(1)"),
    "0213-house-robber-ii": ("O(n)", "O(n) for the two input slices"),
    "0226-invert-binary-tree": ("O(n)", "O(h) auxiliary"),
    "0230-kth-smallest-element-in-a-bst": ("O(n)", "O(n)"),
    "0235-lowest-common-ancestor-of-a-binary-search-tree": ("O(h)", "O(h) auxiliary"),
    "0238-product-of-array-except-self": ("O(n)", "O(n)"),
    "0279-perfect-squares": ("O(n √n)", "O(n)"),
    "0322-coin-change": ("O(amount · c)", "O(amount)"),
    "0416-partition-equal-subset-sum": ("O(n · target)", "O(target)"),
    "0560-subarray-sum-equals-k": ("O(n)", "O(n)"),
    "1072-flip-columns-for-maximum-number-of-equal-rows": ("O(rows · cols)", "O(rows · cols)"),
    "2058-find-the-minimum-and-maximum-number-of-nodes-between-critical-points": ("O(n)", "O(1)"),
    "2265-count-nodes-equal-to-average-of-subtree": ("O(n)", "O(h) auxiliary"),
    "2472-maximum-number-of-non-overlapping-palindrome-substrings": ("O(n²)", "O(n²)"),
    "3414-maximum-score-of-non-overlapping-intervals": ("O(n log n)", "O(n)"),
    "3150-shortest-and-lexicographically-smallest-beautiful-string": ("O(n²)", "O(n) for temporary substrings"),
    "3347-distribute-elements-into-two-arrays-i": ("O(n)", "O(n) for the returned arrays"),
    "3483-unique-3-digit-even-numbers": ("O(n³)", "O(n³) worst case for the set"),
    "3705-find-the-largest-almost-missing-integer": ("O(n²)", "O(n)"),
    "3842-toggle-light-bulbs": ("O(n log n)", "O(n)"),
    "3870-count-commas-in-range": ("O(log n)", "O(1)"),
    "3871-count-commas-in-range-ii": ("O(log n)", "O(1)"),
    "3875-construct-uniform-parity-array-i": ("O(1)", "O(1)"),
    "3876-construct-uniform-parity-array-ii": ("O(n)", "O(n)"),
    "3903-smallest-stable-index-i": ("O(n)", "O(1)"),
    "3904-smallest-stable-index-ii": ("O(n)", "O(n)"),
    "4080-smallest-missing-multiple-of-k": ("O(n²)", "O(1)"),
}


def difficulty(slug: str) -> str:
    payload = json.dumps(
        {"query": QUESTION_QUERY, "variables": {"titleSlug": slug}}
    ).encode()
    request = Request(
        "https://leetcode.com/graphql/",
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "leetcode-metadata-updater"},
        method="POST",
    )
    with urlopen(request, timeout=20) as response:
        data = json.load(response)
    question = data.get("data", {}).get("question", {})
    return str(question.get("difficulty", "Unknown"))


def update_solution(directory: Path, time_complexity: str, space_complexity: str) -> None:
    metadata_path = directory / "metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    slug = str(metadata["slug"])
    # Keep a previously verified value so a temporary LeetCode outage does not
    # prevent documentation from being refreshed after files are reorganized.
    if metadata.get("difficulty") not in {"Easy", "Medium", "Hard"}:
        category = directory.parent.name
        metadata["difficulty"] = (
            category if category in {"Easy", "Medium", "Hard"} else difficulty(slug)
        )
    metadata["time_complexity"] = time_complexity
    metadata["space_complexity"] = space_complexity
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    title = str(metadata["title"])
    number = int(metadata["problem_number"])
    language = str(metadata["language"])
    url = str(metadata["leetcode_url"])
    source_file = directory / "solution.py"
    if not source_file.exists():
        source_file = next(
            (path for path in sorted(directory.iterdir()) if path.suffix == ".py"),
            source_file,
        )
    problem_readme = f"""# {number}. {title}

- Difficulty: {metadata['difficulty']}
- Language: {language}
- LeetCode: [{title}]({url})

## Solution

See [{source_file.name}]({source_file.name}).

## Complexity

- Time: {time_complexity}
- Space: {space_complexity}
"""
    (directory / "README.md").write_text(problem_readme, encoding="utf-8")


def main() -> None:
    for index, (name, complexity) in enumerate(COMPLEXITIES.items(), start=1):
        directory = next(
            (path for path in LEETCODE_ROOT.rglob(name) if path.is_dir()), None
        )
        if directory is None:
            print(f"Skipping {index}/{len(COMPLEXITIES)}: {name} was not found")
            continue
        update_solution(directory, *complexity)
        print(f"Updated {index}/{len(COMPLEXITIES)}: {name}")
        time.sleep(0.1)


if __name__ == "__main__":
    main()
