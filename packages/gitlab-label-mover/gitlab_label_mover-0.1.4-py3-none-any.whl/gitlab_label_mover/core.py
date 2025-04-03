"""Core module for GitLab Label Mover.

This module implements the main business logic.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from .config import load_and_validate_config
from .gitlab_api import connect_to_gitlab_safely, get_group_labels, get_resources_for_migration
from .label_management import compare_labels, create_backup_if_needed, migrate_labels
from .resource_management import filter_resources_by_labels, update_resources
from .visualization import (
    display_initial_context,
    log_migration_header,
    log_no_labels_to_migrate,
)

if TYPE_CHECKING:
    from gitlab.v4.objects import Group, Issue, MergeRequest, Project, ProjectLabel

logger: logging.Logger = logging.getLogger("gitlab-label-mover")


def check_for_labels_to_migrate(
    project_labels: list[ProjectLabel],
    issues: list[Issue],
    merge_requests: list[MergeRequest],
) -> bool:
    """Check if there are any labels to migrate.

    Args:
        project_labels: List of project labels
        issues: List of issues
        merge_requests: List of merge requests

    Returns:
        True if there are no labels to migrate, False otherwise
    """
    if not project_labels:
        log_no_labels_to_migrate(issues, merge_requests)
        return True
    return False


def prepare_labels_for_migration(
    project_labels: list[ProjectLabel],
    root_group: Group,
    issues: list[Issue],
    merge_requests: list[MergeRequest],
) -> tuple[list[ProjectLabel], list[str]] | None:
    """Prepare labels for migration by comparing project labels with group labels.

    Args:
        project_labels: List of project labels
        root_group: The destination group
        issues: List of issues
        merge_requests: List of merge requests

    Returns:
        A tuple containing (labels_to_migrate, existing_label_names) if there are labels to migrate,
        None otherwise
    """
    # Get existing group labels
    group_labels = get_group_labels(root_group)

    # Compare labels to find ones that need to be migrated
    labels_to_migrate, existing_label_names = compare_labels(project_labels, group_labels)

    # If there are no labels to migrate, we're done
    if not labels_to_migrate:
        log_no_labels_to_migrate(issues, merge_requests)
        return None

    return labels_to_migrate, existing_label_names


def process_label_migration(
    labels_to_migrate: list[ProjectLabel],
    root_group: Group,
    dry_run: bool,
) -> tuple[list[str], list[str]]:
    """Process the actual label migration.

    Args:
        labels_to_migrate: List of labels to migrate
        root_group: The destination group
        dry_run: Whether to perform a dry run

    Returns:
        A tuple containing (migrated_label_names, created_label_names)
    """
    # Migrate labels
    created_labels = migrate_labels(labels_to_migrate, root_group, dry_run)

    # Get label names for filtering and updating resources
    migrated_label_names = [label.name for label in labels_to_migrate]
    created_label_names = (
        [label.name for label in created_labels] if not dry_run else migrated_label_names
    )

    return migrated_label_names, created_label_names


def process_resource_updates(
    issues: list[Issue],
    merge_requests: list[MergeRequest],
    migrated_label_names: list[str],
    created_label_names: list[str],
    dry_run: bool,
) -> tuple[int, int]:
    """Process updates to issues and merge requests.

    Args:
        issues: List of issues
        merge_requests: List of merge requests
        migrated_label_names: List of migrated label names
        created_label_names: List of created label names
        dry_run: Whether to perform a dry run

    Returns:
        A tuple containing (updated_issues_count, updated_merge_requests_count)
    """
    # Filter resources by migrated labels
    filtered_issues = filter_resources_by_labels(issues, migrated_label_names)
    filtered_merge_requests = filter_resources_by_labels(merge_requests, migrated_label_names)

    # Log the number of resources that will be updated
    logger.info(
        f"Found {len(filtered_issues)} issues and {len(filtered_merge_requests)} merge requests to update"
    )

    # Update resources
    updated_issues = update_resources(
        filtered_issues, migrated_label_names, created_label_names, dry_run
    )
    updated_mrs = update_resources(
        filtered_merge_requests, migrated_label_names, created_label_names, dry_run
    )

    return updated_issues, updated_mrs


def log_migration_summary(created_label_count: int, updated_issues: int, updated_mrs: int) -> None:
    """Log a summary of the migration.

    Args:
        created_label_count: Number of labels created
        updated_issues: Number of issues updated
        updated_mrs: Number of merge requests updated
    """
    logger.info(f"Migration complete: {created_label_count} labels migrated")
    logger.info(f"Updated {updated_issues} issues and {updated_mrs} merge requests")


def perform_migration(
    resources: tuple[Project, Group, list[ProjectLabel], list[Issue], list[MergeRequest]],
    dry_run: bool,
) -> bool:
    """Perform the actual migration steps.

    Args:
        resources: A tuple containing (subgroup_project, root_group, project_labels, issues, merge_requests)
        dry_run: Whether to perform a dry run (preview only)

    Returns:
        True if successful, False otherwise
    """
    subgroup_project, root_group, project_labels, issues, merge_requests = resources

    # Log migration header
    log_migration_header(subgroup_project, root_group)

    # Check if there are any labels to migrate
    if check_for_labels_to_migrate(project_labels, issues, merge_requests):
        return True

    # Prepare labels for migration
    migration_data = prepare_labels_for_migration(
        project_labels, root_group, issues, merge_requests
    )
    if migration_data is None:
        return True

    labels_to_migrate, _ = migration_data

    # Process label migration
    migrated_label_names, created_label_names = process_label_migration(
        labels_to_migrate, root_group, dry_run
    )

    # Process resource updates
    updated_issues, updated_mrs = process_resource_updates(
        issues, merge_requests, migrated_label_names, created_label_names, dry_run
    )

    # Log summary
    log_migration_summary(len(labels_to_migrate), updated_issues, updated_mrs)

    return True


def perform_label_migration(
    dry_run: bool = True,
    env_file: str | None = None,
    project_id_override: str | None = None,
    group_id_override: str | None = None,
    create_backup: bool = False,
) -> int:
    """Migrate labels from a project to a group.

    Args:
        dry_run: Whether to perform a dry run (preview only)
        env_file: Optional path to a custom environment file
        project_id_override: Optional project ID to override the one from config
        group_id_override: Optional group ID to override the one from config
        create_backup: Whether to create a backup of labels before migration

    Returns:
        Exit code (0 for success, 1 for error)
    """
    try:
        # Load and validate configuration
        config = load_and_validate_config(env_file, project_id_override, group_id_override)
        if config is None:
            return 1

        gitlab_url, private_token, subgroup_project_id, root_group_id = config

        # Connect to GitLab
        gl = connect_to_gitlab_safely(gitlab_url, private_token)
        if gl is None:
            return 1

        # Display initial context to give users information about the migration
        display_initial_context(gl, int(subgroup_project_id), int(root_group_id))

        # Get resources for migration
        resources = get_resources_for_migration(gl, subgroup_project_id, root_group_id)
        if resources is None:
            return 1

        # Create backup if requested
        create_backup_if_needed(resources, create_backup, dry_run)

        # Perform the migration
        if not perform_migration(
            resources,
            dry_run,
        ):
            return 1

        return 0
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return 1
