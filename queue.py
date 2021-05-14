queue=list([])
n=1
while(n>=0):
    print('1.Enter elements in queue')
    print('2.Remove an element')
    print('3.Print queue')
    print('4.Print first element')
    print('5.Print last elemnt')
    print('6.Enter your choice:')
    n=int(input())
    if(n==1):
        queue.append(input())
    elif(n==2):
        z=queue[-1]
        queue.remove(queue[0])
        print('The deleted element is',z)
    elif(n==3):
        print(queue)
    elif(n==4):
        print('The first element of queue is ',queue[0])
    elif(n==5):
        print('The last element of queue is ',queue[-1])
        
