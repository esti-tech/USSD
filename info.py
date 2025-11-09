import subprocess
def has_user():
    try:
        currentUser = subprocess.run(["git", "config", "--global", "user.name", ], check=True,stdout=subprocess.PIPE)
        currentEmail = subprocess.run(["git", "config", "--global", "user.email", ], check=True,stdout=subprocess.PIPE)
        if currentUser.stdout.strip() !="" and currentEmail.stdout.strip() !="":
            return currentUser.stdout.strip(),currentEmail.stdout.strip()
        else:
            return False
    except subprocess.CalledProcessError:
        return False
def check_repo_info():
    try:
        repo_url = subprocess.run(["git", "config", "--get", "remote.origin.url"], check=True, stdout=subprocess.PIPE)
        branch_name = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], check=True, stdout=subprocess.PIPE)
        return repo_url.stdout.strip(), branch_name.stdout.strip()
    except subprocess.CalledProcessError:
        return False
def set_git_user_config():
    username = input("Enter your Git username: ").strip()
    email = input("Enter your Git email: ").strip()
    try:
        subprocess.run(["git", "config", "--global", "user.name", username], check=True)
        subprocess.run(["git", "config", "--global", "user.email", email], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    set_git_user_config()
    input()

