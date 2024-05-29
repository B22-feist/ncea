from question import questionDictionary
question = questionDictionary["questions"]
answer1 = questionDictionary["possible answers 1"]
answer2 = questionDictionary["possible answers 2"]
answer3 = questionDictionary["possible answers 3"]
answer4 = questionDictionary["possible answers 4"]
correctAnswer = questionDictionary["correct answers"]

#sets up a while true loop for my program to run
while True:
    score = 0
    print(" ")
    print("""Welcome, to my Quiz. It is about Maori custom in nz \n to pass you need to get more than 5 out of ten """)

    # sets up a for loop to repeat for the number of questions
    for x in range(10):

        print(question[x])

        # makes the possible answer that don't hold value not appear to make the UI look cleaner
        if answer1[x] != "":
            print(answer1[x])

        if answer2[x] != "":
            print(answer2[x])

        if answer3[x] != "":
            print(answer3[x])

        if answer4[x] != "":
            print(answer4[x])

        while True:
            try:
                userInput = input()
                break
            except:
                print("you have entered an incorrect answer please, enter the answer again")

        # converts the user input into a string or float when needed
        try:
            userInput = float(userInput)
        except:
            userInput = str(userInput)

        # if the user enters a letter the user input is converted to answer they meant to put in.
        match userInput.lower():
            case "a":
                userInput = answer1[x]
            case "b":
                userInput = answer2[x]
            case "c":
                userInput = answer3[x]
            case "d":
                userInput = answer4[x]

        if userInput == correctAnswer[x]:
            print("you got the question right\n")
            score += 1
        else:
            print('you got the question wrong')

    print(f"well done you have finished the quiz and have scored {score} out of 10")

    retake = str(input("do you want to retake the test. T or F"))
    if retake.lower() != "t":
        print("Thank you for taking the test the program will end now.")
        break
