def main():
    from greeting import Greeting
    choices = 0  #choice counter
    wins = 0 #win counter
    player1 = 0 #player1 win counter
    player2 = 0 #player2 win counter
    player = 0
    game_greeting = Greeting()
    game_greeting.greeting() #First we call our game greeting

    game = game_choice() #We assign our game type by calling our game_choice function
    if game == "1":
        print("You chose the one player game option. Let's begin.")
        #We send user to one player game option
        one_player_game(choices,wins,player1,player2,player)
    elif game =="2":
        print("You chose the two player game option. Let's begin.")  
        #We send user to the two player game option
        two_player_game(choices,wins,player1,player2,player)  


     #This will get the game option from the user, either one player or two player game version
    def game_choice():
        #List for our game player options, one player or two

        #Using while loop for data validation
        game_option = ["1","2"]
        game = input("Would you like the one player or two player option?""1"" or ""2"":")
        while game not in game_option:
            print("That is not a valid entry. Let's try this again.")
            game = input("Would you like the one player or two player option?""1"" or ""2"":")
        else: return game


##############################################################################################################################################
#This function will begin our one player game option, which essentially asks for user input, gathers random AI input, and then determines winner

    def one_player_game(choices,wins,player1,player2,player):
        game_type = 1
        gesture_list = ["Rock","Spock","Paper","Lizard","Scissors"]
        print("Here is a list of available gestures:")
        print([gesture_list])
        #we declare our input variable by calling our get_user input function
        #Then we declare our random choice by caling the get_comp_input function
        player1_choice = get_user_input(choices,gesture_list,player)
        player2_choice = get_comp_input(choices,gesture_list)
        choices +=1

        #Now we send our inputs to the function that will determine winner

        find_winner(choices,player1_choice,player2_choice,wins,player1,player2,gesture_list,game_type,player)

#################################################################################################################################################
#This function will begin our two_player game option, which will ask for user input twice,while validating their entries, then determine winner

    def two_player_game(choices,wins,player1,player2,player):
        game_type = 2
        gesture_list = ["Rock","Spock","Paper","Lizard","Scissors"]
        print("Here is a list of available gestures:")
        print([gesture_list])
      #We declare our imput variable by calling our get_user_input function
      #Then declare our random choice by calling the get_comp_input function
        player1_choice = get_user_input(choices,gesture_list,player)
        player +=1
        player2_choice = get_user_input(choices,gesture_list,player)
        player -=1
        choices +=1
        #We now send our inputs to the function that determines winner
        find_winner(choices,player1_choice,player2_choice,wins,player1,player2,gesture_list,game_type,player)

    def get_user_input(choices,gesture_list,player):
        #Asking input from user and run a loop until a proper selection is made
        player1_choice = input("Please choose gesture from above list:")
        player1_choice = player1_choice.capitalize() #Let's capitalize first letter of input only
        while player1_choice not in gesture_list:
            print("That is not a valid entry. Please try again.")
            player1_choice = input("Please choose gesture from above list:")
            player1_choice = player1_choice.capitalize()
        else:
            choices +=1
            player +=1
            print("Player",player,"#",choices,"choice is:",player1_choice,sep="")
            return player1_choice
        
    #Now this function returns a random gesture from our list for our AI player

    def get_comp_input(choices,gesture_list):
        import random
        player2_choice = random.choice(gesture_list)
        choices +=1
        print("Player 2 ",choices,"choice is:",player2_choice, sep="")
        return player2_choice
    

    #This function will determine our winner -best out of three wins

    def final_winner(choices,wins,player1,player2):
        if player1>player2:
            print("Player 1 has",player1,"wins, so player 1 wins best out of three!")
        elif player1<player2:
            print("Player 2 has",player2,"wins, so player 2 wins best out of three!")

    #We now send the user to the function that will allow them to restart game

        choice()

    #This function determines winner for each game(if not a tie). It also adds up the wins each player has,
    #the total number of games, and it also sends the user back to the start of game if necessary

    def find_winner(choices,player1_choice,player2_choice,wins,player1,player2,gesture_list,game_type,player):

        #Block 1 choices
        if player1_choice == gesture_list[0]:
            if player2_choice == gesture_list[0]:
                print("You tie. We will have to try again.")

            if game_type ==1:
                one_player_game(choices,wins,player1,player2,player)
            elif game_type ==2:
                print("Going back to game type 2.")
                two_player_game(choices,wins,player1,player2,player)
            elif player2_choice == gesture_list[1]:
                print("Player 2 wins: SPock vaporizes Rock.")
                wins +=1
                player2 +=1
                if wins <3:
                    print("Game #", wins,"complete. Let's go again!", sep="")
                    if game_type ==1:
                        one_player_game(choices, wins,player1,player2,player)
                    elif game_type ==2:
                        print("Going back to game type 2.")
                        two_player_game(choices,wins,player1,player2,player)
            else:
                print("Now we determine best out of three!")
                final_winner(choices,wins,player1,player2)
        elif player2_choice ==gesture_list[2]:
            print("Player 2 wins: Paper covers Rock!")
            wins +=1
            player2 +=1
            if wins <3:
                print("Game #",wins,"complete. Let's go again!", sep="")
                if game_type==1:
                    one_player_game(choices,wins,player1,player2,player)

            elif game_type == 2:
                print("Going back to game type 2.")     
                two_player_game(choices, wins, player1,player2,player)   
            else:
                print("Now we determine best out of three!")
                final_winner(choices, wins,player1,player2)
        elif player2_choice == gesture_list[3]:
            print("Player 1 wins: Rock crushes Lizard!")
            wins +=1
            player2 +=1
            if wins <3:
                print("Game #",wins,"complete. Let's go again!", sep="")
                if game_type==1:
                    one_player_game(choices,wins,player1,player2,player)
                elif game_type ==2:
                    print("Going back to game type 2.")     
                two_player_game(choices, wins, player1,player2,player) 
            else:
                print("Now we determine best out of three!")
                final_winner(choices, wins,player1,player2)
        elif player2_choice ==gesture_list[4]:
            print("Player 2 wins: Scissors cuts Paper!")
            wins +=1
            player2 +=1
            if wins <3:
                print("Game #",wins,"complete. Let's go again!", sep="")
                if game_type==1:
                    one_player_game(choices,wins,player1,player2,player)

            elif game_type == 2:
                print("Going back to game type 2.")     
                two_player_game(choices, wins, player1,player2,player)   
            else:
                print("Now we determine best out of three!")
                final_winner(choices, wins,player1,player2)


        #Block 2 choices
        elif player1_choice == gesture_list[1]:
            if player2_choice == gesture_list[0]:
                print("Player 1 wins: Spock vaporizes Rock!")
                wins +=1
                player1 +=1
                if wins <3:
                    print("Game #",wins,"complete. Let's go again!", sep="")
                if game_type==1:
                    one_player_game(choices,wins,player1,player2,player)

            elif game_type == 2:
                print("Going back to game type 2.")     
                two_player_game(choices, wins, player1,player2,player)   
            else:
                print("Now we determine best out of three!")
                final_winner(choices, wins,player1,player2)
        elif player2_choice == gesture_list[1]:
            print("You both tie. We now go again!")
            if game_type==1:
                one_player_game(choices,wins,player1,player2,player)
            elif game_type == 2:
                print("Going back to game type 2.")     
                two_player_game(choices, wins, player1,player2,player)   
            elif player2_choice == gesture_list[2]:
                print("Player 2 wins: Paper disproves Spock!")
                wins +=1
                player2 +=1
                if wins <3:
                    print("Game #",wins,"complete. Let's go again!", sep="")
                if game_type==1:
                    one_player_game(choices,wins,player1,player2,player)

            elif game_type == 2:
                print("Going back to game type 2.")     
                two_player_game(choices, wins, player1,player2,player)   
            else:
                print("Now we determine best out of three!")
                final_winner(choices, wins,player1,player2)
        elif player2_choice == gesture_list[3]:
            print("Player 2 wins: Lizard poisons Spock!")
            wins +=1
            player2 +=1
            if wins <3:
                print("Game #",wins,"complete. Let's go again!", sep="")
            if game_type==1:
                one_player_game(choices,wins,player1,player2,player)

            elif game_type == 2:
                print("Going back to game type 2.")     
                two_player_game(choices, wins, player1,player2,player)   
            else:
                print("Now we determine best out of three!")
                final_winner(choices, wins,player1,player2)
        elif player2_choice == gesture_list[4]:
            print("Player 1 wins: Spock smashes Scissors!")
            wins +=1
            player2 +=1
            if wins <3:
                print("Game #",wins,"complete. Let's go again!", sep="")
            if game_type==1:
                one_player_game(choices,wins,player1,player2,player)

        elif game_type == 2:
            print("Going back to game type 2.")     
            two_player_game(choices, wins, player1,player2,player)   
        else:
            print("Now we determine best out of three!")
            final_winner(choices, wins,player1,player2)

        #Block 3 choices

        if player1_choice == gesture_list[2]:
            if player2_choice == gesture_list[0]:
                print("Player 1 wins: Paper covers Rock!")
                wins +=1
                player1 +=1
                if wins <3:
                    print("Game #",wins,"complete. Let's go again!", sep="")
                if game_type==1:
                    one_player_game(choices,wins,player1,player2,player)
                elif game_type == 2:
                    print("Going back to game type 2.")     
                    two_player_game(choices, wins, player1,player2,player)   
            else:
                print("Now we determine best out of three!")
                final_winner(choices, wins,player1,player2)
        elif player2_choice == gesture_list[1]:
            print("Player 1 wins: Paper disproves Spock!")
            wins +=1
            player1 +=1
            if wins <3:
                print("Game #",wins,"complete. Let's go again!", sep="")
            if game_type==1:
                one_player_game(choices,wins,player1,player2,player)
            elif game_type == 2:
                print("Going back to game type 2.")     
                two_player_game(choices, wins, player1,player2,player)   
            else:
                print("Now we determine best out of three!")
                final_winner(choices, wins,player1,player2)


 #MISH REFER TO player2,gesture2 on page 10












