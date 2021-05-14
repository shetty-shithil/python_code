# cook your dish here
T=int(input())
N=list()
P=list()
for i in range(T):
    k=int(input())
    N.append(k)
    X=list(map(int,input().split()))
    P.append(X)
print(N)
print(P)
k=0
for X in P:  
        count=list()
        for b in X:
            p=int(1)
            for z in range(N[k]):
                if(b!=X[z]):
                    if(abs(X[z]-b)<=2):
                        p+=1
                        b=X[z]       
            count.append(p)
        print(count)
        k+=1    
        print(str(min(count))+" "+str(max(count)))           
                       
                    
            
                    
                    
        
    
    
