import hanged
import divination

def choice_game():
    print("*********************************")
    print("*******choice your game!*******")
    print("*********************************")

    print("(1) hangman (2) divination")

    game = int(input("What game? "))

    if(game == 1):
        print("player hanged")
        hanged.play()
    elif(game == 2):
        print("player divination")
        divination.play()

if(__name__ == "__main__"):
    choice_game()
