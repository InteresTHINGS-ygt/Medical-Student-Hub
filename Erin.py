import random

memorize = []
memorize_new = []
index = 0

def erin(): # the start of the program
    global memorize
    global memorize_new
    thing = ""
    print("Having trouble memorizing? Erin will make it easier!")
    print('Write the things that you need to memorize (Type "stop" to end your list):')

    while thing != "stop": # Enter things to memorize until you type "stop"
        thing = input("> ")
        memorize.append(thing)
    
    memorize.remove("stop") # Remove the item "stop"
    memorize_new = memorize.copy() # set the new list
    memo()

        
def memo(): # the main associative function
    global memorize
    global memorize_new
    print("Now, let's make associations between things. Remember, the more creative, the better!")
    for i in range (len(memorize) - 1):                                     # This one gets two random items to make associations between them
        index = random.randint(0, len(memorize_new) - 1)                    # generate a random index value
        t1 = memorize_new[index]                                            # set the first item
        del memorize_new[index]                                             # remove the item to avoid showing the same item
        index = random.randint(0, len(memorize_new) - 1)                    # reset index for the second item
        t2 = memorize_new[index]                                            # get the second item
        print("What's the connection between", t1, "and", t2, "\b?")        # ask for the connection
        connection = input("> ")

    print("Now, write down anything you remember. Anything.")
    remember = input("> ") # this is just for typing, nothing is actually stored

    print("Here is the whole list:")
    for x in range (len(memorize)): # show the whole list
        print(memorize[x])

    print("How many did you remember correctly? (remove 1 point for every incorrect item)")

    while True: # Check if the correct answer count is a valid value
        try:
            correct = int(input("> "))
            break  # Break the loop if the input is a valid integer
        except ValueError:
            print("Invalid input. Please try again.")

    if correct > round(len(memorize)):
        print("Well, you broke the rules of the universe. Would you like to try again?")
        print("Yes / No")
        choice = str(input("> "))
        if choice == "yes":
            memo()
    elif correct > round(len(memorize) * 0.8):
        print("You are doing fantastically! Would you like to try again?")
        print("Yes / No")
        choice = str(input("> "))
        if choice == "yes" or choice == "YES" or choice == "Yes":
            memo()
    elif correct > round(len(memorize) * 0.5):
        print("Yeah, it's pretty good, you'll get better over time! Would you like to try again?")
        print("Yes / No")
        choice = str(input("> "))
        if choice == "yes" or choice == "YES" or choice == "Yes":
            memo()
    else:
        print("Well, that needs some work. Would you like to try again?")
        print("Yes / No")
        choice = str(input("> "))
        if choice == "yes" or choice == "YES" or choice == "Yes":
            memo()

