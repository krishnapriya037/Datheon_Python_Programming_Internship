import random
import os

# ASCII Art Stages for Hangman (0 to 6 mistakes)
HANGMAN_STAGES = [
    """
       ------
       |    |
            |
            |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    ---------
    GAME OVER
    """
]

def get_random_word(filename="words.txt"):
    """Reads a random word from an external words.txt file with defensive fallback handling."""
    if not os.path.exists(filename):
        print(f"⚠️ Warning: '{filename}' not found in directory. Using fallback word list.")
        fallback_words = ["PYTHON", "DEVELOPER", "INTERNSHIP", "ALGORITHM", "ENGINEERING", "PORTFOLIO"]
        return random.choice(fallback_words).upper()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            # Read all lines, strip trailing whitespaces/newlines, and ignore empty lines
            words = [line.strip().upper() for line in file if line.strip()]
            
        if not words:
            print("⚠️ Warning: The words file is empty. Using fallback word.")
            return "PYTHON"
            
        return random.choice(words)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return "PYTHON"

def display_board(mistakes, secret_word, guessed_letters):
    """Renders the current hangman art and masked word progress."""
    print("\n" + "=" * 40)
    print(HANGMAN_STAGES[mistakes])
    
    # Build the masked word view (e.g., P Y _ H O _)
    masked_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print(f"\nWord: {masked_word}")

def play_hangman():
    # Load secret word from words.txt
    secret_word = get_random_word("words.txt")
    guessed_letters = set()
    wrong_letters = set()
    max_mistakes = len(HANGMAN_STAGES) - 1
    
    print("\n" + "🎮" * 15)
    print("Welcome to Terminal Hangman!")
    print(f"The secret word has {len(secret_word)} letters.")
    print("🎮" * 15)

    while len(wrong_letters) < max_mistakes:
        display_board(len(wrong_letters), secret_word, guessed_letters)
        
        # Show incorrect guesses history
        if wrong_letters:
            print(f"Incorrect guesses: {', '.join(sorted(wrong_letters))}")
            
        # Check for win condition
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "🎉" * 15)
            print(f"VICTORY! You successfully guessed the word: {secret_word}")
            print("🎉" * 15)
            return

        # Get player input
        guess = input("\nGuess a letter: ").strip().upper()

        # Input validation: check if single alphabetical character
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Invalid input. Please enter a single alphabetical letter (A-Z).")
            continue
            
        # Check if already guessed
        if guess in guessed_letters or guess in wrong_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
            continue

        # Evaluate guess against secret word
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
            guessed_letters.add(guess)
        else:
            print(f"❌ Sorry, '{guess}' is not in the word.")
            wrong_letters.add(guess)

    # Defeat condition (reached max mistakes)
    display_board(len(wrong_letters), secret_word, guessed_letters)
    print("\n" + "💀" * 15)
    print(f"DEFEAT! The secret word was: {secret_word}")
    print("💀" * 15)

if __name__ == "__main__":
    while True:
        play_hangman()
        replay = input("\nWould you like to play another round? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing! ")
            break