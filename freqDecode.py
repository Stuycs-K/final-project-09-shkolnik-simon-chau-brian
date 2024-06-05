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

plot_spectrogram(f, t, np.abs(Zxx), 7000, 10000)
#plot_spectrogram(f, t, (np.abs(Zxx)))

ONES = get_freq_list(Zxx, f, FREQ_1 - FREQ_SPREAD, FREQ_1 + FREQ_SPREAD)
ZEROS = get_freq_list(Zxx, f, FREQ_0 - FREQ_SPREAD, FREQ_0 + FREQ_SPREAD)
SKIPS = get_freq_list(Zxx, f, FREQ_S - FREQ_SPREAD, FREQ_S + FREQ_SPREAD)

MIN_AMPLITUDE = .25 * np.max([np.max(ONES), np.max(ZEROS)])

BYTES = np.union1d(np.where(ONES > MIN_AMPLITUDE), np.where(ZEROS > MIN_AMPLITUDE))

NUM_BYTES = np.where(np.diff(BYTES) > 1)[0][0]
NUM_BYTES //= 8

#print(Zxx)

bitArray = np.where(ONES > ZEROS, 1, 0)[:NUM_BYTES * 8 + 1]

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

for i in range(NUM_BYTES):
    current_byte = 0

    for j in range(8):
        if bitArray[8 * i + (7 - j)]:
            current_byte += 2 ** j

    decodedString += chr(current_byte)

print(f"Output: |{decodedString}|")