###############################################
#                                             #
#       Author UjjwalSharma 19/9/2020         #
#               Version 1.1                   #
#               							  #
###############################################

# ----Global Variables----

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If the game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Whos turn is it?
current_player = "X"

# display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Play a game of tic tac toe
def play_game():

    # Display initial board
    display_board()

    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if game is ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# Handle a single arbitrary player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("choose a position from 1 to 9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3","4", "5", "6","7", "8", "9"]:
            position = input("Choose a position from 1 to 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Go again.")



    board[position] = player

    display_board()

# Checks if the game has ended and a player has won or
# the game is tied.
def check_if_game_over():
    check_for_winner()
    check_if_tie()

# Checks if any of the two palyers have won the game by
# completing any of the row, column or diagonal.
def check_for_winner():

    # set up global variables
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_cloumns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        #there was no win
        winner = None
    return

# Checks if there is a player who has completed any row.
def check_rows():
    # set up global variables
    global game_still_going
    # check if any row has same value and is not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any row has a match, flag there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner [X or O]
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

# Checks if there is a player who has completed any column.
def check_cloumns():
    # set up global variables
    global game_still_going
    # check if any row has same value and is not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any column has a match, flag there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner [X or O]
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

# Checks if there is a player who has completed a diagonal.
def check_diagonals():
    # set up global variables
    global game_still_going
    # check if any row has same value and is not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    # if any diagonal has a match, flag there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner [X or O]
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return

# Check if the game has tied after every turn
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

# Changes the player after every correct turn.
def flip_player():
    # global variables
    global current_player
    # if current player is X, then change it to O
    if current_player == "X":
        current_player = "O"
    # if current player is O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return

# Calls the main game loop.
play_game()



# We need:

# board
# display board
# play game
# check win
    # check rows
    # check column
    # check diagonal
# check tie
# flip player
