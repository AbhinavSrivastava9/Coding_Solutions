n = int(input("Enter any nth number\n"))

a = 0
b = 1

sum = 0 
for i in range(n):
    print(a,end=",")
    sum = sum + a
    c = a+b
    a=b
    b=c
print("----------------")
print("Sum of the nth fibonacci series is",sum)