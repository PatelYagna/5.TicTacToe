#This is the enitre board which tictactoe will be played on. 
Game_Board = [[0, 0, 0,],
              [0, 0, 0,],
              [0, 0, 0]]

#This prints the GameBoard when at the begining of the play. 
for r in Game_Board:
    print (r)

#This is a loop which keeps the game going. It only breaks once a player wins or enters the wrong rows or columns   
while True:
    #The player playing X chooses the Row (0-2) and Column (0-2). After, the X is places on the GameBoard
    Choose_Row = int(input('Pick_Row X: '))
    Choose_Column = int(input('Pick:_Column X: '))
    #Checks if the chosen index is less than two.
    if Choose_Row or Choose_Column > 2:
        print('Choose Row or Column Lower')
        Choose_Row = int(input('Pick_Row X: '))
        Choose_Column = int(input('Pick:_Column X: '))
    #Checks if the Index is already taken. if so then tells to choose different index. 
    elif Game_Board[Choose_Row][Choose_Column] != 0:
        print('Index Taken. Choose a Different Index.')
        Choose_Row = int(input('Pick_Row X: '))
        Choose_Column = int(input('Pick:_Column X: '))
    Game_Board[Choose_Row][Choose_Column] = ('X')
    
    #Prints GameBord to show what player X chose.
    for Board in Game_Board:
        print (Board)
    
    #A function which checks if the game has been won horizontially by player X or not. 
    for row in Game_Board:
        #It checks if all the index in rows have equalled to X
        if row.count(row[0]) == len(row) and row[0] != 0:
            print ('Player X Wins Horizontally — ')
            break
    
    #A function which checks if the game has been won vertically by player X or not.
    for i in range(len(Game_Board)):
        vertical = []
        #This for loop puts certian indices in the list vertical.
        for r in Game_Board:
            vertical.append(r[i])
        #This if statement checks if the indices in Vertical list are equal to X or not.
        if vertical.count(vertical[0]) == len(vertical) and vertical[0] != 0:
            print ('Player X Wins Vertically | ')
            break
        
    #A function determines if Player X has won diagonally or not. 
    diagnol = []
    #The for loop puts the diagnal indices in the list.
    for i in range(len(Game_Board)):
        diagnol.append(Game_Board[i][i])
    #The list is checked if all indices are X. If so then Player X wins. 
    if diagnol.count(diagnol[0]) == len(diagnol) and diagnol[0] != 0:
        print ('Player X Wins Diagonally \\')
        break
        
    #Function helps to determine if Player X has won diagonally or not.
    diagnol_2 = []
    #This seprates out the indices.
    for k in range(len(Game_Board)):
        #Adds the indcies needed to win.
        diagnol_2.append(Game_Board[k][-(k+1)])
    #Checks if Player X has won Diagonally or not. 
    if diagnol_2.count(diagnol_2[0]) == len(diagnol_2) and diagnol_2[0] != 0:
        print ('Player X Wins Diagonally /')
        break
        
    #This is where the player is switched. 
    else:
        while True:
            #This is a loop which keeps the game going. It only breaks once a player wins or enters the wrong rows or columns.  
            Choose_Row = int(input('Pick_Row O: '))
            Choose_Column = int(input('Pick_Column O: '))
            #Checks if the chosen index is less than two.
            if Choose_Row or Choose_Column > 2:
                print('Choose Row or Column Lower')
                Choose_Row = int(input('Pick_Row X: '))
                Choose_Column = int(input('Pick:_Column X: '))
            #Checks if the Index is already taken. if so then tells to choose different index.
            elif Game_Board[Choose_Row][Choose_Column] != 0:
                print('Index Taken. Choose a Different Index.')
                Choose_Row = int(input('Pick_Row X: '))
                Choose_Column = int(input('Pick:_Column X: '))
            Game_Board[Choose_Row][Choose_Column] = ('O')
            #Prints GameBord to show what player O chose.
            for Board in Game_Board:
                print (Board)
            
            #A function which checks if the game has been won horizontially by player O or not. 
            for row in Game_Board:
                #It checks if all the index in rows have equalled to O
                if row.count(row[0]) == len(row) and row[0] != 0:
                    print ('Player O Wins Horizontally — ')
                    break
            
            #A function which checks if the game has been won vertically by player O or not.
            for i in range(len(Game_Board)):
                vertical = []
                #This for loop puts certian indices in the list vertical.
                for r in Game_Board:
                    vertical.append(r[i])
                #This if statement checks if the indices in Vertical list are equal to O or not.
                if vertical.count(vertical[0]) == len(vertical) and vertical[0] != 0:
                    print ('Player O Wins Vertically | ')
                    break
                
            #A function determines if Player O has won diagonally or not. 
            diagnol = []
            #The for loop puts the diagnal indices in the list.
            for i in range(len(Game_Board)):
                diagnol.append(Game_Board[i][i])
            #The list is checked if all indices are O. If so then Player X wins. 
            if diagnol.count(diagnol[0]) == len(diagnol) and diagnol[0] != 0:
                print ('Player O Wins Diagonally \\')
                break
                
            #Function helps to determine if Player O has won diagonally or not.
            diagnol_2 = []
            #This seprates out the indices.
            for k in range(len(Game_Board)):
                #Adds the indcies needed to win.
                diagnol_2.append(Game_Board[k][-(k+1)])
            #Checks if Player O has won Diagonally or not. 
            if diagnol_2.count(diagnol_2[0]) == len(diagnol_2) and diagnol_2[0] != 0:
                print ('Player O Wins Diagonally /')
                break
            break