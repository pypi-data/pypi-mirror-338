#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#libraries 
import numpy as np 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class CollapseValues:
    def __init__(self,array):
        self.array_raw = np.array(array, dtype=float) 
        


    def normalization_values(self):
        #initialization:
        arr = self.array_raw

        #main:
        for i in range(1, len(arr)):  
            if arr[i] >= 1 or arr[i] <= -1:
                arr[i] = arr[i - 1]*0.7  
            
        return arr


    def mag_values(self):

        #initialization:
        arr = self.array_raw
        
        #main:
        for i in range(1, len(arr)):  
            if arr[i] >= 0:
                arr[i] = arr[i - 1]*0.9  
        return arr
