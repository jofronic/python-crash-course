from pathlib import Path



def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry, the file {path} can not be found!")
        pass
    else:
        #Count the number of words in a file
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words. ")
        

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)