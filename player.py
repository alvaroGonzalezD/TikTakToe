from board import Board

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
