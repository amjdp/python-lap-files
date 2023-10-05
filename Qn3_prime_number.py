
def prime_numbers1(num) :

    if(isinstance(num, str)):
        return False

    if (isinstance(num, float)):
        num=int(num)
    flag = False

    if num < 1:
        return False  

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break

    if flag:
        return False
    else:
        return True


    
    
print(prime_numbers1(3))
print(prime_numbers1(33))
print(prime_numbers1(3.0))
print(prime_numbers1(3.5))
print(prime_numbers1(-3))
print(prime_numbers1('three'))