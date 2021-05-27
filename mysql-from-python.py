import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if runnin on another enviroment)
username = os.getenv('C9_USER')

# Connect to the database
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
# git rm -r --cached Chinook_MySql_AutoIncrementPKs.sql
# echo '*.sql' >> .gitignore

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
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute("*3"CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);"*3")
        # note that the above will still display a warning not error if the
        # table already exists

finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()

mysql -u $C9_USER -p
use Chinook
select * from Friends
"""

"""
# insert data into Friends created above

try:
    # Run a query
    with connection.cursor() as cursor:
        # insert multiple row / rows
        # row = ("Bob", 21, "1990-02-06 23:04:56")
        #cursor.execute("INSERT INTO Friends VALUES(%s, %s, %s);", row)
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("John", 39, "1987-04-04 12:34:00"),
                ("Fred", 35, "1983-03-21 18:50:55")]
        cursor.executemany("INSERT INTO Friends VALUES(%s, %s, %s);", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()

"""
"""
# update
try:
    # Run a query
    with connection.cursor() as cursor:
        # update row
        # cursor.execute("UPDATE Friends SET age = 33 WHERE name = 'Bob';")
        # alternate update
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                        (43, 'Bob'))
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""
"""
# updarte many
try:
    # Run a query
    with connection.cursor() as cursor:
        rows = [(55, 'Bob'),
                (42, 'John'),
                (40, 'Fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                        rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()

"""

"""
#delete

try:
    # Run a query
    with connection.cursor() as cursor:
        #cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        # alternate delete with string interpolation
        #cursor.execute("DELETE FROM Friends WHERE name = %s;", 'John')
        # DELETE many
        cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['bob', 'fred'])
        # rows = cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        connection.commit()

finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()

"""
try:
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'Fred']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        # And this is using something called .format. So in between those curly
        # brackets, we are going to inject the string that we've created above.
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)

        connection.commit()
finally:
    connection.close()