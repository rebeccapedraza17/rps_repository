print("Welcome to Rock, Paper, Scissors game: This is a two-player game. Player 1 and Player 2 will choose rock, "
      "paper, or scissors respectively\n")
 
p_1 = input("Player 1, choose rock, paper, or scissors: ")
p_2 = input("Player 2, choose rock, paper, or scissors: ")
 
def play (player_1, player_2):
    if player_1 == player_2:
        return play_again()
 
    elif player_1 == 'rock'.lower():
        if player_2 == 'scissors'.lower():
            return "Rock hits scissors. Player 1 win!"
 
    elif player_1 == 'paper'.lower():
        if player_2 == 'scissors'.lower():
            return "Scissors cut paper. Player 2 wins"
 
    elif player_1 == 'scissors'.lower():
        if player_2 == 'rock'.lower():
            return "Rock hits scissors. Player 2 wins!"
 
    elif player_1 == 'rock'.lower():
        if player_2 == 'paper'.lower():
            return "Paper covers rock. Player 2 wins!"
 
    elif player_1 == 'scissors'.lower():
        if player_2 == 'paper'.lower():
            return "Scissors cut paper. Player 1 wins!"
 
    elif player_1 == 'paper'.lower():
        if player_2 == 'rock'.lower():
            return "Paper covers rock. Player 1 wins!"
        else:
            return "Paper wins"
    else:
        print("Invalid choice. Type either, type rock, paper, or scissors.")
        return play(p_1, p_2)
 
print(play(p_1, p_2))
 
def play_again ():
    if input("Try again?") == "yes".lower():
        return play(p_1, p_2)
