import random


def play():
    print_message_opening()
    secret_word = loanding_secret_word()

    letters_successful = initialize_letters_successful(secret_word)
    print(letters_successful)

    hanged = False
    hit = False
    mistakes = 0

    while(not hanged and not hit):

        kick = can_kick()

        if(kick in secret_word):
            brand_kick_correct(kick, letters_successful, secret_word)
        else:
            mistakes += 1
            pass_hanged(mistakes)

        hanged = mistakes == 7
        hit = "_" not in letters_successful

        print(letters_successful)

    if(hit):
        print_message_message()
    else:
        print_reader_message(secret_word)


def pass_hanged(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(mistakes == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(mistakes == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(mistakes == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(mistakes == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(mistakes == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (mistakes == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def print_message_message():
    print("Congratulation, you win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_loser_message(secret_word):
    print("you lost!")
    print("the correct one was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def brand_kick_correct(kick, letters_successful, secret_word):
    index = 0
    for letter in secret_word:
        if (kick == letter):
            letters_successful[index] = letter
        index += 1

def can_kick():
    kick = input("Which letter? ")
    kick = kick.strip().upper()
    return kick

def initialize_letters_successful(word):
    return ["_" for letter in word]

def print_message_opening():
    print("*********************************")
    print("***Welcome to the hangman game!***")
    print("*********************************")

def loanding_secret_word():
    archive = open("word.txt", "r")
    word = []

    for line in archive:
        line = line.strip()
        word.append(line)

    archive.close()

    number = random.randrange(0, len(word))
    secret_word = word[number].upper()
    return secret_word


if(__name__ == "__main__"):
    play()