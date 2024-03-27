
#ROCK PAPER SCISSOR GAME
'''
Winning Rules as follows:

Rock vs paper-> paper wins

Rock vs scissor-> Rock wins

paper vs scissor-> scissor wins.
'''
import random 

print("Welcome to the game of ROCK-PAPER-SCISSORS!")

while True:
    
    print("Choose your mode:")
    print("(1) --> Single player")
    print("(2) --> Multiplayer")
    print("--------------------------------------------------")
    
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        
        print("Computer choose : Rock(1) / Paper(2) / Scissor(3) : ?")
        user = int(input("you choose : Rock(1) / Paper(2) / Scissor(3) : "))
        
        print("\n")
        
        n = random.randint(1,3)
        
        print("Computer: ",n)
        print("You: ",user)
        
        print("\n")
        
        if n == 1:
            
            if user == 1:
                print("DRAW")
                
            elif user == 2:
                print("You Win!")
                
            elif user == 3:
                print("Computer Wins!")
                
            else:
                print("Wrong Input!")
                
        elif n == 2:
            
            if user == 1:
                print("Computer Wins!")
                
            elif user == 2:
                print("DRAW")
                
            elif user == 3:
                print("You Win!")
                
            else:
                print("Wrong Input!")
                
        elif n == 3:
            
            if user == 1:
                print("You Win!")
                
            elif user == 2:
                print("Computer Wins!")
                
            elif user == 3:
                print("DRAW")
                
            else:
                print("Wrong Input!")
        
        else:
            print("Wrong Input!")
            
    elif choice == 2:
        
        P1 = int(input("Player 1 choose : Rock(1) / Paper(2) / Scissor(3) : "))
        P2 = int(input("Player 2 choose : Rock(1) / Paper(2) / Scissor(3) : "))
        
        print("\n")
        
        print("Player 1: ",P1)
        print("Player 2: ",P2)
        
        print("\n")
        
        if P1 == 1:
            
            if P2 == 1:
                print("DRAW")
                
            elif P2 == 2:
                print("Player 2 Wins!")
                
            elif P2 == 3:
                print("Player 1 Wins1")
                
            else:
                print("Wrong Input!")
                
        elif P1 == 2:
            
            if P2 == 1:
                print("Player 1 Wins!")
                
            elif P2 == 2:
                print("DRAW")
                
            elif P2 == 3:
                print("Player 2 Wins!")
                
            else:
                print("Wrong Input!")
                
        elif P1 == 3:
            
            if P2 == 1:
                print("Player 2 Wins!")
                
            elif P2 == 2:
                print("Player 1 Wins!")
                
            elif P2 == 3:
                print("DRAW")
                
            else:
                print("Wrong Input!")
        
        else:
            print("Wrong Input!")
            
    else:
        
        print("Incorrect choice! Try again")
        
    print("\n")        
    
    g = input('''Do You want to play again
        Press (y) for yes
        Press (n) for no\n''')    

    if g == "y":
        
        print ("Ok")
        
        print("\n")
        
        continue
    
    elif g == "n":
        
        print("Thank you for playing")
        
        print("\n")
        
        break
    
    else:
        
        print("Invalid choice! try again")
        
        print("\n")
    
    
