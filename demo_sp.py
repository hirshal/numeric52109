import numpy as np
import math
import simple_package.operations as sp
import simple_package.statistics as stats
import simple_package.graphics as gfx

x = np.random.normal(loc=0.0, scale=1.0, size=1000)
stats.find_stats(x)
gfx.plot_histogram(x, bins=30)

sp.calculator()
