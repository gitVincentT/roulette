import random

'''
A roulette gives you the option of choosing something at random. 
Maybe you don't want to do something, and you want to choose the lesser of two or more options. 
Roulette is here for you to decide on what is the least worst or best option for you. 

1. Allows you to enter as many options (up to 6)
    -Input runs on a for loop x6 and then indicates that its at max options 
    -Stores input in a list 
2. Press enter twice or type 'begin' or 'b' to start the roll 
3. Roulette animation runs (that will be up to js animations to do the trick)
4. You end up with your decision. 
5. Offers to re-roll again (press enter)
'''


'''
while len(rlist) < max_length_list:
    item = input("Enter your item to the Roulette:3 ")
    rlist.append(item)
    print (rlist)
'''
def game():
    rlist = []
    max_length_list = 6 
    for _ in range (0,6):
        item = input("Enter up to 6 items to the Roulette:3 \n Type in 'done' to indicate you're done. ")
        if item == "done":
            break
        rlist.append(item)
        print (rlist)

    print ("These are your options: ") #I know that I can combine these two in one line 
    print (rlist)
    print('Begin roll now!\n You got... ')
    print (random.choice(rlist))
    c = input("Press enter to restart again or 'n' to quit")
    if c == 'n':
        print('Good games!')
    else:
        game()

game()
#Some line that sends it back to the top of the command line again (Try again? Y/N)
# Y for re-roll and N to break 