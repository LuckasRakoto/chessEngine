import pygame as pg

from game.loadPieces import drawPieces
from .helper.constants import PINK, SQUARE_SIZE

def squareSelected(Window, board, squareX, squareY):
    pg.draw.rect(Window, PINK, (squareX*SQUARE_SIZE, squareY * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    board.selectedPiece = (board.board[squareY][squareX], squareX, squareY)

# def unselectPiece(board, window,):
#     board.selectedPiece = [None, None, None]
#     m.playerClicks = []
#     m.sqSelected = ()
#     board.drawSquares(window)
#     drawPieces(window, board.board)
#     return