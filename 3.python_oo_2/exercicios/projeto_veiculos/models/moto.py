from models.veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, tipo: str):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self):
        return f"{super().__str__()} | {self._tipo.ljust(25)}"
