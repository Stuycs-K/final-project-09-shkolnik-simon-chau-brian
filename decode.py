import numpy as np
from scipy.signal import stft
from scipy.signal import istft
import matplotlib.pyplot as plt
import audiofile

signal, sampling_rate = audiofile.read("modified_sample_input.mp3")
try:
    signal[1][0]
    signal = sum(signal)
except:
    print("Only one channel")
bitArray = [3] * 10000

while(len(signal) > 20):
    portion = signal[sampling_rate * 0 : sampling_rate * 20]
    signal = signal[sampling_rate * 20 : sampling_rate * 40]
    f, t, Zxx = stft(portion, fs = sampling_rate, nperseg = 4096, noverlap = 0, nfft = 8192)
    Zxx = np.absolute(Zxx)
    nextbit = 0
    oneindex = np.argmin(np.abs(f - 20000))
    zeroindex = np.argmin(np.abs(f - 19000))
    # Zxx[oneindex].sort()
    # Zxx[zeroindex].sort()
    # oneStartIndex = 1
    # zeroStartIndex = 1
    index = 0
    while (index < 217):
        if(Zxx[oneindex][oneStartIndex] < Zxx[zeroindex][zeroStartIndex]):
            bitArray[nextbit] = 1
            oneStartIndex += 1
            nextbit += 1
        elif(Zxx[oneindex][oneStartIndex] > Zxx[zeroindex][zeroStartIndex]):
            bitArray[nextbit] = 0
            zeroStartIndex += 1
            nextbit += 1


        # if(Zxx[oneindex][index] < Zxx[zeroindex][index]):
        #     bitArray[nextbit] = 1
        # elif(Zxx[oneindex][index] > Zxx[zeroindex][index]):
        #     bitArray[nextbit] = 0
        # index += 1
        # nextbit += 1

for x in bitArray:
    if(x != 3):
        print(x)
decodedString = ""

