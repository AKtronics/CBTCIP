# MASTERMIND GAME
'''
Two players play the game against each other; let’s assume Player 1 and Player 2.
Player 1 plays first by setting a multi-digit number.
Player 2 now tries his first attempt at guessing the number.
If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
The game continues till Player 2 eventually is able to guess the number entirely.
Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
If not, then Player 2 wins the game.
'''

key = int(input("Player 1, set the number: "))
guess = int(input("Player 2, guess the number: "))

if len(str(guess)) != 4:
    print("incorrect input, please try again.")
    
if (guess == key):
	print("Great! You guessed the number in just 1 try! You're a Mastermind! \n Player 2 is the Mastermind")

else:
    countA = 0
    
    while(guess != key):
        
        countA += 1
        
        cnt = 0
        
        K = str(key)
        
        G = str(guess)
        
        gap = ['X','X','X','X']
        
        for i in range(4):
            
            if K[i] == G[i]:
                
                cnt += 1
                
                gap[i] = G[i]
                
            else:
                continue
            
        if cnt < 4 and cnt != 0:
        
          print("Not the correct number, but you got ",cnt," digit(s) correct!")
        
          print(gap)
        
          print("--------------------------------------------------")
        
          guess = int(input("Enter your next choice of numbers: "))
    
        elif (cnt == 0):
        
          print("None of the numbers in your input match.")
        
          guess = int(input("Enter your next choice of numbers: "))
        
    if key == guess:
        
        countA += 1
        
        print("Congratulations you guessed the number!") 
        
        print(" It took you only ",countA," tries.")
        
#player 1's turn
        
    key = int(input("Player 2, set the number: "))
    
    guess = int(input("Player 1, guess the number: "))

    if len(str(guess)) != 4:
        print("incorrect input, please try again.")
    
    if (guess == key):
	    print("Great! You guessed the number in just 1 try! You're a Mastermind! \n Player 1 is the Mastermind")
    
            
    else:
        countB = 0
    
        while(guess != key):
            
            countB += 1
        
            cnt = 0
        
            K = str(key)
        
            G = str(guess)
        
            gap = ['X','X','X','X']
        
            for i in range(4):
                
                if K[i] == G[i]:
                    
                    cnt += 1
                
                    gap[i] = G[i]
                
                else:
                    continue
            
            if cnt < 4 and cnt != 0:
                print("Not the correct number, but you got ",cnt," digit(s) correct!")
        
                print(gap)
        
                print("--------------------------------------------------")
        
                guess = int(input("Enter your next choice of numbers: "))
    
            elif (cnt == 0):
        
                print("None of the numbers in your input match.")
        
                guess = int(input("Enter your next choice of numbers: "))
        
        if key == guess:
            countB += 1
            print("Congratulations you guessed the number!") 
            print(" It took you only ",countB," tries.")
        
        if countA == countB:
            print("DRAW")
        elif countA > countB:
            print("Player 1 wins the game!")
            print("Player 1 is the Mastermind")
        else:
            print("Player 2 wins the game!")
            print("Player 2 is the Mastermind")
            
