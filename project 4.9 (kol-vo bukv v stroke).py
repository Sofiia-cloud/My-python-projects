str=input("Введите строку: ")
lst=[i for i in str]
def hash_table(lst):
    res={}
    for i in lst:
        res[i]=lst.count(i)
    sorted_dict = dict(sorted(res.items()))
    return sorted_dict
print(hash_table(lst))