import numpy as np
from scipy.signal import stft
from scipy.signal import istft
import matplotlib.pyplot as plt
import audiofile

signal, sampling_rate = audiofile.read("sample_input.mp3")
# print(f"Sampling rate: {sampling_rate}hz")
try:
    signal[1][0]
    signal = sum(signal)
except:
    print("Only one channel")
bitArray = [3] * 10000
i = 0

while(len(signal) > 20):
    portion = signal[sampling_rate * 0 : sampling_rate * 20]
    signal = signal[sampling_rate * 20 : sampling_rate * 40]
    f, t, Zxx = stft(portion, fs = sampling_rate, nperseg = 4096, noverlap = 0, nfft = 8192)
    Zxx = np.absolute(Zxx)
    nextbit = 0
    oneindex = np.argmin(np.abs(f - 20000))
    zeroindex = np.argmin(np.abs(f - 20000))
    # Zxx = np.transpose(Zxx)
    Zxx[oneindex].sort()
    Zxx[zeroindex].sort()
    for x in Zxx[zeroindex]:
        print(x)
    # for x in f:
    #     print(x)
    # oneStartIndex = 1
    # zeroStartIndex = 1
    # print(len(Zxx[oneindex]))
    # while (oneStartIndex < 217 and zeroStartIndex < 217):
    #     if(Zxx[oneindex][oneStartIndex] < Zxx[zeroindex][zeroStartIndex]):
    #         bitArray[nextbit] = 1
    #         oneStartIndex += 1
    #     else:
    #         bitArray[nextbit] = 0
    #         zeroStartIndex += 1
    #     nextbit += 1
    # i += 1

for x in bitArray:
    if(x != 3):
        print(x)
decodedString = ""

