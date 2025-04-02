"""The main module for the commit package."""

# ruff: noqa: T201
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any

from commit import commits, config, prompt

if TYPE_CHECKING:
    from collections.abc import Callable


def new_filter_function(options: list[str]) -> Callable[[str, int, list[str], dict[str, Any]], tuple[list[str], int]]:
    """A filter function that always keeps the last option in the list.

    Args:
        options (list[str]): The list of options to filter

    Returns:
        Callable[[str, int, list[str], dict[str, Any]], tuple[list[str], int]]: The filter function.
    """

    def fun(state: str, index: int, current_options: list[str], tags: dict[str, Any]) -> tuple[list[str], int]:
        """The filter function the be returned.

        Args:
            state (str): The current state of the prompt.
            index (int): The current index of the prompt.
            current_options (list[str]): The current options of the prompt.
            tags (dict[str, Any]): The tags of the prompt.

        Returns:
            tuple[list[str], int]: The filter result.
        """
        (new_options, new_index) = prompt.get_filter_rule(options)(state, index, current_options, tags)
        if current_options[-1] not in new_options:
            new_options.append(current_options[-1])
        return new_options, new_index

    return fun


def show_more_filter_function() -> Callable[[str, int, list[str], dict[str, Any]], tuple[list[str], int]]:
    """A filter function that shows more options when the last option is selected.

    Returns:
        Callable[[str, int, list[str], dict[str, Any]], tuple[list[str], int]]: The filter function.
    """

    def fun(state: str, index: int, current_options: list[str], tags: dict[str, Any]) -> tuple[list[str], int]:
        """The filter function the be returned.

        Args:
            state (str): The current state of the prompt.
            index (int): The current index of the prompt.
            current_options (list[str]): The current options of the prompt.
            tags (dict[str, Any]): The tags of the prompt.

        Returns:
            tuple[list[str], int]: The filter result.
        """
        current_selection = current_options[index]
        page = tags.get("page", 0)
        if index != 0 and current_options[index] == "...":
            page += 1
            tags["page"] = page
            index = 0
        new_options = commits.get_gitmojis(state, page * 7)
        if current_selection != "..." and current_selection in new_options:
            index = new_options.index(current_selection)
        else:
            index = 0
        return new_options, index

    return fun


def main() -> None:
    """The main function for the commit package."""
    parser = argparse.ArgumentParser(description="Write correct commit messages with gitmojis with ease.")
    parser.add_argument("-a", action="store_true", help="Stage all changes automatically.")
    parser.add_argument("--no-scope", "-n", action="store_true", help="Do not include a scope in the commit message.")
    parser.add_argument(
        "--footer",
        "-f",
        action="store_true",
        help="Include a footer in the commit message.",
    )
    parser.add_argument(
        "--breaking",
        "-b",
        action="store_true",
        help="Mark the commit as a breaking change.",
    )
    args = parser.parse_args()
    try:
        run(args.footer, args.breaking, args.a, args.no_scope)
    except KeyboardInterrupt:
        print("\nExiting...")


def run_precommit() -> bool:
    """Run the pre-commit hook.

    Returns:
        bool: A boolean indicating if the pre-commit hook was successful.
    """
    if not Path(".pre-commit-config.yaml").exists():
        return True
    result = subprocess.run(["pre-commit", "run"], capture_output=True, text=True, check=False)  # noqa: S607 S603
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
    return result.returncode == 0


def run(include_footer: bool, breaking_change: bool, stage_all: bool, no_scope: bool) -> None:
    """Run the commit process.

    Args:
        include_footer (bool): Determine if a footer should be included in the commit message.
        breaking_change (bool): Determine if the commit is a breaking change.
        stage_all (bool): Determine if all changes should be staged automatically.
        no_scope (bool): Determine if a scope should be included in the commit message.
    """
    if commits.get_repo() is None:
        print("Error: Not a git repository.")
        sys.exit(1)

    if not commits.get_stages_files():
        print("Error: No files selected to commit.")
        sys.exit(1)

    conf = config.find_config()

    if stage_all:
        subprocess.run(["git", "add", "."], check=False)  # noqa: S607 S603

    if not run_precommit():
        sys.exit(1)

    commit_types = commits.get_commit_types()
    (_, index, _) = prompt.show_with_filter(commit_types, "Select the type of change that you are committing: ")
    commit_type = commit_types[index].split(":")[0]

    if not no_scope:
        scopes = [*commits.get_possible_scopes(), "Create new scope from current input"]
        (text, index, _) = prompt.show(
            scopes,
            "Select the scope of the change that you are committing: ",
            on_update=new_filter_function(scopes),
        )
        scope = scopes[index] if index != len(scopes) - 1 else text
        scope = "" if scope == "None" else f"({scope})"
    else:
        scope = ""

    ok = False
    while not ok:
        msg = input("Select commit message: ")
        ok, msg = commits.check_commit_message(msg)
        if not ok:
            print("Invalid commit message format. Please try again or prepend '!'.")

    gitmojis = commits.get_gitmojis()
    (_, index, gitmoji) = prompt.show(
        gitmojis,
        "Choose a gitmoji: ",
        on_update=show_more_filter_function(),
        wrap_above=False,
        wrap_below=False,
    )
    gitmoji = gitmoji.split("-")[1].strip()

    print("(optional) Enter a longer description of the changes made in this commit (empty line to exit):")
    description = prompt.multiline_input()

    if include_footer or breaking_change or conf.enable_footer:
        footer = input("Footer information (referenced issues, breaking changes, etc.):\n")
    else:
        footer = ""

    breaking = "!" if breaking_change else ""

    full_message = f"{commit_type}{scope}:{breaking} {gitmoji} {msg}"
    if description:
        full_message += f"\n\n{description}"
    if footer:
        full_message += f"\n\n{footer}"

    result = subprocess.run(["git", "commit", "-m", full_message], capture_output=True, text=True, check=False)  # noqa: S603 S607
    if result.returncode != 0:
        print(result.stderr)
        print(result.stdout)
    else:
        print("Committed successfully:\n", full_message, sep="")


if __name__ == "__main__":
    main()
