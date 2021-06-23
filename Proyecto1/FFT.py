import numpy as np

def my_fft(SEC):
    N = SEC.size
    
    FG1 = np.array([])
    for i in range(0,N):
        FG1 = np.append(FG1, np.cos(np.radians(360*(i/N))) - (np.sin(np.radians(360*(i/N)))*1j))        
        
    FG2 = np.array([])
    for i in range(0,int(N/2)):
        FG2 = np.append(FG2, np.cos(np.radians(360*(i/(N/2)))) - np.sin(np.radians(360*(i/int(N/2))))*1j)
    
    TRANSFORMADA = np.array([])
    for k in range(0,N):
        a=0
        b=0
        for n in range(0,int((N/2))):
            a += SEC[2*n] * FG2[(n*k)%int(N/2)]
        for n in range(0,int((N/2))):
            b += SEC[(2*n)+1] * FG2[(n*k)%int(N/2)]      
        TRANSFORMADA = np.append(TRANSFORMADA, a+(FG1[k]*b))
        print("Muestra: ", k)
    
    return TRANSFORMADA


a = np.array([0, 2, 0, -2])#Este es el ejemplo de la secuencia que se ingresa a la función FFT


#print(FFT(a))