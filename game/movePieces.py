import pygame as pg

from game.loadPieces import drawPieces
from .helper.constants import *
from game.board import Move

def movePiece(iniPos, finalPos, window, gameBoard):
    move = Move(iniPos, finalPos, gameBoard)
    move.moveValidation(gameBoard.board)
    gameBoard.makeAMove(move)
    gameBoard.drawSquares(window)
    drawPieces(window, gameBoard.board)
