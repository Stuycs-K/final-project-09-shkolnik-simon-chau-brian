import numpy as np
from scipy.signal import stft
from scipy.signal import istft
import matplotlib.pyplot as plt
from utils import read_audio, get_stft

NUM_BYTES = 6 #todo: calculate from audio
signal, sampling_rate = read_audio("modified_sample_input.mp3")

f, t, Zxx = get_stft(signal, sampling_rate)

oneindex = (np.argmin(np.abs(f - 20000 - 50)), np.argmin(np.abs(f - 20000 + 50)))
zeroindex = (np.argmin(np.abs(f - 19000 - 50)), np.argmin(np.abs(f - 19000 + 50)))
print(oneindex, zeroindex)
bitArray = []

for i in range(NUM_BYTES * 8):
    if(np.sum(Zxx[oneindex[1] : oneindex[0], i]) > np.sum(Zxx[zeroindex[1] : zeroindex[0], i])):
        bitArray.append(1)
    else:
        bitArray.append(0)

print(bitArray)

decodedString = ""

for i in range(NUM_BYTES):
    current_byte = 0

    for j in range(8):
        if bitArray[8 * i + (7 - j)]:
            current_byte += 2 ** j

    decodedString += chr(current_byte)

print(decodedString)