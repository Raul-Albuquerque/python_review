# book.py


class Livro:
    livros = []

    def __init__(self, titulo: str, autor: str, ano_publicacao: int):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f"Título: {self._titulo.ljust(40)} | Autor: {self._autor.ljust(25)} | Ano Publicação: {str(self._ano_publicacao).ljust(5)} | Disponibilidade: {self._disponivel}"

    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []

        for livro in Livro.livros:
            if livro._ano_publicacao == ano and livro._disponivel:
                livros_disponiveis.append(livro._titulo)

        return livros_disponiveis
