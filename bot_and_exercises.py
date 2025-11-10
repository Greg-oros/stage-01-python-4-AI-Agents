class bod:
    a = 20
    b = 30
print(bod.a)

# Exercise 1  - class structure and object creation.
class Bota:
    pass  # the word 'pass' means: "don't do anything here for now"

# Create an object of the Bot class
my_bot = Bota()
second_bot = Bota()
print(type(my_bot))
print(type(second_bot)) # new instance of the class, checking how class sees new object

# Exercice 2 - passing data to an object upon creation.
class Botb:
    def __init__(self, name):
        self.name = name  # instance attribute
        print("Botb has just born!")

my_botb = Botb("Robot inside me")
print(my_botb.name)

# Exercise 3 speak() method
class Botc:
    def __init__(self, name, job): # the proper way to list arguments is to make them in dictionary
        self.name = name
        self.job = job
        

    def speak(self):
        print(f"Welcome! I am a {self.name}")
    def introduce(self):
        print(f"I can do things, but this time only few like {self.job}") # Added a new argument: job and make it works

my_bot = Botc("bot, Bot C","")
my_bot.speak()
your_bot = Botc("", "say hello")
your_bot.introduce()

# Exercise 4 - checking method with arguments
class Botd:
    def __init__(self, name):
        self.name = name

    def speak(self, message):
        print(f"{self.name} and I say: {message}")
        

my_bot = Botd("I am a botd")
my_bot.speak("Hi, how are you?")

# Exercise 5 - simple bot for dialog and interactions

class Bote:
    def __init__(self, name):
        self.name = name

    def speak(self, message):
        if "hi" in message.lower():
            print(f"{self.name}: Hey! What's up")
        elif "what's your name" in message.lower():
            print(f"{self.name}: My name is {self.name}.")
        elif "bye" in message.lower():
            print(f"See you later!")
        else:
            print(f"{self.name}: Do not know, wthat to say")

    def run(self):
        print(f"{self.name}: Hello! Let's talk (write 'bye', to stop and finish)")
        running = True
        while running:
            user_input = input("You: ")
            if "bye" in user_input.lower():
                self.speak(user_input)
                running = False
            else:
                self.speak(user_input)

# uruchomienie bota
bot = Bote("I am bote")
bot.run()

