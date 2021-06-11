from textoES import consoleText as msg
# Se crea la clase "Player", que hace referencia a los jugadores
class Player:

    # Inicializar clase(__init__, siempre ejecuta esto cuando se llama a un objeto de esta clase)
    def __init__(self, token):
        # print(f"Jugador { token } ha entrado a la sala")
        self.token = token
        # Arreglar el tema de la tabla vacía con "no números" ej "d"


    # Fuera del init, para acceder a los métodos, hay que llamarlos(Jugador.choose())
    # Se hace la elección de casilla válida
    def choose(self, board):
        tokenPlaced = None
        while tokenPlaced == None:
            try:
                captura = input(msg["playPlayer"].format(**{'token': self.token})).upper()
                if captura == 0:
                    print(msg["notCell"])
                elif captura == "E":
                    print(msg["forcedExit"])
                    exit()
                else:
                    tokenPlaced = int(captura)
            except ValueError:
                print(msg["invalid"].format(**{'captura': captura}))
                print(msg["launch"])
                board.draw()

        tokenPlaced -= 1
        return tokenPlaced
