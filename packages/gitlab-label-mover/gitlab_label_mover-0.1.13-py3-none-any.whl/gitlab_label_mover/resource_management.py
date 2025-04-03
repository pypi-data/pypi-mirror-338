"""Resource management module for GitLab Label Mover.

This module handles issues and merge requests.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gitlab.v4.objects import Issue, MergeRequest

logger: logging.Logger = logging.getLogger("gitlab-label-mover")


def filter_resources_by_labels(
    resources: list[Issue] | list[MergeRequest], migrated_label_names: list[str]
) -> list[Issue] | list[MergeRequest]:
    """Filter resources by labels that were migrated.

    Args:
        resources: List of issues or merge requests
        migrated_label_names: List of label names that were migrated

    Returns:
        A list of resources that have at least one of the migrated labels
    """
    # Use list comprehension for better performance
    filtered_resources = [
        resource
        for resource in resources
        if any(label in migrated_label_names for label in resource.labels)
    ]

    return filtered_resources


def update_resources(
    resources: list[Issue] | list[MergeRequest],
    project_label_names: list[str],
    group_label_names: list[str],
    dry_run: bool,
) -> int:
    """Update resources to use group labels instead of project labels.

    Args:
        resources: List of issues or merge requests
        project_label_names: List of project label names that were migrated
        group_label_names: List of group label names that were created
        dry_run: Whether to perform a dry run

    Returns:
        The number of resources that were updated
    """
    updated_count = 0
    resource_type = "issues" if resources and hasattr(resources[0], "iid") else "merge requests"

    for i, resource in enumerate(resources):
        # Get current labels
        current_labels = resource.labels

        # Check if any of the resource's labels were migrated
        if not any(label in project_label_names for label in current_labels):
            continue

        # Create new label list, replacing project labels with group labels
        new_labels = [
            label
            if label not in project_label_names
            else group_label_names[project_label_names.index(label)]
            for label in current_labels
        ]

        if dry_run:
            logger.info(
                f"Would update {resource_type[:-1]} #{resource.iid}: "
                f"Labels: {', '.join(current_labels)} → {', '.join(new_labels)}"
            )
            updated_count += 1
            continue

        try:
            # Show progress indicator every 10 resources
            if i % 10 == 0:
                logger.info(f"Updating {resource_type} ({i}/{len(resources)})...")

            # Update the resource
            resource.labels = new_labels
            resource.save()
            logger.debug(
                f"Updated {resource_type[:-1]} #{resource.iid}: "
                f"Labels: {', '.join(current_labels)} → {', '.join(new_labels)}"
            )
            updated_count += 1
        except Exception as e:
            logger.error(f"Error updating {resource_type[:-1]} #{resource.iid}: {e}")

    return updated_count
