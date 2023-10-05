def prime_number1(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):  
        if num%n==0:
            return False  
    return True
print(prime_number1(13))
print(prime_number1(9.0))
print(prime_number1(3))
print(prime_number1(-3))
# print(prime_number1('three'))
