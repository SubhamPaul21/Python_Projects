# Implementation of classic arcade game Pong

import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [1,1]
paddle1_pos = PAD_HEIGHT / 2
paddle1_vel = 0
paddle2_pos = PAD_HEIGHT / 2
paddle2_vel = 0
score1 = 0
score2 = 0
LEFT = True
RIGHT = False

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel# these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == RIGHT:
        ball_vel = [random.randrange(1, 5),- random.randrange(1, 5)]
    elif direction == LEFT:
        ball_vel = [- random.randrange(2, 5),- random.randrange(2, 5)]
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2# these are ints
    
    spawn_ball(LEFT)
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")# mid-line
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White") #left_gutter
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White") #right_gutter
       
    # update ball
    ball_pos[0] += 1 * ball_vel[0] 
    ball_pos[1] +=  1 * ball_vel[1]
    if ball_pos[0] <= HALF_PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] < paddle1_pos+40 and ball_pos[1] > paddle1_pos - 40:
            ball_vel[0] = 1.5*ball_vel[0] # Increases velocity of ball
            ball_vel[1] = 1.5*ball_vel[1] 
            ball_vel[0] = - ball_vel[0]
        else:
            spawn_ball(RIGHT)
            score2 +=1
    
    elif ball_pos[0] >= (WIDTH-HALF_PAD_WIDTH) - BALL_RADIUS:
        if ball_pos[1] < paddle2_pos+40 and ball_pos[1] > paddle2_pos-40:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] = 1.1*ball_vel[0]
            ball_vel[1] = 1.1*ball_vel[1]
        else:
            spawn_ball(LEFT)
            score1 +=1
    
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2, 'White','Red')
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    if paddle1_pos >= HEIGHT-40: 
        paddle1_pos = HEIGHT-40
    elif paddle1_pos <= 40:
        paddle1_pos = 40
    if paddle2_pos >= HEIGHT-40: 
        paddle2_pos = HEIGHT-40
    elif paddle2_pos <= 40:
        paddle2_pos = 40
    
    # draw paddles
    canvas.draw_line((0, paddle1_pos - 40), (0, paddle1_pos + 40), 16, "White")
    canvas.draw_line((WIDTH, paddle2_pos - 40), (WIDTH, paddle2_pos + 40), 16, "White")
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH/4, 60], 50, "Green")
    canvas.draw_text(str(score2), [WIDTH/1.4, 60], 50, "Green")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 5
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -5
    
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 5
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = -5
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game, 100)
frame.add_label(" ")
frame.add_label(" ")
frame.add_label("W / S to move left paddle", 200)
frame.add_label('Up / Down to move right paddle', 300)


# start frame
new_game()
frame.start()
