import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn

#needs to be executed only once
def create_table(conn,cur):
    """ create a table in SQLite database
    :param conn: Connection object
    :param cur: cursor object to invoke methods that execute SQLite statements
    """
    try:
        cur.execute('''CREATE TABLE Password
        (website TEXT UNIQUE, username CHAR(30),pass PASSWORD)''')
        conn.commit()
    except Exception as e:
        print(e)