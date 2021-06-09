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
        print(f"""\t _______________________
        |       |       |       |
        |   {c[6]}   |   {c[7]}   |   {c[8]}   |
        |_______|_______|_______|
        |       |       |       |
        |   {c[3]}   |   {c[4]}   |   {c[5]}   |
        |_______|_______|_______|
        |       |       |       |
        |   {c[0]}   |   {c[1]}   |   {c[2]}   |
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