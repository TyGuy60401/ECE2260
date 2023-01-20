import math

def calculate_roots(coef):
    a = coef[0]
    b = coef[1]
    c = coef[2]
    in_rad = b*b - 4*a*c
    if in_rad >= 0:
        x1 = (-b + math.sqrt(in_rad))/(2*a)
        x2 = (-b - math.sqrt(in_rad))/(2*a)
    else:
        x1 = (-b + 1j*math.sqrt(-in_rad))/(2*a)
        x2 = (-b - 1j*math.sqrt(-in_rad))/(2*a)
    return (x1, x2)
    
    

def compute_factorial(n):
    if n == 0 or n == 1:
        return 1
    i = n
    while i > 1:
        i -= 1
        n = n*i
    return n
    

def sum_factorial(n):
    i = 1
    val = 0
    while i <= n:
        val += compute_factorial(i)
        i += 1
    return val

def our_function(x):
    return math.e ** (-3*x) * math.cos(math.pi * x)
        
def left_riemann(delta_x, lb, ub):
    i = lb
    val = 0

    while i < ub:
        val += our_function(i) * delta_x
        i += delta_x
    return val
    

def right_riemann(delta_x, lb, ub):
    i = lb + delta_x
    val = 0

    while i <= ub:
        val += our_function(i) * delta_x
        i += delta_x

    return val
    

def midpoint_riemann(delta_x, lb, ub):
    i = lb + delta_x/2
    val = 0

    while i < ub:
        val += our_function(i) * delta_x
        i += delta_x
    return val

    
def trap_riemann(delta_x, lb, ub):
    i = lb
    val = 0
    while i < ub:
        left = i
        right = i + delta_x
        val += (our_function(left) + our_function(right))/2*delta_x
        i += delta_x

    return val

    
def main():


    ##############################################################
    # Part 1
    ##############################################################
    print("Part 1 Results")
    
    coef = [2, 4, 0]
    roots = calculate_roots(coef)
    print("roots 1:")
    print(roots)

    coef = [1, 4, 4]
    roots = calculate_roots(coef)
    print("roots 2:")
    print(roots)
    
    coef = [1, 0, 9]
    roots = calculate_roots(coef)
    print("roots 3:")
    print(roots)

    coef = [2, 8, 26]
    roots = calculate_roots(coef)
    print("roots 4:")
    print(roots)

    ##############################################################
    # Part 2
    ##############################################################
    print("\n")
    print("Part 2 Results")
    
    for n in [4, 10, 16]:
        output_factorial = compute_factorial(n)
        print("computed factorial for n=%i is: %i" %
              (n, output_factorial))
    ##############################################################
    # Part 3
    ##############################################################
    print("\n")
    print("Part 3 Results")
    
    for n in [3, 5, 6]:
        output_summation = sum_factorial(n)
        print("computed factorial summation for n=%i is: %i" %
              (n, output_summation))
    
        
    ##############################################################
    # Part 4
    ##############################################################
    print("\n")
    print("Part 4 Results")
    
    lb = 0
    ub = 10
    
    print("calculating left Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = left_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating right Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = right_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating midpoint Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = midpoint_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating trapezoid Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = trap_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))
    return

        
if __name__ == "__main__":
    main()
