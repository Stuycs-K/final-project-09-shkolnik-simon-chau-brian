# This document is required.

How are Audio and Fourier Transforms related: 

Audio consists of many different frequencies which take up a lot of space. 
Short Time Fourier Transform(STFT) help compress this data by those frequency waves into a table of frequency and times

What are Fourier transforms:

In short a Fourier transform takes an oscillating function like a sin wave and converts it into a frequency table which tells us which frequencies were orignally in the function. The problem with this is that it only gives us one snapshot meaning that we lose out on infomation about when.

How do we fix this?

To solve this problem we just break up our function, or in this case audio in many smaller chunks and perform a Fourier transform on each part. With this Short Time Fourier Transform (STFT) we can see which frequencies were present at which time. 

Computers use this to compress a very big wav file into a compartively small mp3 file by turning the audio into a table. Using an inverse function of the STFT we can transform this table to playing the frequencies that occur at a certain time.

Fourier to encode Audio:

By converting audio into a fourier series through a transform we can get a 2d array of times and frequencies. 
Using the table we can then encode the infomation into the highest frequencies and then convert it back into frequencies
The resulting frequencies will contain both the original audio along with the infomation we want to encode in inaudible frequencies.

How we encoded the Audio:


How we decoded the Audio:


