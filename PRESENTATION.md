# This document is required.

## Audio Steganography
Audio steganography refers to when some data is concealed inside an audio file. With audio steganography, we can hide data allowing us to send the data through public channels securely. 

## What is Audio

Sound is really just air vibrating, which we can hear from our ear detecting variations in pressure. The reason that we're able to hear multiple sounds at the same time is because, like with any kind of wave, we can overlay different sound sources onto eachother. Audio files fundamentally just contain air pressure data sampled many times per second by a microphone, although most real audio files use various types of compression.

## What are Fourier transforms:

In short a Fourier transform takes an oscillating function, which might consist of many sine waves of different frequencies, ampltiudes, and phase shifts added together and converts it into a frequency table which tells us which frequencies were orignally in the function. The frequency table however condenses all of the audio given into one single graph. The problem with this is that it only gives us one snapshot meaning that we don't get infomation about when these frequencies occur in the audio.

![alt text](https://github.com/Stuycs-K/final-project-09-shkolnik-simon-chau-brian/blob/main/Images/FFT-Time-Frequency-View-540.png "Visual Example of Fourier Transform")


## How do we fix this?

To solve this problem we just break up our function, or in this case audio, into many smaller chunks and perform a Fourier transform on each part. With this Short Time Fourier Transform (STFT) we can see which frequencies were present at which time. 
Computers use this to compress a very big wav file into a compartively small mp3 file by turning the audio into a table. Using an inverse function of the STFT we can transform this table to playing the frequencies that occur at a certain time.

## Some other types of Audio Steganography

### LSB Algorithim:

Using the LSB algorithim is just like what we did before with image steganography. By changing the last signficant bit of chunks of audio we can have the infomation stored in the audio without it making a significant change to it. The benefit is the simplicity of this method along with the small, imperceptible change of the audio to the human ear.  

## Encoding Audio Using Inaudible Frequencies

We used two methods to encode audio, adding an inaudible frequency and performing a phase shift. With an inaudible frequency, we chose two high inaudible frequencies to use to represents 1s and 0s. Then, we converted the text we wanted to hide into bytes and then encode the bytes into audio for a certain timeframe. For exmaple, 1s became a frequency of 20000 and a small segment of the audio was encoded to have an additional frequency of 20000 hertz. <br>

To decode the audio we used fourier transforms. Using a short time fourier transforms, we can get all the times where our artifically added frequencies were found. Then, by checking and comparing the times of both, we can construct a bit array of 1s and 0s and convert it back to ASCII to get our hidden string. <br>

### The Problems with Inaudible Frequencies

Inaudible frequencies are easily found on spectrograms and thus an attacker can easily use a program like audacity and just see the encoded messages bytes. As a result, a determined attacker can easily break through this steganography method and find the hidden message.

<img src = "https://github.com/Stuycs-K/final-project-09-shkolnik-simon-chau-brian/blob/main/Images/spectrogramExample.jpg" width="1400" height="1225">

### Syntax:

freqEncode: `python ./freqEncode.py AUDIO_FILE TEXT_FILE` <br>
freqDecode: `python ./freqDecode.py MODIFIED_AUDIO`<br><br> 

## Encoding Audio using Phase Shifts:

Using phase shift, we don't use two inaudible frequncies to represent bits but just use a single frequency. With phase shifts, instead of checking the frequencies the angle of the fourier transform can be used to find the phase shifts. The reason a fourier series can have an angle is that the fourier series is a set of complex numbers. By using the real and imaginary part, the fourier series can have an angle for each value. The angle is also slightly shifted from the pi/2 and -pi/2 values so we apply a correcting shift and then by seeing the phases shifts we can get the 1s and 0s. <br>

![alt text](https://github.com/Stuycs-K/final-project-09-shkolnik-simon-chau-brian/blob/main/Images/phaseShift.jpg "How Phase Shifts Work")

To decode the audio we used fourier transforms. Using a short time fourier transforms, we can get all the times where our artifically added frequencies were found. Then, by checking and comparing the times of both, we can construct a bit array of 1s and 0s and convert it back to ASCII to get our hidden string. With phase shifts, instead of checking the frequencies the angle of the fourier transform can be used to find the phase shifts. The reason a fourier series can have an angle is that the fourier series is a set of complex numbers. By using the real and imaginary part, the fourier series can have an angle for each value. The angle is also slightly shifted from the pi/2 and -pi/2 values so we apply a correcting shift and then by seeing the phases shifts we can get the 1s and 0s.<br>

### The Problems with Phase Shifts

The phase shifts has a similar issue to the two inaudible frequencies methods as it is still easily visible on a spectrogram, though as a single continuous frequency it might not be as obvious that it's hidden data.

### Syntax

phaseEncode: `python ./phaseEncode.py AUDIO_FILE TEXT_FILE`<br>
phaseEncode: `python ./phaseDecode.py MODIFIED_AUDIO`<br>

## Encoding Audio using Phase Shifts(Without inaudible frequencies):

With the original phase shifts, we had to use one inaudible frequency then encode the different phases. Without the inaudible frequency, we need to to do a fourier transform. But, we need chunks of audio to break up and then perform the data analysis on, so first we do that. Next, do a fourier transform on each part. Then, using the array of bits from before, apply the phase shift to the angle of each fourier transform and finally convert it back.<br>

![alt text](https://github.com/Stuycs-K/final-project-09-shkolnik-simon-chau-brian/blob/main/Images/diagram.png "Diagram of phase shift algorithm")

### The problem with this version:
This version uses a fourier transform in the encoding phase. Thus, the conversion from the fourier series back into a wav lead to a lossy conversion and possibly corrupt the data. Also if the nagnitude of the wav file is initially zero, the data will also be lost. As a result, most audio files won't work with the phase shifts algorithm here. 

### Syntax
phaseSpecificDecoder: `python .\phaseSpecificEncoder.py AUDIO_FILE TEXT_FILE`<br>
phaseSpecificEncoder: `python .\phaseSpecificDecoder.py MODIFIED_AUDIO`

## How to detect steganography

Generally you would use a spectrogram as they allow you to visualize the audio waves which makes it exceptionally easy to find any hidden audio. Another thing that can help detect steganography is artifacts of the steganography. Due to the complexity of audio steganography some buzzing or a faint noise can remain which will hint at the presence of a hidden message.<br>
