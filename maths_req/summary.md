# Math concepts for DSA
1. Digit extraction
2. Number of digits in number
3. Reversing a number
4. Palindrome
5. is Armstrong
6. Printing divisors
7. GCD or HCF

# Extracting digits
- For extracting digits from lets take an example of 1223345. We need to get 1,2,2,3,3,4,5.
- This can be done in the easiest way by taking the reminder and storing it in a list. Take the remaining number and divide by 10 then take only the integer part of it for the next iteration.
- Repeat this till the number becomes 0. Note that this way we are getting the digits in backwards order i.e, 5,4,3,3,2,2,1.

# Number of digits in a number
- If we see the digit extraction we see that same sequence of steps can be used for getting number of digits but with some changes.
- All we need to is to change it so that instead of storing all the digits just count them.
- There is another way of doing it i.e, taking the integer part of log10(number) + 1.

# Reversing a number
- If we see the digit extraction we see that same sequence of steps can be used for reversing number also.
- We need to is to change it so that each iteration multiply the number previously stored by 10 and then add the remainder result to it.

# Palindrome
- We run from 0 upto floor(n/2) compare i with n-1-i.
- If at any part of the for loop we get an inequality then return false. else return true

# Armstrong number
- An armstrong number is a number such that sum of the digits raised to the power number of digits is equal to the number itself
- This is the same pattern as extracting digits.
  1. We need to get the number of digits first.
  2. After each digit is extracted raise it to the power of number of digits.
  3. Add it to the previous sum.
