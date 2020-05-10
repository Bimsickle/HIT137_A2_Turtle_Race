# HIT137 Assigment 2: Question 1
# Angie Hollingworth

# This program is a random generate race of two python TURTLES
# Colours, speed and moves are all random so you do not know who will win

import turtle
from turtle import Turtle
import random
turtle.Screen().title("A TURTLE RACE, by A. Hollingworth")# window title
turtle.bgcolor("forestgreen") # Set background to a grass colour

t = Turtle() #Create set up turtle
t.speed(0) # Instant drawing with turtle
start = (-400,-150) #Set starting position

# **FUNCTIONS FOR REPEATED MOVES WITHIN FUNCTIONS **
def fdRight(forwd,rAngle): #Forward and right
    t.fd(forwd)
    t.rt(rAngle)

def fdCircle(distance,radi): #distance of forward move, radious of circle
    t.fd(distance) # move forward
    t.circle(radi,180) # move around a half circle of 'radi" size'

def pupgo(x,y): #pen up, goto, pen down
    t.penup()
    t.goto(x,y) #go to x & y coordinates
    t.pendown()

def writeText(x,y,text,col): #Write text on the screen
    t.penup()
    t.goto(x,y)
    t.color(col)
    t.write(text, move=False, align="center", font=("Arial", 8, "bold"))


# **FUNCTIONS FOR SETTING UP RACE TRACK **
def raceTrack(col,x,y): #Draw a race track
    t.color(col) #colour of track
    pupgo(x,y)
    t.begin_fill()
    t.setheading(0)
    for i in range(4): #draw square starting block
        t.fd(50)
        t.lt(90)
    t.end_fill()
    t.goto(x+50,y+25) #move next to start block
    t.pensize(50) #set turtle pen to size of track
    fdCircle(550,125) #draw first side of oval track
    fdCircle(400,125) #draw other side of oval track

def outLine(x,y,col,dist,circ): #Draw outline around track
    pupgo(x,y) # pen up, go to, pen down
    t.color(col)
    t.speed(0)
    t.pensize(2)
    for i in range(2): #Draw curved end of track
        fdCircle(dist*2,circ)
    t.fd(200)
    t.lt(180)
    fdRight(400,90)
    fdRight(50,90)
    fdCircle(600,100) #Includes starting line in length of track
    fdCircle(400,100)
    t.ht() # hide the turtle

def startsquare(num): #Draw checkerboard line for start line
    t.pensize(5)
    t.color("black")
    for i in range(num):# draw a square for "num" amount of times
        t.pendown()
        t.begin_fill()
        for i in range(4):#draw the square
            t.fd(5)
            t.lt(90)
        t.end_fill()
        t.penup()
        t.fd(15) #move to next square position

def checkline(x,y): # Create full starting line (3x rows of startsquare)
    pupgo(x,y) #pen up, go to coordinates, pen down
    t.setheading(90)
    startsquare(4) #draw starting line 4x squares
    pupgo(x+9,y+9) # move to next row
    startsquare(3) #draw starting line 3x squares
    pupgo(x+18,y) # move to next row
    startsquare(4) #draw starting line 4x squares

# **DRAW THE RACETRACK**
raceTrack("#CF6B31",-400,-150) #Create the race track
outLine(-200,-150,"white",200,150) # draw the track lines
checkline(-400,-150) #create Starting Line
writeText(-390,-170,"START","white")
checkline(100,-150) #create Finish Line
writeText(110,-170,"FINISH","white")


# **SET UP THE TURTLES**
def racerTurtle(racer):# set up turtle basics
    racer.shape("turtle") #shape
    R = random.random()
    B = random.random()
    G = random.random()
    racer.color(R, G, B) # set random turtle colour

# TURTLE RACER A
racerA = Turtle() # create turtle
racerTurtle(racerA) # give turtle racerTurtle values
racerA.penup() #racing turtle does not draw
racerA.goto(-425,-115) # go to starting line
writeText(-440,-120,"A",racerA.pencolor()) # write turtle name, in turtle colour
# TURTLE RACER B
racerB = Turtle() # create turtle
racerTurtle(racerB) # give turtle racerTurtle values
racerB.penup() #racing turtle does not draw
racerB.shape("turtle")
racerB.goto(-425,-135) # go to starting line
writeText(-440,-145,"B",racerB.pencolor()) # write turtle name, in turtle colour

# SET UP MOVING RULES
# Race around a turn
def turnRacer(racer,sectionTotal,move,pos):
    if sectionTotal+move>=distances[pos]: #check if this move will complete the turn
        next = (sectionTotal+move)-distances[pos] #set the next move after the turn
        racer.circle(125,distances[pos]-sectionTotal) #finish the turn
        if pos == "firstTurn": #completed first turn, now at top
            racer.setheading(180)
            return straightRacer(racer,0,next,"secondStretch")# race the straight
        else: #completed second turn, now on home stretch
            racer.setheading(0)
            return straightRacer(racer,0,next,"homeStretch")# race the straight
    else: #Racer still going around the turn
        racer.circle(125,move) #Dstance to move around the turn
        return [pos,sectionTotal+move] #Return new position & distance of section

# Race on an straight
def straightRacer(racer,sectionTotal,move,pos):
    maxsection = distances[pos] #get length of straight section from list
    if sectionTotal+move>=maxsection: #check if total move is greater than section
        next = (sectionTotal+move)-maxsection #set next distance after completing straight
        racer.fd(maxsection-sectionTotal) #move turtle
        if pos == "firstStretch": # Begin first turn with remainder of move (next)
            return turnRacer(racer,0,next,"firstTurn") #Return new position & distance of section
        elif pos == "secondStretch": # begin second turn with remainder of move (next)
            return turnRacer(racer,0,next,"secondTurn") #Return new position & distance of section
        else: # winner!!
            return ["winner",1] #First to cross the line
    else: #Racer still going along the straight
         racer.fd(move)
         return [pos,sectionTotal+move]

# Auto selector to run straight or turn move
def moveSelecter(racer,sectionTotal,move,pos): #AUTO MOVE SELECTOR
    if pos == "firstTurn" or pos == "secondTurn": #on a turn
        return turnRacer(racer,sectionTotal,move,pos) #Return new position & distance of section
    else: #on the straight
        return straightRacer(racer,sectionTotal,move,pos)#return update values for racer

# SET UP THE RACE
# Length of each track section
distances ={"firstStretch":600,"firstTurn":180,"secondStretch":400,"secondTurn":180,"homeStretch":310}

winner = "none" # default winner

# SET UP TURTLE DEFAULTS FOR STARTING THE RACE
posA = "firstStretch" #Set section of track to the start
posB = "firstStretch"
sectionTotalA = 0 # set total distance for stretch to 0
sectionTotalB = 0

# ** TURTLE RACE!!! **
while winner =="none": # loop while there is no winner
    # racer A moves first
    racerA.speed(random.randint(1,5)) # set random speed for move
    moveA = random.randint(1,50) #set random distance for move
    a = moveSelecter(racerA,sectionTotalA,moveA,posA) # run move function
    if a[0]=="winner": # set winner if return statement is "winner"
        winner="Turtle A is the winner!"
        break #exit loop with a winner
    else: # not a winner, continue through loop
        posA = (a[0]) # set new position on section
        sectionTotalA = a[1] #set section name
    # racer B moves second
    racerB.speed(random.randint(1,5))# set random speed for move
    moveB = random.randint(1,50) #set random distance for move
    b  = moveSelecter(racerB,sectionTotalB,moveB,posB) # run move function
    if b[0]=="winner": # set winner if return statement is "winner"
        if winner =="none": # check that turtle A didn't cross first
            winner="Turtle B is the winner!" #declare turtle B the winner
            break #exit loop with a winner
    else: # not a winner, continue through loop
        posB= str(b[0]) # set new position on section
        sectionTotalB = b[1] #set section name

# WRITE WINNING STATEMENT
t.penup()
t.goto(0,0)
t.color("white")
t.write(winner, move=False, align="center", font=("Arial", 20, "bold"))

delay = input("Press enter to finish.") #Delay closing of race
