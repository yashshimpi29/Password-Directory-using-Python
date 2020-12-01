from connection import create_connection, create_table
from encrypt_decrypt import decrypt

try:
    conn = create_connection('passwords.sqlite')
    cur = conn.cursor()
    
    #create_table function will be only run once.
    create_table(conn,cur)

except Exception as e:
    print(e)

def insert_data(wname,uname,pword):
    """ inserts data in the table created
    :param wname: website name 
    :param uname: username
    :param pword: password
    """
    try:
        cur.execute('INSERT INTO Password(website,username,pass) VALUES (?,?,?)',(wname,uname,pword))
        conn.commit()
    except Exception as e:
        print(e)

def get_data(wname):
    """ gets username value for the requested website
    :param wname: website name
    :return: username for website
    """
    try:
        cur.execute('SELECT username FROM Password WHERE website = ? ', (wname,))
        row = cur.fetchone()
    except Exception as e:
        print(e)
    
    return row

def update_data(wname,uname,pword):
    """ updates data in the table
    :param wname: website name
    :param uname: username
    :param pword: password
    """
    try:
        query = '''UPDATE Password SET username = ?, pass = ? WHERE website = ?'''
        cur.execute(query,(uname,pword,wname))
        conn.commit()
    except Exception as e:
        print(e)

def display_data(trigger,wname = None):
    """ displays the website name, username and password
    :param trigger: used to display all passwords or single entry
    :param wname: website name
    """
    try:
        if(trigger == 1):
            query = '''SELECT * FROM Password'''

            for row in cur.execute(query):
                print("Website: ", row[0])
                print("Username: ", row[1])
                password = decrypt(row[2])
                print("Password: ", password.strip('"'))
        else:
            query = '''SELECT * FROM Password WHERE website = ?'''
            for row in cur.execute(query,(wname,)):
                #print("Website: ", row[0])
                print("Username: ", row[1])
                password = decrypt(row[2])
                print("Password: ", password.strip('"'))
    except Exception as e:
        print("Website doesn't exist in db")
        print(e)