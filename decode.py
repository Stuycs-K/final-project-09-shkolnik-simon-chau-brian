import numpy as np
from scipy.signal import stft
from scipy.signal import istft
import matplotlib.pyplot as plt
import audiofile

signal, sampling_rate = audiofile.read("sample_input.mp3")
# print(f"Sampling rate: {sampling_rate}hz")
signal = sum(signal)
bitArray = [255] * 1000
i = 0
while(len(signal) > 20):
    portion = signal[sampling_rate * 0 : sampling_rate * 20]
    signal = signal[sampling_rate * 20 : sampling_rate * 40]
    f, t, Zxx = stft(portion, fs = sampling_rate, nperseg = 4096, noverlap = 0, nfft = 8192)
    Zxx = np.absolute(Zxx)
    nextbit = 0
    
    for j in Zxx: 
        f_index = np.argmin(np.abs(j - 20000))
        if(Zxx[f_index] == 19000):
            bitArray[nextbit] = 0
        if(Zxx[f_index == 20000]):
            bitArray[nextbit] = 1
        nextbit += 1
        
    # Code with minimal libraries 
    # for j in Zxx:
    #     smallestDifference = 10000
    #     frequency = 0
    #     for x in j:
    #         if(x > 8000):
    #             if (x - 8000) < closestFrequency:
    #                 smallestDifference = abs(8000 - j[0])
    #                 frequency = x
    #         if(frequency != 0):
    #             byteArray[nextbyte] = frequency - 8000
    #             nextbyte += 1


        
    
    i += 1
