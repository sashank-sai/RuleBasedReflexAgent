import random
import re

class SupportBot:
    neg_res = ("no", "nope", "nay", "not a chance", "sorry")
    exit_cmds = ("quit", "pause", "exit", "goodbye", "bye", "tata", "farewell")

    def __init__(self):
        self.support_resp = {
            'ask_about_product': r'.*\s*product.*',
            'technical_support': r'.*technical.*support.*',
            'about_returns': r'.*\s*return.*policy.*',
            'general_query': r'.*how.*help.*'
        }

    def greet(self):
        self.name = input("Hello! Welcome to our customer support. What's your name? ")
        will_help = input(f'Hi {self.name}, how can I assist you today? ').lower()
        if will_help in self.neg_res:
            print("Alright, have a great day!")
            return
        self.chat(will_help)

    def make_exit(self, reply):
        for command in self.exit_cmds:
            if command in reply:
                print("Thanks for reaching out. Have a great day!")
                return True
        return False

    def chat(self, will):
        reply = will if will else input("Please tell me your query: ").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_resp.items():
            found_match = re.search(regex_pattern, reply)
            if found_match and intent == 'ask_about_product':
                return self.ask_about_product()
            elif found_match and intent == 'technical_support':
                return self.technical_support()
            elif found_match and intent == 'about_returns':
                return self.about_returns()
            elif found_match and intent == 'general_query':
                return self.general_query()
        return self.no_match_intent()

    def ask_about_product(self):
        responses = [
            "We offer a variety of products, including electronics, apparel, and home goods.",
            "Our product range is diverse, with something for everyone. Would you like information on a specific product?",
            "Can you specify the product you're asking about?"
        ]
        return random.choice(responses)

    def technical_support(self):
        responses = [
            "I can help with technical support! What issue are you experiencing?",
            "Please describe the technical issue, and I'll do my best to assist you.",
            "Is your issue related to hardware or software?"
        ]
        return random.choice(responses)

    def about_returns(self):
        responses = [
            "Our return policy allows returns within 30 days of purchase.",
            "You can return most items within 30 days, but please make sure to check the return policy on specific items.",
            "For returns, please ensure the product is in its original condition and packaging."
        ]
        return random.choice(responses)

    def general_query(self):
        responses = [
            "I'm here to help with any questions you have!",
            "How can I assist you today? Feel free to ask me anything.",
            "I can help with product info, technical support, and more. What would you like to know?"
        ]
        return random.choice(responses)

    def no_match_intent(self):
        responses = [
            "I'm sorry, I don't quite understand your question. Can you rephrase it?",
            "Could you provide more details so I can assist you better?",
            "I'm not sure how to help with that. Could you clarify your query?"
        ]
        return random.choice(responses)


bot = SupportBot()
bot.greet()
