f=open('file4.txt','r')
feven=open('even.txt','w')
fodd=open('odd.txt','w')
str=f.read()
n=str.split(',')
for i in n:
    if (int(i)%2==0):
        feven.write(i+',')
    else:
        fodd.write(i+',')
f.close()
feven.close()
fodd.close()
