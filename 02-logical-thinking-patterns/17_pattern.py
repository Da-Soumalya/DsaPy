random_string, space = "ABCD", 3
for i in range(4):
    print(" "*space, end="")

    temp_string = random_string[:i+1]
    print(temp_string, end="")
    print("".join(reversed(temp_string[:i])))

    #print(" "*space) # lesson learnt
    space -= 1

'''
   A
  ABA
 ABCBA
ABCDCBA
'''