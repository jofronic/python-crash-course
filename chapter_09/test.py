import time

class test:

    def check_battery(self):
        print(f"I am printing this for the human to see. A result of Full has been created by this function") # This shows up on screen
        for i in range(3):
            
            print(f"This script is loading for waiting {i+1}.")
            time.sleep(1)
        
        print(f"This script is complete. Thank you for waiting.")
        return "Full" # This goes back into the code logic

my_inst = test()
my_test = my_inst.check_battery()
my_test
print(my_test)

