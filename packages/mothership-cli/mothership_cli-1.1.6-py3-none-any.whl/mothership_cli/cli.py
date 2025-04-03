import os
import sys
import shutil
import subprocess
from pathlib import Path

BASE_DIR = Path.home() / "Desktop" / "mothership"
CATEGORIES = ["Finance", "General", "Specialist"]

def print_help():
    print("\n🚀 mothership-cli v1.1.6")
    print("Available commands:")
    print("  startup mothership                    Initialize base folders")
    print("  mothership <project>                  Create new project")
    print("  mothership scaffold <project>         Add FastAPI boilerplate")
    print("  mothership pull <git_repo_url>        Clone a repo into mothership")
    print("  mothership push <project>             Git commit + push (with HTTPS fallback)")
    print("  mothership push <project> [--branch <branch>]   Git commit + push to specific branch")
    print("  mothership pull <repo_url> [--from <branch>]    Clone repo into mothership (branch-aware)")
    print("  mothership restore <file> [--from <branch>]     Restore file from main or specific branch")
    print("  mothership flush git                  Remove .git folder from a project")
    print("  mothership vaporize <project>         Delete a project")

    print("")

def init_mothership():
    print(f"🚀 Creating mothership folder at {BASE_DIR}")
    for cat in CATEGORIES:
        os.makedirs(BASE_DIR / cat, exist_ok=True)
    print("✅ Folders created:", ", ".join(CATEGORIES))

def create_project(project):
    folder = input("Choose folder: (f)inance / (g)eneral / (s)pecialist: ").strip().lower()
    target_map = {"f": "Finance", "g": "General", "s": "Specialist"}
    if folder not in target_map:
        print("❌ Invalid input.")
        return
    target_dir = BASE_DIR / target_map[folder] / project
    if target_dir.exists():
        print(f"⚠️  Project already exists at {target_dir}")
        return
    os.makedirs(target_dir / "logic", exist_ok=True)
    os.makedirs(target_dir / "ui", exist_ok=True)
    os.makedirs(target_dir / "web", exist_ok=True)
    os.makedirs(target_dir / "tests", exist_ok=True)
    os.makedirs(target_dir / "experimental", exist_ok=True)
    (target_dir / "main.py").write_text("# Entry point for your project\n")
    (target_dir / "README.md").write_text(f"# {project}\n\nProject scaffolded by mothership-cli.")
    (target_dir / "requirements.txt").write_text("")
    (target_dir / ".gitignore").write_text("venv/\n__pycache__/\n.env\n")
    (target_dir / "logic" / "__init__.py").write_text("")
    (target_dir / "logic" / "core.py").write_text("# Core logic lives here\\n")
    (target_dir / "logic" / "data.py").write_text("# Data lives here\\n")
    (target_dir / "logic" / "utils.py").write_text("# Utility functions live here\\n")
    (target_dir / "ui" / "__init__.py").write_text("")
    (target_dir / "ui" / "interface.py").write_text("# UI logic here\\n")
    (target_dir / "experimental" / "research.ipynb")
    print(f"✅ Project '{project}' created in {target_map[folder]}")

def push_project(project, branch="main"):
    for cat in CATEGORIES:
        proj_path = BASE_DIR / cat / project
        if proj_path.exists():
            os.chdir(proj_path)

            if not (proj_path / ".git").exists():
                subprocess.run(["git", "init"])

            subprocess.run(["git", "checkout", "-B", branch])
            subprocess.run(["git", "add", "."])
            subprocess.run(["git", "commit", "-m", f"Auto commit by mothership CLI to {branch}"], check=False)

            result = subprocess.run(["git", "push", "-u", "origin", branch])
            if result.returncode != 0:
                print("❌ Push failed. Trying HTTPS fallback...")
                url = subprocess.getoutput("git remote get-url origin")
                if url.startswith("git@github.com:"):
                    user_repo = url.replace("git@github.com:", "")
                    https_url = f"https://github.com/{user_repo}"
                    subprocess.run(["git", "remote", "set-url", "origin", https_url])
                    subprocess.run(["git", "push", "-u", "origin", branch])
            print(f"✅ Pushed '{project}' to branch '{branch}'")
            return
    print(f"❌ Project '{project}' not found in mothership.")

def pull_repo(repo_url, branch="main"):
    name = Path(repo_url).stem.replace(".git", "")
    folder = input("Where should it go? (f/g/s): ").strip().lower()
    if folder not in {"f", "g", "s"}:
        print("❌ Invalid input.")
        return

    cat = {"f": "Finance", "g": "General", "s": "Specialist"}[folder]
    dest = BASE_DIR / cat / name

    if dest.exists():
        print("⚠️  Project already exists, overwriting...")
        shutil.rmtree(dest)

    subprocess.run(["git", "clone", "--branch", branch, repo_url, str(dest)])
    
    if (dest / "requirements.txt").exists():
        subprocess.run(["python3", "-m", "venv", "venv"], cwd=dest)
        subprocess.run(["venv/bin/pip", "install", "--upgrade", "pip"], cwd=dest)
        subprocess.run(["venv/bin/pip", "install", "-r", "requirements.txt"], cwd=dest)

    print(f"✅ Repo '{name}' cloned from branch '{branch}' into {cat}/.")

def restore_file(file, branch="main"):
    try:
        subprocess.run(["git", "checkout", branch, "--", file], check=True)
        print(f"✅ Restored '{file}' from branch '{branch}'.")
    except subprocess.CalledProcessError:
        print(f"❌ Could not restore '{file}' from branch '{branch}'.")

def flush_git():
    target = input("Enter project to flush: ").strip()
    for cat in CATEGORIES:
        git_dir = BASE_DIR / cat / target / ".git"
        if git_dir.exists():
            shutil.rmtree(git_dir)
            print(f"🧹 Flushed Git history from {target}")
            return
    print("❌ Project not found or no Git history.")

def vaporize_project():
    target = input("Enter project to vaporize: ").strip()
    for cat in CATEGORIES:
        path = BASE_DIR / cat / target
        if path.exists():
            confirm = input(f"❗ Are you sure you want to delete '{target}'? (y/n): ")
            if confirm.lower() == "y":
                shutil.rmtree(path)
                print(f"🔥 Project '{target}' vaporized.")
            return
    print("❌ Project not found.")

def scaffold_project(project):
    for cat in CATEGORIES:
        proj = BASE_DIR / cat / project
        if proj.exists():
            web = proj / "web"
            os.makedirs(web / "routes", exist_ok=True)
            os.makedirs(web / "templates", exist_ok=True)
            os.makedirs(web / "static", exist_ok=True)
            (web / "routes" / "__init__.py").write_text("from fastapi import APIRouter\n\nrouter = APIRouter()\n")
            (web / "routes" / "base.py").write_text("from . import router\n\n@router.get('/')\ndef home():\n    return {'message': 'Hello World'}\n")
            (web / "templates" / "index.html").write_text("<h1>Hello FastAPI</h1>")
            (web / "static" / "style.css").write_text("body { font-family: sans-serif; }")
            (proj / "requirements.txt").write_text("fastapi\nuvicorn\njinja2\npython-dotenv\n")
            print(f"✅ Web scaffold added to '{project}'")
            return
    print("❌ Project not found.")

VERSION = "1.1.6"

def main():
    args = sys.argv[1:]

    if not args:
        print_help()
        return

    if args[0] in ("--version", "-v"):
        print(f"🛸 mothership-cli version {VERSION}")
        return

    if Path(sys.argv[0]).name == "startup" and args[0] == "mothership":
        init_mothership()
        return

    cmd = args[0]

    if cmd == "flush" and args[1:] == ["git"]:
        flush_git()

    elif cmd == "vaporize":
        vaporize_project()

    elif cmd == "push":
        if len(args) == 2:
            push_project(args[1])  # default to main
        elif len(args) == 4 and args[2] == "--branch":
            push_project(args[1], args[3])
        else:
            print("❌ Invalid usage. Try: mothership push <project> [--branch <branch>]")

    elif cmd == "pull":
        if len(args) == 2:
            pull_repo(args[1])  # default to main
        elif len(args) == 4 and args[2] == "--from":
            pull_repo(args[1], args[3])
        else:
            print("❌ Invalid usage. Try: mothership pull <repo_url> [--from <branch>]")

    elif cmd == "restore":
        if len(args) == 2:
            restore_file(args[1])  # default to main
        elif len(args) == 4 and args[2] == "--from":
            restore_file(args[1], args[3])
        else:
            print("❌ Invalid usage. Try: mothership restore <file> [--from <branch>]")

    elif cmd == "scaffold" and len(args) == 2:
        scaffold_project(args[1])

    elif len(args) == 1:
        create_project(args[0])

    else:
        print_help()


if __name__ == "__main__":
    main()
