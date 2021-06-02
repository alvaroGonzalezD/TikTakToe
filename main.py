class Tablero:
    def __init__(self):
        self.celdas = [
            0, 0, 0, 
            0, 0, 0, 
            0, 0, 0]
        print("Tablero iniciado")

    
    def draw(self):
        print(f"""\t _______________________
\t|       |       |       |
\t|   {self.celdas[6]}   |   {self.celdas[7]}   |   {self.celdas[8]}   |
\t|_______|_______|_______|
\t|       |       |       |
\t|   {self.celdas[3]}   |   {self.celdas[4]}   |   {self.celdas[5]}   |
\t|_______|_______|_______|
\t|       |       |       |
\t|   {self.celdas[0]}   |   {self.celdas[1]}   |   {self.celdas[2]}   |
\t|_______|_______|_______|
""")
        print("Tablero cargado con Éxito")


class Jugador:
    def __init__(self, jugador):
        print(f"Jugador {jugador} ha entrado a la sala")
        self.jugador = jugador


class Juego:
    def __init__(self):
        print("Juego Iniciado")
        self.tablero = Tablero()
        self.jugadores = [
            Jugador('X'),
            Jugador('O')
        ]

    def jugar(self):
        self.tablero.draw()



juego = Juego()
juego.jugar()
