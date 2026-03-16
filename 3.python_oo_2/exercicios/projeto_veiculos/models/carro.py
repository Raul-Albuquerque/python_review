from models.veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, qtd_portas: int):
        super().__init__(marca, modelo)
        self._qtd_portas = qtd_portas

    def __str__(self):
        return f"{super().__str__()} | {str(self._qtd_portas)} portas"
