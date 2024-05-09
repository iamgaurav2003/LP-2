# Define some greetings and responses
greetings = ["hi", "hello", "hey"]
farewells = ["bye", "goodbye", "see you later"]
thanks = ["thank you", "thanks"]
how_are_you = ["how are you", "how's it going"]

# Common customer service phrases
support_options = {
    "order_status": "What's your order number? I can check the status for you.",
    "return_policy": "Our return policy allows for returns within 30 days of purchase. You can find more details on our website: [link to return policy]",
    "payment_options": "We accept major credit cards, debit cards, and secure payment options like PayPal.",
    "shipping_info": "Standard shipping usually takes 3-5 business days. You can find more details on our shipping options: [link to shipping info]",
    "contact_support": "I can't answer that directly, but I can connect you with a live representative. Would you like me to do that?",
}

# Function to handle greetings
def handle_greeting():
  return "Hi there! How can I help you today?"

# Function to handle farewells
def handle_farewell():
  return "See you later! Have a great day!"

# Function to handle thanks
def handle_thanks():
  return "You're welcome!"

# Function to handle how are you
def handle_how_are_you():
  return "I'm doing well, thanks for asking! How about you?"

# Function to handle simple yes/no questions
def handle_yes_no(user_input):
  yes_words = ["yes", "ya", "sure"]
  no_words = ["no", "nope", "not really"]
  if any(word in user_input.lower() for word in yes_words):
    return "Alright, let me know if you need anything else."
  elif any(word in user_input.lower() for word in no_words):
    return "Perhaps you can visit our FAQ page for more information: [link to FAQ]"
  else:
    # User's answer wasn't a clear yes or no
    return "I understand. How else can I assist you?"

# Function to handle user requests
def handle_request(user_input):
  for option, response in support_options.items():
    if option in user_input.lower():
      return response
  return "I'm still under development and learning! Can you rephrase your question or try browsing our FAQ page: [link to FAQ]"

# Get user input
user_input = input("You: ").lower()

# Main loop to simulate conversation
while user_input not in farewells:
  if user_input in greetings:
    print("Chatbot: " + handle_greeting())
  elif user_input in thanks:
    print("Chatbot: " + handle_thanks())
  elif user_input in how_are_you:
    print("Chatbot: " + handle_how_are_you())
  # Handle simple yes/no questions
  elif "?" in user_input and ("can" in user_input or "could" in user_input):
    print("Chatbot: " + handle_yes_no(user_input))
  else:
    print("Chatbot: " + handle_request(user_input))
  user_input = input("You: ").lower()

print("Chatbot: " + handle_farewell())
