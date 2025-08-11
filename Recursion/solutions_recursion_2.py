def print_5_times(name,ct):
    if ct == 5:
        return
    print(name)
    print_5_times(name,ct+1)

# * Time complexity : O(n)
# * Space complexity : O(n)

# ! Here the system/python uses a stack as the data structure for recursion. There are going to be n functions waiting
# ! to be completed. Hence Space complexity is O(n)

def print_1_to_n(ct,n):
    if ct > n:
        return
    print(ct)
    print_1_to_n(ct+1,n)

def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n-1)

def print_1_to_n_back(ct):
    if ct == 0:
        return
    print_1_to_n_back(ct-1)
    print(ct)

def print_n_to_1_back(ct,n):
    if ct > n:
        return
    print_n_to_1_back(ct+1,n)
    print(ct)

print_n_to_1_back(1,5)
