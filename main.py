# Se crea la clase "board"
class board:

    # Inicializar clase(__init__, siempre ejecuta esto cuando se llama a un objeto de esta clase)
    def __init__(self):
        self.cell = [
            0, 0, 0, 
            0, 0, 0, 
            0, 0, 0]
        print("board iniciado")

    # Fuera del init, para acceder a los métodos, hay que llamarlos
    def draw(self):

        # Dibujo del board de juego visible
        print(f"""\t _______________________
\t|       |       |       |
\t|   {self.cell[6]}   |   {self.cell[7]}   |   {self.cell[8]}   |
\t|_______|_______|_______|
\t|       |       |       |
\t|   {self.cell[3]}   |   {self.cell[4]}   |   {self.cell[5]}   |
\t|_______|_______|_______|
\t|       |       |       |
\t|   {self.cell[0]}   |   {self.cell[1]}   |   {self.cell[2]}   |
\t|_______|_______|_______|
""")
        print("board cargado con Éxito")


    def checkCell(self):
        ()


# Se crea la clase "Game"
class Player:

    # Inicializar clase(__init__, siempre ejecuta esto cuando se llama a un objeto de esta clase)
    def __init__(self, player):
        print(f"Jugador {player} ha entrado a la sala")
        self.player = player

    # Fuera del init, para acceder a los métodos, hay que llamarlos(Jugador.choose())
    def choose(self):
        return input(f"Es el turn de {self.player}\nDonde vas a colocar tu ficha?: ")


# Se crea la clase "Game"
class Game:

    # Inicializar clase(__init__, siempre ejecuta esto cuando se llama a un objeto de esta clase)
    def __init__(self):
        print("Juego Iniciado")
        self.board = board()
        self.players = [
            Player('X'),
            Player('O')
        ]
        self.turns = 0


 # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.turn())
    def turn(self):
        return self.players[self.turns % 2].choose()


    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.play())
    def play(self):
        self.board.draw()
        movement=  int(self.turn())
        movement-= 1


# Guardamos "Juego" en una variable
game = Game()
# Se llama ahora a los métodos "play" y "turn" dentro de "juego"("juego" esequivalente a "Juego" en ete caso)
game.play()
