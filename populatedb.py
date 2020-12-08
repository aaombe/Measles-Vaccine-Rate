import sqlite3
from sqlite3 import Error
import db
import openfile


check_list = list()
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def populate_address_table(conn, data):
    """
    Add data to address table
    :param conn:
    :param data:
    :return: address id
    """
    sql = ('''INSERT INTO address (city, county, district, state) 
                VALUES (?,?,?,?)''')
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid


def populate_school_table(conn, data):
    """
    Add data to school table
    :param conn:
    :param data:
    """
    sql = ('''INSERT INTO school (name, type, date, enrolled, mmr, overall, xrel, xmed, xper, address_id) 
                VALUES (?,?,?,?,?,?,?,?,?,?)''')
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()

    return cur.lastrowid


def get_school_data(dictionary):
    school = ['name', 'type', 'year','enroll', 
                'mmr', 'overall', 'xrel', 'xmed', 'xper']
    myList = list(map(dictionary.get, school))
    for i in range(3):
        if myList[i] == '':
            myList[i] ='N/A'
    return myList
    

def school_data (data, fk):
    data.append(fk) 
    return data


def get_address_data(dictionary):
    address = ['city', 'county', 'district', 'state']
    my_list = list(map(dictionary.get, address))
    for index in range(len(my_list)):
        if (my_list[index] == 0.0):
            my_list[index] = "N/A"
    return (my_list)
  

def main(database):
    
    # create a database connection
    conn = create_connection(database)
    data = openfile.main()

    with conn:
        for value in range (len(data)):
            address = get_address_data(data[value])
            address_id = populate_address_table(conn, address)

            school = school_data (get_school_data(data[value]), address_id)
            populate_school_table(conn, school)
           

if __name__ == '__main__':
    database = input("Enter database directory: ")
    main(database)
    #"C:\sqlite\vaccines.db" or mysqldb.db
    #all-measles-rates.csv
    main(database)
