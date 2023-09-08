class Carta:
    def __init__(self, pinta: str, valor: str):
        self.pinta: str = pinta
        self.valor: str = valor
        self.tapada: bool = False


class Baraja:
    def __init__(self):
        self.cartas: list[Carta] = []

    def revolver(self):
        pass

    def repartir_cartar(self, tapa: bool) -> Carta:
        pass


class Mano:
    def __init__(self):
        self.cartas: list[Carta] = []


class Jugador:
    def __init__(self, fichas: int, nombre: str):
        self.fichas: int = fichas
        self.nombre: str = nombre

