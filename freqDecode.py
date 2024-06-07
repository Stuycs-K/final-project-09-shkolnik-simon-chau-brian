import numpy as np
from scipy.signal import stft
from scipy.signal import istft
import matplotlib.pyplot as plt
from utils import *
import sys
from functools import reduce
AUDIO_FILE_NAME = sys.argv[1]

signal, sampling_rate = read_audio(AUDIO_FILE_NAME)
print(f"Reading {AUDIO_FILE_NAME}")

f, t, Zxx = get_stft(signal, sampling_rate)
Zxx = np.absolute(Zxx)

#plot_spectrogram(f, t, np.abs(Zxx), 7000, 10000)
#plot_spectrogram(f, t, (np.abs(Zxx)))

SKIPS = get_freq_list(Zxx, f, FREQ_S - FREQ_SPREAD, FREQ_S + FREQ_SPREAD)
ONES = get_freq_list(Zxx, f, FREQ_1 - FREQ_SPREAD, FREQ_1 + FREQ_SPREAD)
ZEROS = get_freq_list(Zxx, f, FREQ_0 - FREQ_SPREAD, FREQ_0 + FREQ_SPREAD)

MIN_AMPLITUDE = .25 * np.max([np.max(ONES), np.max(ZEROS)])
ONES = ONES[SKIPS < 5]
ZEROS = ZEROS[SKIPS < 5\1]

BITS = np.union1d(np.where(ONES > MIN_AMPLITUDE), np.where(ZEROS > MIN_AMPLITUDE))

NUM_BITS = np.where(np.diff(BITS) > 1)[0][0]

bitArray = np.where(ONES > ZEROS, 1, 0)[:NUM_BITS + 1]

"""
print(bitArray)
print(np.sum(
        Zxx[oneindex[0] : oneindex[1], :NUM_BYTES * 8 + 1],
        axis=0
    ))
print(np.sum(
        Zxx[zeroindex[0] : zeroindex[1], :NUM_BYTES * 8 + 1],
        axis=0
    ))
"""
    
decodedString = ""

for i in range(NUM_BITS // 8):
    current_byte = 0

    for j in range(8):
        if bitArray[8 * i + (7 - j)]:
            current_byte += 2 ** j

    decodedString += chr(current_byte)

print(f"Output: |{decodedString}|")