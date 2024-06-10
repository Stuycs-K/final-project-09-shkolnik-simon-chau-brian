import audiofile
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

FREQ_1 = 19500
FREQ_0 = 19000
FREQ_S = 8500
FREQ_SPREAD = 50

NPERSEG = 4096
NFFT = 8192

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

def get_freq_list(Zxx, f, fmin, fmax):
    return np.max(np.abs(Zxx[np.argmin(np.abs(f - fmin)) : np.argmin(np.abs(f - fmax)), :]), axis=0)

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

def plot_spectrogram(f, t, Zxx, minf = None, maxf = None):
  if minf or maxf:
    Zxx = Zxx[np.argmin(np.abs(f - minf)) : np.argmin(np.abs(f - maxf)), :]
    f = f[np.argmin(np.abs(f - minf)) : np.argmin(np.abs(f - maxf))]

  _, (ax1) = plt.subplots(1, 1)

  ax1.pcolorfast(t, f, Zxx)
  ax1.set_title("Spectrogram")
  ax1.set_ylabel("Frequency [Hz]")
  ax1.set_xlabel("Time [sec]")

  plt.show()

"""
x = open("testfile.txt", "rb").read()
print(string_to_bin(x))
"""