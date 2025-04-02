# Omega CLI

A command-line tool for submitting and monitoring jobs.

## Installation

You can install the package globally using pip:

```bash
pip install omegacloud-cli
```

## Configuration

The service URL can be configured in `pyproject.toml`:

```toml
[tool.omegacloud-cli]
platform_url = "http://127.0.0.1:8000"  # Default value
```

## Usage

After installation, the `omega` command will be available globally. You can use it from any directory:

```bash
# Submit a job from the current directory
omega run

# Stream output from the last submitted job
omega log

# Stop the last submitted job
omega stop

# Stop a specific job by ID
omega stop --job-id 49e5f0d4-7c58-4c99-aa7b-f7464adf24d3

# Check status of the last submitted job
omega inspect

# Check status of a specific job
omega inspect --job-id 49e5f0d4-7c58-4c99-aa7b-f7464adf24d3
```

The tool will:

1. Create a zip archive of the current directory
2. Submit it to the job processing service
3. Stream the job output in real-time
4. Store the job ID in a `.omega` file for later reference

The `log` command allows you to stream the output of the last submitted job without resubmitting the directory.

The `stop` command allows you to stop a running job. If no job ID is provided, it will attempt to stop the last submitted job from the `.omega` file.

The `inspect` command shows the current status and details of a job. Like other commands, it will use the last submitted job ID if none is provided.

## Requirements

- Python 3.8 or higher
- Active job processing service (configurable, defaults to http://127.0.0.1:8000)
