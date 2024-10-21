"""
Starter code for Project 2
BIOEN/EE 460/560, CSE 490N
Adapted by TA Matthew J. Bryan for Autumn 2023, from reference code
 written by Student Iman Tanumihardja and TA Courtnie Paschall,
 Autumn 2022.

NOTES:
 * You will need numpy, scipy, and matplotlib installed for the following code
   to work.
 * You are not required to use this starter code, but it will bootstrap your efforts.
 * Since the are many package managers and Python environments available, and
   there are many great walkthroughs online for their use, we will not provide much
   instruction here for managing the dependencies.
 * You must refrain from using dependencies not listed here so the grader doesn't
   need to work to match your environment.
"""
import numpy as np

# For loadmat, which imports data from Matlab files and stores them in memory as
#  scipy tensors.
import scipy.io as sio

# For graphing
import matplotlib.pyplot as plt

# For filtering
from scipy import signal
from scipy.signal import butter, filtfilt

# Update data_path to point to your downloaded data
data_path = "ECoGData_AvailabletoStudents.mat"
data = sio.loadmat(data_path)

# Create some references to the data so the user doesn't need to copy/paste this indexing elsewhere.
# This first one appears as data.Signal in the Matlab structure. e.g. data_ecog[0] is
#  data.Signal{1, 1}
data_ecog = data["data"]["Signal"][0][0][0]
stim_times = data["data"]["StimTimes"][0][0][0]
Fs = data["data"]["SamplingFreq"][0][0][0][0]

print("Signal: " + str(data_ecog.shape))  # Three stim conditions
print("Stim Times: " + str(stim_times.shape))  # in seconds!
print("SFreq: " + str(Fs))  # 24414 Hz


# For bandpass filtering consider these functions, but check your work!
#  https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html
#  https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.filtfilt.html

# TODO: the rest!
