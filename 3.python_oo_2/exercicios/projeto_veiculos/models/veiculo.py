class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return (
            f"{self._marca.ljust(25)} | {self._modelo.ljust(25)} | { status.ljust(25)}"
        )
