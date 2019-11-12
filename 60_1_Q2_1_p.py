def next_boards(board):
    results = list()
    loc = board.index(0)

    if loc > 2:
        board_temp = list(board)
        board_temp[loc], board_temp[loc-3] = board_temp[loc-3], board_temp[loc]
        board_temp = tuple(board_temp)
        results.append(tuple([board_temp,'U']))

    if loc%3 != 0:
        board_temp = list(board)
        board_temp[loc], board_temp[loc-1] = board_temp[loc-1], board_temp[loc]
        board_temp = tuple(board_temp)
        results.append(tuple([board_temp,'L']))

    if loc < 6:
        board_temp = list(board)
        board_temp[loc], board_temp[loc+3] = board_temp[loc+3], board_temp[loc]
        board_temp = tuple(board_temp)
        results.append(tuple([board_temp,'D']))

    if loc%3 != 2:
        board_temp = list(board)
        board_temp[loc], board_temp[loc+1] = board_temp[loc+1], board_temp[loc]
        board_temp = tuple(board_temp)
        results.append(tuple([board_temp,'R']))

    return sorted(results)

command = input().strip()
start_board = tuple([int(c) for c in list(input().strip())])

if command == '1' :
    print(next_boards(start_board))
    
elif command == '2' :
    
    pending = [(start_board,'')]
    
    while len(pending) > 0 :

        (current_board,moves) = pending.pop(0)
        
        if current_board == (1,2,3,4,5,6,7,8,0) :
            print(moves)
            break
        
        results = next_boards(current_board)
        new_boards_and_moves = [(b,moves+direction) for (b,direction) in results]
        
        for c in new_boards_and_moves:
            pending.append(c)
