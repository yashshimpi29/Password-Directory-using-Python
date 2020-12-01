# Password Directory using Python

A simple python program to store Website Name, Username and Password from a file or terminal and stores the data in SQLite3 Database.Passwords are stored in encrypted format in the SQLite Table

<br>

### Instructions for running the program
----
1. Run settings.py file to create the config folder.
2. Run encryption.py file only once to create the key.txt and creds.txt file.
3. In the encryption.py file, set your master password before executing. This password
    will help in providing security before starting the program.
4. If inserting via Text File, it should be of the format:
    <p>
    Website:
    <br> 
    Username:
    <br>
    Password:
    <br>
    Eachone is followed by 2 spaces.(As shown in Passlist.txt)
    
5. Create the table only once at the start, later comment it as written in sqlite_methods.py   

<br>

#### Required Modules
---
1. Download and import sqlite3
2. pip install cryptography
3. os module

<br>

#### Features
---
1. Enter, Update and Disply Data.
2. Passwords in SQLite Table are store in Encrpyted Format
3. Master Password which will asked each time before starting the program