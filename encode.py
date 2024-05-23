import numpy as np
from scipy.signal import stft
import matplotlib.pyplot as plt
import audiofile

signal, sampling_rate = audiofile.read("sample_input.mp3")
# print(f"Sampling rate: {sampling_rate}hz")
signal = sum(signal)

file = open("testfile.txt", "r")
byteArray = bytearray(file.read(), "utf-8")

i = 0
portion = signal[sampling_rate * 0 : sampling_rate * 20]
while(i * 20 < len(byteArray)):
    f, t, Zxx = stft(portion, fs = sampling_rate, nperseg = 4096, noverlap = 0, nfft = 8192)
    Zxx = np.absolute(Zxx)
    nextbyte = 0
    for j in Zxx:
        if(nextbyte < len(byteArray)):
            j[216] += 25000 + int(byteArray[nextbyte])
        nextbyte += 1
    for x in Zxx:
        print(x[216])
    i += 1  
