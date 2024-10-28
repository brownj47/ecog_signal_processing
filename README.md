# Neural Data Signal Processing: Extracting Multi-Unit Activity from ECoG Recordings

This project focuses on extracting multi-unit activity (MUA) from ECoG recordings collected from a non-human primate cortex, with simultaneous optogenetic stimulation. It was developed as part of a class assignment, with the objective to analyze specific stimulation patterns in neural data.

## Table of Contents
- [Project Overview](#project-overview)
- [Assignment Requirements](#assignment-requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Example Output](#example-output)
- [Credits](#credits)

## Project Overview
This project involves filtering, detecting, and plotting neural responses to optogenetic stimulation. The data consists of three different stimulation patterns, each with unique illumination configurations. Using Python and provided libraries, the project processes the ECoG data to visualize MUA for each condition.

## Assignment Requirements
The assignment includes the following tasks:
1. **Filtering**: Use a bandpass filter between 500 Hz and 5000 Hz on each signal to isolate MUA.
2. **Threshold Detection**: Apply a threshold defined as \( T_{hr} = 3 \sigma \), where:
   - \( \sigma \) is calculated as \( \text{median}\left( \frac{| \text{filtered signal} |}{0.6745} \right) \).
   - The signal is rectified to enhance threshold detection.
3. **Raster Plot**: Create a raster plot showing the timing of each detected MUA from 0.5 seconds before to 0.5 seconds after stimulation for all 50 trials.
4. **Firing Rate Calculation**: Calculate and plot the average firing rate over time for each trial across the 50 repetitions.

### Data Details
- **Data Structure**: The dataset `ECoGData.mat` includes three signals (`data.Signal`) with different stimulation conditions and a timestamp (`data.StimTimes`) marking the start of each stimulation.
- **Conditions**:
  - Signal 1: Constant illumination for 1 second.
  - Signal 2: 3 Hz sine wave illumination for 1 second.
  - Signal 3: 10 Hz sine wave illumination for 1 second.
- Each signal has 50 trials.

## Setup
1. **Requirements**: Ensure Python (3.6+) and Jupyter Notebook are installed.
2. **Dependencies**: Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. **Data File**: Place `ECoGData.mat` in the project directory.

## Usage
1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook process_signal.ipynb
   ```
2. Follow each cell to perform filtering, threshold detection, and generate raster plots and firing rate analyses.

## Example Output
- **Raster Plot**: Shows MUA timing per trial.
- **Firing Rate Plot**: Average firing rate over time across all trials for each stimulation pattern.

## Credits
Starter code adapted by TA Matthew J. Bryan for Autumn 2023, from reference code written by Student Iman Tanumihardja and TA Courtnie Paschall, Autumn 2022. BIOEN/EE 460/560, CSE 490N.