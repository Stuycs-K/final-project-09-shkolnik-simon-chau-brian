import numpy as np
from scipy.signal import stft
import matplotlib.pyplot as plt
import audiofile
from utils import string_to_bin

AUDIO_FILE_NAME = "sample_input.mp3"
TEXT_FILE_NAME = "testfile.txt"

SECTION = (20, 40)
NPERSEG = 4096
NFFT = 8192

FREQ_1 = 20000
FREQ_0 = 19000
AMPLITUDE = 0.1

signal, sampling_rate = audiofile.read(AUDIO_FILE_NAME)
print(f"Sampling rate: {sampling_rate}hz")

#TODO: only sum signal if theres more than 1 channel, bug otherwise
signal = sum(signal) #combine all channels in audio file
print(f"Audio length: {len(signal) / sampling_rate:.2f}s, taking segment from {SECTION[0]}s-{SECTION[1]}s")
signal = signal[sampling_rate * SECTION[0] : sampling_rate * SECTION[1]] #take only section of audio

def get_stft(signal):
  #f, t, Zxx = stft(signal, fs = sampling_rate, nperseg = 4096, noverlap = 4096 - 128, nfft = 8192)
  f, t, Zxx = stft(signal, fs = sampling_rate, nperseg = NPERSEG, noverlap = 0, nfft = NFFT)
  Zxx = np.absolute(Zxx) #we only care about the magnitude of each frequency, not shift

  #chop of frequencies > 10000
  #f_indexes = f < 250000
  #f = f[f_indexes]
  #Zxx = Zxx[f_indexes]

  return f, t, Zxx

_, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

f, t, Zxx = get_stft(signal)
ax1.pcolorfast(t, f, np.abs(Zxx))
ax1.set_title("Spectrogram (before encoding)")
ax1.set_ylabel("Frequency [Hz]")
ax1.set_xlabel("Time [sec]")
ax1.vlines(t, FREQ_0, FREQ_1, "w")

#encoding
bin_data = string_to_bin(open(TEXT_FILE_NAME, "rb").read())

for i, v in enumerate(bin_data):
  if v == "1":
    freq = FREQ_1
  else:
    freq = FREQ_0

  x = np.linspace(0, freq * 2 * np.pi * (NPERSEG / sampling_rate), NPERSEG)
  x = np.sin(x)

  signal[i * NPERSEG : (i + 1) * NPERSEG] += x * AMPLITUDE

  ax2.hlines(freq, t[i], t[i + 1], "r")

f, t, Zxx = get_stft(signal)
ax2.pcolorfast(t, f, np.abs(Zxx))
ax2.set_title("Spectrogram (after encoding)")
ax2.set_ylabel("Frequency [Hz]")
ax2.set_xlabel("Time [sec]")
ax2.vlines(t, FREQ_0, FREQ_1, "w")

audiofile.write("modified_" + AUDIO_FILE_NAME, signal, sampling_rate)

plt.show()