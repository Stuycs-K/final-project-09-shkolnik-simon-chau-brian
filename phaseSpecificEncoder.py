import numpy as np
from scipy.signal import stft
from scipy.io import wavfile
import matplotlib.pyplot as plt
import audiofile
from utils import string_to_bin
import sys

AUDIO_FILE_NAME = sys.argv[1]
TEXT_FILE_NAME = sys.argv[2]

SECTION = (20, 40)
NPERSEG = 4096
NFFT = 8192

string = open(TEXT_FILE_NAME, "rb").read()
string = string.decode('utf-8').ljust(100, '~')
stringlen = len(string) * 8
# hammingBlocks = stringlen//12
# length = stringlen + hammingBlocks * 4
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
# print(strInBin[12:24])
# for x in range(hammingBlocks):
#   bitsUsed = 0
#   xorValue = 0
#   for y in range(16):
#     if y == 0 or (y and (y & (y - 1))):
#       phaseShifts[y + x * 16] = strInBin[bitsUsed + x * 12]
#       if phaseShifts[y + x * 16] == 1:
#         xorValue = xorValue ^ y
#       bitsUsed += 1
#   if xorValue & 1 == 1:
#     phaseShifts[1 + x * 16] = 1
#   if xorValue & 2 == 2:
#     phaseShifts[2 + x * 16] = 1
#   if xorValue & 4 == 4:
#     phaseShifts[4 + x * 16] = 1
#   if xorValue & 8 == 8:
#     phaseShifts[8 + x * 16] = 1
# print(phaseShifts[16:32])

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
  print(signal.shape)
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

# print(chunk[0])

signal[0] = chunks.ravel().astype(np.int16)

# print(signal[:chunkSize])

# print(np.angle(chunk[halfChunk - stringlen: halfChunk]))

# print(magnitudes[0])
# chunk = signal[0, :chunkSize]
# print(np.angle(np.fft.fft(chunk))[halfChunk - stringlen: halfChunk])

audiofile.write("modified_" + AUDIO_FILE_NAME, signal, sampling_rate)