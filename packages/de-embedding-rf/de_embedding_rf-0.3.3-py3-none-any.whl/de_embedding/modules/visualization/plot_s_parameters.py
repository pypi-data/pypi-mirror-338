#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#libraries 
import matplotlib.pyplot as plt 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




def plot_mut(frequency,df_magnitude,df_phase):

    #initialization:
    array_frequency = frequency/1e9
    array_magnitude = df_magnitude.iloc[:,:5].to_numpy()
    array_phase = df_phase.iloc[:,:5].to_numpy()
    title = ['S11','S12','S21','S22']
    
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    plt.rc('font', size=14)  # Tamaño de fuente general
    plt.rc('axes', titlesize=14, labelsize=14)  # Tamaño de fuente para títulos y etiquetas de los ejes
    plt.rc('xtick', labelsize=14)  # Tamaño de fuente para las etiquetas del eje x
    plt.rc('ytick', labelsize=14)  # Tamaño de fuente para las etiquetas del eje y
    plt.rc('lines', linewidth=2.5)  # Grosor de las líneas
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    for i_parameter in range(0,4):
        plt.figure(figsize=(15, 6))  

        #-------------------------------------------------------------------------------------------------------------   
        # Subplot for magnitude en dB
        plt.subplot(1, 2, 1)
        plt.plot(array_frequency, array_magnitude[:,i_parameter], linewidth=3.5,color='#ff7c00')

        
        plt.ylabel(f'|{title[i_parameter]}| (dB)')
        plt.xlabel(f'Frequency (GHz)')

        plt.subplot(1, 2, 2)
        plt.plot(array_frequency, array_phase[:,i_parameter], linewidth=3.5,color='#ff7c00')
        plt.ylabel(r'$ \angle $ '+f'{title[i_parameter]}'+ r'$ (^\circ)$ ')
        plt.xlabel(f'Frequency (GHz)')      
        plt.show()



