import mysql.connector as mydbconnection
from mysql.connector import Error

try:
    conn = mydbconnection.connect(database='usersdb', user='root',password='root')
    cursor=conn.cursor()
    myquery = "CREATE DATABASE RegistrationDB;"
    cursor.execute(myquery)
    print("Database 'RegistrationDB' is created")
except Error as e:
    print("Failed to create database {}".format(e))
finally:
    if conn.is_connected():
        conn.close()
    print("MySQL connection is closed")