import numpy as np

class ComplexConverter:
    def __init__(self, real=None, imag=None, magnitude_db=None, phase_deg=None,phase_rad=None):

        self.real = real
        self.imag = imag
        self.magnitude_db = magnitude_db
        self.phase_deg = phase_deg
        self.phase_rad = phase_rad
    
    def to_magnitude_phase_deg(self):

        if self.real is not None and self.imag is not None:
            # Calcula la magnitud en dB
            magnitude = 20 * np.log10(np.sqrt(self.real**2 + self.imag**2))
            
            # Calcula la fase en grados
            phase = np.degrees(np.angle(self.real + 1j * self.imag))
            
            return magnitude, phase
        else:
            raise ValueError("Se requiere la parte real e imaginaria para calcular la magnitud y fase.")
    
    def to_magnitude_phase_rad(self):

        if self.real is not None and self.imag is not None:
            # Calcula la magnitud en dB
            magnitude = 20 * np.log10(np.sqrt(self.real**2 + self.imag**2))
            
            # Calcula la fase en radianes
            phase = np.angle(self.real + 1j * self.imag)
            
            return magnitude, phase
        else:
            raise ValueError("Se requiere la parte real e imaginaria para calcular la magnitud y fase.")
    
    def to_real_imag_deg(self):

        if self.magnitude_db is not None and self.phase_deg is not None:
            # Convierte la magnitud de dB a valor lineal
            magnitude = 10 ** (self.magnitude_db / 20)
            
            # Convierte la fase de grados a radianes
            phase_rad = np.radians(self.phase_deg)
            
            # Calcula la parte real e imaginaria
            real = magnitude * np.cos(phase_rad)
            imag = magnitude * np.sin(phase_rad)
            
            return real, imag
        else:
            raise ValueError("Se requiere la magnitud en dB y la fase en grados para calcular la parte real e imaginaria.")
    
    def to_real_imag_rad(self):

        if self.magnitude_db is not None and self.phase_deg is not None:
            # Convierte la magnitud de dB a valor lineal
            magnitude = 10 ** (self.magnitude_db / 20)
            
            # Usa la fase en radianes directamente
            phase_rad = self.phase_rad
            
            # Calcula la parte real e imaginaria
            real = magnitude * np.cos(phase_rad)
            imag = magnitude * np.sin(phase_rad)
            
            return real, imag
        else:
            raise ValueError("Se requiere la magnitud en dB y la fase en radianes para calcular la parte real e imaginaria.")