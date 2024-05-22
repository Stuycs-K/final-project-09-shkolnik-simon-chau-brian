import numpy as np
from scipy.signal import stft
import matplotlib.pyplot as plt
import audiofile

signal, sampling_rate = audiofile.read("sample_input.mp3")
print(f"Sampling rate: {sampling_rate}hz")

signal = sum(signal) #combine all channels in audio file
print(f"Audio length: {len(signal) / sampling_rate:.2f}s, taking segment from 20s-40s")
signal = signal[sampling_rate * 20 : sampling_rate * 40] #take only section of audio

#f, t, Zxx = stft(signal, fs = sampling_rate, nperseg = 4096, noverlap = 4096 - 128, nfft = 8192)
f, t, Zxx = stft(signal, fs = sampling_rate, nperseg = 4096, noverlap = 0, nfft = 8192)
#Zxx = np.transpose(Zxx) #Zxx[frequency][times] -> Zxx[times][frequency]
Zxx = np.absolute(Zxx) #we only care about the magnitude of each frequency, not shift

plt.pcolormesh(t, f, np.abs(Zxx), shading="gouraud")
plt.title("STFT Magnitude")
plt.ylabel("Frequency [Hz]")
plt.xlabel("Time [sec]")
plt.show()