# Reverse-Sound-Python

This is a simple Python script that reverses .wav sound file using SoX command line Utility.

For the sake of understanding sound can be viewed as a continuous function 
of time from the positive real numbers (time) to the interval [-1.0, 1.0]
(amplitude). Since a computer can't "hold" a function defined on the reals, 
we have to approximate the function. We do this by measuring (or "sampling") 
the sound several thousand times per second

 ![Alt text](https://github.com/gdhuper/Reverse-Sound-Python/blob/master/reverse-sound.JPG "Optional title")


To use this script:

1. Download Sox from: https://sourceforge.net/projects/sox/files/sox/. Make sure to add SoX to your classpath.
2. Clone my repository on your device: 
	git clone https://github.com/gdhuper/Reverse-Sound-Python.git

3. In the repository there is a sample secret.wav file (reversed sound file). On your terminal or command line do:
	
	sox secret.wav secret.dat

	This will convert .wav file to .dat file
4. Now on your terminal run: 
	python Reverse.py --ifile secret.dat --ofile secret-revealed.dat

5. The last step will get you a reversed .dat file named secret-revealed.dat

6. Now again run:
	sox secret-revealed.dat secret-revealed.wav

7. Play the wav file on your favorite music player. 

