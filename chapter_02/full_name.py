#code passing string value into variable 
first_name = "ada"
last_name =  "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

#Using f (foramt) passing string value. playing with upper and lowercase formating
print(f"Hello, {full_name.title()}!")
message = print(f"Hello, {full_name.title()}!")
print(message)

#playing with formatting
print(" python")
print("\tPython")
print("\n\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#removing space on left and right sides
favorite_language = 'python     '
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = '    python'
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)
favorite_language = '  python   '
print(favorite_language)
favorite_language = favorite_language.strip
print(favorite_language)
