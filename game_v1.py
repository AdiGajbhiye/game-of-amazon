#display board
def display_board():
    for i in range(1,11):
        for j in range(1,11):
            if board[i][j] == -1:
                print "x",
            else:
                print board[i][j],
        print    
    #inp = raw_input()

#generate possible moves
def generate(x, y):
    moves = []
    
    flag = True 
    j = 1
    while flag:
        if board[x][y + j] == 0:
            moves.append((100*x)+(y + j)) 
        else:
            flag = False
        j = j + 1   
    
    flag = True
    j = 1
    while flag:
        if board[x][y - j] == 0 :
             moves.append((100*x)+(y - j)) 
        else:
            flag = False
        j = j + 1   
    
    flag = True
    j = 1
    while flag:
        if board[x + j][y] == 0:
            moves.append((100*(x + j))+y) 
        else:
            flag = False
        j = j + 1    
    
    flag = True
    j = 1
    while flag:
        if board[x - j][y] == 0:
            moves.append((100*(x - j))+y) 
        else:
            flag = False
        j = j + 1    
    
    flag = True
    j = 1
    while flag:
        if board[x + j][y + j] == 0:
             moves.append((100*(x + j))+(y + j)) 
        else:
        	flag = False
        j = j + 1   
    
    flag = True
    j = 1
    while flag:
        if board[x - j][y + j] == 0:
            moves.append((100*(x - j))+(y + j)) 
        else:
            flag = False
        j = j + 1   
    
    flag = True
    j = 1
    while flag:
        if board[x + j][y - j] == 0:
            moves.append((100*(x + j))+(y - j)) 
        else:
            flag = False
        j = j + 1   
    
    flag = True
    j = 1
    while flag:
        if board[x - j][y - j] == 0:
            moves.append((100*(x - j))+(y - j)) 
        else:
            flag = False
        j = j + 1   
     
    return moves
 
#check territory
def territory(player):
    piece = []
    for i in range(4):
        x,y = player_pos[player][i]/100,player_pos[player][i]%100
        moves = generate(x,y)
        piece.append(len(moves))
    return sum(piece)



#recursion
def solve(depth,  turn):
    ter_1 = territory(1)   #territory of oposition
    ter_2 = territory(0)   #minimize 
    if depth == 3: return 0
    if (ter_1 == 0) or (ter_2 == 0): return ter_1
    min_score = 10000
    min_arrow = 0
    min_piece_move = 0
    min_which_piece = -1
    max_score = -10000
    max_arrow = 0
    max_piece_move = 0
    max_which_piece = -1
    for piece in range(4):
        cur_x,cur_y = player_pos[turn][piece]/100,player_pos[turn][piece]%100
        piece_moves = generate(cur_x, cur_y)
        for move in piece_moves:
            board[cur_x][cur_y] = 0
            next_x = move/100
            next_y = move%100
            board[next_x][next_y] = turn + 1
            player_pos[turn][piece] = move
            arrow_moves = generate(next_x, next_y)
            for arrow_move in arrow_moves:
                board[arrow_move/100][arrow_move%100] = -1
                print piece,move,arrow_move
                display_board()
                total_territory = solve(depth + 1, (turn + 1)%2)
                if total_territory <= min_score:
                    min_score = total_territory
                    min_arrow = arrow_move
                    min_piece_move = move
                    min_which_piece = piece
                if total_territory >= max_score:
                    max_arrowscore = total_territory
                    max_arrow = arrow_move
                    max_piece_move = move
                    max_which_piece = piece
                board[arrow_move/100][arrow_move%100] = 0
            #board reset   
            board[next_x][next_y] = 0
            board[cur_x][cur_y] = turn + 1
            player_pos[turn][piece] = (100*cur_x) + cur_y
    if turn == 0:
        choice[0] = min_which_piece
        choice[1] = min_piece_move
        choice[2] = min_arrow
        print choice
        return min_score
    else:
        choice[0] = max_which_piece
        choice[1] = max_piece_move
        choice[2] = max_arrow
        print choice
        return max_score
        


#intialize
board = [[0 for i in range(12)]for i in range(12)] 
for i in range(12): board[0][i] = 9
for i in range(12): board[11][i] = 9
for i in range(12): board[i][0] = 9
for i in range(12): board[i][11] = 9
board[1][4] = 2
board[1][7] = 2
board[4][4] = 2
board[4][9] = 2
board[7][1] = 1
board[7][4] = 1
board[7][10] = 1
board[10][8] = 1
board[2][4] = -1
board[6][4] = -1
board[7][9] = -1
board[10][10] = -1

choice = [0,0,0]
player_pos = [[ 701 , 704 , 710 , 1008 ] , [ 104 , 107 , 404 , 409 ] ] 

#main
display_board()
print solve(1,0)
print choice
display_board()
