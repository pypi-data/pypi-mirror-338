"""CLI module for GitLab Label Mover.

This module handles command-line arguments and user interaction.
"""

from __future__ import annotations

import argparse
import logging
from typing import Optional

from . import __version__, __author__

logger: logging.Logger = logging.getLogger("gitlab-label-mover")


class CustomHelpFormatter(argparse.HelpFormatter):
    """Custom formatter for argparse help text with better indentation."""

    def __init__(
        self,
        prog: str,
        indent_increment: int = 2,
        max_help_position: int = 30,
        width: Optional[int] = None,
    ) -> None:
        super().__init__(prog, indent_increment, max_help_position, width)

    def _format_action_invocation(self, action: argparse.Action) -> str:
        """Format the action invocation part of the help text."""
        if not action.option_strings:
            default = self._get_default_metavar_for_positional(action)
            (metavar,) = self._metavar_formatter(action, default)(1)
            return metavar

        else:
            parts = []

            # If the action is a store_true action, don't add metavar
            if action.nargs == 0:
                parts.extend(action.option_strings)
            else:
                default = self._get_default_metavar_for_optional(action)
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append(f"{option_string} {args_string}")

            return ", ".join(parts)


def configure_logging(debug: bool = False) -> None:
    """Configure logging based on debug flag.

    Args:
        debug: Whether to enable debug logging
    """
    log_level = logging.DEBUG if debug else logging.INFO
    logger.setLevel(log_level)


def determine_operation_mode(execute: bool = False) -> bool:
    """Determine whether to run in dry-run or execute mode.

    Args:
        execute: Whether to execute changes

    Returns:
        False if execute mode, True if dry-run mode
    """
    dry_run = not execute

    if dry_run:
        logger.info("Running in PREVIEW mode. No changes will be made.")
        logger.info("Use --execute to perform the actual migration.")
    else:
        logger.info("Running in EXECUTE mode. Changes will be applied to GitLab.")

    return dry_run


def extract_config_parameters(
    args: argparse.Namespace,
) -> tuple[bool, bool, str | None, str | None, str | None]:
    """Extract configuration parameters from command-line arguments.

    Args:
        args: Command-line arguments

    Returns:
        A tuple containing (dry_run, create_backup, env_file, project_id_override, group_id_override)
    """
    dry_run = determine_operation_mode(args.execute)
    create_backup = args.backup
    env_file = args.env_file
    project_id_override = args.project_id
    group_id_override = args.group_id

    return dry_run, create_backup, env_file, project_id_override, group_id_override


def setup_application() -> tuple[bool, bool, str | None, str | None, str | None]:
    """Set up the application by parsing command-line arguments and configuring logging.

    Returns:
        A tuple containing (dry_run, create_backup, env_file, project_id_override, group_id_override)
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        prog="gitlab-label-mover",
        description=f"GitLab Label Mover v{__version__} - Migrate labels from a project to a group\nDeveloped by {__author__}",
        formatter_class=lambda prog: CustomHelpFormatter(prog, max_help_position=35),
        epilog="By default, configuration is read from .env file in the current directory.",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Execute the migration (without this flag, only a preview is shown)",
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Create a backup of labels before migration",
    )
    parser.add_argument(
        "--env-file",
        type=str,
        help="Path to a custom environment file (default: .env)",
    )
    parser.add_argument(
        "--project-id",
        type=str,
        help="Override the project ID from the environment file",
    )
    parser.add_argument(
        "--group-id",
        type=str,
        help="Override the group ID from the environment file",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable detailed debug logging",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"GitLab Label Mover v{__version__}",
        help="Show version information and exit",
    )

    args = parser.parse_args()

    # Configure logging
    configure_logging(args.debug)

    # Extract configuration parameters
    return extract_config_parameters(args)
