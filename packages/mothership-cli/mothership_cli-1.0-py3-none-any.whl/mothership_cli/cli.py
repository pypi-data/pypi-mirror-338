#!/usr/bin/env python3

import os
import sys
import subprocess
from pathlib import Path

BASE_DIR = os.path.expanduser("~/Desktop/mothership")

def run_startup():
    print(f"🚀 Creating your mothership at {BASE_DIR}")
    for cat in ["Finance", "General", "Specialist"]:
        os.makedirs(os.path.join(BASE_DIR, cat), exist_ok=True)
    print("✅ Mothership structure created:")
    print("  - Finance/")
    print("  - General/")
    print("  - Specialist/")

def list_commands():
    print("\nAvailable commands:")
    print("  mothership <project_name>               Create new project")
    print("  mothership scaffold <project_name>      Add FastAPI web boilerplate")
    print("  mothership pull <github_repo_url>       Clone into mothership + install deps")
    print("  mothership push <project_name>          Push project to GitHub")
    print("  mothership purge <project_name>         Delete a project")
    print("  startup mothership                      One-time setup of mothership folders")

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage:")
        list_commands()
        return

    cmd = args[0]

    if Path(sys.argv[0]).name == "startup" and cmd == "mothership":
        run_startup()
        list_commands()
        return

    print("🔧 This pip-installed version is a stub. For full functionality, run from the bash mothership script.")
    list_commands()

if __name__ == "__main__":
    main()
