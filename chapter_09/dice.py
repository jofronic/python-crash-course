from random import randint

class DiceRoll():
    def __init__(self):
        # self.roll_function = randint
        self.rolls = []
        

    def roll_dice(self, roll_start, roll_stop): 
        self.rolls = []
        for i in range(10):
            
            random = randint(roll_start, roll_stop)
            self.rolls.append(random)  
        
    
    def show_dice(self):
       for i in self.rolls: 
        print(f"{i}")


class Die():
   def __init__(self, sides= 6):
    #   self.roll_die()
      self.sides = sides
      # roll_die attribute
   
   def roll_die(self):
    
    print(randint(1, self.sides))





ceelo = Die()
for i in range(10):
    ceelo.roll_die()
