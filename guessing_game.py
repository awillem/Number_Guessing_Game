
# Python Web Development Techdegree
# Project 1 - Number Guessing Game
# Emma W
# --------------------------------
import random

##################
# Global Variables
##################
player_name = None
game_number = None
high_scores = []
difficulty_scores = []
guesses = 0
player_guess = None
difficulty = 1

##################
# Functions
##################
def play_again():
    play_again = input("\nWould you like to play again? (Y/N) ")
    if play_again.upper() != "Y":
        print("\nThanks for playing.  Have a great day!")
    else:
        start_game()


def record_highscore(guesses, player, difficulty):
    high_scores.append([guesses, player, difficulty])
    high_scores.sort()

# appends high scores for the current difficulty level to the difficulty_scores list
def set_difficulty_highscores(difficulty):
    global difficulty_scores
    global high_scores
    for score in high_scores:
        if score[2] == difficulty:
            difficulty_scores.append(score)

def display_partial_highscores(difficulty):
    global difficulty_scores
    i = 0
    for score in difficulty_scores:
        i += 1
        if i < 11:
            print("{}. {} -- {}".format(i, score[1],score[0]))
    print("\n")      
  

# start_game gets the player's name, sets a new random number, clears the guesses counter, and plays the game
def start_game():
    # allows access to these global variables
    global player_name
    global game_number
    global guesses
    global player_guess
    global difficulty
    global difficulty_scores
    

    # reset values
    player_name = None
    difficulty = None
    guesses = 0
    difficulty_scores = []
    difficulty_name = ""
    player_guess = None
    
    

    # get and set player name - name is required
    while player_name == None:
        try:
            player_name = input("\nPlayer Name:  ").strip() 
            if len(player_name) == 0:
                raise ValueError("\nName required to play")
        except ValueError as err:
            player_name = None
            print(err)

    # get and set difficulty level
    while difficulty == None:
        try:
            difficulty = input("""
                Select Difficulty:
                1. Easy (1 - 10)
                2. Medium (1 - 25)
                3. Hard (1-50)
            """)
            difficulty = int(difficulty)
            if difficulty < 1 or difficulty > 3:
                raise ValueError
            elif difficulty == 1:
                difficulty_name = "Easy"
            elif difficulty == 2:
                difficulty_name = "Medium"
            else:
                difficulty_name = "Hard"
            set_difficulty_highscores(difficulty)
        except ValueError:
            print("Not a valid difficulty level.  Select again")
            difficulty = None
    
    #set random number based on difficulty
    starting_number = 1
    if difficulty == 1:        
        ending_number = 10
    elif difficulty == 2:        
        ending_number = 25
    elif difficulty == 3:        
        ending_number = 50
    game_number = random.randint(starting_number,ending_number)

    #welcome message
    print("""
        Hello, {}.

        =====>    Welcome to the    <=====
        =====> NUMBER GUESSING GAME <=====

            To win this game,  you will  
             need to guess the correct 
               number from 1 to {}.
        """.format(player_name,ending_number))
    
    #showing high scores
    if len(difficulty_scores) > 0 and len(difficulty_scores)< 10:
        print("Top {} {} Highscores".format(len(difficulty_scores), difficulty_name))
        display_partial_highscores(difficulty)
    elif len(difficulty_scores) > 9:
        print("Top 10 {} Highscores".format(difficulty_name))
        display_partial_highscores(difficulty)
    elif len(difficulty_scores) == 0:
        print("There are currently no {} scores.\n".format(difficulty_name))

    # Play Game
    while player_guess != game_number:
        player_guess = input("Please enter a number from 1 to {}: ".format(ending_number))
        
        try:
            player_guess = int(player_guess)
            guesses += 1
            if player_guess < starting_number or player_guess > ending_number:
                print("That number does not fall within {} to {}".format(starting_number, ending_number))        
            elif player_guess == game_number:
                print("""
                ********
                You win!
                ********
                """)
                print("It took you {} attempts.".format(guesses))
                record_highscore(guesses, player_name, difficulty)
                play_again()
            elif player_guess < game_number:
                print("\nYour guess was lower than the correct number")
            else:
                print("\nYour guess was higher than the correct number")
        except ValueError:
            print("\nSorry, that is not a valid number, please try again.")


# Kick off the program by calling the start_game function.
start_game()

