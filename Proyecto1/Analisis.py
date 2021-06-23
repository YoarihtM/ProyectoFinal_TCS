import numpy as np
import librosa
import scipy
from FFT import my_fft

#---------------------------------------------------------------------------------------------
def analizaAudio(path):
  #path = "AudiosEntrenamiento/"+name
  muestras, tasa_muestreo = librosa.load(path, sr=None, mono=True, offset=0.0, duration=None)
  info = dict()#Se crea diccionario
  info['muestras'] = muestras
  info['tasa_muestreo'] = tasa_muestreo
   
  return info
  
#---------------------------------------------------------------------------------------------
def getAmplitudes(muestras):#Retorna arreglo con las amplitudes
  n = len(muestras)
  #ftt = my_fft(muestras)
  fft = scipy.fft.fft(muestras)
  amplitudes = 2.0/n * np.abs(fft[:n//2])
  
  return amplitudes
  
#---------------------------------------------------------------------------------------------
def startAnalisis():
  carpetas = ['AH','EH','IH','OH','UH']
  
  #°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
  promedios = np.array([])
  for carpeta in carpetas:
    maximos = np.array([])
    for i in range(1,6,1):#						IMPORTANTE
      path = 'Audios/'+carpeta+'/'+carpeta+'_'+str(i)+'.wav'
      #print(path)
      analisis = analizaAudio(path)
      amp = getAmplitudes(analisis['muestras'])
      #print('Máximo: ', max(amp))
      maximos = np.append(maximos, max(amp))
    #print('Promedio: ', np.mean(maximos))
    promedios = np.append(promedios, np.mean(maximos))
    #print('-'*30)
  
  return promedios
