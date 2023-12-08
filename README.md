# Time Synchronization Script

## Overview
This repository contains a simple solution to address the issue of time synchronization when switching between Windows and Linux on the same computer. The problem arises due to differences in how the two operating systems handle time, resulting in a 3-hour time difference when switching from Linux to Windows.

To automate the clock synchronization process, a Python script has been developed using the **pyautogui** library. The script can be compiled into an executable (.exe) using **pyInstaller** and set to run automatically upon system startup.

## Prerequisites
- **Python**
- **pyautogui**
- **pyInstaller**
