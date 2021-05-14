class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None      
    def push(self,newdata):
        new_node=Node(newdata)
        new_node.next=self.head
        self.head=new_node
    def append(self,newdata):
        new_node=Node(newdata)
        if(self.head is None): 
            self.head = new_node 
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node    
    def insertAfter(self,prev_node,new_data):
        newnode=Node(new_data)
        newnode.next=prev_node.next
        prev_node.next=newnode
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
llist = Linkedlist()
n=1
while(n>0):
    print('1.Add an element at the beginning')
    print('2.Add an elemnt at end')
    print('3.Insert an element after a given element')
    print('4.Print linkedlist')
    print('Enter your choice:')
    n=int(input())
    if(n==1):
        llist.push(int(input('Enter the element you want to insert')))
    elif(n==2):
        llist.append(int(input('Enter the element you want to insert')))
    elif(n==3):
        llist.insertAfter(int(input('Enter the element after which you want to insert an element')),int(input('Enter the element you want to insert')))
    elif(n==4):
        llist.printlist()
        
