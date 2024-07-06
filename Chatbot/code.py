def chatbot():
    print("Hello! I am a chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").lower()
        
        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I assist you?")
        elif user_input in ["how are you?", "how are you doing?"]:
            print("Chatbot: I'm just a program, but I'm here to help you!")
        elif user_input in ["are you human?"]:
            print("Chatbot:No,I am just a program")
        elif user_input in ["how much do you sleep?"]:
            print("Chatbot:Well, I never sleep and do not have baggy eyes")
        elif user_input in ["what is your name?", "who are you?"]:
            print("Chatbot: I am a simple chatbot created by Sahil.")
        elif user_input in ["bye", "goodbye", "exit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
