import random
import re

class SupportBot:
    neg_res = ("no", "nope", "nay", "not a chance", "sorry")
    exit_cmds = ("quit", "pause", "exit", "goodbye", "bye", "tata", "farewell")

    def __init__(self):
        self.support_resp = {
    'ask_about_product': r'.*\b(product|item|laptop|phone|TV|tablet|camera|electronics?|devices?)\b.*',
    'technical_support': r'.*(technical|support|help|issue|problem|trouble|not working|malfunction|repair|fix|fault).*',
    'about_returns': r'.*\b(return|refund|exchange|replace|replacement|defective|broken|warranty)\b.*',
    'general_query': r'.*(how.*(help|assist|support)|customer service|faq|how do i|what can i|how does this work|assist me).*'
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
                return self.ask_about_product(reply)
            elif found_match and intent == 'technical_support':
                return self.technical_support()
            elif found_match and intent == 'about_returns':
                return self.about_returns()
            elif found_match and intent == 'general_query':
                return self.general_query()
        return self.no_match_intent()

    def ask_about_product(self, reply):

        if re.search(r'laptop', reply, re.IGNORECASE):
            responses = [
                "We have a variety of laptops, including models from Dell, HP, and Apple. What specific features are you looking for?",
                "Our laptop collection includes gaming, business, and everyday use models. Would you like more details on any of these?",
                "Looking for a laptop? We offer great deals on the latest models with powerful processors and long battery life."
            ]
        elif re.search(r'phone', reply, re.IGNORECASE):
            responses = [
                "We offer the latest smartphones, including iPhones, Samsung Galaxy, and Google Pixel. Which one are you interested in?",
                "Our phone selection includes both Android and iOS devices. Would you like to know about any specific model?",
                "Looking for a phone? We have a wide range of smartphones with great camera features and fast processors."
            ]
        elif re.search(r'TV', reply, re.IGNORECASE):
            responses = [
                "Our TVs range from 32-inch to 85-inch models, including 4K and smart TVs. What screen size are you looking for?",
                "We have LED, OLED, and QLED TVs from top brands like Samsung and LG. Can I assist you in choosing one?",
                "Looking for a new TV? Our latest models come with smart features and stunning display quality. Which brand do you prefer?"
            ]
        elif re.search(r'tablet', reply, re.IGNORECASE):
            responses = [
                "We offer a variety of tablets, including iPads, Samsung Galaxy Tabs, and Microsoft Surface devices. What are you looking for?",
                "Need a tablet? We have models for both casual and professional use. Which one would you like to know more about?",
                "Our tablet collection includes options for entertainment, work, and creative tasks. Can I help you with a specific model?"
            ]
        elif re.search(r'camera', reply, re.IGNORECASE):
            responses = [
                "We offer DSLR, mirrorless, and point-and-shoot cameras from top brands like Canon and Nikon. What are you looking to capture?",
                "Our camera selection includes models for both professionals and hobbyists. Would you like recommendations?",
                "Looking for a new camera? We have great options for photography and videography, from action cameras to DSLRs."
            ]
        else:

            responses = [
                "We offer a wide range of electronics, including phones, laptops, TVs, and more. Is there a specific product you're interested in?",
                "Our product selection includes various electronic devices. Let me know if you're looking for something specific!",
                "Can you specify which type of product you're asking about? We have phones, laptops, tablets, TVs, and more."
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
