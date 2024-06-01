import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import audiofile
from utils import read_audio, string_to_bin, get_stft, NPERSEG, NFFT
import sys

AUDIO_FILE_NAME = sys.argv[1]
TEXT_FILE_NAME = sys.argv[2]

SECTION = (20, 40)
AMPLITUDE = 0.2

FREQ_0 = 1500
string = open(TEXT_FILE_NAME, "rb").read()
binary = string_to_bin(string)
stringlen = len(string) * 8
phaseShifts = np.empty(stringlen)
index = 0
for i, v in enumerate(binary):
    if v == '0': phaseShifts[i] = np.pi/2
    elif v == '1': phaseShifts[i] = -np.pi/2

signal, sampling_rate = read_audio(AUDIO_FILE_NAME)
f, t, Zxx = get_stft(signal, sampling_rate)

for i in range(len(phaseShifts)):
    x = np.linspace(0, FREQ_0 * 2 * np.pi * (NPERSEG * .5 / sampling_rate), int(NPERSEG * .5))
    x = np.sin(x + phaseShifts[i])
    signal[int((i + .25) * NPERSEG) : int((i + .75) * NPERSEG)] += x * AMPLITUDE

# test = signal.tolist()
# for i in range(100):
#     print(test[i])

audiofile.write("modified_" + AUDIO_FILE_NAME.replace("mp3", "wav"), signal, sampling_rate)