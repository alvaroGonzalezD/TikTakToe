from boardDraw import consoleDraws as pict
from textoES import consoleText as msg
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
        c = self.cell
        # Dibujo del board de juego visible
        print(pict["table1"].format(**{"zero": c[0],"one": c[1], "two": c[2], "three": c[3], "four": c[4], "five": c[5], "six": c[6], "seven": c[7], "eight": c[8]}))
        # print("tabla cargada con Éxito")

    # Comprueba si la casilla está vacía
    def isCellEmpty(self, movement):
        if self.cell[movement] == "*":
            # print("casilla vacia")
            return True
        print(msg["already"])
        return False
            
    # Llena la casilla con la ficha "X" o "0" (si no hay, por defecto pone "F")
    def fillCell(self, movement, token='F'):
        self.cell[movement] = token
        # print(token)
        # print(self.cell[movement])