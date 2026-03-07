from random import choice

class lotto:
    def __init__(self):
    
        self.pool_lotto = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 'A', 'B', 'C', 'D', 'E']

    def random_selection(self):
        self.results = []
        for i in range(4):
            choices = choice(self.pool_lotto)
            self.results.append(choices)
    
    def show_selection(self):
        
        print(f"{self.results}")

tik = lotto()
tik.random_selection()
tik.show_selection()
