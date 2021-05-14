
i=int(input())
z=[]
for x in range(i):
 m=int(input())
 lis=[]
 pis=[]
 for p in range(m):
     pis=list(map(int, input().strip().split()))[:m]
     lis.append(pis)    
     pis=[]
 k=0
 i=0
 for pis in lis:
     k+=pis[i]
     i+=1
 r=0
 c=0
 for pis in lis:
     for q in pis:
         if(pis.count(q)!=1):
             r+=1
             break
 for i  in range(m):
    l=list([]) 
    for pis in lis:  
        l.append(pis[i])
    for q in l:    
       if(l.count(q)!=1):
            c+=1
            break
        
        
 o=[]    
 o.append(k)     
 o.append(r)
 o.append(c)
 z.append(o)
i=0 
for o in z:
    print("Case #"+str(i+1)+": "+ str(o[0])+" "+str(o[1])+" "+str(o[1])) 
    i+=1
 
 
 
 
 
