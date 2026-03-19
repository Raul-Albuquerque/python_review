import sqlite3

conn = sqlite3.connect("db/hotel.db")
cursor = conn.cursor()

cursor.execute(
    """ 
    CREATE TABLE IF NOT EXISTS usuarios(
      id INTEGER PRIMARY KEY,
      nome TEXT,
      email TEXT
    )
  """
)

conn.commit()
conn.close()
