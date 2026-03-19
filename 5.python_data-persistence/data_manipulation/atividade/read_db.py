import sqlite3

conn = sqlite3.connect("db/hotel.db")
cursor = conn.cursor()

cursor.execute(
    """
    SELECT * FROM usuarios
  """
)

conn.commit()
usuarios = cursor.fetchall()
conn.close()

for usuario in usuarios:
    print(usuario)
