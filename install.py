#/usr/bin/env python3

import os
import shutil

dirpath = "C:/ProgramFiles/servoce-third-libs"

os.mkdir(dirpath)

shutil.copytree("lib", os.path.join(dirpath, "lib"))
shutil.copytree("include", os.path.join(dirpath, "include"))
shutil.copytree("dll", os.path.join(dirpath, "dll"))
