import sqlite3

conn = sqlite3.connect("db/escola.db")
cursor = conn.cursor()

# cursor.execute(
#     """
#     INSERT INTO estudantes(nome, idade)\
#     VALUES (?,?)
#   """,
#     ("Joana", 19),
# )

cursor.execute(
    """
    INSERT INTO disciplinas(estudante_id, nome_disciplina)\
    VALUES(?,?)
  """,
    (1, "Matemática"),
)

conn.commit()
conn.close()
