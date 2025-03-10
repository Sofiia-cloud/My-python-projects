def f(lst):
    ans=[]
    count=0
    for x in range(len(lst)):
        for y in range(x+1, len(lst)):
            if lst[x]>lst[y]:
                count+=1
        ans.append(count)
        count=0
    return ans
a=[1,2,3,4]
print(f(a))


