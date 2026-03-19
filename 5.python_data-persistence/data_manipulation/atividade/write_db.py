import sqlite3

conn = sqlite3.connect("db/hotel.db")
cursor = conn.cursor()

cursor.executemany(
    """
    INSERT INTO usuarios(nome, email) \
    VALUES (?,?)
  """,
    [
        ("João", "joao@teste.com.br"),
        ("Maria", "maria@teste.com.br"),
    ],
)

conn.commit()
conn.close()
