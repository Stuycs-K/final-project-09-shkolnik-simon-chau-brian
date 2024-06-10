import numpy as np
import scipy as sp
import scipy.io.wavfile as wavfile
import sys

MODIFIED_FILE = sys.argv[1]

sampling_rate, signal = wavfile.read(MODIFIED_FILE)
stringlen = 800
# hammingBlocks = stringlen//12
# length = stringlen + hammingBlocks * 4
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

# print(phases[:100])

for x in range(phases.size):
    if phases[x] < 0:
        binary[x] = 1
    else:
        binary[x] = 0

# for x in range(hammingBlocks):
#     xorValue = 0
#     for y in range(16):
#         if binary[y + x * 16] == 1:
#             xorValue = xorValue ^ binary[y + x * 16]
#     if xorValue != 0:
#         if binary[x * 16 + xorValue] == 0:
#             binary[x * 16 + xorValue] = 1
#         else:
#             binary[x * 16 + xorValue] = 0

# nohamming = int(2 * 2**np.ceil(np.log2(2*stringlen)))

ints = np.empty(chunkSize)

# for x in range(hammingBlocks):
#     bitsUsed = 0
#     for y in range(16):
#         if y == 0 or (y and (y & (y - 1))):
#             ints[bitsUsed + x * 12] = binary[y + x * 16]

# ints = ints[halfChunk - length: halfChunk]

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