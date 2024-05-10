Real-Time Distance Monitoring with Arduino

Introduction
This repository contains Python code for real-time distance monitoring using an ultrasonic sensor connected to an Arduino board. The distance data is sent to the computer via serial communication and plotted dynamically using Matplotlib. The program also detects significant changes in mean and variance of the distance readings, indicating the presence of an object (e.g., a ball).

Requirements
Python 3
matplotlib
numpy
pySerial

You can install the required packages using pip:
pip install matplotlib numpy pyserial


Setup
Connect an ultrasonic sensor to the Arduino board. Ensure that the Arduino is connected to the computer via USB.
Upload the Arduino sketch provided in the Arduino_Sketch folder to your Arduino board.
Note the serial port to which the Arduino is connected (e.g., COM12).
Adjust the COM_PORT variable in the Python script to match your Arduino's serial port.


Observe the real-time plot of distance readings on the graph.
Significant changes in mean or variance will trigger a "Ball Detected" message in the console.
Description
The Python script establishes a serial connection with the Arduino board.
It continuously reads distance data from the Arduino and plots it dynamically using Matplotlib.
The script monitors changes in mean and variance of the distance readings to detect the presence of an object (e.g., a ball).
A rolling window of distance samples is maintained to smooth out noise in the sensor readings.
The program displays statistical information such as mean, standard deviation, and variance on the plot.
A threshold is set for mean and variance changes, beyond which a "Ball Detected" message is printed.
