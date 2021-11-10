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


def addPerson(temp, fname, email, address, contactNo, symptom):
    cnx = db()
    cursor = cnx.cursor()

    query = ('INSERT INTO persons(temp, FullName, Email, Address, ContactNum, isSymptoms) VALUES(%s, %s, %s, %s, %s, %s)')
    rowdata=(temp, fname, email, address, contactNo, symptom)

    #Commit to DB
    cursor.execute(query, rowdata)
    cnx.commit()

    #Close Connection
    cursor.close()
    cnx.close()

def getEmails(now_plus, now_minus, now):
    cnx = db()
    cursor = cnx.cursor()

    query = ('SELECT Email from persons where HOUR(DT)=%s OR HOUR(DT)=%s or HOUR(DT)=%s and DATE(DT) = DATE(CURRENT_DATE);')
    rowdata = (now_plus, now_minus, now)

    cursor.execute(query, rowdata)
    results = cursor.fetchall()

    cursor.close()
    cnx.close()

    return results

# def getTemp():
#     cnx = db()
#     cursor = cnx.cursor()

#     query = ('SELECT temperature FROM gettemp')
    
#     cursor.execute(query)
#     results = cursor.fetchall()

#     cursor.close()
#     cnx.close()

#     return results

