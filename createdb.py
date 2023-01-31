import os
from lib.sqlcmds import (
    get_connection,
    exec_write,
)

if __name__ == '__main__':
    print('Dropping existing databases/tables...')
    conn, cursor = get_connection(
        os.getenv('DBServer'),
        os.getenv('AdminName'),
        os.getenv('AdminPass'),
    )
    with open('database/BikeStores Sample Database - drop all objects.sql') as file:
        sql_cmds = file.read()
        exec_write(sql_cmds, cursor, conn)

    # print('Creating BikeStores database...')
    # with open('database/BikeStores Sample Database - create objects.sql') as file:
    #     sql_cmds = file.read()
    #     exec_write(sql_cmds, cursor, conn)
    
    conn.close()