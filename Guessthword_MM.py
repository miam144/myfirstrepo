import random

words = ["movie","tacos","blue","bunny","snapchat"]
hint1 = ["another word for film","food","color","animal","an app"]
hint2 = ["starts with m","you put different ingridients in a shell, like meat, cheese salsa...","color of the ocean","fox eat them","most people use this app"]
hint3 = ["ends with ie","starts with tac","the color of the sky","is fluffy white with a small tail that lives on land.","ends with chat"]

number = random.randint(0,4)

secretword = words[number]

guess = ""

counter = 0

while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2, 'hint3', 'length','first letter', or 'Give up' for help.")
    guess = input()

    if guess == secretword:
        print("You got it!")
        break

    elif guess == "hint1":
        print( hint1[number] )

    elif guess == "hint2":
        print  (hint2 [number] )

    elif guess == "hint3":
        print (hint2 [number] )

    elif guess == "first letter":
        print (secretword [0] )

    elif guess == "last letter":
        print ( secretword [-1] )

    elif guess == "length":
        print (len(secretowrd) )
    elif guess == "Give up":
        print("The secret word was "+ secretword)
        break
