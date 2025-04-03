"""Configuration module for GitLab Label Mover.

This module handles loading and validating configuration from environment files.
"""

from __future__ import annotations

import logging
import os
import shutil
import sys
from pathlib import Path

from dotenv import load_dotenv
from platformdirs import user_config_dir, user_data_dir

# Application constants
APP_NAME = "gitlab-label-mover"
APP_AUTHOR = "nkrusens"

logger: logging.Logger = logging.getLogger(APP_NAME)


def validate_url(url: str) -> str:
    """Validate a URL.

    Args:
        url: The URL to validate

    Returns:
        The validated URL

    Raises:
        ValueError: If the URL is invalid
    """
    if not url:
        raise ValueError("URL cannot be empty")

    if not url.startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")

    return url


def validate_token(token: str) -> str:
    """Validate a GitLab token.

    Args:
        token: The token to validate

    Returns:
        The validated token

    Raises:
        ValueError: If the token is invalid
    """
    if not token:
        raise ValueError("Token cannot be empty")

    if len(token) < 20:  # GitLab tokens are typically longer than 20 characters
        raise ValueError("Token seems too short to be valid")

    return token


def validate_id(id_str: str) -> str:
    """Validate a GitLab ID.

    Args:
        id_str: The ID to validate

    Returns:
        The validated ID

    Raises:
        ValueError: If the ID is invalid
    """
    if not id_str:
        raise ValueError("ID cannot be empty")

    try:
        int(id_str)  # Check if it can be converted to an integer
    except ValueError:
        raise ValueError(f"ID must be an integer, got {id_str!r}") from None

    return id_str


def log_config_file_not_found(custom_path: Path | None = None) -> None:
    """Log error messages when a configuration file is not found.

    Args:
        custom_path: Optional path to a custom configuration file that was not found
    """
    # Use application constants

    # Try to find the example.env file
    example_paths = [
        Path("example.env"),  # Current directory
        Path(__file__).parents[2] / "example.env",  # Package root
        Path(user_data_dir(APP_NAME, APP_AUTHOR)) / "example.env",  # User data directory
        Path(user_config_dir(APP_NAME, APP_AUTHOR)) / "example.env",  # User config directory
        Path(sys.prefix) / "share" / APP_NAME / "example.env",  # System share directory
    ]

    example_path = None
    for path in example_paths:
        if path.exists():
            example_path = path
            break

    if custom_path:
        logger.error(f"Error: Specified environment file '{custom_path}' not found.")
        logger.error("Please check the file path and try again.")
    else:
        logger.error("Error: No environment file (.env) found.")
        logger.error("Please create a .env file with your GitLab configuration:")

        if example_path:
            logger.error(f"  1. Copy the example file: cp {example_path} .env")
        else:
            logger.error("  1. Create a new .env file")

        logger.error("  2. Edit with your details: nano .env")
        logger.error("  3. Run the application again")

        if not example_path:
            logger.error("\nExample .env file content:")
            logger.error("GITLAB_URL=https://gitlab.com")
            logger.error("GITLAB_PRIVATE_TOKEN=your_private_token_here")
            logger.error("GITLAB_SUBGROUP_PROJECT_ID=12345")
            logger.error("GITLAB_ROOT_GROUP_ID=67890")


def find_config_file(config_path: str | None = None) -> tuple[Path | None, str]:
    """Find the configuration file to use.

    Args:
        config_path: Optional path to a custom configuration file

    Returns:
        A tuple containing (path_to_config_file, file_type) if found, (None, "") otherwise
        file_type is always "env" for environment files
    """
    # Check for specified config file first
    if config_path:
        custom_config_path = Path(config_path)
        if custom_config_path.exists():
            return custom_config_path, "env"

        log_config_file_not_found(custom_config_path)
        return None, ""

    # Look for .env file in the current directory
    env_path = Path(".env")
    if env_path.exists():
        return env_path, "env"

    # Fall back to .env file in the project root
    env_path = Path(__file__).parents[2] / ".env"
    if env_path.exists():
        return env_path, "env"

    # Try to create a template .env file
    try:
        # Use application constants

        # Find example.env file
        example_paths = [
            Path("example.env"),  # Current directory
            Path(__file__).parents[2] / "example.env",  # Package root
            Path(user_data_dir(APP_NAME, APP_AUTHOR)) / "example.env",  # User data directory
            Path(user_config_dir(APP_NAME, APP_AUTHOR)) / "example.env",  # User config directory
            Path(sys.prefix) / "share" / APP_NAME / "example.env",  # System share directory
        ]

        example_path = None
        for path in example_paths:
            if path.exists():
                example_path = path
                break

        if example_path:
            # Copy example.env to .env
            env_path = Path(".env")
            shutil.copy2(example_path, env_path)
            logger.info(f"Created template .env file in the current directory from {example_path}")
            logger.info("Please open the .env file in your text editor and follow the step-by-step instructions inside.")
            return env_path, "env"
    except Exception as e:
        logger.debug(f"Failed to create template .env file: {e}")

    log_config_file_not_found()
    return None, ""


def load_env_file(env_path: Path) -> bool:
    """Load environment variables from a .env file.

    Args:
        env_path: Path to the .env file

    Returns:
        True if successful, False otherwise
    """
    try:
        logger.info(f"Loading configuration from {env_path.name}")
        load_dotenv(env_path)
        return True
    except Exception as e:
        logger.error(f"Error loading environment file: {e}")
        logger.error("Please ensure the file exists and has the correct format.")
        return False


def load_configuration_file(env_file: str | None = None) -> bool:
    """Load the configuration file.

    Args:
        env_file: Optional path to a custom environment file

    Returns:
        True if the configuration file was loaded successfully, False otherwise
    """
    config_path, config_type = find_config_file(env_file)
    if not config_path:
        return False

    # Only .env files are supported currently
    return config_type == "env" and load_env_file(config_path)


def get_gitlab_url() -> str | None:
    """Get the GitLab URL from environment variables.

    Returns:
        The validated GitLab URL if found, None otherwise
    """
    try:
        return validate_url(os.getenv("GITLAB_URL", ""))
    except ValueError as e:
        logger.error(f"Invalid GitLab URL: {e}")
        return None


def get_gitlab_token() -> str | None:
    """Get the GitLab token from environment variables.

    Returns:
        The validated GitLab token if found, None otherwise
    """
    try:
        # Try both naming conventions for compatibility
        token = os.getenv("GITLAB_PRIVATE_TOKEN", "") or os.getenv("GITLAB_TOKEN", "")

        # Check if the token is still the template value
        if token in ["your_private_token_here", "your_private_token"]:
            logger.error("GitLab token is still set to the default placeholder value.")
            logger.error("Please check STEP 2 in the .env file for instructions on how to create a personal access token.")
            return None

        return validate_token(token)
    except ValueError as e:
        logger.error(f"Invalid GitLab token: {e}")
        return None


def get_project_id(project_id_override: str | None = None) -> str | None:
    """Get the project ID from environment variables or override.

    Args:
        project_id_override: Optional project ID to override the one from config

    Returns:
        The validated project ID if found, None otherwise
    """
    try:
        if project_id_override:
            return validate_id(project_id_override)

        # Try both naming conventions for compatibility
        project_id_env = os.getenv("GITLAB_SUBGROUP_PROJECT_ID", "") or os.getenv(
            "SUBGROUP_PROJECT_ID", ""
        )

        # Check if the project ID is still the template value
        if project_id_env in ["12345"]:
            logger.error("Project ID is still set to the default placeholder value.")
            logger.error("Please check STEP 3 in the .env file for instructions on how to find your project ID.")
            return None

        return validate_id(project_id_env)
    except ValueError as e:
        logger.error(f"Invalid project ID: {e}")
        return None


def get_group_id(group_id_override: str | None = None) -> str | None:
    """Get the group ID from environment variables or override.

    Args:
        group_id_override: Optional group ID to override the one from config

    Returns:
        The validated group ID if found, None otherwise
    """
    try:
        if group_id_override:
            return validate_id(group_id_override)

        # Try both naming conventions for compatibility
        group_id_env = os.getenv("GITLAB_ROOT_GROUP_ID", "") or os.getenv("ROOT_GROUP_ID", "")

        # Check if the group ID is still the template value
        if group_id_env in ["67890"]:
            logger.error("Group ID is still set to the default placeholder value.")
            logger.error("Please check STEP 4 in the .env file for instructions on how to find your group ID.")
            return None

        return validate_id(group_id_env)
    except ValueError as e:
        logger.error(f"Invalid group ID: {e}")
        return None


def log_missing_configuration() -> None:
    """Log helpful messages about missing configuration."""
    logger.error("Configuration is incomplete or invalid.")
    logger.error("")
    logger.error("Please open the .env file in your text editor and follow the step-by-step instructions inside.")
    logger.error("The file contains detailed guidance on how to obtain all required information.")
    logger.error("")
    logger.error("You can also:")
    logger.error("  - Use a custom environment file: --env-file path/to/custom.env")
    logger.error("  - Override specific IDs: --project-id 123 --group-id 456")


def get_gitlab_config(
    env_file: str | None = None,
    project_id_override: str | None = None,
    group_id_override: str | None = None,
) -> tuple[str, str, str, str] | None:
    """Get GitLab configuration from environment variables.

    Args:
        env_file: Optional path to a custom environment file
        project_id_override: Optional project ID to override the one from config
        group_id_override: Optional group ID to override the one from config

    Returns:
        A tuple containing (gitlab_url, private_token, subgroup_project_id, root_group_id) if successful,
        None otherwise
    """
    # Load configuration file
    if not load_configuration_file(env_file):
        return None

    # Get and validate configuration values
    gitlab_url = get_gitlab_url()
    private_token = get_gitlab_token()
    subgroup_project_id = get_project_id(project_id_override)
    root_group_id = get_group_id(group_id_override)

    # Check if all values are valid
    if None in (gitlab_url, private_token, subgroup_project_id, root_group_id):
        log_missing_configuration()
        return None

    # At this point, we know none of the values are None, but the type checker doesn't
    # So we need to assert that they are all strings
    assert gitlab_url is not None
    assert private_token is not None
    assert subgroup_project_id is not None
    assert root_group_id is not None

    return gitlab_url, private_token, subgroup_project_id, root_group_id


def load_and_validate_config(
    env_file: str | None = None,
    project_id_override: str | None = None,
    group_id_override: str | None = None,
) -> tuple[str, str, str, str] | None:
    """Load and validate configuration.

    Args:
        env_file: Optional path to a custom environment file
        project_id_override: Optional project ID to override the one from config
        group_id_override: Optional group ID to override the one from config

    Returns:
        A tuple containing (gitlab_url, private_token, subgroup_project_id, root_group_id) if successful,
        None otherwise
    """
    config = get_gitlab_config(env_file, project_id_override, group_id_override)
    if config is None:
        logger.error("Failed to load configuration.")
        logger.error("Please open the .env file and follow the detailed instructions inside.")
        return None

    return config
