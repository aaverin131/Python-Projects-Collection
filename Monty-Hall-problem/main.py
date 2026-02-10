import random
import time

random.seed(time.time())

def get_average_winrate(count, switch = True, luckyListLen = 3):
    """Simulates the Monty Hall problem and returns the win rate.
    
    Args:
        count: Number of simulation cycles to run.
        switch: Whether to switch doors after one is revealed. Defaults to True.
        luckyListLen: Number of doors in the problem. Defaults to 3.
    
    Returns:
        Win rate as a decimal (0 to 1).
    """
    wins = 0
    for c in range(count): #do cycles of tests to make more accurate average

        randPrize = random.randint(1, luckyListLen)

        playerChoice = random.randint(1, luckyListLen)

        revealDoor = []
        doorNum = 1
        playerGuessedRight = randPrize == playerChoice
        for i in range(luckyListLen):
            revealDoor.append(doorNum)
            if doorNum == playerChoice or doorNum == randPrize:
                del revealDoor[-1]
            if (doorNum != playerChoice or doorNum != randPrize) and playerGuessedRight: #make sure Monty always leaves a door to switch
                del revealDoor[-1]
                playerGuessedRight = False

            doorNum += 1
        if switch == True:
            playerLastChoice = playerChoice
            playerChoice = 1
            
            while playerChoice == playerLastChoice or playerChoice in revealDoor:
                playerChoice += 1
        
        if playerChoice == randPrize:
            wins += 1

    
    winrate = wins / count
    
    
    return winrate

cycles = 1000000
print("-------------------------------\n3 Door setup:")
timeTaken = time.time()
print("Winrate when we switch: "+str(get_average_winrate(cycles)*100)+"%")
print("Winrate when we don't: "+str(get_average_winrate(cycles, switch=False)*100)+"%")
print(f"Time taken to calculate: {time.time()-timeTaken}s\n-------------------------------")

cycles = 100000
print("-------------------------------\n10 Door setup:")
timeTaken = time.time()
print("Winrate when we switch: "+str(get_average_winrate(cycles, luckyListLen=10)*100)+"%")
print("Winrate when we don't: "+str(get_average_winrate(cycles, switch=False, luckyListLen=10)*100)+"%")
print(f"Time taken to calculate: {time.time()-timeTaken}s\n-------------------------------")

cycles = 10000
print("-------------------------------\n100 Door setup:")
timeTaken = time.time()
print("Winrate when we switch: "+str(get_average_winrate(cycles, luckyListLen=100)*100)+"%")
print("Winrate when we don't: "+str(get_average_winrate(cycles, switch=False, luckyListLen=100)*100)+"%")
print(f"Time taken to calculate: {time.time()-timeTaken}s\n-------------------------------")

cycles = 100
print("-------------------------------\n10000 Door setup:")
timeTaken = time.time()
print("Winrate when we switch: "+str(get_average_winrate(cycles, luckyListLen=10000)*100)+"%")
print("Winrate when we don't: "+str(get_average_winrate(cycles, switch=False, luckyListLen=10000)*100)+"%")
print(f"Time taken to calculate: {time.time()-timeTaken}s\n-------------------------------")