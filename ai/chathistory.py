def get_chat_history():
    with open('chat_history.txt', 'r') as file:
        return file.read()

def add_to_chat_history(prompt, response):
    with open('chat_history.txt', 'a') as file:
        file.write('\n\n User messages you: \n\n' + prompt + '\n\n Your response: \n\n' + response)