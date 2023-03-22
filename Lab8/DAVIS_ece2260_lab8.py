import scipy as sci
import numpy as np
import matplotlib.pyplot as plt

def main():
    # For real and distinct
    # First case: N_s: 96(s+5)(s+12)
    #             N_s: 96s^2 + 1632s + 5760
    #             D_s: s(s+8)(s+6)
    #             D_s: s&3 + 14s^2 + 48s

    N_s_1 = np.array([96, 1632, 5760])
    D_s_1 = np.array([1, 14, 48, 0])
    t_1 = np.array([])

    # For complex and distinct
    N_s_2 = np.array([100, 300])
    D_s_2 = np.array([1, 12, 61, 150])

    # For real and repeating
    N_s_3 = np.array([100, 2500])
    D_s_3 = np.array([1, 15, 75, 125])

    # For complex and repeating
    N_s_4 = np.array([768])
    D_s_4 = np.array([1, 12, 86, 300, 625])

    print("Case 1:")
    inverse_laplace(N_s_1, D_s_1, 1)
    print("Case 2:")
    inverse_laplace(N_s_2, D_s_2, 1)
    print("Case 3:")
    inverse_laplace(N_s_3, D_s_3, 1)
    print("Case 4:")
    inverse_laplace(N_s_4, D_s_4, 1)

    
    return

def inverse_laplace(N_s, D_s, t):
    """
    This function will take in the polynomial coefficients
    N_s and D_s for the Laplace transform as well as a 1D
    array of time values and compute the inverse Laplace
    transform for each time value.
    
    Parameters
    ----------
    N_s:    array_like
        Array or list of polynomial coefficients for N_s
    D_s:    array_like
        Array or list of polynomial coefficients for D_s
    t:  array_like
        Array of time values to compute the inverse Laplace
        transform over
    
    Returns
    -------
    f:  array_like
        The values of the inverse laplace transform for each
        value in the input array t
    """
    r, poles, res = sci.signal.residue(N_s, D_s)
    # Test if it's repeated
    hasRepRoots = False
    for i in range(len(poles)):
        if i == 0:
            continue
        if poles[i] == poles[i-1]:
            hasRepRoots = True
            break
    hasComplex = np.any(np.iscomplex(r))
    if hasRepRoots:
        print("There are repeated roots")
        if hasComplex:
            print("It has complex answers")
        else:
            print("No complex answers")
    else:
        print("There are no repeated roots")
        if hasComplex:
            print("It has complex answers")
        else:
            print("No complex answers")
            

    return 

if __name__ == '__main__':
    main()