import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def main():
    t = np.linspace(0, 0.0002, 500)
    L = 1E-3
    C = 0.01E-6
    v_0 = 0
    v_f = 5
    ic_0 = 0

    v_t = rlc_series(632.455, C, L, v_0, v_f, ic_0, t)
    
    plt.plot(t, v_t)
    plt.ticklabel_format(style='scientific', axis='x', scilimits=(0,0))
    plt.title("RLC Series Circuit - Critically Damped")
    plt.xlabel(r"Time $(s)$")
    plt.ylabel(r"Vc $(V)$")
    plt.tight_layout()
    plt.savefig("py_crit.png")
    # plt.show()

def rlc_series(R, C, L, v_0, v_f, ic_0, t):
    """
    This function takes a time array and associated parameters and
    computes the voltage over the capacitor over for a series RLC
    circuit.

    Parameters
    ----------
    R: float
    resistance value (Ohms)
    C: float
    capacitance value (F)
    L: float
    inductance value (H)
    v_0: float
    initial voltage value
    v_f: float
    final voltage value
    ic_0: float
    initial current through the capacitor
    t: array_like
    1D array of time points
    Returns
    -------
    v_t: array_like
    1D array with voltage values corresponding to the time
    points in the input time array
    """
    A = 1
    B = R/L
    D = 1/(L*C)
    alpha = R/(2*L)
    omega = 1/np.sqrt(L*C)
    diff = alpha-omega
    tolerance = 1E3
    if diff > tolerance:
        # vt = v_f + A1 * e^s1t + A2 * e^s2t
        # Solve two equations
        s_1 = -alpha - np.sqrt(alpha**2 - omega**2)
        s_2 = -alpha + np.sqrt(alpha**2 - omega**2)
        a_1, a_2 = sym.symbols('a_1,a_2')
        eq1 = sym.Eq(a_1 + a_2 + v_f, v_0)
        eq2 = sym.Eq(a_1*s_1 + a_2*s_2, ic_0/C)
        aVals = sym.solve([eq1, eq2], (a_1, a_2))
        v_t = v_f + aVals[a_1]*np.e**(s_1*t) + aVals[a_2]*np.e**(s_2*t)
        return v_t
    elif diff < -tolerance:
        # vt = v_f + B1*e^-alphat * cos(omegad t) + B2*e^-alphat * sin(omegad t)
        omega_d = np.sqrt(omega**2 - alpha**2)
        b_1, b_2 = sym.symbols('b_1,b_2')
        eq1 = sym.Eq(b_1 + v_f, v_0)
        eq2 = sym.Eq(b_1*-alpha + b_2*omega_d, ic_0/C)
        bVals = sym.solve([eq1, eq2], (b_1, b_2))
        v_t = v_f + bVals[b_1]*np.e**(-alpha*t)*np.cos(omega_d*t) + bVals[b_2]*np.e**(-alpha*t)*np.sin(omega_d*t)
        return v_t
    else:
        # vt = v_f + D1*t*e^-alphat + D2*e^-alphat
        d_1, d_2 = sym.symbols('d_1,d_2')
        eq1 = sym.Eq(v_f+d_2,v_0)
        eq2 = sym.Eq(d_1 - alpha*d_2,ic_0/C)
        dVals = sym.solve([eq1,eq2], (d_1, d_2))
        v_t = v_f + dVals[d_1]*t*np.e**(-alpha*t) + dVals[d_2]*np.e**(-alpha*t)
        return v_t


if __name__ == '__main__':
    main()