import MySQLdb
import seaborn as sns
import pandas as pd

# connect to MySQL database called p3
def dbConnect():
    dsn_database = 'p3'
    dsn_uid = 'root'
    dsn_pwd = ''
    conn = MySQLdb.connect(user=dsn_uid, passwd=dsn_pwd, db=dsn_database)
    return conn

# disconnect from MySQL database
def dbDisconnect(conn):
    conn.close()

# convert database table into dataframe
def dbTableToDataFrame(conn, table):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ' + table)
    result = []
    columns = tuple([item[0] for item in cursor.description])
    for row in cursor:
        result.append(dict(zip(columns, row)))
    result_df = pd.DataFrame(result)
    return result_df