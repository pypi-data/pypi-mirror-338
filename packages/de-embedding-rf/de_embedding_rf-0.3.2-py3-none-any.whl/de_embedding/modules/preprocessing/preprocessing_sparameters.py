
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#libraries 
import matplotlib.pyplot as plt 
import itertools
import copy
import numpy as np 
import pandas as pd

#modules: 
from de_embedding.modules.preprocessing.unwarp_phase import UnwarpPhase
from de_embedding.modules.preprocessing.collapse_values import CollapseValues
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class PreprocessingSparameters:
    def __init__(self,ntwk_raw):
        self.ntwk_raw = ntwk_raw
    
    def apply(self, m=0, n=0):

        # Initialization:  
        ntwk = self.ntwk_raw      
        s_parameters = [(0, 0), (0, 1), (1,0), (1, 1)]
        titles = ['S11', 'S12', 'S21', 'S22']        
        self.ntwk_raw.frequency.unit = 'ghz' 

        list_values_mag = []
        list_name_mag = []
        list_values_deg = []
        list_name_deg = []

        # main: 
        #-------------------------------------------------------------------------------------------------------------
        # Magnitude (dB):

        for (m, n), title in zip(s_parameters, titles):
            
            # Subplot para la magnitud en dB
            if (m==0 and n==0) or (m==1 and n==1):
                ntwk_aux = UnwarpPhase(ntwk,m, n).apply()                    
                freq = ntwk_aux.f
                s_mag = ntwk_aux.s_db[:, m, n] 
                s_deg = ntwk_aux.s_deg_unwrap[:, m, n]        

            else:
                freq = ntwk.f                
                s_mag = ntwk.s_db[:, m, n]
                s_deg = ntwk.s_deg_unwrap[:, m, n]
                

            freq = np.asarray(freq)
            s_mag= np.asarray(s_mag) 
            s_deg = np.asarray(s_deg) 

            if len(freq) != len(s_mag) or len(freq) != len(s_deg) :
                raise ValueError("frequency length with magnitude or phase lengths do not match.")              
      
           
            magnitude_s =CollapseValues(s_mag).mag_values()
           
            
            list_values_mag.append(magnitude_s)
            list_name_mag.append(title+'(dB)')
            list_values_deg.append(s_deg)
            list_name_deg.append(title+'(deg)')  

        df_freq = pd.DataFrame( freq, columns=['freq (GHZ)'])
        df_mag = pd.DataFrame( np.column_stack(list_values_mag), columns=list_name_mag)
        df_deg = pd.DataFrame(np.column_stack(list_values_deg), columns=list_name_deg)

        

        df_final = pd.concat([df_freq, df_mag , df_deg], axis=1)

        return df_final




