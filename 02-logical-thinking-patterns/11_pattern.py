for i in range(1, 6):
    if i%2 == 1:
        for j in range(1, i+1):
            if j%2: # if it returns 1 or True
                print("1", end=" ")
            else: # else returns 0 or false
                print("0", end=" ")
    else:
        for j in range(1, i+1):
            if j%2:
                print("0", end=" ")
            else:
                print("1", end=" ")
    print("")

'''
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1
'''

# better solution avoiding the if-else

for i in range(1, 6):
    for j in range(1, i+1):
        # Calculate the value based on the sum of row and column indices
        print((i+j)%2, end=" ")
    print("")
