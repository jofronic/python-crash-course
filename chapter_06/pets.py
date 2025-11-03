person_reg = {

    'owner_profile_01' : {

        'first_name' : 'Jane',
        'last_name' : 'Smith',



    },
    'owner_profile_02' : {

        'first_name' : 'Sally',
        'last_name' : 'Mae',



    }

}
animal_reg = {

    'animal_profile_01' : {

        'name' : 'Jane',
        'pet_type' : 'doberman',


    },

    'animal_profile_02' : {

        'name' : 'Jane',
        'pet_type' : 'doberman',


    },

}

pets = [person_reg, animal_reg]

for pet in pets:
    print(f"{pet}")