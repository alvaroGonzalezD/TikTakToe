import os
import json
from board import Board
from player import Player
from textoES import consoleText as msg

# Se crea la clase "Game", que es en sí, quien define el estado del juego
class Game:

    # Inicializar clase(__init__, siempre ejecuta esto cuando se llama a un objeto de esta clase)
    def __init__(self):
        self.board = Board()
        validToken = ["X","O","0"]
        yourToken = str(input(msg["choseToken"])).upper()
        if yourToken not in validToken:
            print(msg["noToken"])
            print(msg["defaultX"])
            self.players = [
                Player("X"),
                Player("O")
            ]
        elif yourToken == "0":
            print(msg["zeroToken"])
            print(msg["defaultO"])
            self.players = [
                Player("O"),
                Player("X")
            ]
        elif yourToken == "X":
            self.players = [
                Player("X"),
                Player("O")
            ]
        elif yourToken == "O":
            self.players = [
                Player("O"),
                Player("X")
            ]
        self.turns = 0


    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.turn())
    # Se da paso a la jugada de jugador según sea su turno
    def playerMovement(self):
        return self.players[self.turns % 2].choose(self.board)


    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.checkCell())
    # valida si la casilla numérica existe
    def validPlay(self, movement):
        if 9 > movement > -1:
            # print(movement)
            return True
        else:
            print(msg["badCell"])
            return False


    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.checkCell())
    # Nos dice si hemos ganado, si no, epera a un caso de victoria
    def victory(self,case):
        winCondition = ["XXX", "OOO"]
        if case in winCondition:
            self.board.draw()
            print(msg["win"])
            exit()


    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.checkCell())
    # Analiza las jugadas posibles y las envía a la función que analiza si has ganado o no
    def possibleMovements(self,cell,setBoard):
        win = self.victory

        case1 = (cell[0] + cell[1] + cell[2])
        case2 = (cell[3] + cell[4] + cell[5])
        case3 = (cell[6] + cell[7] + cell[8])
        case4 = (cell[0] + cell[3] + cell[6])
        case5 = (cell[1] + cell[4] + cell[7])
        case6 = (cell[2] + cell[5] + cell[8])
        case7 = (cell[0] + cell[4] + cell[8])
        case8 = (cell[2] + cell[4] + cell[6])


        win(case1)
        win(case2)
        win(case3)
        win(case4)
        win(case5)
        win(case6)
        win(case7)
        win(case8)
        

    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.checkCell())
    # Finaliza el juego
    def endGame(self):
        print(msg["end"])
        exit()


    # Fuera del init, para acceder a los métodos, hay que llamarlos(Juego.play())
    # Este es el programa principal en sí
    def play(self):
        setBoard = self.board.whichTable
        while True:
            print(msg["launch"])
            self.board.draw()
            movement = self.playerMovement()
            player = self.players[self.turns % 2]
            
            if self.validPlay(movement) and self.board.isCellEmpty(movement):
                self.board.fillCell(movement, player.token)
                self.turns += 1
            else:
                print(msg["noValid"]) 
            self.possibleMovements(self.board.cell,setBoard)
            if self.turns == 9:
                self.board.draw()
                print(msg["draw"])
                self.endGame()
