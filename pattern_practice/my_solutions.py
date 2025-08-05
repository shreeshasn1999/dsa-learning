n=5
def prob_1_sol(n):
    for _ in range(n):
        for _ in range(n):
            print("* ", end="")
        print("\n", end="")

def prob_2_sol(n):
    for i in range(n):
        for _ in range(i+1):
            print("* ", end="")
        print("\n", end="")

def prob_3_sol(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1," ", end="")
        print("\n", end="")

def prob_4_sol(n):
    for i in range(n):
        for _ in range(i+1):
            print(i+1," ", end="")
        print("\n", end="")

def prob_4_sol(n):
    for i in range(n):
        for _ in range(i+1):
            print(i+1," ", end="")
        print("\n", end="")

def prob_5_sol(n):
    for i in range(n,0,-1):
        for _ in range(i):
            print("* ", end="")
        print("\n", end="")

def prob_6_sol(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(j+1," ", end="")
        print("\n", end="")

def prob_7_sol(n):
    for i in range(n):
        for j in range((2*n)+1):
            if j<n-i or j>n+i:
                print("  ", end="")
            else:
                print("* ", end="")
        print("\n", end="")

def prob_8_sol(n):
    for i in range(n,0,-1):
        for j in range((2*n),0,-1):
            if j<n-i+1 or j>n+i-1:
                print("  ", end="")
            else:
                print("* ", end="")
        print("\n", end="")

def prob_9_sol(n):
    prob_7_sol(n)
    prob_8_sol(n)

def prob_10_sol(n):
    no_cols = 2*n-1
    for i in range(no_cols):
        if i < n:
            for _ in range(i+1):
                print("* ", end="")
        else:
            for _ in range(no_cols-i):
                print("* ", end="")
        print("\n", end="")

def prob_11_sol(n):
    no_to_print = 1
    for i in range(n):
        for _ in range(i+1):
            print(f"{no_to_print} ", end="")
            no_to_print = 0 if no_to_print==1 else 1
        print("\n", end="")

def prob_12_sol(n):
    for i in range(n):
        for j in range(n):
            if(j<=i):
                print(f"{j+1} ", end="")
            else:
                print("  ", end="")
        for j in range(n,0,-1):
            if(j<=i+1):
                print(f"{j} ", end="")
            else:
                print("  ", end="")
        print("\n", end="")

def prob_13_sol(n):
    sum = 1
    for i in range(n):
        for _ in range(i+1):
            print(sum," " ,end="")
            sum+=1
        print("\n", end="")

def prob_14_sol(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j)," ", end="")
        print("\n", end="")

def prob_15_sol(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(chr(65+j)," ", end="")
        print("\n", end="")

def prob_16_sol(n):
    for i in range(n):
        for _ in range(i+1):
            print(chr(i+65)," ", end="")
        print("\n", end="")


def prob_17_sol(n):
    for i in range(n):
        for _ in range(n-i-1):
            print(" "," ", end="")
        for j in range(i+1):
            print(chr(j+65)," ", end="")
        for j in range(i,0,-1):
            print(chr(j+64)," ", end="")

        print("\n", end="")

def prob_18_sol(n):
    for i in range(n):
        for j in range(i+1,0,-1):
            print(chr(n-j+1+65)," ", end="")
        print("\n", end="")

def prob_19_sol(n):
    for i in range(n):
        for j in range((2*n)):
            if j<n-i or j>=n+i:
                print("* ", end="")
            else:
                print("  ", end="")
        print("\n", end="")
    for i in range(n,0,-1):
        for j in range((2*n),0,-1):
            if j<=n-i+1 or j>=n+i:
                print("* ", end="")
            else:
                print("  ", end="")
        print("\n", end="")

def prob_20_sol(n):
    no_r = (2*n) -1
    for i in range(no_r):
        if i < n:
            for j in range(n):
                if j < i+1:
                    print("* ", end="")
                else:
                    print("  ", end="")
            for j in range(n):
                if j < n-i-1:
                    print("  ", end="")  
                else:
                    print("* ", end="")
        else:
            for j in range(n):
                if j < no_r-i:
                    print("* ", end="")
                else:
                    print("  ", end="")
            for j in range(n,0,-1):
                if j < no_r-i+1:
                    print("* ", end="")
                else:
                    print("  ", end="")
        print("\n", end="")

def prob_21_sol(n):
    for i in range(n):
        for j in range(n):
            if j!=0 and i!=0 and j!=n-1 and i!=n-1:
                print("  ", end="")
            else:    
                print("* ", end="")
        print("\n", end="")



def prob_22_sol(n):
    n_loop = (2*n)-1
    for i in range(n_loop):
        for j in range(n_loop):

            k = min([i,j,abs(n_loop-i-1),abs(n_loop-j-1)])
            print(f"{n-k}"," ", end="")
            
        print("\n", end="")

prob_22_sol(n)
