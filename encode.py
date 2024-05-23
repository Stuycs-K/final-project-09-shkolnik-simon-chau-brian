import numpy as np
from scipy.signal import stft
import matplotlib.pyplot as plt
import audiofile

# signal, sampling_rate = audiofile.read("sample_input.mp3")
# print(f"Sampling rate: {sampling_rate}hz")

file = open("testfile.txt", "r")
byteArray = bytearray(file.read(), "utf-8")
for x in byteArray:
    print(int(x))