favorite_languages = {'jen': 'python',
                       'sarah':'c',
                       'edward':'rust',
                       'phil':'python',}


people = ['jen', 'josh', 'phil', 'edward'] 


# for name in favorite_languages:
for name in people:
    if name in favorite_languages:
        print(f"{name.title()}, thank you for taking the poll")

    else:
        print(f"{name.title()} you need to take the poll")