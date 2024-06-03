import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import audiofile
from utils import read_audio, string_to_bin, get_stft, NPERSEG, NFFT
import sys

AUDIO_TO_DECODE =  sys.argv[1]

NUM_BYTES = 23 #todo: calculate from audio
signal, sampling_rate = read_audio(AUDIO_TO_DECODE)
bitArray = np.empty(NUM_BYTES * 8)
f, t, Zxx = get_stft(signal, sampling_rate)
FREQ_1 = 16000
index = np.argmin(np.abs(f - FREQ_1)),

frequency = np.angle(Zxx[index]) #To Fix Offset
print(frequency.tolist()[:100])
bitArray = np.where(
    frequency < 0
    ,0,1
)

decodedString = ""

for i in range(NUM_BYTES):
    current_byte = 0

    for j in range(8):
        if bitArray[8 * i + (7 - j)]:
            current_byte += 2 ** j

    decodedString += chr(current_byte)

print(decodedString)
