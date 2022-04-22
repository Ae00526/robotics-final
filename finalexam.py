from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor, LandmarkMap
from math import pi, atan2, sqrt
import matplotlib.pyplot as plt
from sympy import false, true 
from scipy.io import loadmat
import numpy as np
from time import sleep

startx= float(input("choose X coordinates for the robot: ")) #coordinates of the robot
starty= float(input("choose Y coordinates for the robot: "))
targetx= float(input("choose your targets X coordinates: ")) #coordinates of the target
targety= float(input("choose your targets Y coordinates: "))
obstaclenum= float(input("choose number of obstacles in the map: ")) #number of obstacles randomly generated 

start=[startx,starty] #making a list of the coordinates of the robot
target=[targetx, targety] #making a list of the coordinates of the target
anim = VehicleIcon('pngegg.png', scale =2.5) #the vehicle picture and scale, insert your pictures name.png 
veh=Bicycle(
    animation= anim, #animate the robot
    control= RandomPath,
    dim=20, #dimensions of the grid
    x0= (startx, starty, 0), #coordinates of the robot and centered at 0
)
veh.init(plot=True)
mymap=LandmarkMap(obstaclenum,20) #display the map of obstacles on a grid of dimension of 20x20 to fit
mymap.plot()
sensor=RangeBearingSensor(robot=veh,map=mymap,animate=True) #sensor for distance of robot to random obstacles
print((targetx-startx),",", targety-starty) #starting distance
# print(sensor.h(veh.x))
veh._animation.update(veh.x) #update animation of robot
plt.plot()




target_marker_style={ #design of the target
    'marker':'D',
    'markersize': 7,
    'color': 'b'
}
plt.plot(targetx, targety, **target_marker_style)

plt.plot()

run = True #move robot towards target

# def avoidance(rsensors):
#         for i in sensor.h(veh.x):
#             if (i[0] <3):
#                 goal_heading=atan2(
#                     target[1]-veh.x[1], #calculating distance to target using TAN and the distance
#                     target[0]-veh.x[0]
#                 )
#                 steer=goal_heading-veh.x[2]
#             else:
#                 veh.step(2,0)
#                 veh._animation.update(veh.x)
#                 plt.pause(0.005)
while (run):
    sleep(0.2) #slight delay so output distances arent spammed in terminal, does slow down movement of robot
    goal_heading=atan2(
        target[1]-veh.x[1], #calculating distance to target using TAN and the distance
        target[0]-veh.x[0]
    )
    steer=goal_heading-veh.x[2]
    
    
    veh.step(3,steer)#speed of the robot moving and the angle to target
    
    print("angle to target: ",(steer*180)/pi, "degrees",  end="...") #changing the angle from radian to degrees
    print("distance to target: ",(abs(sqrt((targetx-veh.x[0])**2+(targety-veh.x[1])**2))), "metres") #distance to target using pythagorean theorem
    sens=sensor.h(veh.x) 
    print("distance and angle to obstacles \n", sens) #\n to make the data show below the text
    # for i in sens: 
    #     print("distance to obstacles", i[0]) #distance to randomly generated obstacles
    #     print("angle to obstacles: ",i[1])

    
    if((abs(target[0]-veh.x[0]) >0.2) or (abs(target[1]-veh.x[1]) > 0.2)): #if distance from robot to target is >0.2 the robot keeps moving
        run=True
        
       
    else:
        run=False
        break

    for i in sens:
        if i[0]<2 and i[1]>0: #if robot is within this distance he will turn around and continue moving
            # veh.x[0]+=1
            veh.x[2]+=-pi/3 #move certain direction (right or left) depending whether obstacle ahead or behind (changes angle its facing)
        elif i[0]<2 and i[1]<0:
            veh.x[2]+=pi/4
            
    veh._animation.update(veh.x)
    
    # if avoidance(sensor.h(veh.x))==false:
    #     run=false
    
    plt.pause(0.005)
plt.pause(100)
