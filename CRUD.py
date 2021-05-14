import mysql.connector
db_connection = mysql.connector.connect(
host="localhost",
user="root",
passwd="password_here"
)
my_database = db_connection.cursor()
my_database.execute("CREATE DATABASE MY_TEST_DB")
