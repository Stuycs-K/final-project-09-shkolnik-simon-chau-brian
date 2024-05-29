import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import audiofile
from utils import read_audio, string_to_bin, get_stft, NPERSEG, NFFT
import numpy as np

AUDIO_FILE_NAME = "sample_input.wav"
TEXT_FILE_NAME = "testfile.txt"

SECTION = (20, 40)

FREQ_1 = 20000
FREQ_0 = 19000
AMPLITUDE = .2

signal, sampling_rate = read_audio(AUDIO_FILE_NAME)
signal = signal[sampling_rate * SECTION[0] : sampling_rate * SECTION[1]] #take only section of audio
print(f"Sampling rate: {sampling_rate}hz")
print(f"Audio length: {len(signal) / sampling_rate:.2f}s")

_, (ax1, ax2) = plt.subplots(1, 2)

f, t, Zxx = get_stft(signal, sampling_rate)
ax1.pcolorfast(t, f, np.abs(Zxx))
ax1.set_title("Spectrogram (before encoding)")
ax1.set_ylabel("Frequency [Hz]")
ax1.set_xlabel("Time [sec]")
ax1.vlines(t, FREQ_0, FREQ_1, "w")

#encoding
bin_data = string_to_bin(open(TEXT_FILE_NAME, "rb").read())

for i, v in enumerate(bin_data):
  if v == "1":
    freq = FREQ_1
  else:
    freq = FREQ_0

  x = np.linspace(0, freq * 2 * np.pi * (NPERSEG * .5 / sampling_rate), int(NPERSEG * .5))
  x = np.sin(x)

  signal[int((i + .25) * NPERSEG) : int((i + .75) * NPERSEG)] += x * AMPLITUDE
  
  if v == "1":
    ax2.vlines((i * NPERSEG) / sampling_rate, freq + 10, freq + 50, "g")
    ax2.vlines(((i + 1) * NPERSEG) / sampling_rate, freq + 10, freq + 50, "r")
  else:
    ax2.vlines((i * NPERSEG) / sampling_rate, freq - 50, freq - 10, "g")
    ax2.vlines(((i + 1) * NPERSEG) / sampling_rate, freq - 50, freq - 10, "r")

  ax2.hlines(freq, t[i], t[i + 1], "r")

f, t, Zxx = get_stft(signal, sampling_rate)
ax2.pcolorfast(t, f, np.abs(Zxx))
ax2.set_title("Spectrogram (after encoding)")
ax2.set_ylabel("Frequency [Hz]")
ax2.set_xlabel("Time [sec]")
ax2.vlines(t, FREQ_0, FREQ_1, "w")

audiofile.write("modified_" + AUDIO_FILE_NAME.replace("mp3", "wav"), signal, sampling_rate)

plt.show()