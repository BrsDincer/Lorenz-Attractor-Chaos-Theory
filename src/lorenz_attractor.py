from util_main import CLASSINIT,PROCESS,FORMULATION,DOCUMENTATION,ERROR,POINT,NULL
import numpy as np

class LorenzAttractor(object):
    """
    A class representing a Lorenz attractor system.

    Attributes:
    s (float): Parameter representing the Prandtl number.
    r (float): Parameter representing the Rayleigh number.
    b (float): Parameter representing the physical dimension ratio.
    initial (tuple): Initial conditions for the system (x0, y0, z0).
    num_steps (int): Number of steps for the trajectory calculation.
    dt (float): Time step for the trajectory calculation.
    trajectory (np.ndarray): Calculated trajectory of the system.

    Methods:
    calculate_trajectory(): Calculates the trajectory of the system.
    plot(ax, color): Plots the trajectory on a given matplotlib axis.
    """
    def __init__(self,
                 rrandtl=10,
                 rayleigh=28,
                 dimensionRatio=2.667,
                 initial=(0.,1.,1.05),
                 numSteps=10000,
                 timeStep=0.01)->CLASSINIT:
        self.s = rrandtl
        self.r = rayleigh
        self.b = dimensionRatio
        self.initial = initial
        self.numSteps = numSteps
        self.dt = timeStep
        self.trajectory = np.empty((numSteps+1,3))
        self.CalculateTrajectory()
    def __str__(self)->str:
        return "Lorenz Attractor Class - Script"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        raise NotImplementedError(NotImplemented)
    def __repr__(self)->DOCUMENTATION:
        return LorenzAttractor.__doc__
    def ReturnEquations(self,
                        xPoint:POINT|float,
                        yPoint:POINT|float,
                        zPoint:POINT|float)->FORMULATION:
        xDot = self.s * (yPoint-xPoint)
        yDot = self.r * xPoint-yPoint-xPoint*zPoint
        zDot = xPoint*yPoint-self.b*zPoint
        return xDot,yDot,zDot
    def CalculateTrajectory(self)->PROCESS:
        self.trajectory[0] = self.initial
        for init in range(self.numSteps):
            xDot,yDot,zDot = self.ReturnEquations(
                    *self.trajectory[init]
                )
            self.trajectory[init+1] = self.trajectory[init]+np.array([xDot,yDot,zDot])*self.dt
    def PlotResult(self,ax:CLASSINIT,color:tuple,count:int)->PROCESS:
        ax.plot(
                self.trajectory[:count,0],
                self.trajectory[:count,1],
                self.trajectory[:count,2],
                lw=0.5,
                color=color
            )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        