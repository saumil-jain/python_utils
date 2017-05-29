import os
import subprocess

dir_to_scan = input('Enter dir path:')

if not os.path.isdir(dir_to_scan):
    print('not a valid dir')
    exit()

for sub_dir in os.listdir(dir_to_scan):
    print(os.path.join(dir_to_scan, sub_dir))
    sub_dir = os.path.join(dir_to_scan, sub_dir)
    if os.path.isdir(sub_dir) and '.git' in os.listdir(sub_dir):
        print('git repo found in ' + sub_dir)

        os.chdir(sub_dir)

        # execute command here
        git_pull_command = ['git', 'pull', 'origin', 'master']
        completed_process = subprocess.run(git_pull_command, shell=True, stdout=subprocess.PIPE,
                                           stderr=subprocess.STDOUT)
        print('git pull command executed. Output is:')
        print(completed_process.stdout.decode('utf-8'))

    else:
        print('git repo not found in ' + sub_dir)
