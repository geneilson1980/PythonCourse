

CREATE PROCEDURE projectList()
BEGIN
/* Write your SQL here. Terminate each statement with a semicolon. */
import mysql.connector

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "python_codes"
    )

    mycursor = mydb.cursor()

    mycursor.exec

    print(mysql)


	
    
END