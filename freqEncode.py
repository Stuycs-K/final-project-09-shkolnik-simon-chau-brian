import numpy as np
import matplotlib.pyplot as plt
import audiofile
from utils import *
import numpy as np
import sys

AUDIO_FILE_NAME = sys.argv[1]
TEXT_FILE_NAME = sys.argv[2]

AMPLITUDE = .2

signal, sampling_rate = read_audio(AUDIO_FILE_NAME)
print(f"Reading {AUDIO_FILE_NAME}")
print(f"Sampling rate: {sampling_rate}hz")
print(f"Audio length: {len(signal) / sampling_rate:.2f}s")

f, t, Zxx = get_stft(signal, sampling_rate)

#encoding
bin_data = string_to_bin(open(TEXT_FILE_NAME, "rb").read().strip())
print(f"Encoding {TEXT_FILE_NAME}")

for i, v in enumerate(bin_data):
  if v == "1":
    freq = FREQ_1
  else:
    freq = FREQ_0

  x = np.linspace(0, freq * 2 * np.pi * (NPERSEG * .5 / sampling_rate), int(NPERSEG * .5))
  x = np.sin(x)

  signal[int((i + .25) * NPERSEG) : int((i + .75) * NPERSEG)] += x * AMPLITUDE

#f, t, Zxx = get_stft(signal, sampling_rate)
#plot_spectrogram(f, t, Zxx)

audiofile.write("modified_" + AUDIO_FILE_NAME, signal, sampling_rate)
print(f"Wrote to modified_{AUDIO_FILE_NAME}")
