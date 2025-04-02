"""
apply different types of windows 

"""
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import numpy as np
import matplotlib.pyplot as plt

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class WindowSignalProcessor:
    def __init__(self, signal):
        self.signal = signal

    def apply_hanning_window(self):
        window = np.hanning(len(self.signal))
        return self.signal * window
    def apply_hanning_window_invese(self):
        window = np.hanning(len(self.signal))
        return self.signal / window

    def apply_hamming_window(self):
        window = np.hamming(len(self.signal))
        return self.signal * window

    def apply_blackman_window(self):
        window = np.blackman(len(self.signal))
        return self.signal * window

    def plot_window(self, window_type):
        if window_type == 'hanning':
            window = np.hanning(len(self.signal))
        elif window_type == 'hamming':
            window = np.hamming(len(self.signal))
        elif window_type == 'blackman':
            window = np.blackman(len(self.signal))
        else:
            raise ValueError("Invalid window type. Use 'hanning', 'hamming', or 'blackman'.")

        plt.plot(window)
        plt.title('Window Function - ' + window_type)
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.show()