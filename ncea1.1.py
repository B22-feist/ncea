# this section adds in the question dictionary which I have stored on a seperate file as well as convert the dictionary into something I can use for the questions.
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
    
    print("""\nWelcome, to my Quiz. It is about Maori custom in nz \n to pass you need to get more than 5 out of ten """)
    start = str(input("do you wish to begin? t of f: "))
    
    if start != "f":         
                
                # sets up a for loop to repeat for the number of questions
        for x in range(len(question)):
                
                listOfQuestion = (answer1[x], answer2[x], answer3[x], answer4[x])     
                
                print(question[x])
                
        # makes the possible answer that don't hold value not appear to make the UI look cleaner
                for y in range (len(listOfQuestion)):
                        if listOfQuestion[y] != "":
                                print(listOfQuestion[y])
                

                while True:
                
                 try:
                  userInput = str(input())
                  break
                
                 except:
                  print("you have entered an incorrect answer please, enter the answer again")
                
                # converts the user input into a string or float when needed
                
                userInput = str(userInput)
                
                # if the user enters a letter the user input is converted to answer they meant to put in.
                match userInput.lower():
                                
                        case "a":
                                userInput = answer1[x]
                                
                        case"b":
                                userInput = answer2[x]
                                
                        case "c":
                                userInput = answer3[x]
                                
                        case "d":
                                userInput = answer4[x]
                                
                        case "f":
                                userInput = answer2[x]
                                
                        case "t":
                                userInput = answer1[x]
                        
                        case "true":
                                userInput = answer1[x]

                        case "false":
                                userInput = answer2[x]
                
                if userInput == correctAnswer[x]:
                        print("you got the question right\n")
                        score += 1
                
                else:
                        print('you got the question wrong\n')
         
        
        if score == 10:
              print("You have perfect 10 out of 10 in this quiz, congratulation")
        
        elif score <= 5:
              print(f"well done, you passed with a score of {score}")
        
        else:
              print(f"sorry, you lost with {score} out of 10. Better luck next time.")
        
        retake = str(input("do you want to retake the test. T or F"))
        
        if retake.lower() == "f":
         print("Thank you for taking the test the program will end now.")
         break