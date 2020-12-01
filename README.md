# <b>Password Directory using Python</b>

A simple python program to store Website Name, Username and Password from a file or terminal and stores the data in SQLite3 Database. Passwords are stored in encrypted format in the SQLite Table



## Required Modules
---
1. Download and import sqlite3
2. cryptography
3. os
4. stdiomask

## Instructions for running the program
----
1. Run [settings.py](https://github.com/yashshimpi29/Password-Directory-using-Python/blob/master/settings.py) file to create the config folder.
2. In the [encryption.py](https://github.com/yashshimpi29/Password-Directory-using-Python/blob/master/encryption.py) file, set your master password before executing. This password will help in providing security before starting the program.
3. Run [encryption.py](https://github.com/yashshimpi29/Password-Directory-using-Python/blob/master/encryption.py) file only once to create the key.txt and creds.txt file.
4. If inserting via Text File, it should be of the format:
    <p>
    Website:
    <br> 
    Username:
    <br>
    Password:
    <br>
    Leave 2 spaces before typing the details.(As shown in Passlist.txt) 
5. Create the table only once at the start, later comment it as written in [sqlite_methods.py](https://github.com/yashshimpi29/Password-Directory-using-Python/blob/master/sqlite_methods.py)   

<br>

## Features
---
1. Enter, Update and Disply Data.
2. Passwords in SQLite Table are store in Encrpyted Format
3. Master Password which will asked each time before starting the program