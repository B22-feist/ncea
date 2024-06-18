# Define the question, answers and the correct answers

questions = ("\nIs the treaty of Waitangi becoming more important in NZ law? \n", "What percentage of the NZ population is Maori ?\n", "What is the Waitangi Tribunal\n", "What was an important Piece of legislation during 1972 for Maori rights?\n", "The NZ land wars were a series of wars fought between Maori and British allies. What was the cause of the war? \n","Were the Moriori eaten by Maori? T or F\n","How many Maori seats in parliament are there?\n","What political party is supposed to represent Maori interest in parliament?\n", "Layer these Maori tribal groups from largest to smallest?\n","Who is the Te Kingitanga (Maori king) currently?\n",)
answer1 = ("A) True","A) 16","A) A parliament","A) The Maori language act, which established Maori as a national language","A) White settlers wanting more land","A) True","A) 5","A) labour" ,"A) Iwi, Hapu, Whanau","A) Tūheitia")
answer2 = ("B) False","B) 16.5","B) A body that deals with breaches of the treaty of Waitangi","B) Introduction of the Waitangi tribunal","B) Perceived threat of Maori conquering the white settlers","B) False","B) 6","B) Act","B) Whanau, Hapu, Iwi","B) Pōtatau")
answer3 = ("","C) 17","C) A political movement","C) All stolen Maori land returned","c) Break up of the british empire","","C) 7","C) National","C) Hapu, Iwi, Whanau","C) Koroki")
answer4 = ("","D) 17.5","D) A body of law","D) Maori gaining full access to the bill of rights","D) It didn't happen","","D) 8","D) Te Pati Maori","D) Iwi, Whanau, Hapu","D) Atairangikaahu")
correctAnswer = ("A", "B", "B", "A","A","B","C","D","A","A")

#function to print questions
def printQuestion(num):
        listOfQuestions = (answer1[num], answer2[num], answer3[num], answer4[num]) 
        
        # this code section iterates across list of different possible answers 
        # True/False questions have only two possible answers
        for y in range (len(listOfQuestions)):
                if listOfQuestions[y] != "": #checks if there are more than two possible answers
                        print(listOfQuestions[y])

def passOrFail(userScore):
              #if the user got ten out of ten, the program will tell them they got the question right
        if userScore == 10:
             return print("You have perfect 10 out of 10 in this quiz, congratulation")
        
        #sets up a range so if the user get between 5 and 9 tells the user they got the question right
        elif 9>= userScore <= 5:
              return print(f"well done, you passed with a score of {userScore}")
        
        #tells the user they lost if they get less than four
        else:
              return print(f"sorry, you lost with {userScore} out of 10. Better luck next time.")

#sets up a while true loop for my program to run
while True:
    score = 0
    
    print("""\nWelcome, to my Quiz. It is about Maori custom in nz \n to pass you need to get more than 5 out of ten.\n only enter a, b, c or d """)
    start = str(input("do you wish to begin? t of f: "))
    
    if start != "f":         
                
        # for loop to print questions
        for x in range(len(questions)):
                
                print(questions[x])
                
                # calls function to print questions
                printQuestion(x)
                
                # test if the user's input can be converted to a string and if not ask them to renter their answer
                while True:
                
                 try:
                  userInput = str(input())
                  break
                
                 except:
                  print("\nyou have entered an incorrect answer please, enter the answer again")

                #check if user input is the correct answer, tells the user they got the question correct and 1 to the user score
                if userInput == correctAnswer[x]:
                        print("\nyou got the question right\n")
                        score += 1
                # tells the user they got the question wrong
                else:
                        print('you got the question wrong\n')
         
                passOrFail(score)
        
        # will see if the user wants to retake the, and if so 
        retake = str(input("do you want to retake the test. T or F "))
        
        if retake.lower() == "f":
         print("Thank you for taking the test the program will end now.")
         break