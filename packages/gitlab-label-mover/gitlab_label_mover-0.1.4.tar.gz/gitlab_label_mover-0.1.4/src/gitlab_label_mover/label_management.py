"""Label management module for GitLab Label Mover.

This module handles comparing, migrating, and managing labels.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gitlab.v4.objects import Group, GroupLabel, Issue, MergeRequest, Project, ProjectLabel

logger: logging.Logger = logging.getLogger("gitlab-label-mover")


def compare_labels(
    project_labels: list[ProjectLabel], group_labels: list[GroupLabel]
) -> tuple[list[ProjectLabel], list[str]]:
    """Compare project labels with group labels to find labels that need to be migrated.

    Args:
        project_labels: List of project labels
        group_labels: List of group labels

    Returns:
        A tuple containing (labels_to_migrate, existing_label_names)
    """
    # Get existing group label names
    existing_label_names = [label.name for label in group_labels]

    # Find labels that don't exist in the group
    labels_to_migrate = [
        label for label in project_labels if label.name not in existing_label_names
    ]

    logger.info(f"Found {len(labels_to_migrate)} labels to migrate")
    logger.debug(f"Labels to migrate: {', '.join(label.name for label in labels_to_migrate)}")

    if existing_label_names:
        logger.debug(f"Existing group labels: {', '.join(existing_label_names)}")

    return labels_to_migrate, existing_label_names


def create_label_backup(project_labels: list[ProjectLabel], backup_path: Path) -> None:
    """Create a backup of project labels.

    Args:
        project_labels: List of project labels
        backup_path: Path to save the backup file
    """
    try:
        # Convert labels to a serializable format
        labels_data = [
            {
                "name": label.name,
                "color": label.color,
                "description": label.description if hasattr(label, "description") else "",
            }
            for label in project_labels
        ]

        # Write to file
        with open(backup_path, "w") as f:
            json.dump(labels_data, f, indent=2)

        logger.info(f"Created backup of {len(project_labels)} labels at {backup_path}")
    except Exception as e:
        logger.error(f"Error creating label backup: {e}")


def create_backup_if_needed(
    resources: tuple[Project, Group, list[ProjectLabel], list[Issue], list[MergeRequest]],
    create_backup: bool,
    dry_run: bool,
) -> None:
    """Create a backup of labels if requested.

    Args:
        resources: A tuple containing (subgroup_project, root_group, project_labels, issues, merge_requests)
        create_backup: Whether to create a backup
        dry_run: Whether this is a dry run
    """
    if not create_backup:
        return

    subgroup_project, _, project_labels, _, _ = resources

    if dry_run:
        logger.info("Backup would be created in execute mode")
        return

    # Create backup directory if it doesn't exist
    backup_dir = Path("backups")
    backup_dir.mkdir(exist_ok=True)

    # Create backup file
    backup_path = backup_dir / f"labels_backup_{subgroup_project.id}_{subgroup_project.name}.json"
    create_label_backup(project_labels, backup_path)


def migrate_labels(
    labels_to_migrate: list[ProjectLabel], root_group: Group, dry_run: bool
) -> list[GroupLabel]:
    """Migrate labels from a project to a group.

    Args:
        labels_to_migrate: List of labels to migrate
        root_group: The destination group
        dry_run: Whether to perform a dry run

    Returns:
        A list of created group labels
    """
    created_labels = []

    for label in labels_to_migrate:
        label_name = label.name
        label_color = label.color
        label_description = label.description if hasattr(label, "description") else ""

        if dry_run:
            logger.info(
                f"Would create label '{label_name}' with color '{label_color}' in group '{root_group.name}'"
            )
            continue

        try:
            logger.info(f"Creating label '{label_name}' in group '{root_group.name}'")
            new_label = root_group.labels.create(
                {"name": label_name, "color": label_color, "description": label_description}
            )
            created_labels.append(new_label)
        except Exception as e:
            logger.error(f"Error creating label '{label_name}': {e}")

    return created_labels
