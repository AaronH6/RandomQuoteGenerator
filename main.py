def random_quote():
    import random
    with open('quotes.txt', 'r') as quotes: #opens the text file that contains quotes I found online
        quotes = quotes.readlines()
    quotes = [quote.strip() for quote in quotes if quote.strip()]  # Remove empty lines
    return random.choice(quotes)


# This script will print a random motivational quote when the user presses Enter.
input("Press Enter to get a random motivational quote...")
# This prints the motivational quote to the console with good spacing.
print("Here's a motivational quote for you: \n" + random_quote() + "\n")
print("Hope you enjoyed your quote!\n")
# prompts the user to ask for another quote or end the program
print("Would you like another quote? (yes/no)")
while True:
    user_input = input().strip().lower()
    if user_input == 'yes':
        print("Here's another motivational quote for you: \n" + random_quote() + "\n")
        print("Would you like another quote? (yes/no)")
    elif user_input == 'no':
        print("Thank you for using the motivational quote generator! Goodbye!")
        break
    else:
        print("Please answer with 'yes' or 'no'.")

