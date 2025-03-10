n=int(input('Введите номер числа Фибоначчи:'))
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)
print('Число Фибоначчи под номером',n, 'равно',fib(n))