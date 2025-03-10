n=int(input('Input n:'))
def resh_sund(n):
    lst=[i for i in range(1, (n+1))]
    ans=[2]
    for i in range(1,(n-1)//2+1):
        for j in range(1, (n-1)//2+1):
            p= i+j+2*i*j
            if p in lst:
                lst.remove(p)
    for x in lst:
        if 2*x+1>n:
            break
        else:
            ans.append(2*x+1)
    return ans
    
print('Простые числа:',*resh_sund(n))


