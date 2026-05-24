def get_chatbot_response(user_input):
    """
    This function takes the user's input, converts it to lowercase,
    and returns a predefined reply based on keywords.
    """
   
    user_input = user_input.lower().strip()

   
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
        
    elif "how are you" in user_input:
        return "I'm doing great, thank you for asking! How are you?"
        
    elif "your name" in user_input:
        return "I am AlphaBot, your friendly CodeAlpha assistant."
        
    elif "python" in user_input:
        return "Python is an amazing programming language! Are you working on a project?"

    elif "yes" in user_input:
        return "love to help you with your project!"
        
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a wonderful day!"
        
    else:
       
        return "I'm sorry, I don't quite understand that. Could you try saying something else?"


def start_chatbot():
    """
    The main function that runs the chatbot engine using a loop.
    """
    print("=========================================")
    print("       🤖 WELCOME TO ALPHABOT 🤖        ")
    print("=========================================")
    print("Type 'bye' or 'exit' at any time to quit.\n")

    while True:
        user_message = input("You: ")
        bot_response = get_chatbot_response(user_message)
        print(f"Bot: {bot_response}\n")
        
    
        if "bye" in user_message.lower() or "exit" in user_message.lower():
            break


if __name__ == "__main__":
    start_chatbot()
