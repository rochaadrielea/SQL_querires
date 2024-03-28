import sqlite3


connection = sqlite3.connect('lab.db')
print("passsouuuuuu")

# A cursor is an object used to interact with the database. 
# You can create a cursor using the cursor() method of the connection object:

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS laboratory (
    
id_lab INTEGER PRIMARY KEY,
city VARCHAR(20) ,
country VARCHAR(20) NOT NULL,
zipcode VARCHAR(20),
name VARCHAR(20)

    
);            
   ''')

cursor.execute('''

CREATE TABLE IF NOT EXISTS scientist (
    
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    id_scientist INT,
    fiel_of_research  VARCHAR(20)
      
); 
''')

cursor.execute('''

CREATE TABLE IF NOT EXISTS experiemnt (
    
    ex_id VARCHAR(20),
    ex_name VARCHAR(20),
    project  VARCHAR(20)
      
);
               
               ''')


connection.commit()




