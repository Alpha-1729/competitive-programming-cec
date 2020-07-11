#!usr/bin/python3
import os
global file_no
with open("file_no.txt","r") as aa:
    file_no=aa.read()
name=input("Enter the file name: ").replace(" ","-").title()
file_name="{}-{}".format(file_no.zfill(3),name)
os.mkdir(file_name)
# Adding the template of the python file.
with open("{}/{}.py".format(file_name,"Program"),"w") as ab:
    ab.write('''#!/usr/bin/python3\n# {}\n\n"""\n{}"""\n\nprint(" "); '''.format(name,">>>>\n"*5))
with open("file_no.txt","w") as ac:
    ac.write(str(int(file_no)+1))
