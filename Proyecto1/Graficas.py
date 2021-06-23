import librosa
from librosa import display
from matplotlib import pyplot as plt
import numpy as np
from tkinter import *
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

global canvas
#---------------------------------------------------------------------------------------------
def graficaAudio(muestras, tasa):
  plt.figure()
  librosa.display.waveplot(y=muestras, sr=tasa)
  plt.xlabel("Tiempo (s)")
  plt.ylabel("Amplitud")
  plt.title("Amplitud de Audio")
  plt.show()

#---------------------------------------------------------------------------------------------
def graficaEspectroFrecuencias(amplitudes, tasa):
  n = len(amplitudes)
  T = 1/tasa#Periodo
  xf = np.linspace(0.0, 1.0/(2.0*T), n)
  fig, ax = plt.subplots()
  ax.plot(xf, amplitudes)
  plt.grid()
  plt.xlabel("Frecuencia")
  plt.ylabel("Magnitud")
  plt.title("Espectro de Frecuencias")
  plt.show()
