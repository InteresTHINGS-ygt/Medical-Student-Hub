answer = ""
current_type = 1

# These functions ask you the questions. 36 total questions, you'll be asked 8 of them.
def one_two():
    global current_type
    print("I help others because...")
    print("A. It's morally the right thing to do")
    print("B. I have to take care of their feelings")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 2
    return current_type

def one_three():
    global current_type
    print("I get things done...")
    print("A. The right way")
    print("B. The most efficient way")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 3
    return current_type

def one_four():
    global current_type
    print("I become self-critical because...")
    print("A. I have made a critical mistake")
    print("B. I feel inferior to others")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 4
    return current_type

def one_five():
    global current_type
    print("I gather information...")
    print("A. To improve and perfect the world")
    print("B. For the sake of it, for my own competence")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 5
    return current_type

def one_six():
    global current_type
    print("I follow the rules because...")
    print("A. It's plain wrong to break them")
    print("B. Bad things can happen if I break them")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 6
    return current_type

def one_seven():
    global current_type
    print("My idealism is more like...")
    print("A. Perfection, without mistakes")
    print("B. Optimism, without negativity")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 7
    return current_type

def one_eight():
    global current_type
    print("I express my anger when I...")
    print("A. Should, repressing anything else")
    print("B. Want to, without rules")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 8
    return current_type

def one_nine():
    global current_type
    print("One of my faults are...")
    print("A. Being too impatient and rigid")
    print("B. Being too lax and indulgent")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 9
    return current_type

def two_three():
    global current_type
    print("I prefer getting my attention through...")
    print("A. Giving to others so I feel loved")
    print("B. Being the best so I feel valuable")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 3
    return current_type

def two_four():
    global current_type
    print("I am more aware of...")
    print("A. Others' feelings, I need to take care of them")
    print("B. My own feelings, I explore them in depth")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 4
    return current_type

def two_five():
    global current_type
    print("I am more likely to be...")
    print("A. Too willing to give and express")
    print("B. Too private and contained")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 5
    return current_type

def two_six():
    global current_type
    print("I am helpful because...")
    print("A. I know what the other person needs")
    print("B. I need to feel protected and safe")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 6
    return current_type

def two_seven():
    global current_type
    print("I am more likely to...")
    print("A. Feel obligated to help, others' needs over my own needs")
    print("B. Feel limited by responsibility, I need my freedom and I help when I want to")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 7
    return current_type

def two_eight():
    global current_type
    print("I tend to manipulate others through...")
    print("A. Flattery and compliments")
    print("B. Power and force")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 8
    return current_type

def two_nine():
    global current_type
    print("I tend to...")
    print("A. Know what others want, so I can help them")
    print("B. Go along with what others want, so I can feel peaceful")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 9
    return current_type

def three_four():
    global current_type
    print("Others need to see my...")
    print("A. Best self, I need to be impressive")
    print("B. Real self, I need to show the real me")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 4
    return current_type

def three_five():
    global current_type
    print("I tend to focus on the...")
    print("A. Final goal, I need to succeed")
    print("B. Process, I need to understand the world")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 5
    return current_type

def three_six():
    global current_type
    print("I'm more focused on...")
    print("A. How I appear to others, am I impressive or not?")
    print("B. Avoiding bad consequences, am I safe or not?")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 6
    return current_type

def three_seven():
    global current_type
    print("I tend to...")
    print("A. Play to win")
    print("B. Play to have fun")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 7
    return current_type

def three_eight():
    global current_type
    print("I am more like:")
    print("A. A polished image of success")
    print("B. A raw pillar of strength and power")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 8
    return current_type

def three_nine():
    global current_type
    print("I am more focused on...")
    print("A. Action and getting things done")
    print("B. Relaxation and inner peace")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 9
    return current_type

def four_five():
    global current_type
    print("I tend to be...")
    print("A. Involved with my own feelings to understand myself")
    print("B. Detached from feelings in order to understand the world")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 5
    return current_type

def four_six():
    global current_type
    print("I tend to have a/an...")
    print("A. Very strong sense of myself, based on inner experience")
    print("B. Unsure sense of myself, I do a lot of 'it depends'")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 6
    return current_type

def four_seven():
    global current_type
    print("I feel disappointed, and...")
    print("A. I feel like I will never get what I need")
    print("B. I move on to the better thing")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 7
    return current_type

def four_eight():
    global current_type
    print("I tend to...")
    print("A. Be full of vulnerability")
    print("B. Avoid vulnerability to be strong")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 8
    return current_type

def four_nine():
    global current_type
    print("I prefer being...")
    print("A. Emotionally intense, full of highs and lows ")
    print("B. Emotionally calm, I need to feel peaceful and relaxed")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 9
    return current_type

def five_six():
    global current_type
    print("I tend to...")
    print("A. Trust only my mind, as others are less informed")
    print("B. Struggle trusting my mind, as the world is uncertain")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 6
    return current_type

def five_seven():
    global current_type
    print("I tend to be more naturally...")
    print("A. Focused and intense, I need to feel competent")
    print("B. Expansive and variety-seeking, I need to feel satisfied")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 7
    return current_type

def five_eight():
    global current_type
    print("I am more...")
    print("A. Cerebral, I need to think things through before acting")
    print("B. Physical, I tend to act readily and immediately")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 8
    return current_type

def five_nine():
    global current_type
    print("I am more about...")
    print("A. Contrasts, fine details, detachment, focused mental activity")
    print("B. Similarities, harmony, comfort, drifting mental activity")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 9
    return current_type

def six_seven():
    global current_type
    print("I tend to...")
    print("A. Vividly imagine worst-case scenarios")
    print("B. Believe that things will work for their best")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 7
    return current_type

def six_eight():
    global current_type
    print("When it comes to fear,  I...")
    print("A. Recognize my fears, so I can defeat them")
    print("B. Deny my fears, so I feel stronger")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 8
    return current_type

def six_nine():
    global current_type
    print("I am more likely to...")
    print("A. Worry or overthink more than I should")
    print("B. Downplay the importance of the problem")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 9
    return current_type

def seven_eight():
    global current_type
    print("I tend to seek...")
    print("A. Variety, I need to feel satisfied")
    print("B. Intensity, I need to feel powerful")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 8
    return current_type

def seven_nine():
    global current_type
    print("I tend to...")
    print("A. Seek what I want, as I know what I need for my enjoyment")
    print("B. Go along with what others want, as I need to feel inner comfort")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 9
    return current_type

def eight_nine():
    global current_type
    print("My stability is more like...")
    print("A. Actively controlling my environment, as I need to feel strong")
    print("B. Having inner peace and repressing anger, as I need to feel comfortable")
    answer = str(input("> "))
    if answer.upper() == "B":
        current_type = 9
    return current_type

def archetype(): # This is the actual test.
    print("Welcome to the Medical Student Archetype Test!")
    print("This test is just for fun.")
    print("This test is based on the Enneagram personality theory.")
    print("Press A or B to give answers.")

    for i in range (9):
        if current_type == 1 and i == 0:
            one_two()
        elif current_type == 1 and i == 1:
            one_three()
        elif current_type == 1 and i == 2:
            one_four()
        elif current_type == 1 and i == 3:
            one_five()
        elif current_type == 1 and i == 4:
            one_six()
        elif current_type == 1 and i == 5:
            one_seven()
        elif current_type == 1 and i == 6:
            one_eight()
        elif current_type == 1 and i == 7:
            one_nine()
        elif current_type == 1 and i == 8:
            print("You are the Top Student!")
        elif current_type == 2 and i == 1:
            two_three()
        elif current_type == 2 and i == 2:
            two_four()
        elif current_type == 2 and i == 3:
            two_five()
        elif current_type == 2 and i == 4:
            two_six()
        elif current_type == 2 and i == 5:
            two_seven()
        elif current_type == 2 and i == 6:
            two_eight()
        elif current_type == 2 and i == 7:
            two_nine()
        elif current_type == 2 and i == 8:
            print("You are the Helper!")
        elif current_type == 3 and i == 2:
            three_four()
        elif current_type == 3 and i == 3:
            three_five()
        elif current_type == 3 and i == 4:
            three_six()
        elif current_type == 3 and i == 5:
            three_seven()
        elif current_type == 3 and i == 6:
            three_eight()
        elif current_type == 3 and i == 7:
            three_nine()
        elif current_type == 3 and i == 8:
            print("You are the Influencer!")
        elif current_type == 4 and i == 3:
            four_five()
        elif current_type == 4 and i == 4:
            four_six()
        elif current_type == 4 and i == 5:
            four_seven()
        elif current_type == 4 and i == 6:
            four_eight()
        elif current_type == 4 and i == 7:
            four_nine()
        elif current_type == 4 and i == 8:
            print("You are the Romantic!")
        elif current_type == 5 and i == 4:
            five_six()
        elif current_type == 5 and i == 5:
            five_seven()
        elif current_type == 5 and i == 6:
            five_eight()
        elif current_type == 5 and i == 7:
            five_nine()
        elif current_type == 5 and i == 8:
            print("You are the Library!")
        elif current_type == 6 and i == 5:
            six_seven()
        elif current_type == 6 and i == 6:
            six_eight()
        elif current_type == 6 and i == 7:
            six_nine()
        elif current_type == 6 and i == 8:
            print("You are the Troubleshooter!")
        elif current_type == 7 and i == 6:
            seven_eight()
        elif current_type == 7 and i == 7:
            seven_nine()
        elif current_type == 7 and i == 8:
            print("You are the Adventurer!")
        elif current_type == 8 and i == 7:
            eight_nine()
        elif current_type == 8 and i == 8:
            print("You are the Hero!")
        elif current_type == 9 and i == 8:
            print("You are the Quiet One!")
                            

        
                                    