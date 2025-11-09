from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import info
print("--------------welcome------------------")
choice = inquirer.select(message="what do you want to do",
                         choices=[
                             Choice("check_user",name="check git user info"),
                             Choice("check_repo",name="check repo info"),
                             Choice("set_user",name="set new user info"),
                             Choice("save_locall",name="save changes locally"),
                             Choice("push_remote",name="submit to remote"),]
                               ).execute()

if choice=="check_user":
    user = info.has_user()
    if user:
        print(f"these computer is set with \n user name: {user[0]} \n email: {user[1]}")
    else:
        print("currently the computer is has not been assigned git username and email")
        set_choice = inquirer.select(message="do you want to set now",
                                     choices=[
                                         Choice("yes",name="yes"),
                                         Choice("no",name="no"),]
                                     ).execute()
        if set_choice=="yes":
            is_git_set = info.set_git_user_config()
            if is_git_set:
                print("git user info set successfully")
            else:
                print("failed to set git user info")
elif choice=="set_user":
    is_git_set = info.set_git_user_config()
    if is_git_set:
        print("git user info set successfully")
    else:
        print("failed to set git user info")
elif choice=="check_repo":
    repo_info = info.check_repo_info()
    if repo_info:
        print(f"remote url: {repo_info[0]}\n current branch: {repo_info[1]}")
    else:
        print("this directory is not a git repository or git is not installed")