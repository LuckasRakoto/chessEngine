import pygame as pg

from game.helper.constants import WIDTH, HEIGHT
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
                pass
                
        pg.display.update()
            
    pg.quit()

if __name__ == '__main__':
    main()