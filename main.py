import nltk
import random

class SocialSkillsBot:
    def __init__(self):
        self.conversations = []
        self.greetings = [
            "Hi there",
            "Hello!",
            "Welcome",
        ]

    def respond(self, user_input):

        if "help" in user_input.lower():
            return "I can help improve your social skills."

        return random.choice(self.greetings)

def main():
    bot = SocialSkillsBot()

    print("Type exit to end")

    while True:
        user_input = ("You: ")

        if user_input.lower() == "exit":
            break

        response = bot.respond(user_input)
        print("Bot:" ,response)

if __name__ == "__main__":
    main()