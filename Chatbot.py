import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright, no problem.",]
    ],
    [
        r"(.*) (good|great|fine)",
        ["Nice to hear that.",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have an age.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual chatbot, I exist in the digital world.",]
    ],
    [
        r"exit",
        ["Bye! Take care.", "Goodbye, have a nice day!"]
    ],
]

# Create a chatbot with pairs and reflections
def chatbot():
    print("Hi, I'm ChatBot! How can I assist you today? (type 'exit' to leave)")

    # Create Chat instance
    chat = Chat(pairs, reflections)

    # Start conversation loop
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print("ChatBot:", response)
        
        # Exit loop if user types 'exit'
        if user_input.lower() == 'exit':
            break

if __name__ == "__main__":
    # your code here
    chatbot()