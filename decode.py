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
bitArray = [255] * 1000
i = 0

while(len(signal) > 20):
    portion = signal[sampling_rate * 0 : sampling_rate * 20]
    signal = signal[sampling_rate * 20 : sampling_rate * 40]
    f, t, Zxx = stft(portion, fs = sampling_rate, nperseg = 4096, noverlap = 0, nfft = 8192)
    Zxx = np.absolute(Zxx)
    nextbit = 0
    index = np.argmin(np.abs(f - 19000))
    # f_index = np.argmin(np.abs(Zxx[0] - 19000))
    # high_index = np.argmin(np.abs(Zxx[0] - 20000))
    # print(1/Zxx[0][f_index])

    # for x in f:
    #     print(x)

    # if(frequency < 20000 and frequency >= 19000):
    #     bitArray[nextbit] = 0
    #     nextbit += 1
    #     print(0)
    # elif(frequency >= 20000):
    #     bitArray[nextbit] = 1
    #     nextbit += 1
    i += 1

for x in bitArray:
    if(x != 255):
        print(x)
decodedString = ""

