import MySQLdb
import seaborn as sns
import pandas as pd

def dbConnect():
    """
    connect to MySQL database called p3

    Parameters
    ----------
    None

    Return
    ------
    connection object from MySQLdb.connect()

    """
    dsn_database = 'p3'
    dsn_uid = 'root'
    dsn_pwd = ''
    conn = MySQLdb.connect(user=dsn_uid, passwd=dsn_pwd, db=dsn_database)
    return conn

def dbTableToDataFrame(conn, table):
    """
    convert table from p3 database into a dataframe

    Parameters
    ----------
    1. connection object
    2. table name to select from in database p3

    Return
    ------
    dataframe with contents from table name passed
    
    """
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ' + table)
    result = []
    columns = tuple([item[0] for item in cursor.description])
    for row in cursor:
        result.append(dict(zip(columns, row)))
    result_df = pd.DataFrame(result)
    return result_df