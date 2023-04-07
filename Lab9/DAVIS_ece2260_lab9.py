import matplotlib.pyplot as plt
from scipy import signal

def main():
    sys = signal.TransferFunction([1], [1, 1])

    w, mag, phase = signal.bode(sys)

    plt.figure()
    plt.semilogx(w, mag)
    plt.grid(True)

    plt.figure()
    plt.semilogx(w, phase)
    plt.grid(True)

    plt.show()

if __name__ == '__main__':
    main()