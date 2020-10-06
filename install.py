#/usr/bin/env python3

import os
import shutil

print("APPDATA:", os.getenv("APPDATA"))
dirpath = os.path.join(os.getenv("APPDATA"), "servoce-third-libs")
print("DIRPATH:", dirpath)

if not os.path.exists(dirpath):
	os.mkdir(dirpath)

print("copy lib to", os.path.join(dirpath, "lib"))
shutil.copytree("lib", os.path.join(dirpath, "lib"), dirs_exist_ok=True)

print("copy include to", os.path.join(dirpath, "include"))
shutil.copytree("include", os.path.join(dirpath, "include"), dirs_exist_ok=True)

print("copy dll to", os.path.join(dirpath, "dll"))
shutil.copytree("dll", os.path.join(dirpath, "dll"), dirs_exist_ok=True)

dllpath = "../../pyservoce";
print("copy dll to", dllpath)
shutil.copytree("dll", dllpath, dirs_exist_ok=True)
