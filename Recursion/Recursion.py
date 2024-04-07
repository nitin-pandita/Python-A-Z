def fib(n):
    if n == 1:
        return 1
    
    return n * fib(n - 1)

#? finding the sum of first n natural numbers
def sum_n(n):
    if n == 0:
        return 0
    
    smallOutput = sum_n(n - 1)
    output = smallOutput + n
    return output

#? finding the power of number
def power_n(x,n):
    ans = 1
    while n > 0:
        ans = ans * x
        n -= 1
    


    return ans

x = int(input())
n = int(input())
# print(fib(n))
# print(sum_n(n))
print(power_n(x,n))