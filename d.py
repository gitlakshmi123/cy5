n = int(input("enter the range: ")) 
fact=1
if n==0:
    fact=1; 
else:
    for i in range(1,n+1):
        fact= fact*i 
print(f"The factorial of number {n} is {fact}")
