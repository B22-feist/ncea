# Define the question, answers and the correct answers

questions = ("\nIs the treaty of Waitangi becoming more important in NZ law? \n", "What percentage of the NZ population is Maori ?\n", "What is the Waitangi Tribunal\n", "What was an important Piece of legislation during 1972 for Maori rights?\n", "The NZ land wars were a series of wars fought between Maori and British allies. What was the cause of the war? \n","Were the Moriori eaten by Maori? T or F\n","How many Maori seats in parliament are there?\n","What political party is supposed to represent Maori interest in parliament?\n", "Layer these Maori tribal groups from largest to smallest?\n","Who is the Te Kingitanga (Maori king) currently?\n",)
answer1 = ("A) True","A) 16","A) A parliament","A) The Maori language act, which established Maori as a national language","A) White settlers wanting more land","A) True","A) 5","A) labour" ,"A) Iwi, Hapu, Whanau","A) Tūheitia")
answer2 = ("B) False","B) 16.5","B) A body that deals with breaches of the treaty of Waitangi","B) Introduction of the Waitangi tribunal","B) Perceived threat of Maori conquering the white settlers","B) False","B) 6","B) Act","B) Whanau, Hapu, Iwi","B) Pōtatau")
answer3 = ("","C) 17","C) A political movement","C) All stolen Maori land returned","c) Break up of the british empire","","C) 7","C) National","C) Hapu, Iwi, Whanau","C) Koroki")
answer4 = ("","D) 17.5","D) A body of law","D) Maori gaining full access to the bill of rights","D) It didn't happen","","D) 8","D) Te Pati Maori","D) Iwi, Whanau, Hapu","D) Atairangikaahu")
correctAnswer = ("A) True", "B) 16.5", "B) A body that deals with breaches of the treaty of Waitangi", "A) The Maori language act, which established Maori as a national language","A) White settlers wanting more land","B) False","C) 7","D) Te Pati Maori","A) Iwi, Hapu, Whanau","A) Tūheitia")



#sets up a while true loop for my program to run
while True:
    score = 0
    
    print("""\nWelcome, to my Quiz. It is about Maori custom in nz \n to pass you need to get more than 5 out of ten """)
    start = str(input("do you wish to begin? t of f: "))
    
    if start != "f":         
                
        # for loop to print questions
        for x in range(len(questions)):
                
                listOfQuestions = (answer1[x], answer2[x], answer3[x], answer4[x])     
                
                print(questions[x])
                
        # this code section iterates across list of different possible answers 
        # True/False questions have only two possible answers
                for y in range (len(listOfQuestions)):
                        if listOfQuestions[y] != "": #checks if there are more than two possible answers
                                print(listOfQuestions[y])
                

                while True:
                
                 try:
                  userInput = str(input())
                  break
                
                 except:
                  print("\nyou have entered an incorrect answer please, enter the answer again")
                
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
                        print("\nyou got the question right\n")
                        score += 1
                
                else:
                        print('you got the question wrong\n')
         
        
        if score == 10:
              print("You have perfect 10 out of 10 in this quiz, congratulation")
        
        elif score <= 5:
              print(f"well done, you passed with a score of {score}")
        
        else:
              print(f"sorry, you lost with {score} out of 10. Better luck next time.")
        
        retake = str(input("do you want to retake the test. T or F "))
        
        if retake.lower() == "f":
         print("Thank you for taking the test the program will end now.")
         break