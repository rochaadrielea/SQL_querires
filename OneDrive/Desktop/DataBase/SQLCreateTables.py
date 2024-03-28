import sqlite3


connection = sqlite3.connect('class1210.db')

# A cursor is an object used to interact with the database. 
# You can create a cursor using the cursor() method of the connection object:

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS wrust (
    
id INTEGER PRIMARY KEY,
name VARCHAR(20) NOT NULL,
movie VARCHAR(20),
salary INTEGER
    
);
              
               ''')

cursor.execute('''

CREATE TABLE IF NOT EXISTS Insercts (
    
    name VARCHAR(20),
    posionous  BOOLEAN,
    number_of_wings INTEGER    
);
               
               ''')

cursor.execute('''
INSERT INTO dogs (dog_nr, dog_name, dog_type) VALUES
(1, 'Scoopy', 'Unknown'),
(2, 'Scoopy', 'Beagle'),
(3, 'Lassie', 'Collie'),
(6, 'Fluffy', 'Rotweiter');

'''
)
connection.commit()

 #CREATE TABLE IF NOT EXISTS wrust (
        
 #   wrust_nr INTEGER PRIMARY KEY,
 #  wrust_name  TEXT,
#  wrust_region TEXT    
#);
#




