stack=list([])
n=1
while(n>=0):
    print('1.Add an element')
    print('2.Delete an element')
    print('3.View elements of linkedlist')
    print('Enter your choice:')
    n=int(input())
    if(n==1):
        stack.append(input())
    elif(n==2):
        p=stack.pop()
        print('The deleted element is ',p)
    elif(n==3):
        print(stack)
        
