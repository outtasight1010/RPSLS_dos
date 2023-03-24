class Greeting:
    def __init__(self):
        pass
    

    def greeting(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("You will have the option for a one or two player game!")
        print("")
        print("The rules are: \n1.Scissors cuts Paper.\n2.Paper covers Rock.\n3.Rock crushes Lizard.\n4.Lizard posions Spock.\n5.Spock smashes Scissors.")
        print("\n6.Scissors decapitates Lizard.\n7.Lizard eats paper.\n8.Paper disproves Spock.\n9.Spock vaporizes Rock.\n10.Rock breaks Scissors.")

class GameRules(Greeting):
    def __init__(self):
        super().__init__()



game_greeting = Greeting()       
