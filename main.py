from xml.etree.ElementTree import PI
import pygame as pg

from game.helper.constants import SQUARE_SIZE, WIDTH, HEIGHT, PINK
import game.board as brd
from game.loadPieces import drawPieces
pg.init()
FPS = 30


Window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Chess")


def main():
    run = True
    clock = pg.time.Clock()
    board = brd.Board()

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

                if board.board[squareY][squareX] != '--':
                    pg.draw.rect(Window, PINK, (squareX*SQUARE_SIZE, squareY *
                             SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    board.moveLog.append([{board.board[squareY][squareX]: [squareX, squareY]}])
                    board.selectedPiece = board.board[squareY][squareX]
                    print(board.selectedPiece)
                    drawPieces(Window, board.board)
                    
            if board.selectedPiece != None:
                toGo = pg.mouse.get_pos()
                toGoX = toGo[0] // SQUARE_SIZE
                toGoY = toGo[1] // SQUARE_SIZE 
                print('on part vers:', toGoX, toGoY)
                if board.board[toGoY][toGoX] == '--':
                    board.board[toGoY][toGoX] = board.selectedPiece
                    board.board[squareX][squareY] = '--'
                    board.drawSquares(Window)
                    print('avant de tout redessiner')
                    drawPieces(Window, board.board)
                    board.selectedPiece = None
                        
                    
                
        pg.display.update()
            
    pg.quit()

if __name__ == '__main__':
    main()