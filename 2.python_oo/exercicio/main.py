# main.py

from models.book import Livro

livro_1 = Livro("O Senhor dos Anéis: A Sociedade do Anel", "J. R. R. Tolkien", 1954)
livro_2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)

print(livro_1)
print(livro_2)
print(Livro.verificar_disponibilidade(1954))
