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

dice = DiceRoll()
dice.roll_dice(1,6)
dice.show_dice()
dice.roll_dice(1,10)
dice.show_dice()
dice.roll_dice(1,20)
dice.show_dice()