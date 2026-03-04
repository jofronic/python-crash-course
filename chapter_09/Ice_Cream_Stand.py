class Restaurant:
    """This class has resturant name and cuisine type"""
    def __init__(self, r_name, c_type, icecreamflavors):
        self.restaurant_name = r_name
        self.cusine_type = c_type
        self.flavors = icecreamflavors

        
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}")
        print(f"We serve {self.cusine_type} Mon through Friday")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")



class IceCreamStand:
