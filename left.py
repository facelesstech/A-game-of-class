import random
import os
from time import sleep
from death import Death
from gold import Gold
class Left(object):
    
    def __init__(self, more):
# This sets the HP and attacks for you and who you are fighting in this class also takes the name from the start.py file and adds it in  here
        self.HP = 100
        self.names = more
        self.death = Death("So he kicked you're ass then.")
        self.pikachuhp = 20
        self.mewhp = 30
        self.mewtwohp = 40
        self.hitback = random.randint(5, 20)
        
    def start(self):    
        os.system('clear')
        sleep(0.5)
        print '''
  .oooooo.     .oooooo.   ooo        ooooo oooooooooo.        .o.       ooooooooooooo 
 d8P'  `Y8b   d8P'  `Y8b  `88.       .888' `888'   `Y8b      .888.      8'   888   `8 
888          888      888  888b     d'888   888     888     .8"888.          888      
888          888      888  8 Y88. .P  888   888oooo888'    .8' `888.         888      
888          888      888  8  `888'   888   888    `88b   .88ooo8888.        888      
`88b    ooo  `88b    d88'  8    Y     888   888    .88P  .8'     `888.       888      
 `Y8bood8P'   `Y8bood8P'  o8o        o888o o888bood8P'  o88o     o8888o     o888o     
                                                                                      
ooooooooo.     .oooooo.     .oooooo.   ooo        ooooo  .oooooo..o 
`888   `Y88.  d8P'  `Y8b   d8P'  `Y8b  `88.       .888' d8P'    `Y8 
 888   .d88' 888      888 888      888  888b     d'888  Y88bo.      
 888ooo88P'  888      888 888      888  8 Y88. .P  888   `"Y8888o.  
 888`88b.    888      888 888      888  8  `888'   888       `"Y88b 
 888  `88b.  `88b    d88' `88b    d88'  8    Y     888  oo     .d8P 
o888o  o888o  `Y8bood8P'   `Y8bood8P'  o8o        o888o 8""88888P'  
                                                                    
'''
# Simply askes you who to fight then sets there HP and yours
        sleep(0.5)
        print "\033[34m%r\033[0m You have reached the combat room" % self.names
        sleep(0.5)
        print "You have \033[34m%rHP\033[0m to start with" % self.HP
        sleep(0.5)
        print "and have the attack moves 'punch' and 'spinkick'"
        sleep(0.5)
        print "Who do you want to take on first? \033[1;33m'pikachu'\033[0m \033[1;37m'mewtwo'\033[0m or \033[1;37m'mew'\033[0m"
        sleep(0.5)
        self.pick = raw_input("You need to pick one > ")
        os.system('clear')
        if self.pick == "pikachu":
            print "You come up against \033[1;33mpikachu\033[0m he have %rHP" % self.pikachuhp
            self.punch(self.HP, self.pikachuhp, self.hitback, self.pick)
        elif self.pick == "mewtwo":
            print "You come up against \033[1;37mmewtwo\033[0m he have %rHP" % self.mewtwohp
            self.punch(self.HP, self.mewtwohp, self.hitback, self.pick)
        elif self.pick == "mew":
            print "You come up against \033[1;37mmew\033[0m he have %rHP" % self.mewhp
            self.punch(self.HP, self.mewhp, self.hitback, self.pick)
        else:
            print "You need to pick one"
            self.start()
        
    def punch(self, HP, therehp, hitback, pick):
        self.HP = HP
        self.therehp = therehp
        self.hitback = hitback
        self.pick = pick
        while True:
# You attack first i up the self.attacks in here so it will generate a differnet number every go
            self.attacks = {'punch':random.randint(5,15), 'spinkick':random.randint(10,20)}
            sleep(0.5)
            punch = raw_input("Pick a move to use. 'punch' 'spinkick' > ")
            os.system('clear')           
            self.therehp -= self.attacks[punch]
            print "You hit %r with a \033[34m%r\033[0m and do \033[34m%r\033[0m damage" % (self.pick, punch, self.attacks[punch])
            sleep(0.5)
# I added the if statment here so if i kill him he wont be able to inflict damage back befor moving on
            if self.therehp > 0:
                print "%r has \033[34m%r\033[0m health left" % (self.pick, self.therehp)
                sleep(0.5)
                self.HP -= self.hitback
                print "Enemy %r used kick and does \033[1;31m%r\033[0m damage" % (self.pick, self.hitback)
                sleep(0.5)
                print "You have \033[1;31m%r\033[0m health left" % self.HP
                sleep(0.5)
# If he defeats me i go to the death room within the death.py file
                if self.HP <= 0:
                    self.death()
# If i win i go on to the next class and take my name and HP with me to carry on the battle               
            else:
                print "You deliver the final brow and %r faints" % self.pick    
                print "You win with \033[34m%rHP\033[0m left" % self.HP
                sleep(1)
                self.attack = SecondAttack(self.HP, self.names)
                return self.attack.battle()

                
class SecondAttack(object):
# Here i load the name and HP from the last class
    def __init__(self, more, name):
        self.HP = more
        self.names = name        
        self.mario = 20
        self.luigi = 30
        self.wario = 40
        self.hitback = random.randint(5, 20)
# Here you are asked again who you want to battle        
    def battle(self):
        os.system('clear')
        sleep(0.5)
        print "%r You made it to the next room with \033[34m%rHP\033[0m" % (self.names, self.HP)
        sleep(0.5)
        print "You need to pick one last contender"
        sleep(0.5)
        print "You have learnt new moves 'chop' and 'thunder'"
        sleep(0.5)
        print "Who do you want to pick \033[1;31m'mario'\033[0m, \033[1;32m'luigi'\033[0m or \033[1;35m'wario'\033[0m."
        sleep(0.5)
        self.picker = raw_input("Pick one > ")
        os.system('clear')
        if self.picker == "mario":
            print "You come up against \033[1;31mmario\033[0m they have %rHP" % self.mario
            self.fight(self.HP, self.mario, self.hitback, self.picker)
        elif self.picker == "luigi":
            print "You come up against \033[1;32mluigi\033[0m they have %rHP" % self.luigi
            self.fight(self.HP, self.luigi, self.hitback, self.picker)
        elif self.picker == "wario":
            print "You come up against \033[1;35mwario\033[0m they have %rHP" % self.wario
            self.fight(self.HP, self.wario, self.hitback, self.picker)
        else:
            print "You need to pick one"
            self.battle()
# This is pritty much the same as the last class but also loads the gold room for if/when i win        
    def fight(self, HP, therehp, hitback, picker):
        self.gold = Gold(self.names)
        self.HP = HP
        self.therehp = therehp
        self.hitback = hitback
        self.picker = picker
        self.death = Death("You made it so far, but you died")
        while True:
            self.attacks = {'chop':random.randint(5, 10), 'thunder':random.randint(5, 15)}
            sleep(0.5)
            choose = raw_input("Pick a move 'chop' or 'thunder' > ")
            os.system('clear')
            self.therehp -= self.attacks[choose]
            print "You hit %r with \033[34m%r\033[0m and did \033[34m%r\033[0m damage" % (self.picker, choose, self.attacks[choose])
            sleep(0.5)
            if self.therehp > 0:
                print "%r has \033[34m%r\033[0m damage left" % (self.picker, self.therehp)
                sleep(0.5)
                self.HP -= self.hitback
                print "%r hits you back with a punch and does \033[1;31m%r\033[0m damage" % (self.picker, self.hitback)
                sleep(0.5)
                print "You have \033[1;31m%rHP\033[0m left" % self.HP
                sleep(0.5)
                if self.HP <= 0:
                    self.death()
                    break
            else:
                print "You deliver the final brow and %r faints" % self.picker
                print "You win with \033[34m%rHP\033[0m left" % self.HP
                sleep(1)
                self.gold.gold() 
             
