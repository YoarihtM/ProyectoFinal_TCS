from tkinter import *
from tkinter import ttk
import tkinter as tk
from Grabadora import grabar
from Analisis import analizaAudio, getAmplitudes, startAnalisis
from Graficas import graficaEspectroFrecuencias, graficaAudio
from Identificacion import identificar
from matplotlib import pyplot as plt
import librosa
from librosa import display
import threading
import time
from tkinter import PhotoImage
from PIL import Image,ImageTk
import easygui as eg

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


global promediosH
global app
global vocalEncontrada


def Calibrar():
  promedios = startAnalisis()
  #print("Promedios: ",promedios)

  #°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
  PROM = ""
  for promedio in promedios:
    PROM += str(promedio)+','
  PROM = PROM[:-1]#Se le quita el ',' del final
  result = {}
  result['H'] = PROM

  #°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
  #Se escribe en archivo
  with open('calibracion.txt', 'w') as f:
    f.write(str(result))
    f.write('\n')
  f.close()

#---------------------------------------------------------------------------------
def Grabar():
  Calibrar()  
  promediosH = leerArchivo()
  grabar()
  b1 = tk.Button(app,bg='#24264F', fg='#FFFFFF',cursor="hand1",text="Grafica de Audio",command=lambda: graficaAudio(analisis['muestras'], analisis['tasa_muestreo'])).place(x = 90, y = 270)
  b2 = tk.Button(app,bg='#24264F', fg='#FFFFFF',cursor="hand1",text="Grafica de Espectro de Frecuencia",command=lambda: graficaEspectroFrecuencias(amp, int(analisis['tasa_muestreo']))).place(x = 45, y = 305)

  analisis = analizaAudio("audio.wav")
  amp = getAmplitudes(analisis['muestras'])
  vocaL = str(identificar(promediosH,max(amp)))
  resultado = StringVar()
  vocalEncontrada = Label(app, textvariable = resultado, font=("Verdana",70), bg='#24264F', fg='#FFFFFF').place(x = 105, y = 145)
  
  resultado.set(vocaL)
  print(vocaL)
  #print(max(amp))

#---------------------------------------------------------------------------------
def iniciaContador():
  pb.start(12)
  time.sleep(1.2)
  pb.stop()
#----------------------------------------------------------------------------------
def inicio():
  t1 = threading.Thread(name = "iniciaContador", target = iniciaContador)
  t2 = threading.Thread(name = "Grabar", target = Grabar) 
  t1.start()
  t2.start()
  #t2.join()
  #t1.join()
#---------------------------------------------------------------------------------
def leerArchivo():
  with open('calibracion.txt', 'r') as f:
    promsH = []
    promsM = []
    for line in f.readlines():
      #print('line: ',line)
      line = eval(line)
      H = line['H']
      proms = H.split(",")
      promsH = [float(i) for i in proms]
  f.close()
  return promsH

#=================================================================================

app = tk.Tk()
 # Configuración de ventana
app.geometry('300x350')#ancho,alto
app.config(bd=10, bg='#24264F')#Margen a los contornos
app.title('Proyecto Final')

img = Image.open('microfono.png')
img = img.resize((50, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img = ImageTk.PhotoImage(img)
botonGrabar = tk.Button(app, image=img, text="Grabar", compound="top", command=inicio, bg='#24264F', fg='#FFFFFF')
botonGrabar.place(x=500, y=100)
botonGrabar.pack() 

label = Label(app, text = 'Letra detectada:', font=("Verdana",12), bg='#24264F', fg='#FFFFFF').place(x = 71, y = 115)

pb = ttk.Progressbar(app, orient="horizontal", length=200)
pb.pack()
pb.config(mode="determinate", maximum=100, value = 0)
pb.step(100)

app.mainloop()