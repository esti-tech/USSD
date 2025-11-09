import subprocess
import os

def is_git_installed():
    try:
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def is_git_repo(repo_path):
    if os.path.isdir(os.path.join(repo_path, ".git")):
        return True

    try:
        result = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=repo_path
        )
        return result.stdout.strip() == "true"
    except subprocess.CalledProcessError:
        return False

def create_git_ignore():
    content = """*.exe"""
    with open(".gitignore","w") as f:
        f.write(content.stripe())

def run_git_commands(repo_path, commit_message="Auto commit"):
    if not is_git_installed():
        print("Git is not installed. Please install Git and try again.")
        return
    
    if not is_git_repo(repo_path):
        print(f"The folder '{repo_path}' is not a git repository. run localsave.exe first")
        return

    try:
        subprocess.run(["git", "push"], check=True, cwd=repo_path)
        print("Changes has successfully submitted to remote repository ")
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")

if __name__ == "__main__":
    repo_path = os.path.abspath(".")  # Or set this to your desired repo path
    run_git_commands(repo_path)
    input()
