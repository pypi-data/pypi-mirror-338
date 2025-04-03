"""GitLab Label Mover - Migrate labels from a project to a group.

This script allows you to migrate labels from a GitLab project to a group,
updating all issues and merge requests to use the new group labels.

By default, it runs in dry-run mode to preview changes without executing them.
Use the --execute flag to actually perform the migration.
"""

from __future__ import annotations

import logging
import sys

from .cli import setup_application
from .core import perform_label_migration

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger: logging.Logger = logging.getLogger("gitlab-label-mover")


def main() -> int:
    """Execute the GitLab label migration process.

    Returns:
        Exit code (0 for success, 1 for error)
    """
    # Get all parameters from setup_application
    dry_run, env_file, project_id_override, group_id_override, create_backup = setup_application()

    # Call the migration function with the parameters
    return perform_label_migration(
        dry_run=dry_run,
        env_file=env_file,
        project_id_override=project_id_override,
        group_id_override=group_id_override,
        create_backup=create_backup,
    )


if __name__ == "__main__":
    sys.exit(main())
