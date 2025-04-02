#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#libraries 
import numpy as np 
import copy

#modules:
from de_embedding.modules.preprocessing.collapse_values import CollapseValues

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class UnwarpPhase:
    def __init__(self,ntwk_raw,m_parametre=0,n_parametre=0):            
        self.ntwk_raw = ntwk_raw
        self.m = m_parametre 
        self.n = n_parametre 

    #-------------------------------------------------------------------------------------------

    def apply(self):

        #initialization: 
        network_name = self.ntwk_raw           
        network_copy = copy.deepcopy(network_name)
        m = self.m
        n = self.n
        
        #main: 
        magnitude = np.abs(network_copy.s[:, m, n])
        phase = network_copy.s_deg_unwrap[:, m, n]
        
        # Unwrap the phase
        unwrapped_phase = self.custom_unwrap(phase)


        phase_rad = np.deg2rad(unwrapped_phase)
        real_part = magnitude * np.cos(phase_rad)
        imaginary_part = magnitude * np.sin(phase_rad )

        new_real_part = CollapseValues(real_part).normalization_values()
        new_imaginary_part = CollapseValues(imaginary_part).normalization_values()

        array_complex = new_real_part + 1j * new_imaginary_part
        
        network_copy.s[:, m, n] = array_complex    
        
        return network_copy
    
            

    #-------------------------------------------------------------------------------------------
    def custom_unwrap(self,p, discont=170):

        # Initialization:
        p = np.asarray(p)  
        unwrapped = np.copy(p)  

        # Main: 
        for i in range(1, len(p)):
            
            diff = p[i] - p[i-1]

            if diff > discont:
                
                try: 
                    diff_before = unwrapped[i-1] - unwrapped[i - 2]                
                except Exception:
                    diff_before = 0

                unwrapped[i:] = (unwrapped[i:]- diff) +diff_before
            
            elif diff < -discont:

                try: 
                    diff_before = unwrapped[i-1] - unwrapped[i - 2]                
                except Exception:
                    diff_before = 0

                unwrapped[i:] =  (unwrapped[i:]-diff) +diff_before

        return unwrapped
    
    #--------------------------------------------------------------------------------------------------------

