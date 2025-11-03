people = {
    
            'person_01' : {

            'First Name': 'Cecil',
             'Last Name': 'Oye', 
             'Age':'39',
             'City':'NJ'
             },

             'person_02' : {
            
            'First Name': 'Johan',
             'Last Name': 'Oye', 
             'Age':'39',
             'City':'NJ'
             
             },
            
            'person_03' : {
            
            'First Name': 'Michael',
             'Last Name': 'Oye', 
             'Age':'39',
             'City':'NJ'
             
             }
}

for peoples, info in people.items():
    print(
        f"{peoples.title()} account information. \nTheir first name is {info['First Name']}, "
        f"last name is: {info['Last Name']}, their age is: {info['Age']}"
        f"and they live in {info['Age']}"                                                                                                                                
    )
