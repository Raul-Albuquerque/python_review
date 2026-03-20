import sqlite3


def connection():
    conn = sqlite3.connect("db/loja.db")
    return conn


def criar_tabela_produtos():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        """
      CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco INTEGER      
      )
"""
    )
    conn.commit()
    conn.close()


def inserir_produtos(nome, preco):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO produtos (nome, preco)
        VALUES (?, ?)
""",
        (nome, preco),
    )
    conn.commit()
    conn.close()


def listar_produtos():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM produtos
  """
    )
    produtos = cursor.fetchall()
    conn.commit()
    conn.close()
    for produto in produtos:
        print(produto)
