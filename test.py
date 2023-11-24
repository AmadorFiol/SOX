# Python code to demonstrate the Application of 
# randrange()

import random

sum = 0
sum1 = 0
count = 0
flag = 0

while(1):
	
	# generate random number at each turn 1-10
	r1 = random.randrange(1,2)
	r2 = random.randrange(1,2)
	
    
	# adding to account of players
	sum = sum + r1
	sum1 = sum1 + r2
	count = count+1
	
	print ("Total score of Player 1 after turn %d is : %d " % (count,sum))
	
	# break when player 1 reaches 100 
	if(sum>=100):
	flag=1
	break
	print ("Total score of Player 2 after turn %d is : %d" % (count,sum1))
	
	# break when player 2 reaches 100 
	if(sum1>=100):
	flag=2
	break

if(flag==1):
print("\nPlayer 1 wins the game")
else :
print("\nPlayer 2 wins the game") 
