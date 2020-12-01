from sqlite_methods import insert_data, get_data, update_data, display_data
from encrypt_decrypt import encrypt, master_password
import stdiomask, getpass

def get_input():
    """ gets website name as input
    :return: website name
    """
    w = input("Website: ")
    w = w.lower()
    return w

def file_entry():
    """ takes entry of website, username and password 
    from a txt file
    """
    print("Note: Insert file in txt format")
    fname = input("Enter location of file: ")
    if (len(fname) < 1): fname = 'Passlist.txt'
    fh = open(fname)
    entry_count = 0
    w, u, p = (list() for i in range(3))
    for line in fh:
        if (line.startswith('Website:  ')):
            pieces = line.split()
            w.append(pieces[1].lower())
        if (line.startswith('Username:  ')):
            pieces = line.split()
            u.append(pieces[1])
        if (line.startswith('Password:  ')):
            pieces = line.split()
            p.append(pieces[1])
    
    for entry in range(len(w)):   
        record = get_data(w[entry])
        if record is None:
            password = encrypt(p[entry]) 
            insert_data(w[entry],u[entry],password)
            entry_count += 1
        else:
            print("{} present already \n".format(w[entry]))
            
    print("Added {} entry successfully \n".format(entry_count))

def terminal_entry():
    """ takes entry of website, username and password 
    from the terminal. Used when entry has to be done manually
    """
    trigger = 1
    while(trigger==1):
        print("Enter Website, Username and Password\n")
        w = get_input()
        record = get_data(w)

        if record is None:
            u = input("Username: ")
            p = stdiomask.getpass()
            password = encrypt(p) 
            insert_data(w,u,password)
        else:
            print("Website already exists")
        
        print("\n Press 1 to insert again else 0\n")
        trigger = int(input("1 or 0: "))

def update_entry():
    """ used to update password and username of a existing website
    """
    print("Enter the website you want to update into\n")
    w = get_input()
    
    record = get_data(w)
    if record is None:
        print("Website name doesn't exits!")
        val = int(input("Press 1 to enter the website else 0: "))
        if (val == 1):
            terminal_entry()
    else:
        print("Enter the Username and New Password")
        u = input("Username: ")
        p = stdiomask.getpass()
        password = encrypt(p)
        update_data(w,u,password)

    try:
        print("\nUpdated entry!\n")
        display_data(0,w)
    except:
        print("Website doesn't exist in db")

def find_pass():
    """ the function displays password. It will either 
    display all entries or a single entry of website
    """
    trigger = int(input("Press 1 to show all else 0 to search individually:  "))

    if(trigger == 1):
        display_data(trigger)
    else:
        print("Enter the website name\n")
        w = get_input()
        display_data(trigger,w)


inp = 0
#mvp = getpass.getpass('Master Password: ')
mvp = stdiomask.getpass('Master Password: ')
check = master_password(mvp)

if (check == 1):
    while (inp != 5):
        print("\nSelect the operation:\n")
        choice_list = ['Insert passwords from file', 'Insert Single password', 'Update password',
        'Find password', 'Exit']
        function_list = [ file_entry, terminal_entry, update_entry, find_pass]
        for choice in range(len(choice_list)):
            print(str(choice+1) + "." +  choice_list[choice])
        inp = int(input("Enter the number: "))
        if(inp < 5): function_list[inp-1]()
else:
    print("Incorrect master password")