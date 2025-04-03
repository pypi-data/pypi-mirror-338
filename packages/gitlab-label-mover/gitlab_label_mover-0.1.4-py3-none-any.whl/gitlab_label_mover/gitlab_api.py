"""GitLab API interaction module for GitLab Label Mover.

This module handles connecting to GitLab and fetching resources.
"""

from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING

import gitlab
from gitlab import Gitlab
from gitlab.exceptions import GitlabAuthenticationError, GitlabConnectionError, GitlabError

if TYPE_CHECKING:
    from gitlab.v4.objects import Group, GroupLabel, Issue, MergeRequest, Project, ProjectLabel

logger: logging.Logger = logging.getLogger("gitlab-label-mover")


def connect_to_gitlab_safely(gitlab_url: str, private_token: str) -> Gitlab | None:
    """Connect to GitLab with error handling.

    Args:
        gitlab_url: The GitLab URL
        private_token: The GitLab private token

    Returns:
        A GitLab client instance if successful, None otherwise
    """
    try:
        logger.info(f"Connecting to GitLab at {gitlab_url}")
        gl = gitlab.Gitlab(gitlab_url, private_token=private_token)
        gl.auth()
        logger.info(f"Connected to GitLab as {gl.user.username}")
        return gl
    except GitlabAuthenticationError as e:
        logger.error(f"Authentication error: {e}")
        logger.error("Please check your GitLab token and try again.")
        return None
    except GitlabConnectionError as e:
        logger.error(f"Connection error: {e}")
        logger.error("Please check your GitLab URL and internet connection.")
        return None
    except GitlabError as e:
        logger.error(f"GitLab API error: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error connecting to GitLab: {e}")
        return None


def get_project(gl: Gitlab, project_id: str) -> Project | None:
    """Get a GitLab project by ID.

    Args:
        gl: GitLab client instance
        project_id: The project ID

    Returns:
        The project if found, None otherwise
    """
    try:
        logger.info(f"Fetching project with ID {project_id}")
        project = gl.projects.get(project_id)
        logger.info(f"Found project: {project.name}")
        return project
    except GitlabError as e:
        logger.error(f"Error fetching project: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error fetching project: {e}")
        return None


def get_group(gl: Gitlab, group_id: str) -> Group | None:
    """Get a GitLab group by ID.

    Args:
        gl: GitLab client instance
        group_id: The group ID

    Returns:
        The group if found, None otherwise
    """
    try:
        logger.info(f"Fetching group with ID {group_id}")
        group = gl.groups.get(group_id)
        logger.info(f"Found group: {group.name}")
        return group
    except GitlabError as e:
        logger.error(f"Error fetching group: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error fetching group: {e}")
        return None


def get_project_labels(project: Project) -> list[ProjectLabel]:
    """Get all labels from a project.

    Args:
        project: The GitLab project

    Returns:
        A list of project labels
    """
    try:
        logger.info(f"Fetching labels from project {project.name}")
        labels = project.labels.list(all=True)
        logger.info(f"Found {len(labels)} labels in project {project.name}")
        return labels
    except GitlabError as e:
        logger.error(f"Error fetching project labels: {e}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error fetching project labels: {e}")
        return []


def get_group_labels(group: Group) -> list[GroupLabel]:
    """Get all labels from a group.

    Args:
        group: The GitLab group

    Returns:
        A list of group labels
    """
    try:
        logger.info(f"Fetching labels from group {group.name}")
        labels = group.labels.list(all=True)
        logger.info(f"Found {len(labels)} labels in group {group.name}")
        return labels
    except GitlabError as e:
        logger.error(f"Error fetching group labels: {e}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error fetching group labels: {e}")
        return []


def get_all_issues(project: Project) -> list[Issue]:
    """Get all issues from a project with proper pagination.

    Args:
        project: The GitLab project

    Returns:
        A list of issues
    """
    try:
        logger.info(f"Fetching issues from project {project.name}")
        issues = []
        page = 1
        per_page = 100

        while True:
            batch = project.issues.list(page=page, per_page=per_page)
            if not batch:
                break

            issues.extend(batch)
            logger.debug(f"Fetched {len(batch)} issues (page {page})")

            if len(batch) < per_page:
                break

            page += 1
            time.sleep(0.5)  # Avoid rate limiting

        logger.info(f"Found {len(issues)} issues in project {project.name}")
        return issues
    except GitlabError as e:
        logger.error(f"Error fetching project issues: {e}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error fetching project issues: {e}")
        return []


def get_all_merge_requests(project: Project) -> list[MergeRequest]:
    """Get all merge requests from a project with proper pagination.

    Args:
        project: The GitLab project

    Returns:
        A list of merge requests
    """
    try:
        logger.info(f"Fetching merge requests from project {project.name}")
        merge_requests = []
        page = 1
        per_page = 100

        while True:
            batch = project.mergerequests.list(page=page, per_page=per_page)
            if not batch:
                break

            merge_requests.extend(batch)
            logger.debug(f"Fetched {len(batch)} merge requests (page {page})")

            if len(batch) < per_page:
                break

            page += 1
            time.sleep(0.5)  # Avoid rate limiting

        logger.info(f"Found {len(merge_requests)} merge requests in project {project.name}")
        return merge_requests
    except GitlabError as e:
        logger.error(f"Error fetching project merge requests: {e}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error fetching project merge requests: {e}")
        return []


def get_resources_for_migration(
    gl: Gitlab, subgroup_project_id: str, root_group_id: str
) -> tuple[Project, Group, list[ProjectLabel], list[Issue], list[MergeRequest]] | None:
    """Get all resources needed for migration.

    Args:
        gl: GitLab client instance
        subgroup_project_id: The ID of the source project
        root_group_id: The ID of the destination group

    Returns:
        A tuple containing (subgroup_project, root_group, project_labels, issues, merge_requests) if successful,
        None otherwise
    """
    # Get project and group
    subgroup_project = get_project(gl, subgroup_project_id)
    if not subgroup_project:
        return None

    root_group = get_group(gl, root_group_id)
    if not root_group:
        return None

    # Get labels, issues, and merge requests
    project_labels = get_project_labels(subgroup_project)
    issues = get_all_issues(subgroup_project)
    merge_requests = get_all_merge_requests(subgroup_project)

    return subgroup_project, root_group, project_labels, issues, merge_requests
