# favorite_languages = {'jen': 'python', 'sarah':'c','edward':'rust','phil':'python',}
favorite_languages = {'jen': 'python',
                       'sarah':'c',
                       'edward':'rust',
                       'phil':'python',
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# language = favorite_languages['edward'].title()
# print(f"Edward favorite language is {language}.")

for key, value in favorite_languages.items():
    print(f"\nName:{key.title()}" )
    print(f"Language: {value.title()}")


