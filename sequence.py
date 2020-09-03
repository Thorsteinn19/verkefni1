    #Write in how long the sequence should be
    #Given the first 3 numbers of the sequence 1,2,3 calculate the next
    #value by taking the sum of the three prior numbers in the sequence
    #Repete until you get the desired length of the sequence
n = int(input("Enter the length of the sequence: ")) # Do not change this line
count_int = 4
first_int=1
second_int=2
third_int=3
if n >= 1:
    print(first_int)
if n >= 2:
    print(second_int)
if n >=3:
    print(third_int)
while count_int<=n:
    next_num_int=first_int+second_int+third_int
    print(next_num_int)
    first_int=second_int
    second_int=third_int
    third_int=next_num_int
    count_int += 1
