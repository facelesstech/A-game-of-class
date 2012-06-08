import random
import os
from death import Death
from time import sleep
import time
from gold import Gold
class Lock(object):
# Setting your name, death and the first 2 numbers for the first puzzle    
    def __init__(self, more):
        self.names = more
        self.death = Death("Looks like the lock died, You curl up in a ball and await death.")
        self.first_two = "[%r:%r: ]" % (random.randint(1,10), random.randint(1,10))
        self.sums = Sums(self.names)
        
    def guess(self):
        os.system('clear')
        sleep(0.5)
        print'''
ooooo          .oooooo.     .oooooo.    ooooo   .oooooo.   
`888'         d8P'  `Y8b   d8P'  `Y8b   `888'  d8P'  `Y8b  
 888         888      888 888            888  888          
 888         888      888 888            888  888          
 888         888      888 888     ooooo  888  888          
 888       o `88b    d88' `88.    .88'   888  `88b    ooo  
o888ooooood8  `Y8bood8P'   `Y8bood8P'   o888o  `Y8bood8P'  
                                                           
ooooooooo.     .oooooo.     .oooooo.   ooo        ooooo  .oooooo..o 
`888   `Y88.  d8P'  `Y8b   d8P'  `Y8b  `88.       .888' d8P'    `Y8 
 888   .d88' 888      888 888      888  888b     d'888  Y88bo.      
 888ooo88P'  888      888 888      888  8 Y88. .P  888   `"Y8888o.  
 888`88b.    888      888 888      888  8  `888'   888       `"Y88b 
 888  `88b.  `88b    d88' `88b    d88'  8    Y     888  oo     .d8P 
o888o  o888o  `Y8bood8P'   `Y8bood8P'  o8o        o888o 8""88888P' 
'''
        sleep(0.5)
        print "\033[034m%r\033[0m You enter a room with nothing in it bar a locked door with a keypad" % self.names
        sleep(0.5)
        print "There are 3 numbers you must guess to progress"
        sleep(0.5)
        print "Wait a minuite there are two numbers already keyed in so you only need to guess the final number"
        sleep(0.5)
        print "Here are the first two numbers \033[1;31m%r\033[0m" % self.first_two
        sleep(0.5)
        print "You know need to guess the final number."
        sleep(0.5)
        print "remember it has to be between \033[1;31m0\033[0m and \033[1;31m9\033[0m."
        sleep(0.5)
        print "You only got 6 tryes."
        sleep(0.5)
        last_one = "%r" % random.randint(0,9)
        print last_one
        guesses = 0
        guess = raw_input("> ")
# Uses a if statment but then goes into a while statment so that the first guess is recorded but you can still get it right first go
        if guess != last_one:
            guesses += 1
            print"Guess again you have had %r guess" % guesses
            while guess != last_one and guesses < 6:
                guesses += 1
                guess = raw_input("> ")
                print "Guess again you have guessed %r times." % guesses
            if last_one == guess:
                print "You done it, quickly run on to the next room."
                return self.sums.second()
            else:
                return self.death.dead()
                exit()
        else:
            print "You done it."
            self.sums.second()
            
class Sums(object):
# This is just a simple maths question game nothing special        
    def __init__(self, more):
        self.death = Death("You can't do simple math???")
        self.names = more
        self.list = {'1':"15 + 10 * 6 = ", '2':"22 + 50 = "}
        self.timed = Timed(self.names)

                            
    def second(self):
        os.system('clear')
        sleep(0.5)
        print "\033[34m%r\033[0m So you got past that last door" % self.names
        sleep(0.5)
        print "This seams to be a math challange are you ready"
        sleep(0.5)
        print "there are two envelope in front of you numbered \033[1;31m'1'\033[0m and \033[1;31m'2'\033[0m"
        sleep(0.5)
        print "Pick one of these envelope."
        sleep(0.5)
        self.picker = raw_input("'1' or '2' ")
        print "%r" % self.list[self.picker]
        answer = raw_input("??? ")
# For some reason i can't get it to just acept the right answer, it will give a positive if i enter 150 or 72
        while answer != "150" and answer != "72":
            print "Try again"
            answer = raw_input("??? ")              
        if answer == "150":
            os.system('clear')
            print "right on, you run thought the open door to the next room."
            return self.timed.test1()
        elif answer == "72":
            os.system('clear')
            print "right on, you run thought the open door to the next room."
            return self.timed.test1()
        else:
            return self.death.dead()
            exit()
            
class Timed(object):
# This is a self timing game. It takes the start time and takes the end time from it    
    def __init__(self, more):
        self.names = more
        self.gold = Gold(self.names)
        self.death = Death("You forever burn in hell.")
        self.test1
                            
    def test1(self):
        sleep(0.5)
        print "\033[34m%r\033[0m You enter a room with a button on a pillar right in the middle of the room" % self.names
        sleep(0.5)
        print "There are a set of instructions. You will need to press the button"
        sleep(0.5)
        print "Then count in your head to ten then press the button again."
        self.begin = raw_input("Press enter ")
        self.start = time.time()
        enter = raw_input("Press enter again after 10 seconds ")
        self.finish = time.time()
        end = int(self.finish) - int(self.start)
        if end <= 9:
            print end
            return self.death.dead()
# This gives you a bit of wigal room so you can go over by a few seconds
        elif end >= 10 and end <= 12:
            sleep(0.5)
            print "Wow you done it. You can count lol."
            sleep(0.5)
            print "Here is your reward."
            sleep(1)
            return self.gold.gold()
        else:
            return self.death.dead()
