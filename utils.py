import audiofile
import numpy as np
from scipy.signal import stft

def string_to_bin(s):
  out = ""

  for i in s:
    out += bin(i)[2:].rjust(8, "0")

  return out

def read_audio(filename):
  signal, sampling_rate = audiofile.read(filename)

  if len(signal.shape) > 1:
    signal = sum(signal)

  return signal, sampling_rate

NPERSEG = 4096
NFFT = 8192

def get_stft(signal, sampling_rate, nperseg = None):
  #f, t, Zxx = stft(signal, fs = sampling_rate, nperseg = 4096, noverlap = 4096 - 128, nfft = 8192)
  f, t, Zxx = stft(signal, fs = sampling_rate, nperseg = nperseg or NPERSEG, noverlap = 0, nfft = 8192, padded=True)
  Zxx = np.absolute(Zxx) #we only care about the magnitude of each frequency, not shift

  #chop of frequencies > 10000
  #f_indexes = f < 250000
  #f = f[f_indexes]
  #Zxx = Zxx[f_indexes]

  return f, t, Zxx

"""
x = open("testfile.txt", "rb").read()
print(string_to_bin(x))
"""