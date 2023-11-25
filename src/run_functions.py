from util_main import PROCESS
from lorenz_attractor import LorenzAttractor
import numpy as np,matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')

attractors:list = [
        LorenzAttractor(initial=(0.,1.,1.05)),
        LorenzAttractor(initial=(0.,1.,1.05001)),
        LorenzAttractor(initial=(0.,1.,1.0500001))
    ]

figure = plt.figure(figsize=(18,8))
colors = ["blue","red","green"]
axes = [figure.add_subplot(1,4,init+1,projection="3d") for init in range(4)]

def ProportionalDifference(valueOne:int or float,valueTwo:int or float)->PROCESS:
    """
    Calculate the proportional difference between two values.

    Args:
    valueOne (float): The first value.
    valueTwo (float): The second value.

    Returns:
    float: The proportional difference between the two values.
    """
    absDiff = abs(valueOne-valueTwo)
    avrValue = (valueOne+valueTwo)/2
    propDiff = absDiff/avrValue
    return propDiff

proportionalDiffirence_1_2 = ProportionalDifference(1.05,1.05001)
proportionalDiffirence_1_3 = ProportionalDifference(1.05,1.0500001)

def InitialFunction()->PROCESS:
    for init,axs in enumerate(axes):
        axs.clear()
        axs.set_xlim([-20,20])
        axs.set_ylim([-30,30])
        axs.set_zlim([0,50])
        axs.set_xlabel("X-Axis")
        axs.set_ylabel("Y-Axis")
        axs.set_zlabel("Z-Axis")
        if init < 3:
            if init == 0:
                axs.set_title(f"Probability Plane Event - {init+1}")
            elif init == 1:
                formatted_output = "{:.2e}".format(proportionalDiffirence_1_2)
                axs.set_title(f"Probability Plane Event - {init+1}\nProportional Diffirence\nFrom One: {formatted_output}")
            elif init == 2:
                formatted_output = "{:.2e}".format(proportionalDiffirence_1_3)
                axs.set_title(f"Probability Plane Event - {init+1}\nProportional Diffirence\nFrom One: {formatted_output}")
            else:
                pass
        else:
            axs.set_title("Combined Plane Events")
    figure.suptitle("Lorenz-Attractor Probability Plane Event",fontsize=14)
    return axes

def AnimateFunction(init:PROCESS)->PROCESS:
    for k,attractor in enumerate(attractors):
        attractor.PlotResult(axes[k],colors[k],init)
    for color,attr in zip(colors,attractors):
        axes[3].plot(attr.trajectory[:init,0],
                     attr.trajectory[:init,1],
                     attr.trajectory[:init,2],
                     lw=0.2,
                     color=color)
                # attr.PlotResult(axes[3],color,init)
    return axes

animation = FuncAnimation(figure,
                          AnimateFunction,
                          frames=np.arange(0,attractors[0].numSteps,20),
                          init_func=InitialFunction,
                          interval=100,
                          blit=False)

plt.show()


