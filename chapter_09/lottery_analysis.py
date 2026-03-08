from random import choice
from lottery import lotto as l

class mylott: 
    def __init__(self):
        self.my_ticket = [2, 3, 'A', 'C']
        self.lottey_machine = l()


    def draw_tickets(self):
        
        draw = self.lottey_machine.random_selection()

        return draw
            

    def compare_tickets(self):
        attempts = 0
        draw = self.draw_tickets()
        while draw != self.my_ticket:
            draw = self.draw_tickets()
            attempts += 1
        return attempts

    def show_results(self):

       return f"My lottery number is {self.my_ticket}. It took {self.compare_tickets()} attempts to win the lotto!"       
      

test1 = mylott()
print(test1.show_results())