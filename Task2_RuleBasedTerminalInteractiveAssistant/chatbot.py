import json
import re
import os
import sys

def load_faq():
    """Load the JSON dataset from the data folder."""
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'faq.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Could not find 'data/faq.json'. Check your folder structure.")
        sys.exit(1)

def get_bot_response(user_input, data):
    """Determine the bot's response based on rules and keywords."""
    clean_input = user_input.strip().lower()
    
    # 1. Check for Exit Commands
    if clean_input in ['bye', 'exit', 'quit', 'goodbye']:
        return "Goodbye! Have a great day ahead! 👋", True

    # 2. Check for Greetings
    for greeting in data.get("greetings", []):
        if re.search(r'\b' + re.escape(greeting) + r'\b', clean_input):
            return "Hello! Welcome to the Support Assistant. How can I help you today?", False

    # 3. Check for FAQs
    for faq in data.get("faqs", []):
        question = faq["question"].lower()
        answer = faq["answer"]
        
        # Extract keywords longer than 2 characters
        keywords = [word for word in re.findall(r'\w+', question) if len(word) > 2]
        match_count = sum(1 for kw in keywords if re.search(r'\b' + re.escape(kw) + r'\b', clean_input))
        
        if match_count >= 2 or any(kw in clean_input for kw in keywords if len(kw) > 4):
            return answer, False

    # 4. Fallback Response
    return "I'm sorry, I didn't quite catch that. Try asking about our hours or internship submissions!", False

def run_chatbot():
    data = load_faq()
    
    print("=" * 60)
    print("🤖 Rule-Based Interactive Terminal Assistant is Running!")
    print("Type 'exit', 'quit', or 'bye' to end.")
    print("=" * 60)
    print("\nBot: Hello! How can I assist you with your internship today?\n")
    
    while True:
        try:
            user_input = input("You: ")
            if not user_input.strip():
                continue
                
            response, should_exit = get_bot_response(user_input, data)
            print(f"\nBot: {response}\n")
            
            if should_exit:
                break
        except (KeyboardInterrupt, EOFError):
            print("\n\nBot: Goodbye!")
            break

if __name__ == "__main__":
    run_chatbot()