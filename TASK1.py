# TASK-1 CHATBOT WITH RULE-BASED RESPONSES

def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. How can I assist you today?")
    print("Type 'exit' to end the conversation.")
    
    while True:
        
        user_input = input("You: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning as expected! How about you?")
        
        elif "what is your name" in user_input:
            print("Chatbot: I am a chatbot created to assist you with predefined queries.")
        
        elif "who created you" in user_input:
            print("Chatbot: Piyush Khachane created me") 
        
        elif "why are you created" in user_input:
            print("Chatbot: I am created for CODSOFT INTERNSHIP and to assist you with some predefined queries.")
        
        elif "where are you from" in user_input:
            print("Chatbot: I’m from the digital world, always ready to chat!")    
        
        elif "do you have any hobbies or interests?" in user_input:
            print("Chatbot: I’m always busy helping users, so my hobby is chatting with people like you!")             
        
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
        
            break
        
        elif "help" in user_input:
            print("Chatbot: I can respond to basic queries like greetings, time, or general questions. Try asking me something!")
        
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")


chatbot()
