# This document is required.

How are Audio and Fourier Transforms related: 

Audio consists of many different frequencies which take up a lot of space. 
Fast Fourier Transform(FFT) help compress this data by those frequency waves into a table of frequency and times
FFT converts those waves into peaks and valleys where the peaks represents the frequency in at a given time
Similarly, the computer can transform this table by playing the frequencies that occur at a certain time

Fourier to encode Audio:

By converting audio into a fourier series through a transform we can get a 2d array of times and frequencies. 
Using the table we can then encode the infomation into the highest frequencies and then convert it back into frequencies
The resulting frequencies will contain both the original audio along with the infomation we want to encode in inaudible frequencies.


