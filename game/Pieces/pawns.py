import operator

from .changePiece import changePawn

def movesPawn(pieceCol, pieceRow, board, pieceColor, win):
    movesPossible = []
    print(pieceRow)
    if pieceColor == 'w':
        verticalMovement = operator.sub
    else:
        verticalMovement = operator.add


    if pieceColor == 'w' and pieceRow == 6 or pieceColor == 'b' and pieceRow == 1:
        movesPossible.append((pieceCol, verticalMovement(pieceRow, 2)))
    if pieceRow != 0 and pieceRow != 7:
        if board.board[verticalMovement(pieceRow, 1)][pieceCol] == '--':
            movesPossible.append((pieceCol, verticalMovement(pieceRow, 1))) 
        if pieceCol < 7:
            if board.board[verticalMovement(pieceRow, 1)][pieceCol + 1][0] != pieceColor and board.board[verticalMovement(pieceRow, 1)][pieceCol + 1] != '--':
                movesPossible.append((pieceCol + 1, verticalMovement(pieceRow, 1)))
        if pieceCol > 0:
            if board.board[verticalMovement(pieceRow, 1)][pieceCol - 1][0] != pieceColor and board.board[verticalMovement(pieceRow, 1)][pieceCol - 1] != '--':
                movesPossible.append(((pieceCol - 1), verticalMovement(pieceRow, 1)))

    

    return movesPossible

