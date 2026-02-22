# Agent Development Guide for Crush Patcher

## Purpose

This repository contains a patch file for applying upstream changes from the main Crush/OpenCode repository.

## Patch Details

- **Base commit**: `3f07c90efe618e4889d09d8e2effe4d75867c4ce` (chore(legal): @erikstmartin has signed the CLA)
- **To commit**: `5489d0a268f3bb6a16d1bf5128abbb39cacd3353` (Merge remote-tracking branch 'origin/main' into opencode-features)

This patch only includes ahati's changes, not upstream changes.

## Fetching Base Version

```bash
# Clone the repository
git clone https://github.com/charmbracelet/crush.git
cd crush

# Fetch and checkout the base commit
git fetch origin 3f07c90efe618e4889d09d8e2effe4d75867c4ce
git checkout 3f07c90efe618e4889d09d8e2effe4d75867c4ce
```

## Applying the Patch

```bash
git apply crush-main-patch.diff
```

## Building the Project

### Using Go (recommended if available)

```bash
go build .
```

### Using Docker/Podman

If Go is not installed, use the Python build script:

```bash
python3 build_with_docker.py --docker    # For Docker
python3 build_with_docker.py --podman    # For Podman
```

The script will:
1. Clone the Crush repository if not present
2. Apply the patch
3. Build the binary using a Go Docker image

## Repository Structure

```
crush-patcher/
├── README.md              # This file
├── AGENTS.md              # Agent instructions
├── crush-main-patch.diff  # The patch file
└── build_with_docker.py   # Build script for systems without Go
```

## Upstream and Patch Management

### Adding Upstream Remote

```bash
# In your local crush repository
git remote add upstream https://github.com/charmbracelet/crush.git
git fetch upstream
```

### Updating the Patch

When upstream main branch has new commits:

```bash
# Fetch latest from upstream
git fetch upstream main

# Find the new base commit (last common ancestor)
git merge-base HEAD upstream/main

# Generate new patch
git diff <base-commit>..HEAD > crush-main-patch.diff
```

### Workflow Example

```bash
# 1. In your local crush repo (on your feature branch)
git checkout opencode-features

# 2. Fetch and merge upstream
git fetch upstream
git merge upstream/main

# 3. Generate patch (adjust commit ranges as needed)
git diff 3f07c90e..5489d0a2 > /path/to/crush-patcher/crush-main-patch.diff

# 4. Commit the new patch in this repo
cd /path/to/crush-patcher
git add crush-main-patch.diff
git commit -m "Update patch with latest upstream changes"
git push origin main
```
