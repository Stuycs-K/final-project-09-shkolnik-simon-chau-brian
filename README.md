[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ecp4su41)
# THIS DOCUMENT IS REQUIRED
## Group Info
Audio Stegnoraphy LLC
Brian Chau and Simon Shkolnik

## Overview
The project focuses on using Fourier Transforms in audio steganography. We can add hidden data to an audio file by adding signals and extract the hidden data by using fourier transforms and reading the frequency data of the modified file. In this project we have used two different ways of encoding our message: hiding the message as binary data using 2 inaudible frequencies and using one frequency with varying phase shifts.

## Usage
`python <freqEncode.py / phaseEncode.py> <audio> <file with text to encode>`

`python <freqDecode.py / phaseDecode.py> <modified_audio>`

## Presentation
[PRESENTATION.md](PRESENTATION.md)

## Requirements
The library used in this program are:
- **numpy**: vector math
- **audiofile**: audio reading and writing
- **scipy**: signal processing
- **matplotlib**: plotting / visualising

To install requirements: `python -m pip install numpy audiofile scipy matplotlib`
