import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time

# Initialize serial connection to Arduino
ser = serial.Serial('COM12', 9600)

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Initialize lists to store data
xdata, ydata = [], []

# Create a line plot for the animation
ln, = plt.plot([], [], 'r-')

# Number of samples to keep in memory
samples = 20

# Initialize variables for previous mean and variance
prev_mean, prev_variance = None, None

# Animation update function
def update(frame):
    global prev_mean, prev_variance

    # Read incoming data from Arduino
    while ser.inWaiting():
        line = ser.readline().decode('utf-8').strip()
        try:
            distance = float(line)

            # Keep a rolling window of samples
            if len(ydata) >= samples:
                ydata.pop(0)
                xdata.pop(0)

            xdata.append(len(xdata))
            ydata.append(distance)

        except ValueError:
            pass

    # Update the plot
    ax.clear()
    ax.plot(xdata, ydata, 'r-')
    ax.set_title("Distance over Time")
    ax.set_xlabel("Sample Number")
    ax.set_ylabel("Distance (cm)")

    if len(ydata) > 0:
        mean = np.mean(ydata)
        variance = np.var(ydata)

        # Check for significant change in mean or variance
        if prev_mean is not None and prev_variance is not None:
            mean_change = np.abs(mean - prev_mean) > threshold_mean
            variance_change = np.abs(variance - prev_variance) > threshold_variance

            # If there's a change, print "Ball Detected"
            if mean_change or variance_change:
                print("Ball Detected")

        # Update previous values
        prev_mean, prev_variance = mean, variance

        ax.axhline(y=mean, color='g', linestyle='-', label=f'Mean: {mean:.2f} cm')
        ax.axhline(y=mean + np.sqrt(variance), color='b', linestyle='--',
                   label=f'Mean + Std Dev: {mean + np.sqrt(variance):.2f} cm')
        ax.axhline(y=mean - np.sqrt(variance), color='b', linestyle='--',
                   label=f'Mean - Std Dev: {mean - np.sqrt(variance):.2f} cm')
        # ax.axhline(y=variance, color='p', linestyle='dotted', label=f'Variance: {variance:.2f} cm')
        ax.legend()

    else:
        # If no data, print "Waiting for ball"
        print("Waiting for ball")

    return ln,

# Set threshold values for mean and variance changes
threshold_mean = 2.0
threshold_variance = 5.0

# Create animation
ani = FuncAnimation(fig, update, interval=50)

# Show the plot
plt.show()
