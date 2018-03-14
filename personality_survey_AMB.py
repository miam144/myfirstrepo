while True:
    print ("What's your favorite sport?")
    sport = input ()

    if sport == "tennis":
        print ("That's my favorite sport too!")
    elif sport == "soccer":
        print ("Soccer is my other favorite s[port to play!")
    elif sport == "squash":
        print ("I love squash aswell")

    print ("What's your favorite food?")
    food = input ()

    if food == "crepe" or food =="crepes":
        print ("What is your favorite kind of salty crepe?")
        favoritecrepe = input ()
        if favoritecrepe == "jambon et fromage":
            print ("Thinking about that makes me hungry!")


    myrestaurants = [ 'Meli-Melo', 'Medeterranio', 'Melting Pot', 'Abis']
    print ("Where do you like to eat?")
    food = input()

    if food in myrestaurants:
        print ("Cool")




    print("Play agin? (Yes/No)")
    answer = input()
    if answer == "Yes":
        print ("Ok, let's do it again.")
    else:
        print("Alright, see you later.")
        break
