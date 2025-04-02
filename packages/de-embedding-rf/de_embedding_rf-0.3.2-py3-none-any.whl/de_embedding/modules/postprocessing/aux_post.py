#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#libraries 
import numpy as np 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def phase_s_parameters(signal_phase):

    new_signal_phase = custom_unwrap(signal_phase)
  
    return new_signal_phase

def magnitude_s_parameters(signal_mag):


    new_signal_mag = replace_values_mag(signal_mag)    


    return new_signal_mag


def replace_values_mag(arr):
    arr = np.array(arr, dtype=float)  
    for i in range(1, len(arr)):  
        if arr[i] >= 0:
            arr[i] = arr[i - 1]*0.85  
    return arr


def custom_unwrap(p, discont=170):

    p = np.asarray(p)  
    unwrapped = np.copy(p)  

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