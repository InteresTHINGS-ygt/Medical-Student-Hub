import random

def ventor():
    print("Feeling like the world is coming apart? Ventor comes to help you!")
    print("Mental health plays a supreme importance in our lives.")
    print("If you are feeling overwhelmed, type this exact sentence (without quotes):")
    print('"I am overwhelmed!"')
    sentence = str(input("> ")) # type "I am overwhelmed!"

    if sentence == "I am overwhelmed!":
        print("Now, enter all of your negative thoughts and feelings which overwhelm you:")
        print("Vent anything out! No one is watching you. Your thoughts will be kept private.")
        thought = str(input("> ")) # Enter your negative thoughts

        print("Now, type the counter-thoughts. (if you have any)")
        print("This will help you see your negative thoughts as they really are. Just unhelpful thoughts.")
        print('For example, if your negative thought is "I am the worst", then a counter-thought can be something like "I am just improving".')
        thought = str(input("> ")) # Enter your counter-thoughts (if you have any)

        print("Now, choose between these 3 options:")
        print("1- Do as many pushups as you can")
        print("2- Do some math problems")
        print("3- Take a photo of an object")
        option = int(input("> ")) # Choose an option

        if option == 1:
            print("Pushup time!")
            print("Press any key to start")
            space = input() # press any key
            print("When you are done, press any key")
            space = input()
            print("Enter the number of pushups you have done:")
            pushups = int(input("> "))

            if pushups > 30:
                print("You are doing great! Thank you!")
            elif pushups > 10:
                print("Nice job, you'll get better over time!")
            else:
                print("Well, it's a bit on the low side. Make sure to improve yourself!")
        elif option == 2:
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            x = 0
            y = 0
            correct = 0

            for i in range(5):
                x = numbers[random.randint(0, 9)] # Get a random number from the list
                y = numbers[random.randint(0, 9)] # Get a random number from the list
                print(x, "*", y, "= ?")           # Ask the math problem
                answer = int(input("> "))         # Give an answer
                if answer == x * y:               # Each correct answer is worth 1 point
                    correct += 1

            print("Your correct answers:", correct, "\b/5")
            if correct == 5:
                print("Perfection! Congrats!")
            elif correct == 4:
                print("You are doing great!")
            elif correct == 3:
                print("It's quite good!")
            else:
                print("Keep trying! You'll do better next time!")
        elif option == 3:
            objects = ["glass", "car", "lamp", "notebook", "table", "your room", "fridge", "toilet", "windows", "mirror", "door", "sky", "book", "flower", "tree", "water", "shoes"]
            print("Take a photo of", objects[random.randint(0, 16)]) # Choose a random object
            print("When you are done, press any key")
            space = input()
            print("Congratulations, you are now more present!")
                

