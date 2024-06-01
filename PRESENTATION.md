# This document is required.

## How are Audio and Fourier Transforms related: 

Audio consists of many different frequencies which take up a lot of space. 
Short Time Fourier Transform(STFT) help compress this data by those frequency waves into a table of frequency and times

## What are Fourier transforms:

In short a Fourier transform takes an oscillating function like a sin wave and converts it into a frequency table which tells us which frequencies were orignally in the function. The problem with this is that it only gives us one snapshot meaning that we lose out on infomation about when.

![alt text](https://github.com/Stuycs-K/final-project-09-shkolnik-simon-chau-brian/blob/main/Images/FFT-Time-Frequency-View-540.png "Visual Example of Fourier Transform")


## How do we fix this?

To solve this problem we just break up our function, or in this case audio in many smaller chunks and perform a Fourier transform on each part. With this Short Time Fourier Transform (STFT) we can see which frequencies were present at which time. 

Computers use this to compress a very big wav file into a compartively small mp3 file by turning the audio into a table. Using an inverse function of the STFT we can transform this table to playing the frequencies that occur at a certain time.

## Some other types of Audio Steganography

### LSB Algorithim:

Using the LSB algorithim is just like what we did before with image steganography. By changing the last signficant bit of chunks of audio we can have the infomation stored in the audio without it making a significant change to it.

### Echo hiding

The data is embed into the audio by creating an echo of the host signal. This echo is a resonace which is then added on top of this host audio which allows it to blend into the audio and makes it impossible for human ear to hear.

## Encoding Audio Using Inaudible Frequencies

We used two methods to encode audio, adding an inaudible frequency and performing a phase shift. With an inaudible frequency, we chose two high inaudible frequencies to use to represents 1s and 0s. Then, we converted the text we wanted to hide into bytes and then encode the bytes into audio for a certain timeframe. For exmaple, 1s became a frequency of 20000 and a small segment of the audio was encoded to have an additional frequency of 20000 hertz. <br>

To decode the audio we used fourier transforms. Using a short time fourier transforms, we can get all the times where our artifically added frequencies were found. Then, by checking and comparing the times of both, we can construct a bit array of 1s and 0s and convert it back to ASCII to get our hidden string. <br>

## Encoding Audio using Phase Shifts:

To decode the audio we used fourier transforms. Using a short time fourier transforms, we can get all the times where our artifically added frequencies were found. Then, by checking and comparing the times of both, we can construct a bit array of 1s and 0s and convert it back to ASCII to get our hidden string. With phase shifts, instead of checking the frequencies the angle of the fourier transform can be used to find the phase shifts. The reason a fourier series can have an angle is that the fourier series is a set of complex numbers. By using the real and imaginary part, the fourier series can have an angle for each value. The angle is also slightly shifted from the pi/2 and -pi/2 values so we apply a correcting shift and then by seeing the phases shifts we can get the 1s and 0s.<br>

With phase shifts, instead of checking the frequencies the angle of the fourier transform can be used to find the phase shifts. The reason a fourier series can have an angle is that the fourier series is a set of complex numbers. By using the real and imaginary part, the fourier series can have an angle for each value. The angle is also slightly shifted from the pi/2 and -pi/2 values so we apply a correcting shift and then by seeing the phases shifts we can get the 1s and 0s. <br>


