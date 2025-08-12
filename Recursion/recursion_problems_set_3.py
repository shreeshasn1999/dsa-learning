
# * Single pointer approach
def reverse_arr(arr,i):
    length = len(arr)
    if i >= length//2:
        # print(arr)
        return arr
    arr[i],arr[length-1-i] = arr[length-1-i],arr[i]
    return reverse_arr(arr,i+1)

# def reverse_arr_func(arr,i):
#     if i == len(arr)//2:
#         if len(arr)%2:
#             return [arr[i]]
#         else:
#             return []
#     return [arr[len(arr)-1-i]] + reverse_arr_func(arr,i+1) + [arr[i]]

# * Two pointers approach
def reverse_arr_two_p(arr,l,r):
    if l >= r:
        return arr
    arr[l],arr[r] = arr[r],arr[l]
    return reverse_arr_two_p(arr,l+1,r-1)

arr = ["1","2","3","4","5"]
length = len(arr)
# reverse_arr(arr,0,length)

# * Two pointers approach
def valid_palindrome(string,l,r):
    if l >= r:
        return True
    
    if string[l] != string[r]:
        return False
    
    else:
        return valid_palindrome(string,l+1,r-1)
    
to_check = "112111"
print(valid_palindrome(to_check,0,len(to_check)-1))