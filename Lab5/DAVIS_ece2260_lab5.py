import numpy as np
import matplotlib.pyplot as plt


def main():
    tau = 0.001
    t = np.linspace(0, 5*tau)
    f_t = 5-5*np.e**(-t/tau)
    plt.plot(t, f_t)
    plt.xlabel("Time    [s]")
    plt.ylabel("V_0(t)    [V]")
    plt.show()
    print(find_time_constant(t, f_t))

def find_time_constant(t,f_t):
    """This function takes a time vector and associated voltage curve
    and determines and returns the time constant tau.
    
    Parameters
    ----------
    t:  array_like
        1D array of time points
    f_t:    array_like
        1D array of voltage values with t
    
    Returns
    -------
    tau: float
        time-constant value
    """
    vMax = max(f_t)
    midPoint = 0.632*vMax
    differenceArray = np.absolute(f_t - midPoint)
    index = differenceArray.argmin()
    tau = t[index]
    # print("index", index)
    # print("tau:", tau)
    return tau

if __name__ == '__main__':
    main()