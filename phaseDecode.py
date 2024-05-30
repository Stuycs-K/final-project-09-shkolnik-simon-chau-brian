import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import audiofile
from utils import read_audio, string_to_bin, get_stft, NPERSEG, NFFT
NUM_BYTES = 21 #todo: calculate from audio
signal, sampling_rate = read_audio("modified_sample_input.wav")
signal2, sampling_rate2 = read_audio("sample_input.wav")
bitArray = np.empty(NUM_BYTES * 8)
# f, t, Zxx = get_stft(signal, sampling_rate)
# f2, t2, Zxx2 = get_stft(signal2, sampling_rate2)

# FREQ_1 = 1500
# FREQ_SPREAD = 50
# index = [
#     np.argmin(np.abs(f - (FREQ_1 - FREQ_SPREAD))),
#     np.argmin(np.abs(f - (FREQ_1 + FREQ_SPREAD)))
# ]
# zeroindex = [
#     np.argmin(np.abs(f - (FREQ_0 - FREQ_SPREAD))),
#     np.argmin(np.abs(f - (FREQ_0 + FREQ_SPREAD)))
# ]

"""
_, (ax1) = plt.subplots(1, 1)

ax1.pcolorfast(t, f, np.abs(Zxx))
ax1.set_title("Spectrogram (before encoding)")
ax1.set_ylabel("Frequency [Hz]")
ax1.set_xlabel("Time [sec]")

ax1.vlines(t, FREQ_0, FREQ_1, "w")
ax1.hlines(f[oneindex], t[0], t[-1])

plt.show()
"""
# frequency = np.angle(Zxx[index])
# frequency2 = np.angle(Zxx2[index])
# frequency = sum(frequency)
# frequency2 = sum(frequency2)
# print(frequency)
# print(frequency2)

# diff = frequency[0] - frequency2[0]
for i in range(NUM_BYTES * 8):
    test = signal[int((i + .25) * NPERSEG) : int((i + .75) * NPERSEG)]
    original = signal2[int((i + .25) * NPERSEG) : int((i + .75) * NPERSEG)]
    angle = np.arcsin(test-original)
    if(angle[0] > 0):
        bitArray[i] = 0
    else:
        bitArray[i] = 1
print(bitArray)

decodedString = ""

for i in range(NUM_BYTES):
    current_byte = 0

    for j in range(8):
        if bitArray[8 * i + (7 - j)]:
            current_byte += 2 ** j

    decodedString += chr(current_byte)

print(decodedString)
