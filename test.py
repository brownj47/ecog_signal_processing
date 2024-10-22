import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate time values
t = np.linspace(0, 2, 500)  # Time from 0 to 2 seconds, 500 samples

# Step 2: Create a signal (for example, a sine wave)
frequency = 5  # 5 Hz
signal = np.sin(2 * np.pi * frequency * t)

# Step 3: Plot the signal over time
plt.plot(t, signal)

# Step 4: Add labels and title
plt.title('Sine Wave Signal Over Time')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Optional: Add grid and show the plot
plt.grid(True)
plt.show()
