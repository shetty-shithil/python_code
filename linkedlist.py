ll=list([])
n=1
while(n>=0):
    print('1.Enter element in a linkedlist')
    print('2.Delete first element')
    print('3.Delete last element')
    print('4.Insert an element as per given index')
    print('5.Delete an element as per given index')
    print('6.Display linkedlist')
    print('Enter your choice')
    n=int(input())
    if(n==1):
        ll.append(input())
    elif(n==2):
        z=ll[0]
        ll.remove(ll[0])
        print('The deleted element is ',z)
    elif(n==3):
        z=ll.pop()
        print('The deleted element is ',z)
    elif(n==4):
        print('Enter the index at which you want to insert an element')
        z=int(input())
        print('Enter the element')
        ll.insert(z, input())
    elif(n==5):
        print('Enter the index at which you want to delete an element')
        z=int(input())
        p=ll[z]
        ll.remove(ll[z])
        print('The delted element is ',p)
    elif(n==6):
        print(ll)
    
