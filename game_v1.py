#display board
def display_board():
    for i in range(12):
        print board[i]


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
        '''
        for j in moves:
            arrow_x = j/100
            arrow_y = j%100
            arrow = generate(arrow_x, arrow_y)
        '''    
    return sum(piece)



#recursion
def solve(depth,  turn):
    ter_1 = territory(0)
    ter_2 = territory(1)
    if depth == 5: return ter_1
    if (ter_1 == 0) or (ter_2 == 0): return ter_1
    min_score = []
    min_score_piece = []
    for piece in range(4):
        cur_x,cur_y = player_pos[turn][piece]/100,player_pos[turn][piece]%100
        score_move = []
        piece_moves = generate(cur_x, cur_y)
        min_score_arrow = []
        for move in piece_moves:
            board[cur_x][cur_y] = 0
            next_x = move/100
            next_y = move%100
            board[next_x][next_y] = turn + 1
            score_arrow = []
            arrow_moves = generate(next_x, next_y)
            for arrow_move in arrow_moves:
                board[arrow_move/100][arrow_move%100] = -1
                score_arrow.append(territory(turn))
                #do something
                board[arrow_move/100][arrow_move%100] = 0
            #index of arrow having min score of a piece move    
            min_index = score_arrow.index(min(score_arrow))
            #list of arrow move for min score of a piece move
            min_score_arrow.append(arrow_moves[min_index])
            #list of min score of a piece move
            score_move.append(min(score_arrow))    
            #board reset   
            board[next_x][next_y] = 0
            board[cur_x][cur_y] = turn + 1
        #list of min score of each piece
        min_score.append(min(score_move))
        #index of min score piece
        min_index = score_move.index(min_score[piece])
        #list of piece move with min score piece
        min_score_piece.append(piece_moves[min_index])
    score = min(min_score)
    choice[0] = player_pos[turn][min_score.index(score)]
    choice[1] = 
    choice[2] = 
    if turn == 0:
        


#intialize
board = [[0 for i in range(12)]for i in range(12)] 
for i in range(12): board[0][i] = 9
for i in range(12): board[11][i] = 9
for i in range(12): board[i][0] = 9
for i in range(12): board[i][11] = 9
board[1][4] = 2
board[1][7] = 2
board[4][1] = 2
board[4][10] = 2
board[10][4] = 1
board[10][7] = 1
board[7][1] = 1
board[7][10] = 1

choice = [0,0,0]
player_pos = [[ 1004 , 1007 , 701 , 710 ] , [ 104 , 107 , 401 , 410 ] ] 

#main
display_board()
solve(1,0)
