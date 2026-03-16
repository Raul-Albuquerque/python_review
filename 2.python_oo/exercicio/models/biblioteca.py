# biblioteca.py

from models.book import Livro

livro_1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro_2 = Livro("1984", "George Orwell", 1949)
livro_1.emprestar()

print(livro_1)
print(livro_2)
print(Livro.verificar_disponibilidade(1899))
