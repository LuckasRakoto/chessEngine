import pygame as pg

from .Pieces.changePiece import changePawn

from .Pieces.pawns import movesPawn

from .loadPieces import drawPieces
from .helper.constants import WHITE, ROWS, BLACK, SQUARE_SIZE, PINK

rowIndex = ['1', '2', '3', '4', '5', '6', '7', '8']
colIndex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
pg.init()


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
        self.selectedPieceColor = None
        self.moveLog = []
        self.movesPossible = []

    def findAvailableMoves(self, win):
        pieceColor = self.selectedPiece[0][0]
        pieceType = self.selectedPiece[0][1]
        pieceRow = self.selectedPiece[2]
        pieceCol = self.selectedPiece[1]

        match pieceType:
            
            case 'P':
                self.movesPossible = movesPawn(pieceCol, pieceRow, self, pieceColor, win)
                if pieceRow == 0 or pieceRow == 7:
                    changePawn(pieceRow,pieceCol, pieceColor, self, win)

            case 'R':
                for i in range(8):
                    pass
                pass
            case 'N':
                pass
            case 'B':
                pass
            case 'Q':
                pass
            case 'K':
                pass
        for position in self.movesPossible:
            pg.draw.rect(win, PINK, (position[0]*SQUARE_SIZE, position[1]* SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def drawSquares(self, win):
        win.fill(BLACK)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pg.draw.rect(win, WHITE, (col*SQUARE_SIZE, row *
                             SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def makeAMove(self, move, window):
        if (move.endCol, move.endRow) in (self.movesPossible):
            self.board[move.startRow][move.startCol] = '--'
            self.board[move.endRow][move.endCol] = self.selectedPiece[0]
            self.moveLog.append(move.moveNotation(move.endRow, move.endCol))
            self.drawSquares(window)
            drawPieces(window,self.board)
            self.whiteToMove = not self.whiteToMove
        else:
            print('t stuck', self.movesPossible)
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
        self.pieceMoved = board.selectedPiece[0]

    def moveNotation(self, r, c):
        return self.pieceMoved[1] + self.colToAlg[c] + self.rowToAlg[r]

    