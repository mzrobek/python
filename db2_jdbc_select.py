# A sample program which connects to a Db2 for z/OS database
# using ODBC and executes a SELECT
# Written by Maciej Zrobek

### IMPORTANT:
### Before running this script make sure that the complete path to the
### license file db2jcc_license_cisuz.jar is in your CLASSPATH env variable

import jaydebeapi
import os

print("CLASSPATH=",os.getenv("CLASSPATH"))

# Replace the connection parameters with your values
db_location = "<db2 location>"
db_host = "<db host>"
db_port = 99999
db_uid = "<userid>"
db_pwd = "<password>"

# Replace with the complete path to the driver file
# This parameter is not required if the path is in your CLASSPATH
jdbc_driver_path = "<path to db2jcc4.jar>"

jdbc_driver_class = "com.ibm.db2.jcc.DB2Driver"
jdbc_conn_str = "jdbc:db2://" + db_host + ":" + str(db_port) + "/" + db_location + ":"

conn = jaydebeapi.connect(jdbc_driver_class,
        jdbc_conn_str,
        {'user': db_uid, 'password': db_pwd},
        jdbc_driver_path,)

if (conn):
    print("Connected to Db2 on z/OS via JDBC.")
    sql = "SELECT NAME, COLCOUNT, CREATEDTS "
    sql = sql + "FROM SYSIBM.SYSTABLES "
    sql = sql + "WHERE CREATOR=\'" + db_uid.upper() + "\' "
    sql = sql + "ORDER BY NAME"
    print("SQL:\n", sql)
    
    curs = conn.cursor()
    curs.execute(sql)
    print("Executed SELECT")
    print("NAME\t\t\tCOLUMNS\tCREATED")
    print("==========================================================")
    row = curs.fetchone()
    while (row):
        print("%-16s %7d %-15s" % (str(row[0]).rstrip(),
                                   row[1],
                                   str(row[2]).rstrip()))
        row = curs.fetchone()
    curs.close()
    conn.close()
