import numpy as np
import matplotlib.pyplot as plt
import audiofile
from utils import *
import numpy as np
import sys

AUDIO_FILE_NAME = sys.argv[1]
TEXT_FILE_NAME = sys.argv[2]

AMPLITUDE = .005

signal, sampling_rate = read_audio(AUDIO_FILE_NAME)
print(f"Reading {AUDIO_FILE_NAME}")
print(f"Sampling rate: {sampling_rate}hz")
print(f"Audio length: {len(signal) / sampling_rate:.2f}s")

f, t, Zxx = get_stft(signal, sampling_rate)

ONES = get_freq_list(Zxx, f, FREQ_1 - FREQ_SPREAD, FREQ_1 + FREQ_SPREAD)
ZEROS = get_freq_list(Zxx, f, FREQ_0 - FREQ_SPREAD, FREQ_0 + FREQ_SPREAD)
SKIPS = get_freq_list(Zxx, f, FREQ_S - FREQ_SPREAD, FREQ_S + FREQ_SPREAD)

#encoding
bin_data = string_to_bin(open(TEXT_FILE_NAME, "rb").read().strip())
print(f"Encoding {TEXT_FILE_NAME}")

#TODO SEPERATE POINTERS
i_data = 0
for i_frame in range(len(bin_data)):
  SKIP_FRAME = False
  v = bin_data[i_data]

  if max(ONES[i_frame], ZEROS[i_frame], SKIPS[i_frame]) > 1: #TODO less arbitrary threshold
    freq = FREQ_S
    SKIP_FRAME = True
  elif v == "1":
    freq = FREQ_1
  else:
    freq = FREQ_0

  x = np.linspace(0, freq * 2 * np.pi * (NPERSEG * .5 / sampling_rate), int(NPERSEG * .5))
  x = np.sin(x)

  signal[int((i_frame + .25) * NPERSEG) : int((i_frame + .75) * NPERSEG)] += x * AMPLITUDE
  
  if not SKIP_FRAME:
    i_data += 1

f, t, Zxx = get_stft(signal, sampling_rate)
#plot_spectrogram(f, t, np.abs(Zxx))
#plot_spectrogram(f, t, np.abs(Zxx), 7000, 10000)

audiofile.write("modified_" + AUDIO_FILE_NAME, signal, sampling_rate)
print(f"Wrote to modified_{AUDIO_FILE_NAME}")
