from left import Left
from right import Lock
import os
from time import sleep
class Pick(object):

    def __init__(self):
# This simply clears the terminal windows befor you start to play the game
        os.system('clear')
        
    def new(self):
# This is where you set your name. if nothing is entered it asks you to enter a name again
        self.names = raw_input("Welcom befor we get started what is your name?....")
        if len(self.names) == 0:
            print "Please pick a name for yourself."
            self.new()
        else:
# This passes the name you picked for yourself over to the next class in there other file
            self.left = Left(self.names)
            self.right = Lock(self.names)
            os.system('clear')
# I get my ascii art/text from http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
            print '''
      .o.       
     .888.      
    .8"888.     
   .8' `888.    
  .88ooo8888.   
 .8'     `888.  
o88o     o8888o 
                                                
  .oooooo.          .o.       ooo        ooooo oooooooooooo 
 d8P'  `Y8b        .888.      `88.       .888' `888'     `8 
888               .8"888.      888b     d'888   888         
888              .8' `888.     8 Y88. .P  888   888oooo8    
888     ooooo   .88ooo8888.    8  `888'   888   888    "    
`88.    .88'   .8'     `888.   8    Y     888   888       o 
 `Y8bood8P'   o88o     o8888o o8o        o888o o888ooooood8 
                                                                                                                        
  .oooooo.   oooooooooooo 
 d8P'  `Y8b  `888'     `8 
888      888  888         
888      888  888oooo8    
888      888  888    "    
`88b    d88'  888         
 `Y8bood8P'  o888o        
                                                                              
  .oooooo.   ooooo              .o.        .oooooo..o  .oooooo..o 
 d8P'  `Y8b  `888'             .888.      d8P'    `Y8 d8P'    `Y8 
888           888             .8"888.     Y88bo.      Y88bo.      
888           888            .8' `888.     `"Y8888o.   `"Y8888o.  
888           888           .88ooo8888.        `"Y88b      `"Y88b 
`88b    ooo   888       o  .8'     `888.  oo     .d8P oo     .d8P 
 `Y8bood8P'  o888ooooood8 o88o     o8888o 8""88888P'  8""88888P'    
 '''
 # This simply asks where you want to go. left and right are done in separate txt files
        sleep(0.5)
        print "\033[34m%r\033[0m You begin your game standing in a hall way" % self.names
        sleep(0.5)
        print "There are two doors waiting to be walked through"
        sleep(0.5)
        self.choose = raw_input("Please pick one 'left' or 'right'> ")
        if self.choose == "right":
            print "%r" % self.names
            self.right.guess()
        elif self.choose == "left":
            return self.left.start()
        else:
            print "Please pick one."
            sleep(0.5)
            self.new()
            
start = Pick()
start.new()
