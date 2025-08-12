# Sum of first n numbers.

# ! Paramaterised way
# * We observe the change in parameters at each stage then change them accordingly.
# * Here we see that the sum variable should be incremented by n amount. While n gets decremented.

def sum_first_n(sum,n):
    if n==0:
        print(sum)
        return
    sum_first_n(sum+n,n-1)

# ! Functional way recursion 
# * When we want to return something from a function without changing the parameters
# * Applying it to the given problem we see that any f(n) = n + f(n-1)
# * f(3) = 3 + f(2) = 2 + f(1) = 1

def sum_first_n_func(n):
    if n==1:
        return 1
    return n + sum_first_n_func(n-1)

def fact_n_func(n):
    if n == 1:
        return 1
    return n * fact_n_func(n-1)

def fact_n_para(prod,n):
    if n==1:
        print(prod)
        return
    fact_n_para(prod*n,n-1)

print(fact_n_para(1,5))

# Time and Space Complexity
# TC : O(n)
# SC : O(n), because the auxiliary space is a stack. that occupies a space of O(n)