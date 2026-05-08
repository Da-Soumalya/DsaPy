star, space = 5, 0
for _ in range(1, 6):
    print("*"*star + (" "*space if space > 0 else "") + "*"*star)
    star -= 1
    space += 2
star, space = 1, 8
for _ in range(1, 6):
    print("*"*star + (" "*space if space > 0 else "") + "*"*star)
    star += 1
    space -= 2

'''
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''