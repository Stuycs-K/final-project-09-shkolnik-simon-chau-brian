import numpy as np
from scipy.signal import stft
from scipy.signal import istft
import matplotlib.pyplot as plt
from utils import *
import sys

AUDIO_FILE_NAME = sys.argv[1]

signal, sampling_rate = read_audio(AUDIO_FILE_NAME)
print(f"Reading {AUDIO_FILE_NAME}")

f, t, Zxx = get_stft(signal, sampling_rate)
Zxx = np.absolute(Zxx)

#plot_spectrogram(f, t, np.abs(Zxx))
#plot_spectrogram(f, t, (np.abs(Zxx)))

ONES = get_freq_list(Zxx, f, FREQ_1 - FREQ_SPREAD, FREQ_1 + FREQ_SPREAD)
ZEROS = get_freq_list(Zxx, f, FREQ_0 - FREQ_SPREAD, FREQ_0 + FREQ_SPREAD)

MIN_AMPLITUDE = 2 #.25 * np.max([np.max(ONES), np.max(ZEROS)])
#print(MIN_AMPLITUDE)

bitArray = np.where(ONES > ZEROS, 1, 0)[np.logical_xor(ONES > MIN_AMPLITUDE, ZEROS > MIN_AMPLITUDE)]
#print(np.logical_xor(ONES > MIN_AMPLITUDE, ZEROS > MIN_AMPLITUDE))

NUM_BYTES = 0
for j in range(8):
    if bitArray[7 - j]:
        NUM_BYTES += 2 ** j

#print(NUM_BYTES)
bitArray = bitArray[8 : 8 + NUM_BYTES * 8 + 1]

decodedString = ""

for i in range(min(NUM_BYTES, len(bitArray) // 8)):
    current_byte = 0

    for j in range(8):
        if bitArray[8 * i + (7 - j)]:
            current_byte += 2 ** j

    decodedString += chr(current_byte)

print(f"Output: |{decodedString}|")