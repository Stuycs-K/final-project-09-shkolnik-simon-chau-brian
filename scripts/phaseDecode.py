import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import audiofile
from utils import read_audio, string_to_bin, get_stft, NPERSEG, NFFT
import sys

AUDIO_TO_DECODE =  sys.argv[1]

signal, sampling_rate = read_audio(AUDIO_TO_DECODE)
f, t, Zxx = get_stft(signal, sampling_rate)
FREQ_1 = 20000
index = np.argmin(np.abs(f - FREQ_1)),
phases = Zxx[index]
MIN_AMPLITUDE = .25 * np.max(np.max(phases))
NUM_BYTES = 1 + np.max(np.where(phases > MIN_AMPLITUDE))
NUM_BYTES //= 8 
bitArray = np.empty(NUM_BYTES * 8)

frequency = np.angle(phases)
bitArray = np.where(
    frequency < 0
    ,0,1
)

decodedString = ""

for i in range(NUM_BYTES):
    current_byte = 0

    for j in range(8):
        if bitArray[8 * i + (7 - j)]:
            current_byte += 2 ** j

    decodedString += chr(current_byte)

print(f"Output: |{decodedString}|")
