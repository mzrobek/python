# A sample program which connects to a Db2 for z/OS database
# using ODBC and executes a SELECT

import ibm_db

# Replace the connection parameters with your values
db_location = "MOPDBB0"
db_host = "zt01.pssc.mop.fr.ibm.com"
db_port = 4751
db_uid = "mzrobek"
db_pwd = "wj1030j"

conn_str =  "DATABASE=" + db_location + ";HOSTNAME=" + db_host +";PORT=" + str(db_port) + ";"\
            "PROTOCOL=TCPIP;UID=" + db_uid + ";PWD=" + db_pwd + ";"

db_conn = ibm_db.connect(conn_str, "", "")

if (db_conn):
    print("Connected to Db2 on z/OS via ODBC.")
    sql = "SELECT NAME, COLCOUNT, CREATEDTS "
    sql = sql + "FROM SYSIBM.SYSTABLES "
    sql = sql + "WHERE CREATOR=\'" + db_uid.upper() + "\' "
    sql = sql + "ORDER BY NAME"
    print("SQL:\n", sql)
    db_stmt = ibm_db.prepare(db_conn, sql)
    if (ibm_db.execute(db_stmt)):
        print("Executed SELECT")
        print("NAME\t\t\tCOLUMNS\tCREATED")
        print("==========================================================")
        row = ibm_db.fetch_both(db_stmt)
        while (row):
            print("%-16s %7d %-15s" % (str(row[0]).rstrip(),
                                      row[1],
                                      str(row[2]).rstrip()))
            row = ibm_db.fetch_both(db_stmt)
    ibm_db.close(db_conn)

