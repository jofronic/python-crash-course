favorite_numbers = {'james': {0,12},
                    'marshall': {34,56},
                    'sanjeef' : {45},
                    'michalangelo' : {39,35,258,1684,564,658}, 
                    'raphael' : {63},


                    }

for name, numbers in favorite_numbers.items():
    print(f"\nName: {name.title()}")
    print(f"Favorite number: {numbers}")
