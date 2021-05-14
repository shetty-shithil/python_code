import os

f=open('file1.txt','r')
l=0
w=0
c=0
for line in f:
    l+=1
    c=c+len(line)
    words=line.split()
    w=w+len(words)
print('The no. of lines is '+str(l)+',no. of characters is '+str(c)+'and words is '+str(w))
