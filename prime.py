import math
def isprime(n):
    a=True
     if(n==1):
         return False
    if(n==2):
        return True
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            a=False
    return a
n=input("Enter the number")
print(isprime(int(n)))