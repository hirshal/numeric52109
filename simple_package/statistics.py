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


def find_stats(data):
    """Calculate the mean, median and standard deviation of the data."""
    
    # Check if input is a list, convert to numpy array if so
    try:
        import numpy as np
    except ImportError:
        print("Error: numpy is not installed. Please install numpy to use this function.")

    try:
        if isinstance(data, list):
            data = np.array(data)
        elif not isinstance(data, np.ndarray):
            raise TypeError("Input data must be a list or numpy array.")

        mean_value = np.mean(data)
        median_value = np.median(data)
        std_value = np.std(data)
        print(f"The mean of the data is: {mean_value:.3f}")
        print(f"The median of the data is: {median_value:.3f}")
        print(f"The standard deviation of the data is: {std_value:.3f}")
        return mean_value, median_value, std_value
    
    except NameError:
        print("Error: Unable to compute mean due to invalid data.")
    except TypeError as te:
        print(f"Type Error: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

