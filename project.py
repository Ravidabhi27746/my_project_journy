import Qmodule


def level():
    
    print("There are Four Levels To Play the Quiz!")
    print("1. Easy\n2. Medium\n3. Hard\n4. Logical")
    
    try:
        level_choice = int(input("Enter Your Level (1-4):\n"))
        
        if level_choice == 1:
            print("You Have Chosen Easy Level\n")
            print("You Will Get 1 Point For Each Correct Answer\n")
            print("You Will Get 0 Points For Each Wrong Answer\n")
            score=Qmodule.Easy()
            print("Your Total Score is:",score)
           
        
        elif level_choice == 2:
            print("You Have Chosen Medium Level\n")
            print("You Will Get 1 Points For Each Correct Answer\n")
            print("You Will Get 0 Points For Each Wrong Answer\n")
            score=Qmodule.Medium()
            print("Your Total Score is:",score)
        
        elif level_choice == 3:
            print("You Have Chosen Hard Level\n")
            print("You Will Get 1 Points For Each Correct Answer\n")
            print("You Will Get 0 Points For Each Wrong Answer\n")
            score=Qmodule.Hard()
            print("Your Total Score is:",score)
        
        elif level_choice == 4:
            print("You Have Chosen Logical Level\n")
            print("You Will Get 1 Points For Each Correct Answer\n")
            print("You Will Get 0 Points For Each Wrong Answer\n")
            score=Qmodule.Logical()
            print("Your Total Score is:",score)
        
        else:
            print("Wrong Option! Please choose a level between 1 and 4.")
            level()

    except ValueError:
        print("Invalid input! Please enter a number.")
        level()





# Main Quiz Code
start_quiz=1
while(start_quiz!=0):
    print("\t\t\tWelcome to the World of Quiz!\n")
    start_quiz= int(input("If you want to start the quiz, enter 1,else enter 0: "))

    if start_quiz == 1:
        print("")
        print("Quiz Started!\n")
        level()
    elif(start_quiz==0):
        print("thank you for watched my quiz")
        start_quiz=0
    else:
        print('re-renter the option:')
