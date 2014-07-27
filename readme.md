# PyData 2014 Berlin
## IPython and Sympy to Develop a Kalman Filter for Multisensor Data Fusion
~ Paul Balzer ~

The best filter algorithm to fuse multiple sensor informations is the Kalman filter. To implement it for non-linear dynamic models (e.g. a car), analytic calculations for the matrices are necessary. In this talk, one can see, how the IPython Notebook and Sympy helps to develop an optimal filter to fuse sensor information from different sources (e.g. acceleration, speed and GPS position) to get an optimal estimate.

## Topics

### 1. Sensor Noise

Believe it or not: No sensor on the whole world is providing the 'real value'. And even if, you do not know, if it is the real value.

![ax noise](https://raw.githubusercontent.com/balzer82/PyData-Berlin-2014-Kalman/master/ax_dist.png)

`sensor value = real value + some error`

See [Sensor-Noise.ipynb](http://nbviewer.ipython.org/github/balzer82/PyData-Berlin-2014-Kalman/blob/master/Sensor-Noise.ipynb)


### 2. Filter idea in 1D

Basic introduction to the theory behind the filter algorithm in just one dimension.

![Kalman 1D](https://raw.githubusercontent.com/balzer82/PyData-Berlin-2014-Kalman/master/Kalman-Filter-1D-Step.png)

See [Kalman-Filter-1D.ipynb](http://nbviewer.ipython.org/github/balzer82/PyData-Berlin-2014-Kalman/blob/master/Kalman-Filter-1D.ipynb)

### 3. Multi-Dimensional Kalman Filter

Now we are going multi-dimensional with matrices.

![Kalman Filter](https://raw.githubusercontent.com/balzer82/PyData-Berlin-2014-Kalman/master/Kalman-Filter-CA-Ball-StateEstimated.png)

See [Kalman-Filter-CA-Ball.ipynb](http://nbviewer.ipython.org/github/balzer82/PyData-Berlin-2014-Kalman/blob/master/Kalman-Filter-CA-Ball.ipynb)

### 4. Extended Kalman Filter

This is actually a real life example, which fuses GPS measurements and IMU measurements of a real vehicle.

![GPS Position and Kalman Filter Estimation](https://raw.githubusercontent.com/balzer82/PyData-Berlin-2014-Kalman/master/EKF-Position.png)

See [Extended-Kalman-Filter-CTRV.ipynb](http://nbviewer.ipython.org/github/balzer82/PyData-Berlin-2014-Kalman/blob/master/Extended-Kalman-Filter-CTRV.ipynb)


## Video

*coming soon...*

## Presentation

[Presentation](https://github.com/balzer82/PyData-Berlin-2014-Kalman/blob/master/Presentation.html) is made with [cleaver](https://github.com/jdan/cleaver): Simply `cleaver Presentation.md`
