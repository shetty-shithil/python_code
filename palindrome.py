str1=input("Enter a string:")
str1=str1.casefold()
str2=reversed(str1)
if list(str1)==list(str2):
    print('The given string is a palindrome.')
else:
    print('It is not a palindrome.')
