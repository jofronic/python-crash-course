class Restaurant:
    """This class has resturant name and cuisine type"""
    def __init__(self, r_name, c_type, flavors):
        self.restaurant_name = r_name
        self.cusine_type = c_type
        self.flavors = flavors

        
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}")
        print(f"We serve {self.cusine_type} Mon through Friday")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")



class IceCreamStand(Restaurant):

    def __init__(self, r_name, c_type, flavors):
        super().__init__(r_name, c_type, flavors)
        """This method sets the contstuctors that can be used throughout this class."""
    
    def  display_icecream(self):
        """This method only displays. Methods that display shouldnt change the values. If you want to change the values, create another method that does that. """    
        for flavor in self.flavors: 
           
            print(f"I hope you enjoy your {flavor.title()} ice cream")


myicecream = IceCreamStand('Carvel', 'Ice Cream', ['chocalate', 'vanilla'])
myicecream.describe_restaurant()
myicecream.display_icecream()
