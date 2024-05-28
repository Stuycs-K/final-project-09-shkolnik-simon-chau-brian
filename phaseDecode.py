import numpy as np
from scipy.signal import stft
from scipy.io import wavfile
import matplotlib.pyplot as plt
import audiofile

AUDIO_FILE_NAME = "sample_input.wav"
TEXT_FILE_NAME = "testfile.txt"

SECTION = (20, 40)
NPERSEG = 4096
NFFT = 8192

sampling_rate, signal = wavfile.read(AUDIO_FILE_NAME)
signal = signal.copy()