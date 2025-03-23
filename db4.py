# import sqlite3
import os

# connection = sqlite3.connect('zoo.db')
# cursor = connection.cursor()

# cursor.execute("DROP TABLE animals")

# connection.commit()
# connection.close()

if os.path.exists('zoo.db'):
    os.remove('zoo.ds')
