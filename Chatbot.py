class ChatBot:
    
    def __init__(self, name):
        self.name = name
        self.memory = []

    def greet(self):
        print(f"Hello! I am {self.name}")

    def respond(self, message):
        self.memory.append(message)

        if "hello" in message.lower():
            return "Hi there!"
        elif "bye" in message.lower():
            return "Goodbye!"
        else:
            return "I don't understand."

bot = ChatBot("NemoBot")
bot.greet()
print(bot.respond("hello"))