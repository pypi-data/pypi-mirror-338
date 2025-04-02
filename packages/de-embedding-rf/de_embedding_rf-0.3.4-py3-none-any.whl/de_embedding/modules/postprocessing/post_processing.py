#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from de_embedding.modules.windows.window_kaiser import WindowKaiser
from de_embedding.modules.postprocessing.complex_converter import ComplexConverter
from de_embedding.modules.postprocessing.aux_post import magnitude_s_parameters, phase_s_parameters
import numpy as np 
import pandas as pd 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



class Postprocessing:
    def __init__(self,ntwk_data):
        self.s_parameters = ntwk_data
        self.s_parameters.frequency.unit = 'ghz' 
        self.freq = self.s_parameters.f 
        

    def run(self,sigma,p):
        
        s_start = (sigma*10)-(p*10)
        s_end = (sigma*10)+(p*10)
        s11_new, s12_new,s21_new,_ = self.postprocessing_gate(s_start,s_end)
        _, _,_,s22_new = self.postprocessing_gate(s_start+100,s_end-100)

        mag_s11, deg_s11 = ComplexConverter(real=s11_new.real,imag=s11_new.imag).to_magnitude_phase_deg()    
        mag_s12, deg_s12 = ComplexConverter(real=s12_new.real,imag=s12_new.imag).to_magnitude_phase_deg()        
        mag_s21, deg_s21 = ComplexConverter(real=s21_new.real,imag=s21_new.imag).to_magnitude_phase_deg()        
        mag_s22, deg_s22 = ComplexConverter(real=s22_new.real,imag=s22_new.imag).to_magnitude_phase_deg()

        mag_s11 = magnitude_s_parameters(mag_s11)
        mag_s12 = magnitude_s_parameters(mag_s12)        
        mag_s21 = magnitude_s_parameters(mag_s21)
        mag_s22 = magnitude_s_parameters(mag_s22)
        
        deg_s11 = phase_s_parameters(deg_s11)
        deg_s12 = phase_s_parameters(deg_s12)        
        deg_s21 = phase_s_parameters(deg_s21)
        deg_s22 = phase_s_parameters(deg_s22)
        
        list_mag = [ mag_s11,mag_s12 ,mag_s21,mag_s22]
        list_deg = [ deg_s11,deg_s12 ,deg_s21,deg_s22]
        list_name_mag = ['S11 (dB)','S12 (dB)','S21 (dB)','S22 (dB)' ]
        list_name_deg = ['S11 (deg)','S12 (deg)','S21 (deg)','S22 (deg)' ]

        
        df_mag = pd.DataFrame( np.column_stack(list_mag ), columns=list_name_mag)
        df_deg = pd.DataFrame(np.column_stack(list_deg), columns=list_name_deg)

        return self.freq,df_mag,df_deg 


    def postprocessing_gate(self,s_start=1800,s_end=6200):

        #initialization: 
        s11_freq = self.s_parameters.s[:,0,0]
        s12_freq = self.s_parameters.s[:,0,1]
        s21_freq = self.s_parameters.s[:,1,0]
        s22_freq = self.s_parameters.s[:,1,1]

        # apply windows:  

        windowed_s11 = s11_freq
        windowed_s12 = s12_freq
        windowed_s21 = s21_freq
        windowed_s22 = s22_freq
    
        # IFFT transform: 
        N_z = 8000
        s11_time = np.fft.fftshift(np.fft.ifft(windowed_s11  ,n= N_z))
        s12_time = np.fft.fftshift(np.fft.ifft(windowed_s12  ,n= N_z))
        s21_time = np.fft.fftshift(np.fft.ifft(windowed_s21  ,n= N_z))
        s22_time = np.fft.fftshift(np.fft.ifft(windowed_s22  ,n= N_z))

        # create and apply gate :
        t_start = s_start
        t_end = s_end

        # gating_window = np.zeros_like(s11_time)
        # gating_window[t_start:t_end] = 1

        gating_window = WindowKaiser(start=t_start, end=t_end,total_size=N_z).run()
        

        s11_filtered = s11_time * gating_window
        s12_filtered = s12_time * gating_window
        s21_filtered = s21_time * gating_window
        s22_filtered = s22_time * gating_window
        
        # FFT transform:

        new_s11_freq = np.fft.fft(np.fft.ifftshift(s11_filtered ),n= N_z)
        new_s12_freq = np.fft.fft(np.fft.ifftshift(s12_filtered ),n= N_z)
        new_s21_freq = np.fft.fft(np.fft.ifftshift(s21_filtered ),n= N_z)
        new_s22_freq = np.fft.fft(np.fft.ifftshift(s22_filtered ),n= N_z)

        size_original = len(s11_freq)
        
        return  new_s11_freq[:size_original], new_s12_freq[:size_original], new_s21_freq[:size_original], new_s22_freq[:size_original]
    


