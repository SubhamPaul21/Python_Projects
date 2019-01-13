# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# install simplegui on windows as follows first ---
 `pip install SimpleGUITk`


import simpleguitk as simplegui
import random
secret_number = 0
count = 1
max_chance = 0

# helper function to start and restart the game
def new_game(start_r,end_r,max_chanc):
    # initialize global variables used in your code here
    global count
    count = 0
    global secret_number 
    global max_chance
    max_chance = max_chanc
    secret_number = random.randrange(start_r,end_r)
    print ("Let the game begin.... Range is [",start_r,",",end_r,")")
    print ('You have',max_chance,' chances left') 

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global count
    count = 0
    new_game(0,100,7)
    #print('The range is [0,100), Enjoy the game...!')

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global count
    count = 0
    new_game(0,1000,10)
    #print('The range is [0,1000), Enjoy the game...!')



def input_guess(guess):
    # main game logic goes here	
    number = int(guess)
    print ('Guess was', number)
    global count 
    count += 1
    if count < max_chance:
        if number != secret_number:
            left = max_chance - count
            print (left,'chances left')
            if number > secret_number:
                print ('LOWER')
            elif number < secret_number:
                print ('HIGHER')
            
        else:
            print ('Correct')
            print('Hurray You guessed right and finished before chances end')
            if max_chance == 7:range100()
            else:range1000()
    else:
        print("You ran out of chances")
        print ('The correct number was',secret_number)
        if max_chance == 7:
            range100()
        else:
            range1000()
        
        
# create frame
frame = simplegui.create_frame('Guess The number',200,200)

# register event handlers for control elements and start frame
frame.add_button('Range is [0,100)',range100,200)
frame.add_button('Range is [0,1000)',range1000,200)
frame.add_input('Enter your guess',input_guess,100)

# call new_game 
new_game(0,100,7)
frame.start()


