import numpy as np
from scipy.signal import stft
import matplotlib.pyplot as plt
import audiofile
from utils import string_to_bin

FILE_NAME = "sample_input.mp3"
SECTION = (20, 40)

signal, sampling_rate = audiofile.read(FILE_NAME)
print(f"Sampling rate: {sampling_rate}hz")

signal = sum(signal) #combine all channels in audio file
print(f"Audio length: {len(signal) / sampling_rate:.2f}s, taking segment from {SECTION[0]}s-{SECTION[1]}s")
signal = signal[sampling_rate * 20 : sampling_rate * 40] #take only section of audio

def get_stft(signal):
  #f, t, Zxx = stft(signal, fs = sampling_rate, nperseg = 4096, noverlap = 4096 - 128, nfft = 8192)
  f, t, Zxx = stft(signal, fs = sampling_rate, nperseg = 4096, noverlap = 0, nfft = 8192)
  Zxx = np.absolute(Zxx) #we only care about the magnitude of each frequency, not shift

  #chop of frequencies > 10000
  #f_indexes = f < 250000
  #f = f[f_indexes]
  #Zxx = Zxx[f_indexes]

  return f, t, Zxx

_, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

f, t, Zxx = get_stft(signal)
ax1.pcolormesh(t, f, np.abs(Zxx), shading="gouraud")
ax1.set_title("Spectrogram (before encoding)")
ax1.set_ylabel("Frequency [Hz]")
ax1.set_xlabel("Time [sec]")

#encoding
bin_data = string_to_bin(open("testfile.txt", "rb").read())

for i, v in enumerate(bin_data):
  if v == "1":
    f = 20000
  else:
    f = 19000

  x = np.linspace(0, f * 2 * np.pi * (4096 / sampling_rate), 4096)
  x = np.sin(x)

  signal[i * 4096 : (i + 1) * 4096] += x / 10

f, t, Zxx = get_stft(signal)
ax2.pcolormesh(t, f, np.abs(Zxx), shading="gouraud")
ax2.set_title("Spectrogram (after encoding)")
ax2.set_ylabel("Frequency [Hz]")
ax2.set_xlabel("Time [sec]")

audiofile.write("modified_" + FILE_NAME, signal, sampling_rate)

plt.show()