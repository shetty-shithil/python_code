class Abc:
    def __init__(self,str):
        self.str=str
    def check(self):
        rev=reversed(self.str)
        if list(rev)==list(self.str):
            print(self.str,'is a palindrome.')
        else:
            print(self.str,'is not a palindrome.')
a=Abc(input('Enter a string:'))
a.check()
del a
