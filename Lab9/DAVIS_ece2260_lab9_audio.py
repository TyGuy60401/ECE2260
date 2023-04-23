import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import sounddevice as sd
import soundfile as sf
import sys

def main(argv):
    if len(argv) > 1:
        userChoice = argv[1]
    else:
        userChoice = input("Input:\n   plots | sound | quit\n>> ")

    if "sound" in userChoice.lower():
        filename = 'handel.wav'
        makeMusic(filename)
    elif "plot" in userChoice.lower():
        makePlot([2E7], [1, 2500, 2E7], "Low Pass Bode Plot", "low_pass_python.png")
        makePlot([1, 0, 0], [1, 25000, 2E8], "High Pass Bode Plot", "high_pass_python.png")
        plt.show()
    elif "quit" in userChoice.lower():
        return

def makePlot(num, den, title="", fout="out.png"):
    sys = signal.TransferFunction(num, den)
    w, mag, phase = signal.bode(sys)

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

def makeMusic(filename):
    data, fs = sf.read(filename, dtype='float32')
    data = data[:,0]
    numSamples = len(data)
    t = np.linspace(0, 0.004, 1000)

    h_lp = f_lp(t)
    h_hp = f_hp(t)
    print("Compute convolution")
    data_lp = np.convolve(data, h_lp)
    data_lp /= max(abs(data_lp))
    data_hp = np.convolve(data, h_hp)
    data_hp /= max(abs(data_hp))

    sound_break = np.zeros(fs * 2)
    
    data_play = np.hstack((data, sound_break, 
                           data_lp, sound_break,
                           data_hp))
    print("Should play now")
    sd.play(data_play, fs)
    sd.wait()
    sd.stop()


def f_lp(t):
    return 16000*np.sqrt(5)/np.sqrt(59) * np.e**(-1250 * t) * np.sin(250*np.sqrt(295) * t)

def f_hp(t):
    return -25000 * np.e**(-12500 * t) * np.cos(2500 * np.sqrt(7) * t) + 45000 / np.sqrt(7) * np.e ** (-12500 * t) * np.sin(2500 * np.sqrt(7) * t)

if __name__ == '__main__':
    main(sys.argv)