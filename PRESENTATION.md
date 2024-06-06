# This document is required.

## How are Audio and Fourier Transforms related: 

Audio files contain infomation about all the different frequencies, their amplitudes and other infomation abouut the audio. These audio files logically are extremely big in order to accomadate the data. Short Time Fourier Transform(STFT) help compress this data by those turning the massive frequency waves into an array.

## What are Fourier transforms:

In short a Fourier transform takes an oscillating function like a sin wave and converts it into a frequency table which tells us which frequencies were orignally in the function. The frequency table however condenses all of the audio given into one single graph. The problem with this is that it only gives us one snapshot meaning that we don't get infomation about when these frequencies occur in the audio.

![alt text](https://github.com/Stuycs-K/final-project-09-shkolnik-simon-chau-brian/blob/main/Images/FFT-Time-Frequency-View-540.png "Visual Example of Fourier Transform")


## How do we fix this?

To solve this problem we just break up our function, or in this case audio, into many smaller chunks and perform a Fourier transform on each part. With this Short Time Fourier Transform (STFT) we can see which frequencies were present at which time. 
Computers use this to compress a very big wav file into a compartively small mp3 file by turning the audio into a table. Using an inverse function of the STFT we can transform this table to playing the frequencies that occur at a certain time.

## Some other types of Audio Steganography

### LSB Algorithim:

Using the LSB algorithim is just like what we did before with image steganography. By changing the last signficant bit of chunks of audio we can have the infomation stored in the audio without it making a significant change to it.

### Echo hiding

The data is embed into the audio by creating an echo of the host audio. This echo is a resonace frequency which is then added on top of this host audio.The biggest benefit of echo hiding is that it is hard to detect on a spectrogram, but the audio can be changed by this method. This would cause the audio to sound a bit warped, cluing the listener in that there is something hidden. Therefore this method requires good quality audio.

## Encoding Audio Using Inaudible Frequencies

We used two methods to encode audio, adding an inaudible frequency and performing a phase shift. With an inaudible frequency, we chose two high inaudible frequencies to use to represents 1s and 0s. Then, we converted the text we wanted to hide into bytes and then encode the bytes into audio for a certain timeframe. For exmaple, 1s became a frequency of 20000 and a small segment of the audio was encoded to have an additional frequency of 20000 hertz. <br>

To decode the audio we used fourier transforms. Using a short time fourier transforms, we can get all the times where our artifically added frequencies were found. Then, by checking and comparing the times of both, we can construct a bit array of 1s and 0s and convert it back to ASCII to get our hidden string. <br>

### The Problems with Inaudible Frequencies

Inaudible frequencies are easily found on spectrograms and thus an attacker can easily use a program like audacity and just see the encoded messages bytes. As a result, a determined attacker can easily break through this steganography method and find the hidden message.

![alt text](https://github.com/Stuycs-K/final-project-09-shkolnik-simon-chau-brian/blob/main/Images/spectrogramExample.jpg "Example of how this method looks on a spectrogram")

## Encoding Audio using Phase Shifts:

Using phase shift, we don't use two inaudible frequncies to represent bits but just use a single frequency. With phase shifts, instead of checking the frequencies the angle of the fourier transform can be used to find the phase shifts. The reason a fourier series can have an angle is that the fourier series is a set of complex numbers. By using the real and imaginary part, the fourier series can have an angle for each value. The angle is also slightly shifted from the pi/2 and -pi/2 values so we apply a correcting shift and then by seeing the phases shifts we can get the 1s and 0s. <br>

![alt text](https://github.com/Stuycs-K/final-project-09-shkolnik-simon-chau-brian/blob/main/Images/phaseShift.jpg "How Phase Shifts Work")

To decode the audio we used fourier transforms. Using a short time fourier transforms, we can get all the times where our artifically added frequencies were found. Then, by checking and comparing the times of both, we can construct a bit array of 1s and 0s and convert it back to ASCII to get our hidden string. With phase shifts, instead of checking the frequencies the angle of the fourier transform can be used to find the phase shifts. The reason a fourier series can have an angle is that the fourier series is a set of complex numbers. By using the real and imaginary part, the fourier series can have an angle for each value. The angle is also slightly shifted from the pi/2 and -pi/2 values so we apply a correcting shift and then by seeing the phases shifts we can get the 1s and 0s.<br>

### The Problems with Phase Shifts

The phase shifts has a similar issue to the two inaudible frequencies methods as it is still easily visible on a spectrogram.

## How to use our tool
Our tool is coded in python and contains four files: **freqEncode.py**, **freqDecode.py**, **phaseEncode.py**, **phaseDecode.py**<br>
To use steganography with inaudible frequencies you have to use **freqEncode.py** and **freqDecode.py**<br>
To use steganography with phase shifts, use **phaseEncode.py** and **phaseDecode.py**<br>

### Syntax:

freqEncode:`python .\freqEncode.py AUDIO_FILE TEXT_FILE` <br>
freqDecode:`python .\freqEncode.py AUDIO_FILE`<br><br> 

phaseEncode: `python .\phaseEncode.py AUDIO_FILE TEXT_FILE`<br>
phaseEncode: `python .\phaseDecode.py MODIFIED_AUDIO ORIGINAL_AUDIO`<br>