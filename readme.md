# PyData 2014 Berlin
## IPython and Sympy to Develop a Kalman Filter for Multisensor Data Fusion
~ Paul Balzer ~

The best filter algorithm to fuse multiple sensor informations is the Kalman filter. To implement it for non-linear dynamic models (e.g. a car), analytic calculations for the matrices are necessary. In this talk, one can see, how the IPython Notebook and Sympy helps to develop an optimal filter to fuse sensor information from different sources (e.g. acceleration, speed and GPS position) to get an optimal estimate.

## Topics

### 1. Sensor Noise

Believe it or not: No sensor on the whole world is providing the 'real value'. And even if, you do not know, if it is the real value.

![ax noise](ax_dist.png)

`sensor value = real value + some error`

See [Sensor-Noise.ipynb](http://localhost:8888/notebooks/Sensor-Noise.ipynb)
--

### 2. Filter idea in 1D

Basic introduction to the theory behind the filter algorithm in just one dimension.

![Kalman 1D](Kalman-Filter-1D-Step.png)

See [Kalman-Filter-1D.ipynb](http://localhost:8888/notebooks/Kalman-Filter-1D.ipynb)

--

### 3. Multi-Dimensional Kalman Filter

Now we are going multi-dimensional with matrices.

![Kalman Filter](Kalman-Filter-CA-Ball-StateEstimated.png)

See [Kalman-Filter-CA-Ball.ipynb](http://localhost:8888/notebooks/Kalman-Filter-CA-Ball.ipynb)

--

### 4. Extended Kalman Filter

This is actually a real life example, which fuses GPS measurements and IMU measurements of a real vehicle.

![Data](EKF-Position.png)

See [Extended-Kalman-Filter-CTRV.ipynb](http://localhost:8888/notebooks/Extended-Kalman-Filter-CTRV.ipynb)


## Video

*coming soon...*

## Presentation

[Presentation.html](Presentation.html) is made with [cleaver](https://github.com/jdan/cleaver): Simply `cleaver Presentation.md`
