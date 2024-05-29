import audiofile
import numpy as np
from scipy.fft import fft, fftfreq

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

def get_stft(signal, sampling_rate):
  t_signal = np.resize(signal, (len(signal) // NPERSEG) * NPERSEG)
  t_signal = np.reshape(t_signal, (-1, NPERSEG))

  f = fftfreq(NFFT, 1 / sampling_rate)[:NFFT // 2]
  t = np.arange(0, len(signal), NPERSEG) / sampling_rate
  Zxx = fft(t_signal, NFFT, axis=1)[:, :NFFT // 2]

  Zxx = np.transpose(Zxx)

  t = t[:-1]
  Zxx = Zxx[:-1, :]

  return f, t, Zxx

"""
x = open("testfile.txt", "rb").read()
print(string_to_bin(x))
"""