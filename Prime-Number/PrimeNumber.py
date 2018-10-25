# Function to check if given number is a prime number
def isPrime(num):
    if (num>=2):
        for i in range(2,num):
            if not (num%i):
                return False
    else:
        return False
    return True

n = int(input("Enter a number : "))
if (isPrime(n)):
    print(n,"is a prime number")
else:
    print(n, "is not a prime number")