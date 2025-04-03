"""Visualization module for GitLab Label Mover.

This module handles displaying tree structures and other visual elements.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from gitlab import Gitlab
    from gitlab.v4.objects import Group, Project

logger: logging.Logger = logging.getLogger("gitlab-label-mover")


def get_group_hierarchy(gl: Gitlab, group_id: int) -> list[Group]:
    """Get the hierarchy of groups from the given group up to the root.

    Args:
        gl: GitLab client instance
        group_id: The ID of the group to start from

    Returns:
        A list of groups representing the hierarchy, with the root group first
    """
    hierarchy = []
    current_group = gl.groups.get(group_id)
    hierarchy.append(current_group)

    # Traverse up the hierarchy until we reach a group with no parent
    while current_group.parent_id is not None:
        current_group = gl.groups.get(current_group.parent_id)
        hierarchy.append(current_group)

    # Reverse the list so the root group is first
    hierarchy.reverse()
    return hierarchy


def get_project_and_namespace(gl: Gitlab, project_id: int) -> tuple[Project, int]:
    """Get the project and its namespace ID.

    Args:
        gl: GitLab client instance
        project_id: The ID of the source project

    Returns:
        A tuple containing (project, namespace_id)
    """
    project = gl.projects.get(project_id)
    project_namespace = project.namespace["id"]
    return project, project_namespace


def check_root_in_hierarchy(gl: Gitlab, hierarchy: list[Group], root_group_id: int) -> None:
    """Check if the root group is in the hierarchy and log a message if not.

    Args:
        gl: GitLab client instance
        hierarchy: The group hierarchy
        root_group_id: The ID of the root group
    """
    root_in_hierarchy = any(group.id == root_group_id for group in hierarchy)

    if not root_in_hierarchy:
        # If the root group is not in the hierarchy, get its details separately
        root_group = gl.groups.get(root_group_id)
        logger.info(
            f"Note: The destination group '{root_group.name}' is not in the project's hierarchy.",
        )


def print_group_hierarchy(hierarchy: list[Group], root_group_id: int, project: Project) -> None:
    """Print the group hierarchy as a tree structure.

    Args:
        hierarchy: The group hierarchy
        root_group_id: The ID of the root group
        project: The source project
    """
    logger.info("Group hierarchy:")

    for i, group in enumerate(hierarchy):
        prefix = "  " * i
        marker = "└─ " if i > 0 else ""
        logger.info(f"{prefix}{marker}Group: {group.name} (ID: {group.id})")

        # Highlight if this is the destination group
        if group.id == root_group_id:
            logger.info(f"{prefix}  └─ [DESTINATION GROUP]")

    # Add the project at the end
    prefix = "  " * len(hierarchy)
    logger.info(f"{prefix}└─ Project: {project.name} (ID: {project.id}) [SOURCE PROJECT]")


def display_tree_structure(gl: Gitlab, project_id: int, root_group_id: int) -> None:
    """Display the tree structure between the root group and the source project.

    Args:
        gl: GitLab client instance
        project_id: The ID of the source project
        root_group_id: The ID of the root group
    """
    # Get project and namespace
    project, project_namespace = get_project_and_namespace(gl, project_id)

    # Get the hierarchy from the project's parent group up to the root
    hierarchy = get_group_hierarchy(gl, project_namespace)

    # Check if the root group is in the hierarchy
    check_root_in_hierarchy(gl, hierarchy, root_group_id)

    # Print the hierarchy as a tree structure
    print_group_hierarchy(hierarchy, root_group_id, project)


def display_initial_context(gl: Gitlab, project_id: int, root_group_id: int) -> None:
    """Display the source and destination information with hierarchy at the beginning of migration.

    This function provides users with context about the migration operation by showing
    the source project, destination group, and their hierarchical relationship.

    Args:
        gl: GitLab client instance
        project_id: The ID of the source project
        root_group_id: The ID of the root group
    """
    try:
        # We need minimal project and group info to display the tree
        project = gl.projects.get(project_id)
        root_group = gl.groups.get(root_group_id)
        logger.info(f"Source Project: {project.name} (ID: {project_id})")
        logger.info(f"Destination Group: {root_group.name} (ID: {root_group_id})")
        display_tree_structure(gl, project_id, root_group_id)
    except (ValueError, KeyError, AttributeError) as tree_error:
        # Don't fail the whole operation if tree display fails
        logger.warning(f"Could not display group hierarchy: {tree_error}")


def log_migration_header(subgroup_project: Project, root_group: Group) -> None:
    """Log the migration header with source and destination information.

    Args:
        subgroup_project: The source project
        root_group: The destination group
    """
    logger.info(f"Migration: Source='{subgroup_project.name}' → Destination='{root_group.name}'")


def log_no_labels_to_migrate(issues: list[Any], merge_requests: list[Any]) -> None:
    """Log a message when there are no labels to migrate.

    Args:
        issues: List of issues in the project
        merge_requests: List of merge requests in the project
    """
    logger.info("No labels to migrate.")
    logger.info(f"Project has {len(issues)} issues and {len(merge_requests)} merge requests.")
    logger.info("No changes will be made.")
