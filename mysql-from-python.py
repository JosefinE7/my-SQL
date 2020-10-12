import os  # os = operating system
import pymysql

# Get username from Github?
username = os.getenv('C9_USER')

# Connect to database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close the connection regardless of whether the above was successful
    connection.close()
