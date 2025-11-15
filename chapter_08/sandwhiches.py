def lunch(name, *sandwhich):
    print(f"{name.title()} has odered some sanwhiches here they are: ")
    for sand in sandwhich:
        print(sand)


lunch('johan', 'cheese')
    
lunch ('onyi', 'cheese', 'ham', 'turkey')
lunch('Sharma','Turkey', 'chicken')