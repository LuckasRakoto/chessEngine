import pygame as pg

from ..helper.constants import SQUARE_SIZE, WIDTH, BLUE
from ..loadPieces import loadImages



def changePawn(row, col, color, board, screen):
    loadImages()
    pieces = [color + 'R', color + 'Q', color + 'N', color + 'B']
    if color == 'w':
        yPos = SQUARE_SIZE
    elif color == 'b':
        yPos = 3*SQUARE_SIZE
    pg.draw.rect(screen, BLUE, ((col)*SQUARE_SIZE, yPos,SQUARE_SIZE, SQUARE_SIZE*4))
    