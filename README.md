# easy7z
easy7z is a full back up program that uses 7 zip to compress and encrypt a list of directories

# Directories For Back Up
Create a text file called backupfiles.txt in the project directory. Each line should contain a directory path that you want backed up

For example
```
C:/Users/david/Documents
C:/Users/david/Pictures
C:/Users/david/Music
```

# Back Up
Use the following command to initiate a full back up. You will be asked for a password for the encryption to work
```
$ python easy7z.py
```

# Recover Back Ups
easy7z creates standard .7z files. Use 7 Zip to open these files. You should be prompted for the password you used during the initial back up step by 7 Zip