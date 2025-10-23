

def min_takes(A, B, C, D):
    """
    Solution demo to test
    """
    print(f"Number of blue shirts {A}")
    print(f"Number of red shirts {B}")
    print(f"Number of blue socks {C}")
    print(f"Number of red socks {D}")
    
    total_number_blue = A + C
    total_number_red = B + D
    
    if total_number_blue < total_number_red:
        print(total_number_blue + 2)
    else:
        print(total_number_red + 2)

# min_takes(6, 8, 7, 3)


# Solution to submit
"""
A = int(input())
B = int(input())
C = int(input())
D = int(input())


total_number_blue = A + C 
total_number_red = B + D 

if A and B and C and D:
    if total_number_blue < total_number_red:
        print(A + 1, C + 1)
    elif total_number_blue == total_number_red:
        print(min(A, B, C, D) + 1, 1)
    else:
        print(B + 1, D + 1)
else:
    if not A:
        print(1, C + 1)
    elif not B:
        print(1, D + 1)
    elif not C:
        print(A + 1, 1)
    elif not D:
        print(B + 1, 1)
"""
    

