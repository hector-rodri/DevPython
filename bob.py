print("Welcome to Bob's Chatbot!")
print()
print("Bob is a lackadaisical teenager. He likes to think that he's very cool.")
print("And he definitely doesn't get excited about things. That wouldn't be cool.")
print("When people talk to him, his responses are pretty limited.")
print()
print("Instructions:")
print("Your task is to talk to Bob and see how he replies to what you say.")
print("Bob only ever answers one of five things:")
print()
print('1. "Sure." - If you ask him a question (ends with a "?")')
print('2. "Whoa, take it easy!" - If you YELL AT HIM (ALL CAPS).')
print('3. "Whoa, chill out! I know what I\'m doing!" - If you yell a question at him.')
print('4. "Fine. Be that way!" - If you say nothing or only spaces.')
print('5. "Whatever." - For anything else.')
print()
print("Try saying something to Bob and see how he reacts!")


user_input = input('Talk to Bob: ')

if user_input.isupper() and user_input.endswith('?'):
    print("Whoa, chill out! I know what I'm doing!")
elif user_input.isupper():
    print("Whoa, take it easy!")
elif user_input.endswith('?'):
    print("Sure.")
elif user_input.isspace:
    print("Fine. Be that way!")
else:
    print("Whatever")
