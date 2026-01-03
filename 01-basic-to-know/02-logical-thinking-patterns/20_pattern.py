star, space = 1, 8
for _ in range(5):
    print("*"*star + (" "*space if space > 0 else "") + "*"*star)
    star += 1
    space -= 2
space, star = 2, 4
for _ in range(4):
    print("*"*star + (" "*space if space > 0 else "") + "*"*star)
    star -= 1
    space += 2

'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''