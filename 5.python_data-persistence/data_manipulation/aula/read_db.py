import sqlite3

conn = sqlite3.connect("db/escola.db")
cursor = conn.cursor()

# cursor.execute(
#     """
#     SELECT * FROM estudantes
#   """
# )

cursor.execute(
    """
      SELECT * FROM disciplinas
  """
)


conn.commit()

# estudantes = cursor.fetchall()
# for estudante in estudantes:
#     print(estudante)

disciplinas = cursor.fetchall()
conn.close()

for disciplina in disciplinas:
    print(disciplina)
