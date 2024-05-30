import numpy as np
from scipy.signal import stft
from scipy.io import wavfile
import matplotlib.pyplot as plt
import audiofile
from utils import string_to_bin, get_stft, read_audio

AUDIO_FILE_NAME = "sample_input.wav"
TEXT_FILE_NAME = "testfile.txt"

SECTION = (20, 40)
NPERSEG = 4096
NFFT = 8192

FREQ_0 = 1500
string = open(TEXT_FILE_NAME, "rb").read()
binary = string_to_bin(string)
stringlen = len(string) * 8
phaseShifts = np.empty(stringlen)
index = 0
for i, v in enumerate(binary):
    if v == '0': phaseShifts[index] = np.pi/2
    elif v == '1': phaseShifts[index] = -np.pi/2
    index += 1

signal, sampling_rate = read_audio(AUDIO_FILE_NAME)
f, t, Zxx = get_stft(signal, sampling_rate)
index = np.argmin(np.abs(f - FREQ_0))
magnitudes = np.abs(Zxx[FREQ_0])
phases = np.angle(Zxx[FREQ_0])
phaseDiff = np.diff(phases, axis=0)
print(magnitudes)
print(phases)

for x in range(len(phaseShifts)):
    phases[x] += phaseShifts[x]
# phases[0, halfChunk - stringlen: halfChunk] = phaseShifts
# phases[0, halfChunk + 1: halfChunk + 1 + stringlen] = -phaseShifts[::-1]

print(phases)

# chunks = (magnitudes * np.exp(1j * phases))
# chunks = np.fft.ifft(chunks).real
# signal[0] = chunks.ravel().astype(np.int16) 
# wavfile.write("modified_" + AUDIO_FILE_NAME, sampling_rate, signal.T)