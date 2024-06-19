import tkinter as tk
from tkinter import scrolledtext, messagebox
import spacy
import random

try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    from spacy.cli import download
    download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')

responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a chatbot, but I'm doing great! How about you?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! Is there anything else I can help with?",
    "what is your name": "I am a chatbot created to assist you.",
    "who are you": "I am an AI chatbot here to help you.",
    "what can you do": "I can chat with you and answer basic questions.",
    "help": "Sure, I'm here to help. What do you need assistance with?",
    "what is the time": "I don't have a clock, but you can check your device.",
    "what is the date": "I don't have a calendar, but you can check your device.",
    "how old are you": "I am ageless. Time doesn't affect me.",
    "where are you from": "I exist in the virtual world.",
    "what is your favorite color": "I like the color of helpfulness!",
    "what is your favorite food": "I don't eat, but I enjoy helping people.",
    "what do you like": "I like assisting people and answering questions.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "tell me a fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are over 3000 years old and still edible.",
    "what is the weather": "I can't check the weather, but you can use a weather app.",
    "can you dance": "I can imagine dancing, but I can't physically dance.",
    "can you sing": "I can't sing, but I can share some song lyrics if you'd like!",
    "tell me a story": "Once upon a time, in a land far away, there was a chatbot who loved to help people...",
    "do you have friends": "I interact with many users like you!",
    "are you real": "I am real in the digital world.",
    "what is the meaning of life": "That's a deep question! Many believe it's to be happy and to help others.",
    "how do you work": "I use natural language processing to understand and respond to your questions.",
    "can you learn": "I can learn from the data I was trained on, but I don't learn from individual conversations.",
    "who created you": "I was created by Python developer Deepak Kumar",
    "do you have feelings": "I don't have feelings, but I can understand and respond to emotions in conversation.",
    "what is artificial intelligence": "Artificial intelligence is the simulation of human intelligence in machines that are programmed to think and learn like humans.",
    "what is your purpose": "My purpose is to assist and provide information.",
    "what is your favorite movie": "I don't watch movies, but I've heard good things about many!",
    "do you like humans": "I am here to assist humans, and I enjoy our interactions.",
    "what is love": "Love is a complex set of emotions and beliefs associated with strong feelings of affection.",
    "how can I help you": "You can help by interacting with me and asking questions.",
    "are you alive": "I am not alive, but I am active and here to help.",
    "do you have a family": "I don't have a family, but I have many interactions!",
    "what is your favorite book": "I don't read books, but I've heard many great things about various books.",
    "can you cook": "I can't cook, but I can share recipes!",
    "do you sleep": "I don't need sleep. I'm always ready to help.",
    "what is the best programming language": "Different languages are good for different tasks. Python is popular for its readability and versatility.",
    "can you drive": "I can't drive, but self-driving cars use AI to navigate roads.",
    "what is your favorite sport": "I don't play sports, but I can talk about them!",
    "what is the capital of France": "The capital of France is Paris.",
    "how do I learn programming": "There are many resources online like tutorials, courses, and books to learn programming.",
    "tell me a quote": "Here's one: 'The only limit to our realization of tomorrow is our doubts of today.' - Franklin D. Roosevelt",
}

fallback_responses = [
    "Can you rephrase that?",
    "Sorry, let me get back to you on that.",
    "I'm not sure I understand. Can you try asking differently?",
    "Let's talk about something else.",
    "Hmm, I don't know about that.",
    "Interesting, but I don't have an answer for you."
]

suggested_questions = list(responses.keys())

def get_response(user_input):
    user_input = user_input.lower().strip()
    if user_input in responses:
        return responses[user_input]
    else:
        return random.choice(fallback_responses)

def send_message(event=None):
    user_input = entry.get().strip()
    if user_input.lower() in ["bye", "exit", "quit"]:
        chat_window.insert(tk.END, "You: " + user_input + "\n\n")
        chat_window.insert(tk.END, "Chatbot: Goodbye! Have a great day!\n\n")
        entry.delete(0, tk.END)
        window.after(200, window.destroy)
    else:
        chat_window.insert(tk.END, "You: " + user_input + "\n\n")
        response = get_response(user_input)
        chat_window.insert(tk.END, "Chatbot: " + response + "\n\n")
        entry.delete(0, tk.END)
        update_suggestions()

def suggestion_click(suggestion):
    entry.delete(0, tk.END)
    entry.insert(0, suggestion)
    send_message()

def update_suggestions():
    for widget in suggestion_frame.winfo_children():
        widget.destroy()
    suggestions = random.sample(suggested_questions, 5)
    for suggestion in suggestions:
        button = tk.Button(suggestion_frame, text=suggestion, command=lambda s=suggestion: suggestion_click(s), bg="#87CEEB", fg="#000000", font=("Arial", 10))
        button.pack(side=tk.LEFT, padx=5, pady=5)

def on_exit():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        window.destroy()

window = tk.Tk()
window.title("Chatbot")
window.configure(bg="#444444")

chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD, bg="#F0F0F0", fg="#000000", font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.insert(tk.END, "Chatbot: Welcome to the chatbot! Type 'bye' to exit.\n\n")

entry = tk.Entry(window, bg="#FFFFFF", fg="#000000", font=("Arial", 12))
entry.pack(padx=10, pady=10, fill=tk.X, expand=False)
entry.bind("<Return>", send_message)

button_frame = tk.Frame(window, bg="#444444")
button_frame.pack(padx=10, pady=10, fill=tk.X, expand=False)

send_button = tk.Button(button_frame, text="Send", command=send_message, bg="#4CAF50", fg="#FFFFFF", font=("Arial", 12))
send_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=on_exit, bg="#FF6347", fg="#FFFFFF", font=("Arial", 12))
exit_button.pack(side=tk.RIGHT, padx=5)

suggestion_frame = tk.Frame(window, bg="#444444")
suggestion_frame.pack(padx=10, pady=10, fill=tk.X, expand=False)
update_suggestions()



window.mainloop()

