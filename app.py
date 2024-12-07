import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    
    try:
        sql = """ 
            CREATE TABLE warehouse (
                w_warehousekey decimal(9,0)  not null PRIMARY KEY,
                w_name char(100) not null,
                w_capacity decimal(6,0) not null,
                w_suppkey decimal(9,0) not null,
                w_nationkey decimal(2,0) not null)
        """
        _conn.execute(sql)
        print("success")    
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


# def dropTable(_conn):
#     print("++++++++++++++++++++++++++++++++++")
#     print("Drop tables")
    
#     #cur = _conn.cursor()
#     try:
#         sql= "DROP TABLE warehouse"
#         _conn.execute(sql)
        
#         _conn.commit()
#         print("success")
        
#     except Error as e:
#         _conn.rollback()
#         print(e)
    
#     print("++++++++++++++++++++++++++++++++++")


def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")
    
    cur = _conn.cursor()
    
   
    _conn.commit()
    print("++++++++++++++++++++++++++++++++++")



def main():
    database = r"Checkpoint3-dbase.db"
   
    # create a database connection
    conn = openConnection(database)
    with conn:
        #dropTable(conn)
        createTable(conn)
        populateTable(conn)

      

    #closeConnection(conn, database)


if __name__ == '__main__':
    main()
