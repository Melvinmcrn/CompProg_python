def same_row(i,j):
    return (i//9 == j//9)

#--------------------------------------------------------------
def same_col(i,j):
    return (i-j) % 9 == 0

#--------------------------------------------------------------
def same_block(i,j):
    return (i//27 == j//27 and i%9//3 == j%9//3)

#--------------------------------------------------------------
def show(board):
    for i in range(3):
        print('+---+---+---+')
        for j in range(3):
            k = 9*(3*i+j)
            print('|'+board[k:k+3]+'|'+board[k+3:k+6]+'|'+board[k+6:k+9]+'|')
    print('+---+---+---+')

#--------------------------------------------------------------
def solve(board):

    print(show(board))
    
#    for e in T:
#        newboard = board
#        sol = solve(newboard)
#        if sol != '' :
#            return sol
#    return ''

#main==========================================================
sol = solve(input().strip())
show(sol)
