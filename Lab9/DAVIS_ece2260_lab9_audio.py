import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import sounddevice as sd
import soundfile as sf
import time

def main():

    filename = 'handel.wav'
    data, fs = sf.read(filename, dtype='float32')
    data = data[:,0]
    numSamples = len(data)
    numSeconds = numSamples / fs
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
    return

def f_lp(t):
    return 16000*np.sqrt(5)/np.sqrt(59) * np.e**(-1250 * t) * np.sin(250*np.sqrt(295) * t)

def f_hp(t):
    return -25000 * np.e**(-12500 * t) * np.cos(2500 * np.sqrt(7) * t) + 45000 / np.sqrt(7) * np.e ** (-12500 * t) * np.sin(2500 * np.sqrt(7) * t)

if __name__ == '__main__':
    main()