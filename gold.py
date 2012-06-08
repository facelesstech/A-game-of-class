import random
import os
from time import sleep
class Gold(object):

    def __init__(self, more):
# Carrys the name from the last class and sets the chest amounts with these random numbers
        self.names = more
        self.rusty = random.randint(500, 1000)
        self.shiny = random.randint(1, 100)
        
    def gold(self):
        os.system('clear')
        sleep(0.5)
        print'''\033[1;33m
  .oooooo.      .oooooo.   ooooo        oooooooooo.   
 d8P'  `Y8b    d8P'  `Y8b  `888'        `888'   `Y8b  
888           888      888  888          888      888 
888           888      888  888          888      888 
888     ooooo 888      888  888          888      888 
`88.    .88'  `88b    d88'  888       o  888     d88' 
 `Y8bood8P'    `Y8bood8P'  o888ooooood8 o888bood8P'   
                                            
ooooooooo.     .oooooo.     .oooooo.   ooo        ooooo 
`888   `Y88.  d8P'  `Y8b   d8P'  `Y8b  `88.       .888' 
 888   .d88' 888      888 888      888  888b     d'888  
 888ooo88P'  888      888 888      888  8 Y88. .P  888  
 888`88b.    888      888 888      888  8  `888'   888  
 888  `88b.  `88b    d88' `88b    d88'  8    Y     888  
o888o  o888o  `Y8bood8P'   `Y8bood8P'  o8o        o888o 
\033[0m'''
        sleep(0.5)
        print "Congratulations \033[34m%r\033[0m you made it to the Treasure room" % self.names
        sleep(0.5)
        print "You have to chooses from two chests in front of you"
        sleep(0.5)
        print "There is a really \033[33m'rusty'\033[0m looking one and a \033[37m'shiny'\033[0m new looking one"
        sleep(0.5)
        pick = raw_input(" Which one will it be? ")
        os.system('clear')
        if pick == "rusty":            
            sleep(0.5)
# Thought i would mix it up by putting the rusty one with the most and the shiny one with the least
            print "Looks like you weren't gready and don't jugde a book by it's cover"
            sleep(0.5)
            print "You found \033[1;33m%r gold\033[0m pieces in the chest." % self.rusty
            exit()
        elif pick == "shiny":            
            sleep(0.5)
            print "It looks like you are a shallow person"
            sleep(0.5)
            print "You find \033[1;30m%r silver\033[0m pieces in the chest." % self.shiny
            exit()
        else:
            print "\033[1;31mYou need to pick one of the chests\033[0m"
            self.gold()      
