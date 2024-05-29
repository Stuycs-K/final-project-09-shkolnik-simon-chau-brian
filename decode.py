import numpy as np
from scipy.signal import stft
from scipy.signal import istft
import matplotlib.pyplot as plt
from utils import read_audio, get_stft

NUM_BYTES = 23 #todo: calculate from audio
signal, sampling_rate = read_audio("modified_sample_input.wav")

f, t, Zxx = get_stft(signal, sampling_rate)

FREQ_1 = 20000
FREQ_0 = 19000
FREQ_SPREAD = 50

oneindex = [
    np.argmin(np.abs(f - (FREQ_1 - FREQ_SPREAD))),
    np.argmin(np.abs(f - (FREQ_1 + FREQ_SPREAD)))
]
zeroindex = [
    np.argmin(np.abs(f - (FREQ_0 - FREQ_SPREAD))),
    np.argmin(np.abs(f - (FREQ_0 + FREQ_SPREAD)))
]

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

bitArray = np.where(
    np.sum(
        Zxx[oneindex[0] : oneindex[1], :NUM_BYTES * 8 + 1],
        axis=0
    ) > np.sum(
        Zxx[zeroindex[0] : zeroindex[1], :NUM_BYTES * 8 + 1],
        axis=0
    ),
    1, 0
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