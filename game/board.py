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
        self.selectedPiece = None
        self.moveLog = []

    def drawSquares(self, win):
        win.fill(BLACK)

        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pg.draw.rect(win, WHITE, (row*SQUARE_SIZE, col *
                             SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
               
