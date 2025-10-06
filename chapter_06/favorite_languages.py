# favorite_languages = {'jen': 'python', 'sarah':'c','edward':'rust','phil':'python',}
favorite_languages = {'jen': 'python',
                       'sarah':'c',
                       'edward':'rust',
                       'phil':'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

language = favorite_languages['edward'].title()
print(f"Edward favorite language is {language}.")

for key, value in favorite_languages.items():
    print(f"\nName:{key.title()}" )
    print(f"Language: {value.title()}")

for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"\nHi{name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

favorite_languages_01 = {'jen': ['python', 'c'],
                       'sarah':['java', 'python'],
                       'edward':['json','ruby'],
                       'phil':'python',
}

for names in favorite_languages_01.items(): 
    print(names)

