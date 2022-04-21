from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor, LandmarkMap
from math import pi, atan2
import matplotlib.pyplot as plt
from sympy import false, true 
from scipy.io import loadmat
import numpy as np

startx= int(input("choose X coordinates for the robot: ")) #coordinates of the robot
starty= int(input("choose Y coordinates for the robot: "))
targetx= int(input("choose your targets X coordinates: ")) #coordinates of the target
targety= int(input("choose your targets Y coordinates: "))
obstaclenum= int(input("choose number of obstacles in the map: ")) #number of obstacles randomly generated 

start=[startx,starty] #making a list of the coordinates of the robot
target=[targetx, targety] #making a list of the coordinates of the target
anim = VehicleIcon('pngegg.png', scale =3) #the vehicle picture and scale
veh=Bicycle(
    animation= anim, #animate the robot
    control= RandomPath,
    dim=20, #dimensions of the grid
    x0= (startx, starty, 0), #coordinates of the robot and centered at 0
)
veh.init(plot=True)
mymap=LandmarkMap(obstaclenum,20) #display the map of obstacles on a grid of dimension of 20x20 to fit
mymap.plot()
sensor=RangeBearingSensor(robot=veh,map=mymap,animate=True) #sensor for distanceof robot to random obstacles
print(targetx-startx,",", targety-starty)
# print(sensor.h(veh.x))
veh._animation.update(veh.x) #update animation of robot
plt.plot()




target_marker_style={ #design of the target
    'marker':'D',
    'markersize': 6,
    'color': 'b'
}
plt.plot(targetx, targety, **target_marker_style)

plt.plot()

run = True#move robot towards target
while (run):
    goal_heading=atan2(
        target[1]-veh.x[1], #calculating distance and angle to target using TAN
        target[0]-veh.x[0]
    )
    steer=goal_heading-veh.x[2]
    veh.step(2,steer)
    print("angle to target",(steer*180)/pi, end="") #changing the angle from radian to degrees
    print(sensor.h(veh.x))
    
    if((abs(target[0]-veh.x[0]) >0.1) or (abs(target[1]-veh.x[1]) > 0.1)): #if distance from robot to target is >0.1 the robot keeps moving
        run=True
        
       
    else:
        run=False
 
    veh._animation.update(veh.x)
    
    
    plt.pause(0.005)
plt.pause(100)

