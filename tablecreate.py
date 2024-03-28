import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='grpcchat')

# Create the users table
cursor = cnx.cursor()
cursor.execute('''
    CREATE TABLE users
    (id INT AUTO_INCREMENT PRIMARY KEY,
     username VARCHAR(255) NOT NULL UNIQUE,
     password VARCHAR(255) NOT NULL)
''')

cnx.commit()

cursor.close()
cnx.close()
