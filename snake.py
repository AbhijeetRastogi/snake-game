import curses
from random  import randint 

curses.initscr()
curses.noecho()
curses.curs_set(0)
boardX = 70
boardY = 30
win = curses.newwin(boardY, boardX, 0, 0)# y,x
win.keypad(1)
win.border(0)
win.nodelay(1)

snake = [(3,10),(3,9),(3,8)]
food = (10,20)

ESC = 27
score = 0
key = curses.KEY_RIGHT

while key != ESC:
    win.addstr(0,2," Score = "+ str(score)+" ")
    win.timeout(100)#100ms
    
    prev_key = key
    event = win.getch()
    
    key = event if event !=1 else prev_key

    if key not in [curses.KEY_LEFT,curses.KEY_UP,curses.KEY_DOWN,curses.KEY_RIGHT,ESC]:
        key = prev_key
    
    win.addch(food[0],food[1],"0")

    #calculate next coordinates
    y = snake[0][0]
    x = snake[0][1]

    if key == curses.KEY_DOWN:
        y +=1
    if key == curses.KEY_UP:
        y -=1
    if key == curses.KEY_LEFT:
        x -=1
    if key == curses.KEY_RIGHT:
        x +=1
    snake.insert(0,(y,x))

    #check border
    y = snake[0][0]
    x = snake[0][1]
    
    if x==boardX:break
    if y==boardY:break
    if x==0     :break
    if y==0     :break
    
    #check sakebite
    if snake[0] in snake[1]:
        break

    # if food is eatten
    if snake[0] == food:
        score+=1
        food = ()
        while food == ():
            food = (randint(1,boardX), randint(1,boardY))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], "O")
    else:
        #moveing the snake 
        last = snake.pop()
        win.addch(last[0],last[1]," ")

    for c in snake:
        win.addch(c[0],c[1],"*")

score = 0
curses.endwin()
print(f"Score = {score}")












'''
import time

stdcr = curses.initscr()

curses.noecho()
curses.cbreak()
stdcr.keypad(True)

stdcr.addstr(5, 5, "hello")
stdcr.refresh()
time.sleep(3)

curses.echo()
curses.nocbreak()
stdscr.keypad(False)

curses.endwin()

'''

