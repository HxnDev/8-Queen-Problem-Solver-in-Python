#!/usr/bin/env python
# coding: utf-8

# In[6]:


###########################################################################################################################
#               Hassan Shahzad
#               18i-0441
#               CS-D
#               FAST-NUCES ISB
#               chhxnshah@gmail.com
###########################################################################################################################



################################################## GLOBAL DECLARATIONS ####################################################
import numpy as np
import random
###########################################################################################################################


################################################# DEFINING THE BOARD ######################################################    

def makeBoard():                                            #Creating an 8x8 chess board
	arr=np.zeros((8,8))
	return arr

###########################################################################################################################


################################################ PRINTING THE BOARD #######################################################    

def printState(state):
	print(state)

###########################################################################################################################


################################### RANDOM GENERATION OF QUEENS IMPLEMENTATION ############################################    
    
def placeQueens(state, location):                           # This function will randomly place 8 queens in the maze 
	i=0
	location=[]
	while(i<=7):
		index_x=random.randint(0,7)
		index_y=random.randint(0,7)
		while(1):
			if state[index_x][index_y]!=1:                  # Checks if the queen is already placed in that location
				state[index_x][index_y]=1                   # The Queen is represented by "1"
				location.append(index_x)
				location.append(index_y)
				break
			else:
				index_x=random.randint(0,7)
				index_y=random.randint(0,7)
				random.seed(random.randint(0,10))

		random.seed(random.randint(0,10))
		i=i+1

	return location


###########################################################################################################################


####################################### OBJECTIVE FUNCTION IMPLEMENTATION #################################################

def objectiveFunction(state,location):                       # This function will calculate the number of attacking queens in each possibility
	attackingQueens=0
	
	q=0
	while(q<=7):
		y=location.pop()
		x=location.pop()
		index_x=x
		index_y=y
		
		i=0
		count=0
		while(i<=7):                                         # Checking all possible combinations
			if state[x][i]==1:
				count=count+1

			if count==2:
				attackingQueens=attackingQueens+1            # Incrementing by 1 upon attack of two queens
			i=i+1                                            # Will divide by 2 at the end

## We will keep on repeating these steps for each column and each row of that column		
		if count<2:
			count=0
			i=0
			while(i<=7):
				if state[i][y]==1:
					count=count+1

				if count==2:
					attackingQueens=attackingQueens+1
				i=i+1
		
		if count<2:
			count=0
			x=index_x
			y=index_y
			while(y>0 & x>0 & x<7 & y<7):
				if state[x][y]==1:
					count=count+1
					x=x+1
					y=y+1
				else:
					x=x+1
					y=y+1

			if count==2:
				attackingQueens=attackingQueens+1
				
		if count<2:
			count=0
			x=index_x
			y=index_y
			while(y>0 & x>0 & x<7 & y<7):
				if state[x][y]==1:
					count=count+1
					x=x-1
					y=y-1
	
				else:
					x=x-1
					y=y-1

			if count==2:
				attackingQueens=attackingQueens+1
			
	
		if count<2:
			count=0
			x=index_x
			y=index_y
			while(y>0 & x>0 & x<7 & y<7):
				if state[x][y]==1:
					count=count+1
					x=x-1
					y=y+1
				
				else:
					x=x-1
					y=y+1

			if count==2:
				attackingQueens=attackingQueens+1
		
		if count<2:
			count=0
			x=index_x
			y=index_y
			while(y>0 & x>0 & x<7 & y<7):
				if state[x][y]==1:
					count=count+1
					x=x+1
					y=y-1
				else:
					x=x+1
					y=y-1

			if count==2:
				attackingQueens=attackingQueens+1
	
			

		q=q+1
	print("Number of attacking queens = ")
	print(int(attackingQueens/2))


###########################################################################################################################

################################################ MAIN IMPLEMENTATION ######################################################


def main():

    board=makeBoard()
    lis=[]
    lis=placeQueens(board,lis)
    print()
    print("Board after placing queens = ")
    print()
    printState(board)
    print()
    print()
    print("Queens are randomly palced at following locations : ")
    print(lis)
    print()

    objectiveFunction(board,lis)

# Tell python to run main method
if __name__ == "__main__": main()

###########################################################################################################################


# In[ ]:





# In[ ]:




