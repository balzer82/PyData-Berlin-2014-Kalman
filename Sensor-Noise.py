# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# A brief introduction to sensor noise

# <markdowncell>

# PyData Berlin 2014

# <codecell>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.html.widgets import interact
import matplotlib.mlab as mlab
import seaborn as sb
#sb.set()  # Reset Style
sb.set(style="white", palette="muted")
sb.set_context("talk")

# <codecell>

%matplotlib inline

# <headingcell level=3>

# All right, let's look at some real sensor data

# <markdowncell>

# Read some measurements in, which are collected with [Tinkerforge IMU](http://www.tinkerforge.com/en/doc/Hardware/Bricks/IMU_Brick.html) and [GPS](http://www.tinkerforge.com/en/doc/Hardware/Bricklets/GPS.html#gps-bricklet) sensors, which layed flat on the ground, without moving in any direction (static measurement).

# <codecell>

df = pd.read_csv('2014-06-27-001-Data.csv')

# <codecell>

# Convert Epoch Millis to Timestamp
# http://pandas.pydata.org/pandas-docs/dev/timeseries.html#epoch-timestamps
df.index = pd.to_datetime(df['millis'], unit='ms')

# <headingcell level=2>

# Acceleration

# <codecell>

accelerations = df[['ax','ay']].dropna()

# <codecell>

accelerations.plot();

# <headingcell level=3>

# Let's try to fit a distribution

# <codecell>

import scipy.stats as stats
from IPython.html.widgets import interact
dists = ['Normal', 'Rayleigh', 'Weibull']

# <codecell>

@interact
def plot_sb_dist(column=accelerations.columns.tolist(), dist=dists):
    plt.figure(figsize=(10, 6))
    dist_map = {
        'Rayleigh': stats.rayleigh,
        'Weibull': stats.exponweib,
        'Normal': stats.norm,
    }
    sb.distplot(accelerations[column], fit=dist_map[dist])
    plt.savefig("ax_dist.png", dpi=72, bbox_inches='tight')

# <headingcell level=3>

# The Normal Distribution fits it perfectly!

# <codecell>

accelerations.describe()

# <markdowncell>

# One can use `mean` and `std` to describe, what's going on.

# <headingcell level=2>

# GPS Measurement

# <markdowncell>

# GPS measurements are in decimal degrees `DD.dddddd`

# <codecell>

gps = pd.DataFrame()

# <markdowncell>

# Convert decimal degress approximately to meters

# <codecell>

arcLon = 2*np.pi*6378.0/360.0
arcLat = arcLon * np.cos(df.longitude*np.pi/180.0)

gps['LonM'] = df.longitude * arcLon * 1000.0
gps['LatM'] = df.latitude * arcLat * 1000.0

# <codecell>

sb.jointplot(gps.LonM, gps.LatM, kind='kde', \
             xlim=(gps.LonM.min()-1, gps.LonM.max()+1), \
             ylim=(gps.LatM.min()-1, gps.LatM.max()+1), \
             size=10, space=1)
plt.savefig('gps_dist.png', dpi=150)

# <markdowncell>

# Thanks Rob Story for the code in your [PyData Silicon Valley 2014 talk](https://www.youtube.com/watch?v=kmy-sfm3cC8)!

# <codecell>

@interact
def plot_sb_dist(column=gps.columns.tolist(), dist=dists):
    plt.figure(figsize=(10, 6))
    dist_map = {
        'Rayleigh': stats.rayleigh,
        'Weibull': stats.exponweib,
        'Normal': stats.norm,
    }
    sb.distplot(gps[column], fit=dist_map[dist])

# <headingcell level=3>

# Even if it's not perfect, it matches the sensor readings pretty well.

# <codecell>

gps.describe()

# <markdowncell>

# One can use `mean` and `std` to describe, what's going on.

# <headingcell level=1>

# The Normal Distribution / Gauss-Distribution

# <markdowncell>

# $f(x, \mu, \sigma) = \large \frac{1}{\sigma\sqrt{2\pi}} \ e^{\Large -\frac{(x-\mu)^2}{2\sigma^2} } \\$ with $\mu$ as mean and $\sigma^2$ as variance ($\sigma$ is the standard deviation).

# <codecell>

def pltnormpdf(mean, variance):
    plt.figure(figsize=(8,5))
    plt.plot(x,mlab.normpdf(x, mean, variance))
    plt.ylim(0,1)

# <codecell>

x = np.linspace(-10,10,500)
interact(pltnormpdf, mean=(-5,5,0.5), variance=(0.1,10,0.1));

# <headingcell level=1>

# Conclusion

# <markdowncell>

# With the help of statistical parameters, it is possible to describe a sensor reading and it's noise.
# A lot of sensors can be described be the assumption:
# 
# [`real value`] + [`white`, `gaussian` noise]
# 
# so one can use the Kalman filter! Even it is not a perfect normal distribution, the Kalman Filter is the best estimator of the `real value`. The Kalman Filter does not work, if the sensor reading is `multimodal` (two or more peaks).

