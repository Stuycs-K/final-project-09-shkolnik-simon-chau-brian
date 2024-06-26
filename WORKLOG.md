# Work Log

## Simon Shkolnik

### 5/22/2024

Implemented audio reading & basic spectrogram

### 5/23/2024

Worked on basic encoding

### 5/24/2024

Added audio encoding, cleaned up main.py, should be ready to start working on decoding

### 5/28/2024

Rewrote scipy STFT because it had some weird behavior where it would blend in adjacent chunks

### 5/29/2024

Fixed decode!!!, helped Brian with phase encoding, removed audio files from git repo

### 5/30/2024 and 5/31/2024

Created debug script and made files command line programs

### 6/3/2024

Made automatic length detection for frequency encode, started working on start sequence

### 6/5/2024

Started working on skipping algorithm

### 6/7/2024

Continued working on skipping algorithm


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

### 5/27/2024

Spent time researching and then creating phase encoding audio stegnography.

### 5/27/2024

Spent time setting up phase decode and then fixed a few bugs in phase encoder.

### 5/29/2024

Was not sure if phase encoder was working so just spent most trying to figure it out. Eventually scraped phaseDecoder to make a decodeer similar to Simon's decoder

### 5/30/2024

Remade phase encoder and then created phase decoder using arcsin. Going to attempt to use fourier transform later.

### 5/31/2024

Finished phase decoder with help from Simon and improved our presentation

### 6/1/2024

Continued to work on the presentation as well as working on making the encoding on the phaseEncode impossible to hear.

### 6/2/2024

Tried to work on the phase encoding but failed and then just worked on the presentation

### 6/3/2024

Finished up phase encoding and then worked on the presentation. Also, spent time making sure the presentation was big enough that it filled the time we needed by doing multiple pratice runs of the presentation.  

### 6/4/2024

Added and adjusted Simon's code that checks for number of bytes into phase decoder and worked more on the presentation.

### 6/5/2024

Reviving my old version of phase encoder and decoder to see if it works.

### 6/6/2024

I revived my old version but it only works with one specific audio clip

### 6/7/2024

Realized it only worked with one audio file but failed to find the problem

### 6/8/2024

Spent more time testing and realized that the error was just a part of using different data types.
Updated presentation to reflect this discovery.

### 6/9/2024

Finished up presentation and tested out using hamming codes but couldn't get it to work

### References used
https://numpy.org/doc/stable/reference/routines.math.html

https://docs.scipy.org/doc/scipy/reference/fft.html

https://numpy.org/doc/stable/reference/generated/numpy.linspace.html

https://medium.com/@achyuta.katta/audio-steganography-using-phase-encoding-d13f100380f2

https://www.youtube.com/watch?v=-Yxj3yfvY-4&t=587s

https://www.youtube.com/watch?v=spUNpyF58BY

https://www.youtube.com/watch?v=ZUi_jdOyxIQ&list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0&index=13

https://svenruppert.com/2024/04/17/audio-steganography-in-more-detail/

https://www.researchgate.net/figure/Echo-data-hiding-adjustable-parameters-16_fig9_257879537

