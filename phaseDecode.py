import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import audiofile
from utils import read_audio, string_to_bin, get_stft, NPERSEG, NFFT
import sys

AUDIO_TO_DECODE =  sys.argv[1]

NUM_BYTES = 21 #todo: calculate from audio
signal, sampling_rate = read_audio(AUDIO_TO_DECODE)
bitArray = np.empty(NUM_BYTES * 8)
f, t, Zxx = get_stft(signal, sampling_rate)
FREQ_1 = 1500
index = np.argmin(np.abs(f - FREQ_1)),

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
frequency = np.angle(Zxx[index]) + .964 #To Fix Offset
print(frequency.tolist()[:100])
bitArray = np.where(
    frequency > 0
    ,0,1
)
print(bitArray)

decodedString = ""

for i in range(NUM_BYTES):
    current_byte = 0

    for j in range(8):
        if bitArray[8 * i + (7 - j)]:
            current_byte += 2 ** j

    decodedString += chr(current_byte)

print(decodedString)
