# Work Log

## Simon Shkolnik

### 5/22/2024

Implemented audio reading & basic spectrogram

### 5/24/2024

Added audio encoding, cleaned up main.py, should be ready to start working on decoding

### 5/28/2024

Rewrote scipy STFT because it had some weird behavior where it would blend in adjacent chunks

## GROUP MEMBER 2

### 5/22/2024

Started taking notes on research of fourier transformations with audio stegnoraphy in presentation and worked on README

### 5/23/2024

Started work on encoding text into audio by transforming string into byte array and using stft to split the audio

### 5/24/2024

Transformed my encoder into a decoder. Messed around with finding frequencies not using a numpy library. Then used a numpy library to then get the chosen frequencies that represent 0s(19000), and 1s(20000)

### 5/25/2024

Continued messing with Zxx array and figured out more about it. Was able to get bits although they seem to be in the wrong order so still working on understanding the array and on how to get the decoder to work.

### 5/26/2024

Updated the presentation to add more of my research and add more clarification on the overview to the Readme