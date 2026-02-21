#!/usr/bin/env python3
"""
Build script for Crush/OpenCode when Go is not available.
Uses Docker or Podman to build the project.
"""

import argparse
import os
import shutil
import subprocess
import sys


def run_cmd(cmd, cwd=None, check=True):
    """Run a command and return success status."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if check and result.returncode != 0:
        print(f"Command failed with exit code {result.returncode}")
        sys.exit(1)
    return result.returncode == 0


def check_container_available(container_type):
    """Check if the container runtime is available."""
    cmd = [container_type, "--version"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Found {container_type}: {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        pass
    return False


def main():
    parser = argparse.ArgumentParser(
        description="Build Crush/OpenCode using Docker or Podman"
    )
    parser.add_argument(
        "--docker",
        action="store_true",
        help="Use Docker to build",
    )
    parser.add_argument(
        "--podman",
        action="store_true",
        help="Use Podman to build",
    )
    parser.add_argument(
        "--repo",
        default="https://github.com/charmbracelet/crush.git",
        help="Git repository to clone",
    )
    parser.add_argument(
        "--workdir",
        default="/workspaces/crush-patcher",
        help="Working directory for build",
    )

    args = parser.parse_args()

    if not args.docker and not args.podman:
        print("Error: Please specify --docker or --podman")
        parser.print_help()
        sys.exit(1)

    container = "docker" if args.docker else "podman"

    if not check_container_available(container):
        print(f"Error: {container} is not available")
        sys.exit(1)

    workdir = args.workdir
    script_dir = os.path.dirname(os.path.abspath(__file__))
    patch_file = os.path.join(script_dir, "crush-main-patch.diff")

    if not os.path.exists(patch_file):
        print(f"Error: Patch file not found: {patch_file}")
        sys.exit(1)

    crush_dir = os.path.join(workdir, "crush")

    if not os.path.exists(crush_dir):
        print(f"Cloning repository...")
        run_cmd(
            ["git", "clone", "--depth", "1", args.repo, crush_dir],
            check=True,
        )
    else:
        print(f"Repository already exists at {crush_dir}")

    print("Applying patch...")
    run_cmd(
        ["git", "apply", "crush-main-patch.diff"],
        cwd=crush_dir,
        check=False,
    )

    print(f"Building with {container}...")

    dockerfile = f"""
FROM golang:1.26.0

WORKDIR /build

COPY . .

RUN go build -o crush .

CMD ["ls", "-la"]
"""

    dockerfile_path = os.path.join(workdir, "Dockerfile")
    with open(dockerfile_path, "w") as f:
        f.write(dockerfile)

    image_name = "crush-builder:latest"
    container_name = "crush-build-container"

    print(f"Building Docker image...")
    run_cmd(
        [
            container, "build",
            "-t", image_name,
            "-f", dockerfile_path,
            workdir,
        ],
        check=True,
    )

    print("Running build container...")
    run_cmd(
        [
            container, "run",
            "--name", container_name,
            "-v", f"{crush_dir}:/build",
            image_name,
        ],
        check=True,
    )

    binary_path = os.path.join(crush_dir, "crush")
    if os.path.exists(binary_path):
        print(f"Build successful! Binary at: {binary_path}")
    else:
        print("Warning: Binary not found at expected location")
        print(f"Contents of crush dir: {os.listdir(crush_dir)}")

    print("\nCleanup...")
    run_cmd([container, "rm", container_name], check=False)


if __name__ == "__main__":
    main()
