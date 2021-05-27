import os
import pymysql

#Get username from Cloud9 workspace
# (modify this variable if runnin on another enviroment)
username = os.getenv('C9_USER')

#Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

"""
try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()
"""
#git rm -r --cached Chinook_MySql_AutoIncrementPKs.sql
#echo '*.sql' >> .gitignore

"""
cursor returning tuple
try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        for row in cursor:
            print(row)

finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()

"""

"""
cursor returnig dictionary

try:
    #Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)

finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()

"""
"""
create a table

#mysql-ctl start
#mysql -u $C9_USER -p

try:
    #Run a query
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        #note that the above will still display a warning not error if the
        # table already exists

finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()

mysql -u $C9_USER -p
use Chinook
select * from Friends
"""