import sqlite3
from sqlite3 import Error


# c = conn.cursor()
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql_table):
    try:
        c = conn.cursor()
        c.execute(sql_table)
        conn.commit()
    except Error as e:
        print(e)


def main(database):
    sql_create_address_table = (""" CREATE TABLE IF NOT EXISTS address(
                                            id integer PRIMARY KEY,
                                            city text,
                                            county text,
                                            district text,
                                            state text
                                    );"""
                                )
    sql_create_school_table = ("""CREATE TABLE IF NOT EXISTS school(
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        type text, 
                                        date text,
                                        enrolled integer,
                                        mmr real,
                                        overall real,
                                        xrel real,
                                        xmed real,
                                        xper real,
                                        address_id integer NOT NULL,
                                        FOREIGN KEY (address_id) REFERENCES address (id)
                                    );"""
                               )

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_address_table)
        create_table(conn, sql_create_school_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    database = input("Enter database directory: ")
    main(database)
