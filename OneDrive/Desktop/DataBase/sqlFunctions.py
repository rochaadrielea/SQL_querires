import sqlite3


connection = sqlite3.connect('movies.db')

# A cursor is an object used to interact with the database. 
# You can create a cursor using the cursor() method of the connection object:

cursor = connection.cursor()

cursor.execute('''
SELECT * FROM actors                
               ''')  


connection.commit()           
