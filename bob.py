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
