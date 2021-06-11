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
        self.table = self.whichTable()
        # print("Tabla iniciada")


    # Fuera del init, para acceder a los métodos, hay que llamarlos
    def whichTable(self):
        land = ["S","T","L","R","E"]
        tableChoice = str(input(msg["tables"])).upper()

        if tableChoice not in land:
            print(msg["noTable"])
            tableUsed = "noneTable"            
            return tableUsed
        elif tableChoice == land[0]:
            tableUsed = "Square"
            return tableUsed
        elif tableChoice == land[1]:
            tableUsed = "Tiny"
            return tableUsed
        elif tableChoice == land[2]:
            tableUsed = "Ladded"
            return tableUsed
        elif tableChoice == land[3]:
            tableUsed = "Romboid"
            return tableUsed
        else:
            print(msg["forcedExit"])
            exit()


    # Fuera del init, para acceder a los métodos, hay que llamarlos
    def draw(self):
        c = self.cell

        # print(self.table)
        # Dibujo del "board" de juego visible
        print(pict[self.table].format(**{
            "a": c[0],
            "b": c[1], 
            "c": c[2], 
            "d": c[3], 
            "e": c[4], 
            "f": c[5], 
            "g": c[6], 
            "h": c[7], 
            "i": c[8]
        }))
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