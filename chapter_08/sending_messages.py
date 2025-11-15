text_list = ['This is a song that doesnt end','I will be home later','see you at the crossroads','wyd','booo','brb',]

def show_text(text_list):
    print(f"below you will find the results for Show_text")
    for texts in text_list:        
        print(texts)

def send_messages(text_list):
    print(f"This is the result for send_messages")
    for texts in text_list:
        sent_messages = []
        sent_messages.append(texts)
    print(sent_messages)
    print(text_list)
    


show_text(text_list)
send_messages(text_list)
print(text_list)