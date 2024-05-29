import numpy as np
from scipy.signal import stft
from scipy.io import wavfile
import matplotlib.pyplot as plt
import audiofile
from utils import string_to_bin

AUDIO_FILE_NAME = "modified_sample_input.wav"
TEXT_FILE_NAME = "testfile.txt"

SECTION = (20, 40)
NPERSEG = 4096
NFFT = 8192

signal, sampling_rate = audiofile.read(AUDIO_FILE_NAME)
signal = signal.copy()

string = open(TEXT_FILE_NAME, "rb").read()
binary = string_to_bin(string)
stringlen = len(string) * 8
chunkSize = int(2 * 2**np.ceil(np.log2(2*stringlen)))
numOfChuncks = int(np.ceil(signal.shape[0]/chunkSize))

if len(signal.shape) == 1:
    encodedPart = signal[:chunkSize]
    print("hello")
else:
    encodedPart = signal[:chunkSize,0]
encodedPart = (np.angle(np.fft.fft(encodedPart))[chunkSize//2 - stringlen: chunkSize//2])
encodedPart = encodedPart.reshape((-1,8)).dot(np.arange(8 - 1, -1, -1))
string = np.char.mod('%c', encodedPart)
print(string)
# print(encodedPart)
