# Documentation

Required version of python: 3.6-3.8.9

Required to download library for roboticstoolbox

Required to download python extensions: pip3

Required to change the file name of the .png file of users robot image

The code is designed to take in inputs from the user for the robots starting position and the desired targets position. (X and Y coordinates) 
The user is also given the option to add the desired amount of obstacles on a set map size of 20mx20m, these obstacles are randomly placed.

The main outputs:

  Distance of robot to target in metres
  
  Angle of robot to target in degrees
  
  Distance of robot to all randomly placed obstacles in metres 
  
  Angle of robot to all randomly placed obstacles in radians
  
  The map, which is 20mx20m and the robot moving towards the target
  
Advanced algorithm for manouvering past obstacles was used, depending on the angle from the robot to the obstacle, acts as a way of figuring out if the obstacle is ahead or behind the robot, the robot would chose the most efficient way to avoid the obstacle, turning 60 degrees to the left or 45 degrees to the right. These degrees have been calculated after numerous tests and gave the best and smoothest movement.
The robot is not fast because of implementation of a delay for the output data so it doesnt spam, this delay unfortunatly affects the robots speed, the line (sleep(0.2) could be removed if the user wants to, to allow smoother movement however the data displayed in the terminal would be too fast to be useful, in the future i will figure out a way to delay data without affecting the speed of the robot.
For future innovations, i would like to customize the map and create different looking maps for the robot to navigate in, i would also add a way for the robot to fully ignore obstacles behind it and only focus on obstacles in a span of around 70 degrees ahead of it, and recognize obstacles from far away so it can move away earlier to find the most optimal direction to the target from the beggining. Sometimes if the target set is too close to the obstacles the robot struggles to reach the target, in the future i plan to put restrictions so that random obstacles do not spawn within a certain distance to the target.
