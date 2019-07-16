import random

def play():

    print("*********************************")
    print("Welcome to the guessing game!")
    print("*********************************")

    number_secret = random.randrange(1,101)
    total_attempt = 0
    points = 1000

    print("What level of difficulty?")
    print("(1) easy (2) medium (3) hard ")

    nivel = int(input("level: "))

    if(nivel == 1):
        total_attempt = 20
    elif(nivel == 2):
        total_attempt = 10
    else:
        total_attempt = 5

    for roundi in range(1, total_attempt + 1):
        print("Tentativa {} de {}".format(roundi, total_attempt))

        kick_str = input("Enter a number between 1 and 100: ")
        print("you typed " , kick_str)
        kick = int(kick_str)

        if(kick < 1 or kick > 100):
            print("Enter a number between 1 and 100!")
            continue

        hit = kick == number_secret
        bigger   = kick > number_secret
        smaller   = kick < number_secret

        if(hit):
            print("you did {} points!".format(points))
            break
        else:
            if(bigger):
                print("you missed! Your kick was bigger than the secret number.")
            elif(smaller):
                print("you missed! Your kick was smaller than the secret number.")
            points_lost = abs(number_secret - kick)
            points = points - points_lost

    print("End of the game")

if(__name__ == "__main__"):
    play()
