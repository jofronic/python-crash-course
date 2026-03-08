from random import choice
from lottery import lotto as l

class mylott: 
    def __init__(self):
        self.my_ticket = [2, 3, 'A', 'C']
        self.lottey_machine = l()
        self.attempt_results = None


    def draw_tickets(self):
        
        draw = self.lottey_machine.random_selection()

        return draw
            

    def lotto_sim(self):
        attempts = 1
        draw = self.draw_tickets()
        while draw != self.my_ticket:
            draw = self.draw_tickets()
            attempts += 1
        self.attempt_results = attempts
        return self.attempt_results

    def show_results(self): 

        if self.attempt_results is None:
           print(f"Sim has not run yet. Run Lotto_sim first.")
        else:    
            print(f"My lottery number is {self.my_ticket}. It took {self.attempt_results} attempts to win the lotto!")
   
      

test1 = mylott()
test1.show_results()
test1.lotto_sim()
test1.show_results()