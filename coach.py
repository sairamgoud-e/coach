t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=0
    z=3
    sm=sum(l[a:z])
    mx=sm
    while z<len(l):
        sm=sm-l[a]+l[z]
        if sm>mx:
            mx=sm
            
        #print(sm,mx)
        a=a+1
        z=z+1
    p=l[n-1]+l[0]+l[n-2]
    q=l[0]+l[1]+l[n-1]
    print(max(mx,p,q))
        
        
