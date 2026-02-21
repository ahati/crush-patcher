# Crush Patcher

This repository contains a patch file with changes from the base commit `3f07c90efe618e4889d09d8e2effe4d75867c4ce`.

**Note**: This patch is for personal use only. The content of the patch file should be considered as MIT license.

## Overview

The patch file `crush-main-patch.diff` contains changes from base commit:
- `3f07c90efe618e4889d09d8e2effe4d75867c4ce` (chore(legal): @erikstmartin has signed the CLA)

## Features

This patch adds the following features:

- **Exa Search Tool**: New tool for web searching using Exa AI API
  - `internal/agent/tools/exa_search.go` - Exa search implementation
  - `internal/agent/tools/exa_search.md` - Tool specification

- **OpenCode Branding**: Application renamed from Crush to OpenCode

- **Reduced System Prompt Tokens**: Significantly shortened agent templates
  - Simplified critical rules (from 13 to 8 rules)
  - Removed verbose communication style guidelines
  - Streamlined workflow instructions
  - Reduced token usage for cost efficiency

- **OpenCode Zen Free Model Decision**: Intelligent model selection
  - Automatic free model selection when paid API keys unavailable
  - Falls back to free providers seamlessly
  - Configurable provider priority

- **LSP Support**: New LSP installation script
  - `scripts/install-lsp.sh` - Installs and configures language servers

- **Config Improvements**: Enhanced configuration loading
  - `internal/config/load.go` - New config loading logic

- **Event System Refactoring**: Improved event handling
  - Removed redundant event files
  - Simplified event structure

## Fetching Base Version

Before applying the patch, you need to fetch the base commit:

```bash
# Clone the repository
git clone https://github.com/charmbracelet/crush.git
cd crush

# Fetch and checkout the base commit
git fetch origin 3f07c90e
git checkout 3f07c90e
```

## Applying the Patch

To apply this patch to your local checkout:

```bash
git apply crush-main-patch.diff
```

Or if you have merge conflicts:

```bash
git apply --3way crush-main-patch.diff
```

## Building

### With Go (>= 1.26)

```bash
go build .
```

### Without Go (using Docker/Podman)

If your system doesn't have Go installed, use the provided build script:

```bash
# Make the script executable
chmod +x build_with_docker.py

# Run with Docker
python3 build_with_docker.py --docker

# Or with Podman
python3 build_with_docker.py --podman
```

## Requirements

- Go >= 1.26 (if building natively)
- Docker or Podman (if using the build script)
- Python 3 (for the build script)
