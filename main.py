class Tablero:
    def __init__(self):
        print("__init__ Tablero")
    
    def draw(self):
        print("Dibujo Tablero")


class Jugador:
    def __init__(self, jugador):
        print("__init__ Jugador")
        self.jugador = jugador


class Juego:
    def __init__(self):
        print("__init__ Juego")
        self.tablero = Tablero()
        self.jugadores = [
            Jugador('X'),
            Jugador('O')
        ]

    def jugar(self):
        self.tablero.draw()


juego = Juego()
juego.jugar()
