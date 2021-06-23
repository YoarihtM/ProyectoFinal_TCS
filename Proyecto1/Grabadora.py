import sounddevice
from scipy.io.wavfile import write

def grabar():
  fs=44100
  second=1.0
  print("recording...")
  record_voice = sounddevice.rec(int(second*fs),samplerate=fs, channels=2)
  sounddevice.wait()
  print ("finished recording")
  write("audio.wav",fs,record_voice)
  return
