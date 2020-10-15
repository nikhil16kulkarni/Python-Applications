import mysql.connector

con = mysql.connector.connect(

    user = "root",
    password = "Enter Your Password :)",
    host = "127.0.0.1",
    database = "pythonmega"

)

cursor = con.cursor()

word = input("Enter a word : ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " %word)

results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])

else:
    print("No word found")