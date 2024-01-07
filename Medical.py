import Questions as q

def med_career():
    suitability = -13 # Set that way in order to make the lowest score 0 and highest score 39 which will become 100
    answer = 0
    question = 0

    print()
    print("There are 13 questions. Determine how much do you agree with each statement.")
    print("BE AS HONEST AS POBBISLE. OTHERWISE, THE TEST IS INVALID.")
    print("1 = Strongly Disagree")
    print("2 = Disagree")
    print("3 = Agree")
    print("4 = Strongly Agree")
    print()
    
    while question < 13: # This loop shows each question
        print("Question", (question + 1))
        print(q.medical_questions[question])
        answer = input("> ")
        if answer == "1" or answer == "2" or answer == "3" or answer == "4":
            answer = int(answer) # turns answer into integer
            if question >= 8: # negative-keyed items
                suitability += (5 - answer)
                print()
                question += 1
            else: # positive-keyed items
                suitability += answer
                print()
                question += 1
        else: # In case of an invalid answer, show the same question again
            print("Your answer is invalid, try again")
            print()

    suitability = round((suitability/39)*100) # Convert it to a percentage
    print("Your suitability for a medical career is", suitability,"%")

    if suitability > 80:
        print("You would have a great time pursuing a medical lifestyle!")
    elif suitability > 60:
        print("Although you may have a good time having a medical lifestyle, make sure to check out other options before deciding.")
    else:
        print("You are better off pursuing something else. Medical lifestyle may not be for you.")

    