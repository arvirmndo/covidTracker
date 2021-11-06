import os
import sys
import mysql.connector
import numpy

def function1():

    test1 = "Test variable for name"
    return test1

def db():
    from mysql.connector import errorcode

    flag = 1
    
    try:
        cnx = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='ctracker_db')
                                
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            flag=2
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            flag=2
        else:
            flag=2

    return cnx


def addPerson(fname, email, address, contactNo):
    cnx = db()
    cursor = cnx.cursor()

    query = ('INSERT INTO persons(FullName, Email, Address, ContactNum) VALUES(%s, %s, %s, %s)')
    rowdata=(fname, email, address, contactNo)

    #Commit to DB
    cursor.execute(query, rowdata)
    cnx.commit()

    #Close Connection
    cursor.close()
    cnx.close()



