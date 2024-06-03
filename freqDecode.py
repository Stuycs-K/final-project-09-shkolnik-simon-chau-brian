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

#plot_spectrogram(f, t, Zxx)

FREQ_SPREAD = 50

oneindex = [
    np.argmin(np.abs(f - (FREQ_1 - FREQ_SPREAD))),
    np.argmin(np.abs(f - (FREQ_1 + FREQ_SPREAD)))
]
zeroindex = [
    np.argmin(np.abs(f - (FREQ_0 - FREQ_SPREAD))),
    np.argmin(np.abs(f - (FREQ_0 + FREQ_SPREAD)))
]

ONES = np.sum(Zxx[oneindex[0] : oneindex[1], :], axis=0)
ZEROS = np.sum(Zxx[zeroindex[0] : zeroindex[1], :], axis=0)

MIN_AMPLITUDE = .25 * np.max([np.max(ONES), np.max(ZEROS)])

NUM_BYTES = 1 + np.max([
  np.max(np.where(ONES > MIN_AMPLITUDE)),
  np.max(np.where(ZEROS > MIN_AMPLITUDE))
])
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