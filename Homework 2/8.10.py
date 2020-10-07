user_input = input()
no_space_input = user_input.replace(' ', '')
reverse_no_space=''.join(reversed(no_space_input))

if no_space_input == reverse_no_space:
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")
