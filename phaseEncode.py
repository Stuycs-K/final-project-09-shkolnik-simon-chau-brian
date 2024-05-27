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
try:
    signal[1][0]
    signal = sum(signal)
except:
    print("Only one channel")

string = open(TEXT_FILE_NAME, "rb").read()
binary = string_to_bin(string)

f, t, Zxx = stft(signal, fs = sampling_rate, nperseg = NPERSEG, noverlap = 0, nfft = NFFT)
Zxx = np.absolute(Zxx)

