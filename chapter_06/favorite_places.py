places = {
        'Johan' :{
            'favorite_01' :'haiti',
            'favorite_02' : 'DR',
            'favorite_03' : 'columbia'

        } , 
        'Onyi' : {
            
            'favorite_01' :'nigeria',
            'favorite_02' : 'DR',
            'favorite_03' : 'columbia'


        }, 
        'Sharma' : {

            'favorite_01' :'surnanme',
            'favorite_02' : 'DR',
            'favorite_03' : 'columbia'

        },
        'Cecilia' : {

            'favorite_01' :'lagos',
            'favorite_02' : 'DR',
            'favorite_03' : 'columbia'
        }

}

for name, place in places.items():
    print(f" This is {name} and their favorite place is {place['favorite_01'].title()}")