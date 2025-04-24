#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "rigging",
#     "typer",
# ]
# ///
import asyncio
import os
import typing as t

import rigging as rg
import typer

TRUNCATION_WARNING = (
    "\n---\n**Note**: Due to the large size of this diff, some content has been truncated."
)


@rg.prompt
def generate_pr_description(diff: str) -> t.Annotated[str, rg.Ctx("markdown")]:  # type: ignore[empty-body]
    """
    Analyze the provided git diff and create a PR description in markdown format.
    <guidance>
    - Keep the summary concise and informative.
    - Use bullet points to structure important statements.
    - Focus on key modifications and potential impact - if any.
    - Do not add in general advice or best-practice information.
    - Write like a developer who authored the changes.
    - Prefer flat bullet lists over nested.
    - Do not include any title structure.
    - If there are no changes, just provide "No relevant changes."
    - Order your bullet points by importance.
    </guidance>
    """


async def _run_git_command(args: list[str]) -> str:
    """
    Safely run a git command with validated input.
    """
    # Validate git exists in PATH
    git_path = "git"  # Could use shutil.which("git") for more security
    if not any(
        os.path.isfile(os.path.join(path, "git")) for path in os.environ["PATH"].split(os.pathsep)
    ):
        raise ValueError("Git executable not found in PATH")

    # Validate input parameters
    if not all(isinstance(arg, str) for arg in args):
        raise ValueError("All command arguments must be strings")

    # Use os.execv for more secure command execution
    try:
        # nosec B603 - Input is validated
        proc = await asyncio.create_subprocess_exec(
            git_path,
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()

        if proc.returncode != 0:
            raise RuntimeError(f"Git command failed: {stderr.decode()}")

        return stdout.decode().strip()
    except Exception as e:
        raise RuntimeError(f"Failed to execute git command: {e}")


async def get_diff(base_ref: str, source_ref: str, *, exclude: list[str] | None = None) -> str:
    """
    Get the git diff between two branches.
    """
    # Validate refs
    for ref in (base_ref, source_ref):
        if not isinstance(ref, str) or not ref.strip():
            raise ValueError("Invalid git reference")

    # Get merge base
    merge_base = await _run_git_command(["merge-base", source_ref, base_ref])

    # Prepare diff command
    diff_command = ["diff", "--no-color", merge_base, source_ref]
    if exclude:
        validated_excludes = []
        for path in exclude:
            # Validate path
            if not isinstance(path, str) or ".." in path:
                raise ValueError(f"Invalid exclude path: {path}")
            validated_excludes.append(f":(exclude){path}")
        diff_command.extend(["--", ".", *validated_excludes])

    # Get diff
    return await _run_git_command(diff_command)


def main(
    base_ref: str = "origin/main",
    source_ref: str = "HEAD",
    generator_id: str = "openai/gpt-4o-mini",
    max_diff_lines: int = 1000,
    exclude: list[str] | None = None,
) -> None:
    """
    Use rigging to generate a PR description from a git diff.
    """
    diff = asyncio.run(get_diff(base_ref, source_ref, exclude=exclude))
    diff_lines = diff.split("\n")
    if len(diff_lines) > max_diff_lines:
        diff = "\n".join(diff_lines[:max_diff_lines]) + TRUNCATION_WARNING
    description = asyncio.run(generate_pr_description.bind(generator_id)(diff))
    print(description)


if __name__ == "__main__":
    typer.run(main)
