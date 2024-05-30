import numpy as np
from scipy.signal import stft
from scipy.signal import istft
import matplotlib.pyplot as plt
from utils import read_audio, get_stft, FREQ_1, FREQ_0, plot_spectrogram
import sys

AUDIO_FILE_NAME = sys.argv[1]

NUM_BYTES = 31 #todo: calculate from audio

signal, sampling_rate = read_audio(AUDIO_FILE_NAME)
print(f"Reading {AUDIO_FILE_NAME}")

f, t, Zxx = get_stft(signal, sampling_rate)
Zxx = np.absolute(Zxx)

plot_spectrogram(f, t, Zxx)

FREQ_SPREAD = 50

oneindex = [
    np.argmin(np.abs(f - (FREQ_1 - FREQ_SPREAD))),
    np.argmin(np.abs(f - (FREQ_1 + FREQ_SPREAD)))
]
zeroindex = [
    np.argmin(np.abs(f - (FREQ_0 - FREQ_SPREAD))),
    np.argmin(np.abs(f - (FREQ_0 + FREQ_SPREAD)))
]

print(Zxx)

bitArray = np.where(
    np.sum(
        Zxx[oneindex[0] : oneindex[1], :NUM_BYTES * 8 + 1],
        axis=0
    ) > np.sum(
        Zxx[zeroindex[0] : zeroindex[1], :NUM_BYTES * 8 + 1],
        axis=0
    ),
    1, 0
)

print(bitArray)
print(np.sum(
        Zxx[oneindex[0] : oneindex[1], :NUM_BYTES * 8 + 1],
        axis=0
    ))
print(np.sum(
        Zxx[zeroindex[0] : zeroindex[1], :NUM_BYTES * 8 + 1],
        axis=0
    ))
decodedString = ""

for i in range(NUM_BYTES):
    current_byte = 0

    for j in range(8):
        if bitArray[8 * i + (7 - j)]:
            current_byte += 2 ** j

    decodedString += chr(current_byte)

print(f"Output: |{decodedString}|")