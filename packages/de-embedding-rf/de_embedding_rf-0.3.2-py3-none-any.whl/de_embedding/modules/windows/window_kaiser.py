"""
Obtener pico del reflect 

"""
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import kaiser_bessel_derived

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



class WindowKaiser:

    def __init__(self, start=35, end=75, total_size=1000, beta=np.pi*31.83):
        self.start = start
        self.end = end
        self.total_size = total_size
        self.N = self.end- self.start 
        self.beta = beta


    def run(self):
        full_window = np.zeros(self.total_size)
        kbd_window = kaiser_bessel_derived(self.N, beta=self.beta)
        
        # Insertar la ventana en el rango deseado
        full_window[self.start:self.end] = kbd_window

        return full_window
    
    
