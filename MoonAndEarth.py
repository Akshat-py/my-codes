########## Made by Akshat ##########
######### github: Akshat-py ########

import turtle
from math import *

# Making the bodies and giving them color, circle shape.
t1 = turtle.Pen()
t2 = turtle.Pen()
t3 = turtle.Pen()
t1.shape("circle")
t2.shape("circle")
t3.shape("circle")
t1.pu()
t2.pu()
t3.pu()
t1.color("red")
t2.color("green")
t3.color("blue")
t1.speed(0)
t2.speed(0)
t3.speed(0)

# Constants of TIME and GRAVITATIONAL CONSTANT
T = 0.01
G = 100

# Assigning MASS, SIZE, INITIAL SPEED(v) and LOCATION(s) to the bodies.
mass1 = 1
t1.shapesize(0.5)  # Earth
s1 = [-300,0]
v1 = [0,-(100/sqrt(3))]

mass2 = 0.1
t2.shapesize(0.1)  # Moon
s2 = [-300,-10]
v2 = [-(sqrt(10)),v1[1]]

mass3 = 10000
t3.shapesize(3)    # Sun
s3 = [0,0]
v3 = [0,0]

# Setting up the bodies for simulation.
t1.goto(s1[0],s1[1])
t2.goto(s2[0],s2[1])
t3.goto(s3[0],s3[1])
t1.pd()
t2.pd()
t3.pd()

while True:
    t1.goto(s1[0],s1[1])
    t2.goto(s2[0],s2[1])
    t3.goto(s3[0],s3[1])

# Squares of distances btw the 3 bodies.
    rs12 = ((s1[0]-s2[0])**2 + (s1[1]-s2[1])**2)
    rs23 = ((s2[0]-s3[0])**2 + (s2[1]-s3[1])**2)
    rs31 = ((s3[0]-s1[0])**2 + (s3[1]-s1[1])**2)

    print(sqrt(rs12)) # PRINTING DISTANCE BTW MOON AND EARTH

# Acceleration acting on t1 due to t2 and t3.
    acc12v = (G*mass2)/(rs12)
    ang12 = radians(t1.towards(s2[0],s2[1]))
    acc12 = [acc12v*cos(ang12), acc12v*sin(ang12)]
    acc13v = (G*mass3)/(rs31)
    ang13 = radians(t1.towards(s3[0],s3[1]))
    acc13 = [acc13v*cos(ang13), acc13v*sin(ang13)]

# Kinematics of t1.
    acc1 = [(acc12[0]+acc13[0]),(acc12[1]+acc13[1])]
    v1[0] += acc1[0]*T
    v1[1] += acc1[1]*T
    s1[0] += v1[0]*T
    s1[1] += v1[1]*T

# Acceleration acting on t2 due to t1 and t3.
    acc21v = (G*mass1)/(rs12)
    ang21 = radians(t2.towards(s1[0],s1[1]))
    acc21 = [acc21v*cos(ang21), acc21v*sin(ang21)]
    acc23v = (G*mass3)/(rs23)
    ang23 = radians(t2.towards(s3[0],s3[1]))
    acc23 = [acc23v*cos(ang23), acc23v*sin(ang23)]

# Kinematics of t2.
    acc2 = [(acc21[0]+acc23[0]),(acc21[1]+acc23[1])]
    v2[0] += acc2[0]*T
    v2[1] += acc2[1]*T
    s2[0] += v2[0]*T
    s2[1] += v2[1]*T

# Acceleration acting on t3 due to t1 and t2.
    acc31v = (G*mass1)/(rs31)
    ang31 = radians(t3.towards(s1[0],s1[1]))
    acc31 = [acc31v*cos(ang31), acc31v*sin(ang31)]
    acc32v = (G*mass2)/(rs23)
    ang32 = radians(t3.towards(s2[0],s2[1]))
    acc32 = [acc32v*cos(ang32), acc32v*sin(ang32)]

# Kinematics of t3.
    acc3 = [(acc31[0]+acc32[0]),(acc31[1]+acc32[1])]
    v3[0] += acc3[0]*T
    v3[1] += acc3[1]*T
    s3[0] += v3[0]*T
    s3[1] += v3[1]*T

