from random import choice


# Class #

class generator():
    def generator_password(size):
        characters = "0123456789abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        password = ""
        for i in range(size):
            password += choice(characters)
        return password
    def question_archive(answer):
        while answer != "yes" and answer != "no" and answer != "no":
            answer = input("Do you want to save to an archive? yes/no: ")
        if answer == "yes":
            name_of_archive = input("file name: ")
            archive = open("{}.txt".format(name_of_archive), "a") 
            archive.write("user name: {}\n".format(name)) 
            archive.write("password: {}\n".format(password)) 
            archive.close() 
            leave = input("Do you want to leave? yes/no: ")
            while leave == "no" or leave == "nao":
                leave = input("Do you want to leave? yes/no: ")
        elif answer == "no" or answer == "nao":
            print("**************************")
            print("user name: {}".format(name))
            print("password: {}".format(password))
            print("**************************")
            leave = input("Do you want to leave? yes/no: ")
            while leave == "no" or leave == "nao":
                leave = input("Do you want to leave? yes/no: ")                



print("*************************")
print("password generator")
print("*************************")

name = input("input username: ")
amount = int(input("Type the desired amount of characters  for the password? password: "))

password = generator.generator_password(amount)
print("YOUR PASSWORD: {}".format(password))
print()
question = input("Do you want to save to a file? yes/no: ")
question = generator.question_archive(question)