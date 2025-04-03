# GitLab Label Mover

[![PyPI version](https://badge.fury.io/py/gitlab-label-mover.svg)](https://badge.fury.io/py/gitlab-label-mover)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/gitlab-label-mover.svg)](https://pypi.org/project/gitlab-label-mover/)

A tool to migrate labels from a GitLab project to a group, updating all issues and merge requests to use the new group labels. Developed by Nikolai von Krusenstiern.

## Features

- Migrate labels from a project to a group
- Update issues and merge requests to use the new group labels
- Dry-run mode to preview changes without executing them
- Support for custom environment files
- Backup option to create a backup of labels before migration

## Installation

### Prerequisites

- Python 3.9 or higher
- Required dependencies (automatically installed when using pip):
  - python-gitlab: For interacting with the GitLab API
  - python-dotenv: For loading environment variables from .env files

### Install from PyPI

The easiest way to install GitLab Label Mover is from PyPI:

```bash
pip install gitlab-label-mover
```

If you prefer using Poetry:

```bash
poetry add gitlab-label-mover
```

Or if you prefer using pipx for isolated installation:

```bash
pipx install gitlab-label-mover
```

### Install from Source

Alternatively, you can install from source:

1. Clone the repository:

   ```bash
   git clone https://github.com/nkrusens/gitlab-label-mover.git
   cd gitlab-label-mover
   ```

2. Install using Poetry (recommended):

   ```bash
   # Install dependencies and the package in development mode
   poetry install

   # Activate the virtual environment
   poetry shell
   ```

   Or using pip:

   ```bash
   # Install dependencies
   pip install -r requirements.txt

   # Install the package in development mode
   pip install -e .
   ```

3. Create and configure your environment file:

   ```bash
   cp example.env .env
   # Edit .env with your GitLab details
   ```

## Usage

### After PyPI Installation

If you installed the package via pip, you can run GitLab Label Mover directly from the command line:

```bash
gitlab-label-mover [options]
```

### From Source Directory

If you're running from the source directory, make sure you have the dependencies installed in your environment, then use the provided script:

```bash
# Make the script executable (first time only)
chmod +x ./gitlab-label-mover

# Run the script
./gitlab-label-mover [options]
```

The script will automatically detect whether you're running from source or using an installed package.

### Command-line Options

```text
usage: gitlab-label-mover [-h] [--execute] [--backup] [--env-file ENV_FILE] [--project-id PROJECT_ID] [--group-id GROUP_ID] [--debug]

GitLab Label Mover - Migrate labels from a project to a group

options:
  -h, --help               show this help message and exit
  --execute                Execute the migration (without this flag, only a preview is shown)
  --backup                 Create a backup of labels before migration
  --env-file ENV_FILE      Path to a custom environment file (default: .env)
  --project-id PROJECT_ID  Override the project ID from the environment file
  --group-id GROUP_ID      Override the group ID from the environment file
  --debug                  Enable detailed debug logging

By default, configuration is read from .env file in the current directory.
```

### Examples

```bash
# Perform a dry run (no changes will be made)
gitlab-label-mover

# Execute the migration
gitlab-label-mover --execute

# Create a backup before executing the migration
gitlab-label-mover --execute --backup

# Use a custom environment file
gitlab-label-mover --env-file custom.env

# Override project and group IDs
gitlab-label-mover --project-id 123 --group-id 456
```

## Environment Configuration

Create a `.env` file with the following variables:

```env
GITLAB_URL=https://gitlab.example.com
GITLAB_PRIVATE_TOKEN=your_private_token
GITLAB_SUBGROUP_PROJECT_ID=your_project_id
GITLAB_ROOT_GROUP_ID=your_group_id
```

See `example.env` for more details.

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/nkrusens/gitlab-label-mover.git
cd gitlab-label-mover

# Install dependencies with Poetry using the Makefile
make install

# Activate the virtual environment
poetry shell
```

### Development Commands

The project includes a Makefile to simplify common development tasks:

```bash
# Show available commands
make help

# Run tests
make test

# Run linting checks
make lint

# Format code
make format

# Clean build artifacts
make clean
```

### Version Management

Use Poetry's version management through the Makefile. The commands automatically update all version references, commit the changes, and create a git tag:

```bash
# Bump patch version (0.0.x)
make bump-patch

# Bump minor version (0.x.0)
make bump-minor

# Bump major version (x.0.0)
make bump-major
```

Each command will:

1. Update the version in pyproject.toml using Poetry
2. Update the version in src/gitlab_label_mover/__init__.py
3. Commit the changes with a message "Bump version to X.Y.Z"
4. Create an annotated git tag "vX.Y.Z"

### Building and Publishing

```bash
# Build the package
make build

# Test publishing to TestPyPI (recommended before publishing to PyPI)
make publish-test

# Publish to PyPI (maintainers only)
make publish
```

After publishing to TestPyPI, you can install the package with:

```bash
pip install --index-url https://test.pypi.org/simple/ gitlab-label-mover
```

__Note for maintainers:__ After publishing to PyPI, update the README badges to use the PyPI badges:

```markdown
[![PyPI version](https://badge.fury.io/py/gitlab-label-mover.svg)](https://badge.fury.io/py/gitlab-label-mover)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/gitlab-label-mover.svg)](https://pypi.org/project/gitlab-label-mover/)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- __Nikolai von Krusenstiern__ - [GitHub](https://github.com/nkrusens)
