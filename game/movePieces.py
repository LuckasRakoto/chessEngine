import pygame as pg

from game.loadPieces import drawPieces
from .helper.constants import *
from game.board import Move

def movePiece(iniPos, finalPos, window, gameBoard):
    move = Move(iniPos, finalPos, gameBoard)
    gameBoard.makeAMove(move, window)
    gameBoard.movesPossible = []
    gameBoard.selectedPiece = [None, None, None]
