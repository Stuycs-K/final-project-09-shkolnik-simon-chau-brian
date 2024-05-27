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

string = open(TEXT_FILE_NAME, "rb").read()
binary = string_to_bin(string)
stringlen = len(string) * 8
phaseShifts = [0]*stringlen
index = 0
for i, v in enumerate(binary):
    if v == '0': phaseShifts[index] = np.pi/2
    elif v == '1': phaseShifts[index] = -np.pi/2
    index += 1


signal1, sampling_rate = audiofile.read(AUDIO_FILE_NAME)

chunkSize = int(2 * 2**np.ceil(np.log2(2*stringlen)))
numOfChuncks = int(np.ceil(signal1.shape[0]/chunkSize))
signal = signal1.copy()

signal.resize(numOfChuncks*chunkSize, refcheck=False)
signal = signal[np.newaxis]

