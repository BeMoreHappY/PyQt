import mysql.connector
from PyQt5 import QtWidgets

mydb = mysql.connector.connect(host="remotemysql.com", user="j1YsHSws9I", passwd="VhHRTVrhde", port="3306", database='j1YsHSws9I')

mycursor = mydb.cursor()


def szukaj(username):
    mycursor.execute("SELECT * FROM Schronisko WHERE Username = '%s'" % (username))
    result = mycursor.fetchall()
    if len(result) > 0:
        return True
    else:
        return False
def dane(username):

    mycursor.execute("SELECT * FROM Schronisko WHERE Username = '%s'" % (username))
    result = mycursor.fetchall()
    if result != []:
        return (result[0][1], result[0][2])
    else:
        return False

def addToDb(email, username, password):
    query = "INSERT INTO Schronisko (Username, Password, Email) VALUE (%s, %s, %s)"
    mycursor.execute(query, (username, password, email))
    mydb.commit()
    return True









