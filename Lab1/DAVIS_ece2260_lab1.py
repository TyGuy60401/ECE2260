import math

def calculate_roots(coef):
    a = coef[0]
    b = coef[1]
    c = coef[2]
    try:
        x1 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
        x2 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
        return (x1, x2)
    except ValueError as err:
        return err
    
    

def compute_factorial(n):
    if n == 0 or n == 1:
        return 1
    i = n
    while (i > 1):
        i -= 1
        n = n*i
    return n
    # to do
    

def sum_factorial(n):
    i = 1
    val = 0
    while i <= n:
        val += compute_factorial(i)
        i += 1
    return val
    # to do
    
        
def left_riemann(delta_x, lb, ub):
    return
    # to do
    

def right_riemann(delta_x, lb, ub):
    return
    # to do
    

def midpoint_riemann(delta_x, lb, ub):
    return
    # to do

    
def trap_riemann(delta_x, lb, ub):
    return
    # to do

    
def main():
    # print(calculate_roots([2, 4, 0]))
    # print(calculate_roots([1, 4, 4]))
    # print(calculate_roots([1, 0, 9]))
    # print(calculate_roots([2, 8, 26]))
    
    # return


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
        print(output_summation)
        print("computed factorial summation for n=%i is: %i" %
              (n, output_summation))
    
    return
        
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

        
if __name__ == "__main__":
    main()
