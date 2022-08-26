import pygame as pg
from .helper.constants import SQUARE_SIZE

images = {}

def loadImages():
    pieces = ['wP','wQ', 'wK', 'wB', 'wN', 'wR', 'bP', 'bQ', 'bK', 'bB', 'bN', 'bR']
    for piece in pieces:
        images[piece] = pg.transform.scale(pg.image.load('game/images/' + piece + '.png'), (SQUARE_SIZE, SQUARE_SIZE))

def drawPieces(screen, board):
    loadImages()
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece != '--':
                screen.blit(images[piece], pg.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def drawMainPieces(screen):
    pass