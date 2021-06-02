# Se crea la clase "Tablero"
class Tablero:

    # Inicializar clase(__init__, siempre ejecuta esto cuando se llama a un objeto de esta clase)
    def __init__(self):
        self.celdas = [
            0, 0, 0, 
            0, 0, 0, 
            0, 0, 0]
        print("Tablero iniciado")

    # Fuera del init, para acceder a los métodos, hay que llamarlos
    def draw(self):

        # Dibujo del tablero de juego visible
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


# Se crea la clase "Jugador"
class Jugador:

    # Inicializar clase(__init__, siempre ejecuta esto cuando se llama a un objeto de esta clase)
    def __init__(self, jugador):
        print(f"Jugador {jugador} ha entrado a la sala")
        self.jugador = jugador

    # Fuera del init, para acceder a los métodos, hay que llamarlos(Jugador.eleccion())
    def eleccion(self):
        input(f"Es el turno de {self.jugador}")


# Se crea la clase "Juego"
class Juego:

    # Inicializar clase(__init__, siempre ejecuta esto cuando se llama a un objeto de esta clase)
    def __init__(self):
        print("Juego Iniciado")
        self.tablero = Tablero()
        self.jugadores = [
            Jugador('X'),
            Jugador('O')
        ]
        self.turnos = 0


    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.jugar())
    def jugar(self):
        self.tablero.draw()


    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.turno())
    def turno(self):
        if self.turnos % 2:
            self.jugadores[1].eleccion()
        else:
            self.jugadores[0].eleccion()

# Guardamos "Juego" en una variable
juego = Juego()
# Se llama ahora a los métodos "jugar" y "turno" dentro de "juego"("juego" esequivalente a "Juego" en ete caso)
juego.jugar()
juego.turno()
