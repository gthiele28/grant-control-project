import numpy as np
from simulator import Simulator

def controller(x):
    """controller for a car

    Args:
        x (ndarray): numpy array of shape (5,) containing [x, y, heading, velocity, steering angle]

    Returns:
        ndarray: numpy array of shape (2,) containing [fwd acceleration, steering rate]
    """
    ... # YOUR CODE HERE
    xPos = x[0]
    yPos = x[1]
    heading = x[2]
    velocity = x[3]
    steeringAngle = x[4]

    
    return np.array([1,0])


sim = Simulator(controller)
sim.run()
sim.animate()
sim.plot()