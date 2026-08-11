from pathlib import Path

response = ''
content = input("What is your name? Press q to stop program\n")
while content != 'q':    
    response += content+"\n"
    content = input("What is your name? Press q to stop program\n")

path = Path('Guest_book.txt')
path.write_text(response)

read_new = path.read_text() 

for line in read_new.splitlines():

    print(line)
