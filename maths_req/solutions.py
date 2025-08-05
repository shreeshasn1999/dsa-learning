import math

def extract_digits(n):
    digits = []
    x = n
    while x > 0:
        digits.append(x%10)
        x //= 10
    # digits.reverse()
    return digits 

def no_of_digits(n):
    # num = 0
    # while n > 0:
    #     num += 1 
    #     n //= 10
    return math.floor(math.log10(n)+1)

def reverse_num(n):
    sum = 0
    while n > 0:
        sum = (sum*10) + n%10
        n //= 10
    return sum

def check_palindrome(str_to_check):
    s_len = len(str_to_check)
    for i in range(s_len//2):
        if str_to_check[i] != str_to_check[s_len-1-i]:
            return "No"
    return "Yes"

def isArmstrong(num):
    sum = 0
    x = num
    power = math.floor(math.log10(num)+1)
    while x > 0:
        sum += (x%10)**power
        x //= 10
    if(sum == num):
        return True
    else:
        return False

def printAllDivisors(num):
    n_iter = math.floor(num ** 0.5)
    for i in range(1,n_iter+1):
        if num % i == 0:
            if i == num//i:
                print(i)
            else:
                print(i,num//i)

def check_prime(num):
    n_iter = math.floor(num ** 0.5)
    for i in range(2,n_iter+1):
        if num % i == 0:
            return False
        
    return True

def euclidean_algo_gcd(num1,num2):
    b = min(num1,num2)
    a = max(num1,num2)
    if b == 0:
        return a
    else:
        return euclidean_algo_gcd(a%b,b)

def euclidean_algo_gcd_simplified(a,b):
    while a!=0 and b!=0:
        if(a > b):
            a = a % b
        else:
            b = b % a
    if a == 0: 
        return b
    else:
        return a

print(euclidean_algo_gcd_simplified(35,37))
