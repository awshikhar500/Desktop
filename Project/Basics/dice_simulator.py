# wap to create a function that will
# generate random 3 dice numbers and if all 3 match, then 
# display 'you win' else display 'you lose / try again'

import random as rnd
def streak():
    dice = [1,2,3,4,5,6]
    x1 = rnd.choices(dice, k=3)
    if x1[0] == x1[1] == x1[2]:
        return x1,'you win'
    else:
        return x1,'you lose / try again'

ans,msg = streak()
print('rolling the dice...')
print(ans)
print(msg)

