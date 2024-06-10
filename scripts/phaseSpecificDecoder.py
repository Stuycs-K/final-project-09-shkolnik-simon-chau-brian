import numpy as np
import scipy as sp
import scipy.io.wavfile as wavfile
import sys

MODIFIED_FILE = sys.argv[1]

sampling_rate, signal = wavfile.read(MODIFIED_FILE)
stringlen = 800
chunkSize = int(2 * 2**np.ceil(np.log2(2*stringlen)))
halfChunk = chunkSize//2
numOfChuncks = int(np.ceil(signal.shape[0]/chunkSize))

try:
    encoded = signal[:chunkSize, 0]
except:
    encoded = signal[:chunkSize]

chunk = np.fft.fft(encoded)

phases = np.angle(np.fft.fft(encoded))[halfChunk - stringlen: halfChunk]
binary = np.empty(phases.size)

for x in range(phases.size):
    if phases[x] < 0:
        binary[x] = 1
    else:
        binary[x] = 0

for x in range(binary.size):
    test = 0
    for y in range(8):
        if binary[x*8 + y] == 1:
            test += pow(2,7-y)
    if test == 126:
        ints = ints[:x]
        break
    else:
        ints[x] = test
string = ""
for x in ints:
    string += chr(int(x))
print(string)