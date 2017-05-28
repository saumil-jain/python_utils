import os

def update_git_repos_in_dir(root_dir):
    if not os.path.isdir(root_dir):
        print('not a valid dir')
        return

    for sub_dir in os.listdir(root_dir):
        print(os.path.join(root_dir, sub_dir))
        sub_dir = os.path.join(root_dir, sub_dir)
        if os.path.isdir(sub_dir) and '.git' in os.listdir(sub_dir):
            print('git directory')

            os.chdir(sub_dir)

            # execute command here

        else:
            print('not a git directory')


if __name__=='__main__':
    dir_to_scan = input('Enter dir path:')
    update_git_repos_in_dir(dir_to_scan)
