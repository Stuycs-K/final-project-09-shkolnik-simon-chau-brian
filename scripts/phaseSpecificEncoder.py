import numpy as np
from scipy.signal import stft
from scipy.io import wavfile
import matplotlib.pyplot as plt
import audiofile
from utils import string_to_bin
import sys
import warnings 

warnings.filterwarnings('ignore') 
AUDIO_FILE_NAME = sys.argv[1]
TEXT_FILE_NAME = sys.argv[2]

SECTION = (20, 40)
NPERSEG = 4096
NFFT = 8192

string = open(TEXT_FILE_NAME, "rb").read()
string = string.decode('utf-8').ljust(100, '~')
stringlen = len(string) * 8
phaseShifts = np.empty(stringlen) * 0
strInBin = np.empty([len(string), 8]) * 0

index = 0
for x in string:
    val = ord(x)
    binaryArray = np.empty(8) * 0
    for y in range(8):
        if(val & pow(2,y)):
            binaryArray[y] = int(1)
    binaryArray = binaryArray[::-1]
    strInBin[index] = binaryArray
    index += 1
strInBin = np.ravel(strInBin)

phaseShifts = strInBin.copy()
phaseShifts[phaseShifts == 0] = -1
phaseShifts = phaseShifts * -np.pi / 2

sampling_rate, signal = wavfile.read(AUDIO_FILE_NAME)
signal = signal.copy()
chunkSize = int(2 * 2 ** np.ceil(np.log2(2 * stringlen)))
numOfChuncks = int(np.ceil(signal.shape[0] / chunkSize))

# checks shape to change data to 1 axis
if len(signal.shape) == 1:
  signal.resize(numOfChuncks * chunkSize, refcheck=False)
  signal = signal[np.newaxis]
else:
  signal.resize((numOfChuncks * chunkSize, signal.shape[1]), refcheck=False)
  signal = signal.T

chunks = signal[0].reshape((numOfChuncks, chunkSize))

chunks = np.fft.fft(chunks)
magnitudes = np.abs(chunks)
phases = np.angle(chunks)
phaseDiff = np.diff(phases, axis=0)

testArray = chunks
halfChunk = chunkSize//2
phases[0, halfChunk - stringlen: halfChunk] = phaseShifts
phases[0, halfChunk + 1: halfChunk + 1 + stringlen] = -phaseShifts[::-1]

for i in range(1, len(phases)):
    phases[i] = phases[i-1] + phaseDiff[i-1]

chunks = (magnitudes * np.exp(1j * phases))
chunks = np.fft.ifft(chunks).real

signal[0] = chunks.ravel().astype(np.int16)

audiofile.write("modified_" + AUDIO_FILE_NAME, signal, sampling_rate)