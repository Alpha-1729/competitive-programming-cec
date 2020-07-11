#!usr/bin/python3
import os
global file_no
with open("file_no.txt","r") as aa:
    file_no=aa.read()
all_folder=[i for i in os.listdir() if os.path.isdir(i)]
file_no=str(int(file_no)-1).zfill(3)
for i in all_folder:
    if i.startswith(file_no):
        os.chdir(i)
        os.system("python Program.py")