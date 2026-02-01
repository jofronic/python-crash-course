class Restaurant:
    """This class has resturant name and cuisine type"""
    def __init__(self, restaurant_name, cuisine_type):
        self.r_name = restaurant_name
        self.c_type = cuisine_type
        self.number_served = 0
        
        
    def describe_restaurant(self):
        print(f"Welcome to {self.r_name.title()}")
        print(f"We serve {self.c_type.title()} Mon through Friday")

      

    def open_restaurant(self):
        print(f"{self.r_name} is open!")
    
    def set_number_served(self, served):

        if served > 0:
           self.number_served = served         
        
    
    def increment_number(self, new_servedTotal):
        if new_servedTotal > 0:
            self.number_served = self.number_served + new_servedTotal

    def read_newnumber(self):
        print(f"{self.number_served}")
        print(f"{self.number_served}")
        
           
    

restaurant = Restaurant('mcdonalds', 'burgers')
restaurant.describe_restaurant()
restaurant.set_number_served(14)
restaurant.increment_number(10)
restaurant.read_newnumber()
