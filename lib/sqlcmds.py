import pymysql

def get_connection(host, user, password, database=None):
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )
    cursor = conn.cursor()
    return conn, cursor

def exec_query(statement, cursor):
    cursor.execute(statement)
    results = cursor.fetchall()
    return results

def exec_write(statement, cursor, conn):
    cursor.execute(statement)
    conn.commit()
