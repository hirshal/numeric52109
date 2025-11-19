###
## simple_package - Module statistics.py
## Basic statistics calculations
###

## Here I need functions to take in data and do the
## following:
##
## 1) Calculate the mean, median, and standard deviation. 
##
## 2) Display the result with a clear and pretty print 
##    statement.
##
## 3) Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4) Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5) Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.
##

import numpy as np


def find_mean(data):
    """Calculate the mean of the data."""
    
    # Check if input is a list, convert to numpy array if so
    try:
        if isinstance(data, list):
            data = np.array(data)
        elif not isinstance(data, np.ndarray):
            raise TypeError("Input data must be a list or numpy array.")

        mean_value = np.mean(data)
        print(f"The mean of the data is: {mean_value:.3f}")
        return mean_value
    except NameError:
        print("Error: numpy is not installed. Please install numpy to use this function.")
        return None


def find_median(data):
    """Calculate the median of the data."""

    # Check if input is a list, convert to numpy array if so
    try:
        if isinstance(data, list):
            data = np.array(data)
        elif not isinstance(data, np.ndarray):
            raise TypeError("Input data must be a list or numpy array.")

        median_value = np.median(data)
        print(f"The median of the data is: {median_value:.3f}")
        return median_value
    except NameError:
        print("Error: numpy is not installed. Please install numpy to use this function.")
        return None

def find_std(data):
    """Calculate the standard deviation of the data."""

    # Check if input is a list, convert to numpy array if so
    try:
        if isinstance(data, list):
            data = np.array(data)
        elif not isinstance(data, np.ndarray):
            raise TypeError("Input data must be a list or numpy array.")

        std_value = np.std(data)
        print(f"The standard deviation of the data is: {std_value:.3f}")
        return std_value
    except NameError:
        print("Error: numpy is not installed. Please install numpy to use this function.")
        return None

x = [1, 2, 3, 4, 5]
find_mean(x)
find_median(x)
find_std(x)