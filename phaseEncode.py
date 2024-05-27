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

signal, sampling_rate = audiofile.read(AUDIO_FILE_NAME)
try:
    signal[1][0]
    signal = sum(signal)
except:
    print("Only one channel")

segements = signal/NFFT
signal.resize(NFFT * segements)
print(signal)
# string = open(TEXT_FILE_NAME, "rb").read()
# binary = string_to_bin(string)

# f, t, Zxx = stft(signal, fs = sampling_rate, nperseg = NPERSEG, noverlap = 0, nfft = NFFT)
# Zxx = np.absolute(Zxx)

# phaseShifts = [0]*(len(string) * 8)
# index = 0
# for i, v in enumerate(binary):
#     if v == '0': phaseShifts[index] = np.pi/2
#     elif v == '1': phaseShifts[index] = -np.pi/2
#     index += 1


