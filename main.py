# Se crea la clase "board" que hace referencia al tablero en sí
class Board:

    # Inicializar clase(__init__, siempre ejecuta esto cuando se llama a un objeto de esta clase)
    def __init__(self):
        self.cell = [
            "*", "*", "*", 
            "*", "*", "*", 
            "*", "*", "*"
        ]
        # print("Tabla iniciada")

    # Fuera del init, para acceder a los métodos, hay que llamarlos
    def draw(self):

        # Dibujo del board de juego visible
        print(f"""\t _______________________
        |       |       |       |
        |   {self.cell[6]}   |   {self.cell[7]}   |   {self.cell[8]}   |
        |_______|_______|_______|
        |       |       |       |
        |   {self.cell[3]}   |   {self.cell[4]}   |   {self.cell[5]}   |
        |_______|_______|_______|
        |       |       |       |
        |   {self.cell[0]}   |   {self.cell[1]}   |   {self.cell[2]}   |
        |_______|_______|_______|
        """)
        # print("tabla cargada con Éxito")

    # Comprueba si la casilla está vacía
    def isCellEmpty(self, movement):
        if self.cell[movement] == "*":
            # print("casilla vacia")
            return True
        print("casilla ocupada")
        return False
            
    # Llena la casilla con la ficha "X" o "0" (si no hay, por defecto pone "F")
    def fillCell(self, movement, token='F'):
        self.cell[movement] = token
        # print(token)
        # print(self.cell[movement])



# Se crea la clase "Player", que hace referencia a los jugadores
class Player:

    # Inicializar clase(__init__, siempre ejecuta esto cuando se llama a un objeto de esta clase)
    def __init__(self, token):
        # print(f"Jugador { token } ha entrado a la sala")
        self.token = token
        # Arreglar el tema de la tabla vacía con "no números" ej "d"
        self.board = Board()

    # Fuera del init, para acceder a los métodos, hay que llamarlos(Jugador.choose())
    # Se hace la elección de casilla válida
    def choose(self):
        tokenPlaced = None
        while tokenPlaced == None:
            try:
                captura = input(f"Es el turno de {self.token}\nDonde vas a colocar tu ficha?: ")
                if captura == 0:
                    print("Esa casilla no existe")
                else:
                    tokenPlaced = int(captura)
            except ValueError:
                print(f"\t({ captura }) No es un valor válido")
                self.board.draw()
        tokenPlaced -= 1
        return tokenPlaced


# Se crea la clase "Game", que es en sí, quien define el estado del juego
class Game:

    # Inicializar clase(__init__, siempre ejecuta esto cuando se llama a un objeto de esta clase)
    def __init__(self):
        print("Juego Iniciado")
        self.board = Board()
        self.players = [
            Player('X'),
            Player('O')
        ]
        self.turns = 0


    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.turn())
    # Se da paso a la jugada de jugador según sea su turno
    def playerMovement(self):
        return self.players[self.turns % 2].choose()


    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.checkCell())
    # valida si la casilla numérica existe
    def validPlay(self, movement):
        if 9 > movement > -1:
            # print(movement)
            return True
        else:
            print("Esa casilla no existe")
            return False


    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.checkCell())
    # Determina si es victoria o no
    def winGame(self,cell):
        winCondition = ["XXX", "OOO"]

        case1 = (cell[0] + cell[1] + cell[2])

        if case1 == winCondition:
            print("You Win")
            exit()

    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.checkCell())
    # Finaliza el juego
    def endGame(self):
        print("Game Has Finished")
        exit()

    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.play())
    # Este es el programa principal en sí
    def play(self):
        while True:
            self.board.draw()
            movement = self.playerMovement()
            player = self.players[self.turns % 2]
            
            if self.validPlay(movement) and self.board.isCellEmpty(movement):
                self.board.fillCell(movement, player.token)
                self.turns += 1
            else:
               print("Movimiento NO válido") 
            self.winGame(self.board.cell)
            if self.turns == 9:
                self.board.draw()
                self.endGame()

# Guardamos "Juego" en una variable
game = Game()
# Se llama ahora a los métodos "play" y "turn" dentro de "juego"("juego" esequivalente a "Juego" en ete caso)
game.play()
