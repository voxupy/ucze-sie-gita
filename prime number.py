
n = int(input("Check this number:"))


def prime_checker(n):

    if n % 2 == 0:
        return "Prime number"
    else:
        return "It's not prime number"
        
        
print(prime_checker(n))