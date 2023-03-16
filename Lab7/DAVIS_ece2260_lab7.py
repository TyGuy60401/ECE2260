import numpy as np
import matplotlib.pyplot as plt
import sys

def main():
    num_samples = 1000
    frequencies = np.linspace(1000, 100E3, num_samples)
    omegas = 2*np.pi*frequencies

    Z_l = 4.7E-3*omegas*1j
    Z_c = -1j/(0.033E-6*omegas)
    Z_r = 1000

    Z_s = Z_l + Z_c + Z_r 
    Z_p = calc_parallel([Z_l, Z_c, Z_r]) 

    mag_Z_s = np.abs(Z_s)
    angle_Z_s = np.angle(Z_s, True)

    mag_Z_p = np.abs(Z_p)
    angle_Z_p = np.angle(Z_p, True)
    
    # Do all of the pyplot stuff
    plt.suptitle("Magnitude and Phase Angle of Impedances")
    make_subplot(221, frequencies, mag_Z_s, r"RLC Series $|Z_s|$", r"Ohms $[\Omega ]$")
    make_subplot(222, frequencies, angle_Z_s, r"RLC Series $\angle Z_s$", r"Degrees $[\degree ]$")
    make_subplot(223, frequencies, mag_Z_p, r"RLC Parallel $|Z_p|$", r"Ohms $[\Omega ]$")
    make_subplot(224, frequencies, angle_Z_p, r"RLC Parallel $\angle Z_p$", r"Degrees $[\degree ]$")

    plt.tight_layout()
    if len(sys.argv) < 2:
        plt.show()
    
    print("RLC Series: ", find_omega_0(Z_s, omegas, "series"), sep='\t')
    print("RLC Parallel: ", find_omega_0(Z_p, omegas, "parallel"), sep='\t')


def make_subplot(num, x_axis, y_axis, title, y_axis_title):
    plt.subplot(num)
    plt.xlabel(r"Frequency $[Hz]$")
    plt.ylabel(y_axis_title)
    plt.title(title)
    plt.plot(x_axis, y_axis)
    plt.semilogx()

def calc_parallel(vals):
    total_value_reciprocal = 0
    for value in vals:
        total_value_reciprocal += 1/value
    return 1/total_value_reciprocal


def find_omega_0(Z, omega, circuit_type):
    """
    This function takes an array Z and array of frequency
    values omega and returns omega_0
    
    Parameters
    ----------
    Z:  array_like
        Array of impedance values
    Omega:  array_like
        Array of frequency values in radians/second
    circuit_type:   string
        This can either be 'series' or 'parallel'
    
    Returns
    -------
    omega_0:    float
        The resonant frequency in radians/second
    f_0:    float
        The resonant frequency in hertz
    
    """
    mag_Z = np.abs(Z)
    if circuit_type == "series":
        critical_Z = min(mag_Z)
    elif circuit_type == "parallel":
        critical_Z = max(mag_Z)
    
    diff_Z = mag_Z - critical_Z
    for i in range(len(diff_Z)):
        if diff_Z[i] == 0:
            break
    frequencies = omega/(2*np.pi)
    omega_0, f_0 = omega[i], frequencies[i]
    
    return omega_0, f_0 

if __name__ == '__main__':
    main()