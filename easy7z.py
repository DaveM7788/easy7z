# requires 7Zip
import os
import datetime
import getpass

dateoflastbackup = ""
dateoflast = "dateoflastbackup.txt"
with open(dateoflast) as f:
    dateoflastbackup = f.readlines()

print("Date of last backup")
print(dateoflastbackup)

folderstoback = "backupfiles.txt"
backupto = "C:/Users/david/OneDrive"

with open(folderstoback) as f:
    content = f.readlines()

content = [line.rstrip('\n') for line in open(folderstoback)]

backupfiles = ""
for i in range(0, len(content)):
    backupfiles += str(content[i]) + " "

backupfilesDisp = ""
for i in range(0, len(content)):
    backupfilesDisp += str(content[i]) + "\n"

now = datetime.datetime.now()
backuptime = str(now.year) + "_" + str(now.month) + "_" + str(now.day)
backupto += backuptime

print("\nFolders that will be backed up")
print(backupfilesDisp)

print("Destination of backup")
print(backupto + "\n")

command7z = r'"C:/Program Files/7-Zip/7z.exe" a ' + backupto + " " + backupfiles + "-p"
print("Perform the following operation [y/N]")
print(command7z)
response = input()

if response == "y" or response == "Y":
    pass1 = getpass.getpass("Enter password (no spaces): ")
    pass2 = getpass.getpass("Confirm password: ")
    if pass1 == pass2:
        with open(dateoflast, 'w') as f:
            f.write(str(now))
        command7z += pass1
        os.system(command7z)
    else:
        print("passwords do not match")


# 7 Zip can be used from the command line as follows
# .\7z a C:/Users/blue/OneDrive/backup C:/Users/blue/Music C:/Users/blue/Documents/PythonScripts -p

# "C:/Program Files/7-Zip/7z.exe"

# for windows task scheduler
# C:/Users/blue/AppData/Local/Continuum/anaconda3/python.exe C:/Users/blue/Documents/PythonScripts/Easy7Z/easy7z.py
# C:/Users/dm/AppData/Local/Programs/Python/Python37/python.exe C:/Users/dm/Documents/Py_Projects/Easy7Z/easy7z.py