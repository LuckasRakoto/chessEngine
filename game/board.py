import pygame as pg
from .helper.constants import WHITE, ROWS, BLACK, SQUARE_SIZE

rowIndex = ['1', '2', '3', '4', '5', '6', '7', '8']
colIndex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
pg.init()
font = pg.font.Font(None, 64)


class Board:
    def __init__(self):
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
            ]
        
        self.whiteToMove = True
        self.selectedPiece = [None, None, None]
        self.moveLog = []

    def drawSquares(self, win):
        win.fill(BLACK)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pg.draw.rect(win, WHITE, (row*SQUARE_SIZE, col *
                             SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def makeAMove(self, move):
        if move.moveValid == True:
            self.board[move.startRow][move.startCol] = '--'
            self.board[move.endRow][move.endCol] = self.selectedPiece[0]
            self.moveLog.append(move.moveNotation(move.endRow, move.endCol))
            self.whiteToMove = not self.whiteToMove
            print(self.moveLog)
            print('allo')
        else:
            print('t stuck')
            pass
        
               

class Move():

    algToRow = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowToAlg = {row: alg for alg, row in algToRow.items()}
    algToCol = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colToAlg = {col: alg for alg, col in algToCol.items()}


    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[1]
        self.startCol = startSq[0]
        self.endRow = endSq[1]
        self.endCol = endSq[0]
        self.pieceMoved = board.selectedPiece[0][1]
        self.moveValid = None

    def moveNotation(self, r, c):
        return self.pieceMoved + self.colToAlg[c] + self.rowToAlg[r]

    def moveValidation(self, board):
        match self.pieceMoved:
            case 'P':
                print('m')
                if self.endCol != self.startCol:
                    print('a')
                    self.moveValid = False
                elif self.startRow-self.endRow == 1 :
                    print('b')
                    print(self.endRow)
                    print(self.startRow)
                    print('c')
                    self.moveValid = True
                

            case 'R':
                pass
            case 'N':
                pass
            case 'B':
                pass
            case 'Q':
                pass
            case 'K':
                pass