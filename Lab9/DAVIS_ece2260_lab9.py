import matplotlib.pyplot as plt
from scipy import signal

def main():
    sys = signal.TransferFunction([2E7], [1, 2500, 2E7])
    sys_2 = signal.TransferFunction([1, 0, 0], [1, 25000, 2E8])


    w_1, mag_1, phase_1 = signal.bode(sys)
    w_2, mag_2, phase_2 = signal.bode(sys_2)

    makePlot(w_1, mag_1, phase_1, "Low Pass Bode Plot", "low_pass_python.png")
    makePlot(w_2, mag_2, phase_2, "High Pass Bode Plot", "high_pass_python.png")

    plt.show()

def makePlot(w, mag, phase, title="", fout="out.png"):
    fig, ax1 = plt.subplots()
    ax1.set_title(title)

    ax1.set_xlabel('Frequency [Hz]')
    ax1.set_ylabel('Magnitude [dB]', color="blue")
    ax1.semilogx(w, mag)
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.set_ylabel('Phase Shift (degrees)', color="red")
    ax2.semilogx(w, phase, color="red")
    fig.tight_layout()

    fig.savefig("./imgs/" + fout)


if __name__ == '__main__':
    main()