import scipy as sci
import numpy as np
import math
import matplotlib.pyplot as plt

def main():
    # For real and distinct
    # First case: N_s: 96(s+5)(s+12)
    #             N_s: 96s^2 + 1632s + 5760
    #             D_s: s(s+8)(s+6)
    #             D_s: s&3 + 14s^2 + 48s
    t = np.linspace(0, 3, 50)

    N_s_1 = np.array([0, 96, 1632, 5760])
    D_s_1 = np.array([1, 14, 48, 0])
    
    td_1 = 120 - 72*np.e**(-8*t) + 48*np.e**(-6*t)
    out_1 = inverse_laplace(N_s_1, D_s_1, t)

    # For complex and distinct
    N_s_2 = np.array([100, 300])
    D_s_2 = np.array([1, 12, 61, 150])

    td_2 = (-12*np.e**(-6*t) + np.e**(-3*t)* (12*np.cos(4*t) + 16*np.sin(4*t)))
    out_2 = (inverse_laplace(N_s_2, D_s_2, t))

    # For real and repeating
    N_s_3 = np.array([100, 2500])
    D_s_3 = np.array([1, 15, 75, 125, 0])

    td_3 = 20 - 200*t**2*np.e**(-5*t) - 100*t*np.e**(-5*t) - 20*np.e**(-5*t)
    out_3 = inverse_laplace(N_s_3, D_s_3, t)

    # For complex and repeating
    N_s_4 = np.array([768])
    D_s_4 = np.array([1, 12, 86, 300, 625])

    td_4 = -24*t*np.e**(-3*t) * np.cos(4*t) + 6*np.e**(-3*t)*np.cos(4*t - np.radians(90))
    out_4 = inverse_laplace(N_s_4, D_s_4, t)

    # Pyplot stuff
    fig, axis = plt.subplots(4, figsize=(5,6))

    # ax1 = plt.axes()
    # fig.add_axes(ax2)
    axis[0].plot(t, td_1)
    axis[0].plot(t, out_1, '.', color="xkcd:booger")
    axis[0].set_title("Real and Distinct")

    # ax2 = plt.axes()
    # fig.add_axes(ax2)
    axis[1].plot(t, td_2)
    axis[1].plot(t, out_2, '.', color="xkcd:baby poop green")
    axis[1].set_title("Complex and Distinct")

    axis[2].plot(t, td_3)
    axis[2].plot(t, out_3, '.', color="#ab625c")
    axis[2].set_title("Real and Repeated")

    axis[3].plot(t, td_4)
    axis[3].plot(t, out_4, '.', color="#3782b4")
    axis[3].set_title("Complex and Repeated")
    plt.tight_layout()
    plt.show()

    
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
    pole = poles[0]
    f = np.zeros(np.size(t))
    # Test if it's repeated
    numRepRoots = 1
    prepole = None
    for i in range(len(poles)):
        pole = poles[i]
        if pole == prepole:
            numRepRoots += 1
        else:
            numRepRoots = 1
        prepole = poles[i]
        f = f + (r[i] * t **(numRepRoots - 1) * np.exp(poles[i] * t)) / math.factorial(numRepRoots - 1)
    return f


    # for i in range(len(poles)):
    #     if i == 0:
    #         continue
    #     if poles[i] == poles[i-1]:
    #         # Needs support for multiple repeated roots
    #         numRepRoots += 1
    #         hasRepRoots = True
    #     else:
    #         numRepRoots = 0


    hasComplex = np.any(np.iscomplex(r))
    # We probably Dont need this section
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
            
    # The equation we want to use.
    # (t^(n-1) * e(-at)) / (n!)  ==  1/(s+a)**n

    return 

if __name__ == '__main__':
    main()