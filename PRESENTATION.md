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

We used two methods to encode audio, adding an inaudible frequency and performing a phase shift. With an inaudible frequency, we chose two high inaudible frequencies to use to represents 1s and 0s. Then, we converted the text we wanted to hide into bytes and then encode the bytes into audio for a certain timeframe. For exmaple, 1s became a frequency of 20000 and a small segment of the audio was encoded to have an additional frequency of 20000 hertz. This was repeated until the audio was all encoded. With a phase shift, the 1s and 0s become phase shifts that change the sign wave of a frequency. Similar to inaudible frequencies, the audio then has a phase shift of pi/2 for 0s and -pi/2 for 1s. By applying then applying the phase shift since audio is a sin wave, the audio will experience minimum change.

How we decoded the Audio:

To decode the audio we used fourier transforms. Using a short time fourier transforms, we can get all the times where our artifically added frequencies were found. Then, by checking and comparing the times of both, we can construct a bit array of 1s and 0s and convert it back to ASCII to get our hidden string. With phase shifts, instead of checking the frequencies the angle of the fourier transform can be used to find the phase shifts. The reason a fourier series can have an angle is that the fourier series is a set of complex numbers. By using the real and imaginary part, the fourier series can have an angle for each value. The angle is also slightly shifted from the pi/2 and -pi/2 values so we apply a correcting shift and then by seeing the phases shifts we can get the 1s and 0s.
