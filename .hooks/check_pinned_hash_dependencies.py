#!/usr/bin/env python
import re
import sys
from pathlib import Path
from typing import List, Tuple


class GitHubActionChecker:
    def __init__(self):
        # Pattern for actions with SHA-1 hashes (pinned)
        self.pinned_pattern = re.compile(r"uses:\s+([^@\s]+)@([a-f0-9]{40})")

        # Pattern for actions with version tags (unpinned)
        self.unpinned_pattern = re.compile(
            r"uses:\s+([^@\s]+)@(v\d+(?:\.\d+)*(?:-[a-zA-Z0-9]+(?:\.\d+)*)?)"
        )

        # Pattern for all uses statements
        self.all_uses_pattern = re.compile(r"uses:\s+([^@\s]+)@([^\s\n]+)")

    def format_terminal_link(self, file_path: str, line_number: int) -> str:
        """Format a terminal link to a file and line number.

        Args:
            file_path: Path to the file
            line_number: Line number in the file

        Returns:
            str: Formatted string with file path and line number
        """
        return f"{file_path}:{line_number}"

    def get_line_numbers(self, content: str, pattern: re.Pattern) -> List[Tuple[str, int]]:
        """Find matches with their line numbers."""
        matches = []
        for i, line in enumerate(content.splitlines(), 1):
            for match in pattern.finditer(line):
                matches.append((match.group(0), i))
        return matches

    def check_file(self, file_path: str) -> bool:
        """Check a single file for unpinned dependencies."""
        try:
            content = Path(file_path).read_text()
        except Exception as e:
            print(f"\033[91mError reading file {file_path}: {e}\033[0m")
            return False

        # Get matches with line numbers
        pinned_matches = self.get_line_numbers(content, self.pinned_pattern)
        unpinned_matches = self.get_line_numbers(content, self.unpinned_pattern)
        all_matches = self.get_line_numbers(content, self.all_uses_pattern)

        print(f"\n\033[1m[=] Checking file: {file_path}\033[0m")

        # Print pinned dependencies
        if pinned_matches:
            print("\033[92m[+] Pinned:\033[0m")
            for match, line_num in pinned_matches:
                print(f" |- {match} \033[90m({file_path}:{line_num})\033[0m")

        # Track all found actions for validation
        found_actions = set()
        for match, _ in pinned_matches + unpinned_matches:
            action_name = self.pinned_pattern.match(match) or self.unpinned_pattern.match(match)
            if action_name:
                found_actions.add(action_name.group(1))

        has_errors = False

        # Check for unpinned dependencies
        if unpinned_matches:
            has_errors = True
            print("\033[93m[!] Unpinned (using version tags):\033[0m")
            for match, line_num in unpinned_matches:
                print(f" |- {match} \033[90m({file_path}:{line_num})\033[0m")

        # Check for completely unpinned dependencies (no SHA or version)
        unpinned_without_hash = [
            (match, line_num)
            for match, line_num in all_matches
            if not any(match in pinned[0] for pinned in pinned_matches)
            and not any(match in unpinned[0] for unpinned in unpinned_matches)
        ]

        if unpinned_without_hash:
            has_errors = True
            print("\033[91m[!] Completely unpinned (no SHA or version):\033[0m")
            for match, line_num in unpinned_without_hash:
                print(
                    f" |- {match} \033[90m({self.format_terminal_link(file_path, line_num)})\033[0m"
                )

        # Print summary
        total_actions = len(pinned_matches) + len(unpinned_matches) + len(unpinned_without_hash)
        if total_actions == 0:
            print("\033[93m[!] No GitHub Actions found in this file\033[0m")
        else:
            print("\n\033[1mSummary:\033[0m")
            print(f"Total actions: {total_actions}")
            print(f"Pinned: {len(pinned_matches)}")
            print(f"Unpinned with version: {len(unpinned_matches)}")
            print(f"Completely unpinned: {len(unpinned_without_hash)}")

        return not has_errors


def main():
    checker = GitHubActionChecker()
    files_to_check = sys.argv[1:]

    if not files_to_check:
        print("\033[91mError: No files provided to check\033[0m")
        print("Usage: python script.py <file1> <file2> ...")
        sys.exit(1)

    results = {file: checker.check_file(file) for file in files_to_check}

    # Print final summary
    print("\n\033[1mFinal Results:\033[0m")
    for file, passed in results.items():
        status = "\033[92m✓ Passed\033[0m" if passed else "\033[91m✗ Failed\033[0m"
        print(f"{status} {file}")

    if not all(results.values()):
        sys.exit(1)


if __name__ == "__main__":
    main()
