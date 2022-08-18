import pygame as pg

from game.helper.constants import SQUARE_SIZE, WIDTH, HEIGHT
import game.board as brd
from game.loadPieces import drawPieces
from game.movePieces import movePiece
from game.pieceSelector import squareSelected

pg.init()

FPS = 30


Window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Chess")

def main():
    run = True
    clock = pg.time.Clock()
    board = brd.Board()
    sqSelected = ()
    playerClicks = []
    

    board.drawSquares(Window)
    drawPieces(Window, board.board)

    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                squareX = location[0] // SQUARE_SIZE 
                squareY = location[1] // SQUARE_SIZE

                if board.board[squareY][squareX][0] == 'w' and board.whiteToMove == True or board.board[squareY][squareX][0] == 'b' and board.whiteToMove == False :
                    squareSelected(Window, board, squareX, squareY)
                    drawPieces(Window, board.board)

                if sqSelected == (squareX, squareY):
                    sqSelected = ()
                    playerClicks = []
                    board.movesPossible = []
                    board.selectedPiece = [None, None, None]
                    board.drawSquares(Window)
                    drawPieces(Window, board.board)  
                else:
                    sqSelected = (squareX, squareY)
                    playerClicks.append(sqSelected)

                if board.selectedPiece[0] != None and board.selectedPieceColor == board.board[squareY][squareX][0] and len(playerClicks) > 1:
                    sqSelected = ()
                    playerClicks = []
                    board.movesPossible = []
                    board.selectedPiece = [None, None, None] 
                    board.drawSquares(Window)
                    drawPieces(Window, board.board)         
                
                if len(playerClicks) == 2:
                    iniPos = playerClicks[0]
                    sqSelected = ()
                    playerClicks = []
                    toGo = pg.mouse.get_pos()
                    toGo = ( toGo[0] // SQUARE_SIZE, toGo[1] //SQUARE_SIZE )
                    movePiece(iniPos, toGo, Window, board)
                

                    
                    
                
        pg.display.update()
            
    pg.quit()

if __name__ == '__main__':
    main()