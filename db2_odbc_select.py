# A sample program which connects to a Db2 for z/OS database
# and executes a query

import ibm_db

# Replace the connection parameters with your values
db_location = "mylocation"
db_host = "123.456.789.012"
db_port = 4750
db_uid = "????????"
db_pwd = "????????"

conn_str =  "DATABASE=" + db_location + ";HOSTNAME=" + db_host +";PORT=" + str(db_port) + ";"\
            "PROTOCOL=TCPIP;UID=" + db_uid + ";PWD=" + db_pwd + ";"

db_conn = ibm_db.connect(conn_str, "", "")

if (db_conn):
    print("Connected to Db2 on z/OS")
    sql = "SELECT * FROM MZROBEK.TEST1"
    db_stmt = ibm_db.prepare(db_conn, sql)
    if (ibm_db.execute(db_stmt)):
        print("Executed SELECT")
        print("COL1\t\tCOL2\tCOL3")
        print("==========================================================")
        row = ibm_db.fetch_both(db_stmt)
        while (row):
            print("%-14s %7d %-15s" % (str(row['COL1']).rstrip(), \
                                      row['COL2'], \
                                      str(row['COL3']).rstrip()))
            row = ibm_db.fetch_both(db_stmt)
    ibm_db.close(db_conn)
else:
    print("*** Database connection error!")

