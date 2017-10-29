def func(n):
    summ=0
    c=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    s=0                    
                    if i==k:                       
                        s+=1                        
                    if i==l:                        
                        s+=1                        
                    if j==k:
                        s+=1                        
                    if j==l:
                        s+=1                    
                    summ+=s    
    print("4n^3 =",4*n**3)
    return summ

def func2(n):
    summ=0
    c=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    s=0
                    if k==l and i==j:
                        s+=1
                        pass
                    if l==i:
                        s+=1
                        pass
                    if l==j:
                        s+=1
                        pass
                    if k==l:
                        s+=1
                        pass
                    summ+=s
    #print("3n^3 =",3*n**3)
    print("3n^3+n^2 =",3*n**3+n**2)
    return summ

def f(n):
    for i in range(n):
        print("n =",i)
        print()
        print("F_1:",func(i))        
        print()
        print("F_2:",func2(i))        
        print('-'*50)
        #print("3n^3+n^2 =",3*i**3+i**2)

