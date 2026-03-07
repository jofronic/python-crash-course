from random import choice
from lottery import random_selection as R, show_selection as S

class mylott: 
    def __init__(self):
        my_ticket = [2, 3, 'A', 'C']

    def drawing(self):

        self.draw = choice((R.random_selection()))
        return self.draw