#day 3 of my coding resolution
#this function reverses an input string
def string_reverse():
    text =  input()
    if text == text[::-1]:
        print("Your input is a palindrome")
    else:
        print("Your input is not a palindrome")


string_reverse()
