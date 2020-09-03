#Program takes in a value
#Check if the value is positive,
#if it is negative stop the check else While the number is positive,
#save the value as a variable
#Check if he new variable is larger than previous variable
#If the new variable is larger than the previous replace the
#old one with the new variable.
#Then ask for a new variable and repeat the algorithm from line 2

num_int = int(input("Input a number: "))
max_int = 0
while num_int>=0:
	if num_int>max_int:
		max_int=num_int
print("The maximum is", max_int)
