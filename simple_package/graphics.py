def plot_histogram(data, bins=10):
    """Plot a histogram of the data with mean and median marked."""
    try:
        import numpy as np
        import matplotlib.pyplot as plt
    except ImportError as e:
        print("Error: Required packages are not installed. Please install numpy and matplotlib to use this function.")
        return

    # Check if input is a list, convert to numpy array if so
    if isinstance(data, list):
        data = np.array(data)
    elif not isinstance(data, np.ndarray):
        raise TypeError("Input data must be a list or numpy array.")

    mean_value = np.mean(data)
    median_value = np.median(data)

    plt.hist(data, bins=bins, alpha=0.3, color='blue', edgecolor='black')
    plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_value:.2f}')
    plt.axvline(median_value, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_value:.2f}')
    plt.title('Histogram of Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
    return None

