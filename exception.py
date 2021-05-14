try:
 a=10
 print(a)
except ArithmeticError:
 print("This statement is raising an Arithmetic exception")
except OverflowError:
 print("This statement is raising an Overflow exception")
except ArithmeticError:
 print("This statement is raising an exception")
finally:
 print("This statement will always Excute")
