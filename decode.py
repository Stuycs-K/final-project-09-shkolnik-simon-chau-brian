import numpy as np
from scipy.signal import stft
from scipy.signal import istft
import matplotlib.pyplot as plt
from main import get_stft
from utils import read_audio

NUM_BYTES = 6 #todo: calculate from audio
signal, sampling_rate = read_audio("modified_clipped_sample_input.mp3")

f, t, Zxx = get_stft(signal)

oneindex = np.argmin(np.abs(f - 20000))
zeroindex = np.argmin(np.abs(f - 19000))

bitArray = []

for i in range(NUM_BYTES * 8):
    if(Zxx[oneindex][i] > Zxx[zeroindex][i]):
        bitArray.append(1)
    else:
        bitArray.append(0)

    # if(Zxx[oneindex][index] < Zxx[zeroindex][index]):
    #     bitArray[nextbit] = 1
    # elif(Zxx[oneindex][index] > Zxx[zeroindex][index]):
    #     bitArray[nextbit] = 0
    # index += 1
    # nextbit += 1

# for x in bitArray:
#     if(x != 3):
#         print(x)

decodedString = ""

for i in range(NUM_BYTES):
    current_byte = 0

    for j in range(8):
        if bitArray[8 * i + (7 - j)]:
            current_byte += 2 ** j

    decodedString += chr(current_byte)

print(decodedString)