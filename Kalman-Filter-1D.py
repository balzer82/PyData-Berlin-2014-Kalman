# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Kalman Filter in 1 Dimension (=Distance)

# <codecell>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sb
from scipy import stats
import time
sb.set()  # Reset Style
#sb.set(style="white")
sb.set_context("talk")

# <codecell>

%matplotlib inline

# <codecell>

# Plot the Distributions in this range:
x = np.linspace(-100,100,1000)

# <headingcell level=2>

# In the beginning

# <codecell>

mean0 = 0.0   # e.g. meters or miles
var0  = 20.0

# <codecell>

plt.figure(figsize=(16,5))
plt.plot(x,mlab.normpdf(x, mean0, var0), label='Normal Distribution')
plt.ylim(0, 0.1);
plt.legend(loc='best');
plt.xlabel('Position');

# <markdowncell>

# You are at position `0` and you are pretty unsure (flat normal distribution)

# <headingcell level=2>

# Now we have something, which estimates the moved distance

# <codecell>

meanMove = 25.0  # e.g. meters, calculated from velocity*dt or step counter or wheel encoder ...
varMove  = 10.0   # Estimated or determined with static measurements

# <codecell>

plt.figure(figsize=(16,5))
plt.plot(x,mlab.normpdf(x, meanMove, varMove), label='Normal Distribution')
plt.ylim(0, 0.1);
plt.legend(loc='best');
plt.xlabel('Distance moved');

# <headingcell level=2>

# Both Distributions have to be merged together

# <markdowncell>

# $\mu_\text{new}=\mu_\text{0}+\mu_\text{move}$ is the new mean and $\sigma^2_\text{new}=\sigma^2_\text{0}+\sigma^2_\text{move}$ is the new variance.

# <codecell>

def predict(var, mean, varMove, meanMove):
    new_var = var + varMove
    new_mean= mean+ meanMove
    return new_var, new_mean

# <codecell>

new_var, new_mean = predict(var0, mean0, varMove, meanMove)

# <codecell>

plt.figure(figsize=(16,5))
plt.plot(x,mlab.normpdf(x, mean0, var0), label='Beginning Normal Distribution')
plt.plot(x,mlab.normpdf(x, meanMove, varMove), label='Movement Normal Distribution')
plt.plot(x,mlab.normpdf(x, new_mean, new_var), label='Resulting Normal Distribution')
plt.ylim(0, 0.1);
plt.legend(loc='best');
plt.title('Normal Distributions of 1st Kalman Filter Prediction Step');
plt.savefig('Kalman-Filter-1D-Step.png', dpi=150)

# <markdowncell>

# What you see: The resulting distribution is flat > uncertain.
# 
# The more often you run the `predict` step, the flatter the distribution get

# <headingcell level=1>

# First Sensor Measurement (Position) is coming in...

# <headingcell level=3>

# Sensor Defaults for Position Measurements

# <markdowncell>

# (Estimated or determined with static measurements)

# <codecell>

meanSensor = 25.0
varSensor  = 12.0

# <codecell>

plt.figure(figsize=(16,5))
plt.plot(x,mlab.normpdf(x, meanSensor, varSensor))
plt.ylim(0, 0.1);

# <headingcell level=2>

# Now both Distributions have to be merged together

# <markdowncell>

# $\sigma^2_\text{new}=\cfrac{1}{\cfrac{1}{\sigma^2_\text{old}}+\cfrac{1}{\sigma^2_\text{Sensor}}}$ is the new variance and the new mean value is $\mu_\text{new}=\cfrac{\sigma^2_\text{Sensor} \cdot \mu_\text{old} + \sigma^2_\text{old} \cdot \mu_\text{Sensor}}{\sigma^2_\text{old}+\sigma^2_\text{Sensor}}$

# <codecell>

def correct(var, mean, varSensor, meanSensor):
    new_mean=(varSensor*mean + var*meanSensor) / (var+varSensor)
    new_var = 1/(1/var +1/varSensor)
    return new_var, new_mean

# <codecell>

var, mean = correct(new_var, new_mean, varSensor, meanSensor)

# <codecell>

plt.figure(figsize=(16,5))
plt.plot(x,mlab.normpdf(x, new_mean, new_var), label='Beginning (after Predict)')
plt.plot(x,mlab.normpdf(x, meanSensor, varSensor), label='Position Sensor Normal Distribution')
plt.plot(x,mlab.normpdf(x, mean, var), label='New Position Normal Distribution')
plt.ylim(0, 0.1);
plt.legend(loc='best');
plt.title('Normal Distributions of 1st Kalman Filter Update Step');

# <markdowncell>

# You see: Sensor readings increase the certainty!

# <headingcell level=3>

# This is called the Measurement or Correction step! The Filter get's more serious about the actual state.

# <headingcell level=2>

# Let's put everything together: The 1D Kalman Filter

# <markdowncell>

# *"Kalman-Filter: Predicting the Future since 1960"*

# <markdowncell>

# Let's say, we have some measurements for position and for distance traveled. Both have to be fused with the 1D-Kalman Filter.

# <codecell>

positions = (10, 20, 30, 40, 50)+np.random.randn(5)
distances = (10, 10, 10, 10, 10)+np.random.randn(5)

# <codecell>

positions

# <codecell>

distances

# <codecell>

mean = mean0
var = var0

plt.figure(figsize=(16,5))
for m in range(len(positions)):
    
    # Predict
    var, mean = predict(var, mean, varMove, distances[m])
    #print('mean: %.2f\tvar:%.2f' % (mean, var))
    plt.plot(x,mlab.normpdf(x, mean, var), label='%i. step (Prediction)' % (m+1))
    
    # Correct
    var, mean = correct(var, mean, varSensor, positions[m])
    print('After correction:  mean= %.2f\tvar= %.2f' % (mean, var))
    plt.plot(x,mlab.normpdf(x, mean, var), label='%i. step (Correction)' % (m+1))
    
plt.ylim(0, 0.1);
plt.legend();    

# <headingcell level=1>

# Conclusion

# <markdowncell>

# The sensors are represented as normal distributions with their parameters ($\mu$ and $\sigma^2$) and are calculated together with addition or convolution. The prediction decreases the certainty about the state, the correction increases the certainty.
# 
# * Prediction: Certainty $\downarrow$
# * Correction: Certainty $\uparrow$
# 
# If you have more than one state (here: position), than you have to use the multidimensional Kalman Filter, which is pretty much the same, but with matrices:
# 
# ![Kalman Filter](Kalman-Filter-Step.png)

# <markdowncell>

# In order to use the Kalman filter to estimate the internal state $x$ of a process given only a sequence of noisy observations $z$, one must model the process in accordance with the framework of the Kalman filter. This means specifying the following matrices:
# 
# * $A$, the state-transition model, which is applied to the previous state $x$
# * $H$, the observation model, which maps the true state space into the observed space
# * $Q$, the covariance of the process noise
# * $R$, the covariance of the observation noise
# * $P$, the error covariance matrix (a measure of the estimated accuracy of the state estimate)
# * $K$, the Kalman-Gain, which weights between the model and the observation
# * and sometimes $B$, the control-input model, which is applied to the control vector $u$
# 
# for each time-step, $k$.
# 
# *Source: [Wikipedia](http://en.wikipedia.org/wiki/Kalman_filter)*

# <markdowncell>

# And you can run the `Prediction` in high update rate Open-Loop mode (means: without `Correction`) and use a correction, only if it is available.
# 
# Typical Example: You have a high update rate acceleration sensor (typical 100Hz) and a low update rate GPS sensor (typical 1Hz). Then you run the `Prediction` with 100Hz (mean 100 times a second) and only correct every 100th filter step.

