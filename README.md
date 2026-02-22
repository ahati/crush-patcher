# Crush Patcher

This repository contains a patch file with changes from the base commit `3f07c90efe618e4889d09d8e2effe4d75867c4ce`.

**Note**: This patch is for personal use only. The content of the patch file should be considered as MIT license.

## Overview

The patch file `crush-main-patch.diff` contains changes from base commit:
- `3f07c90efe618e4889d09d8e2effe4d75867c4ce` (chore(legal): @erikstmartin has signed the CLA)

To commit:
- `c1d294d161dbee0d1bd5061c3270050c980b8d98` (feat(ui): indicate when skills are loaded)

## Features

This patch adds the following features:

- **Skill Loading Indicators**: UI now shows when skills are loaded
  - `internal/agent/tools/view.go` - Added resource type, name, and description to view response metadata
  - `internal/ui/chat/tools.go` - New skill content rendering function
  - `internal/ui/styles/styles.go` - New styles for resource loading indicators

- **UI Improvements**: Various UI rendering fixes
  - Message rendering now applies style prefix to each line
  - Header details spacing fixes
  - Status bar width calculations corrected
  - Compact header/footer rendering fixes

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
