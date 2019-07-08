#!/usr/bin/env python
import os
from shutil import copyfile

# get current working dir

current_working_dir = os.getcwd()
one_level_up = "\\".join(current_working_dir.split("\\")[:-1]) + "\\" + current_working_dir.split("\\")[-1] +
if not os.path.isdir(one_level_up):
    os.mkdir(one_level_up)
    print("Creating backup directory: \n{}".format(one_level_up))
else:
    print("Backup Directory {} already exists.".format(one_level_up))

# adding all files in git (to have the status complete)
git_add = os.system("git add .")

# running git status to get all affected files
git_status = os.popen("git status").readlines()

# reseting the git add

git_reset = os.popen("git reset").readlines()


files_to_save = {} # interface file_to_save: [from, to]
for line in git_status:
    if "new file" in line or "modified" in line:
        files_to_save[line.split(":")[1].lstrip().replace("\n","")] = [current_working_dir, one_level_up]

if files_to_save:
    for file in files_to_save:
        orig_dir = files_to_save[file][0]
        dest_dir = files_to_save[file][1]
        file = str(file).replace(r"/", "\\")
        file_path = "\\".join(file.split("\\")[:-1])
        os.makedirs(dest_dir + "\\" + file_path, exist_ok=True)
        file_from = orig_dir + "\\" + file
        file_to = dest_dir + "\\" + file
        copyfile(file_from, file_to)
        print("Backing-up: {}".format(file))