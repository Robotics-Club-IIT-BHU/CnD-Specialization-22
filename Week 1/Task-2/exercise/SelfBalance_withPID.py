# # Introduction

# Description of the implementation of Control Systems namely PID(#pid_sec) on our robot. 
# The "pidcontrol.py" file has been used for our project. I haven't written this library. I have downloaded from this github project.[1](#pid)

# #### Importing Libraris

import sys
import pidcontrol as pid
import numpy as np
import pybullet as p
import math
import time
import pybullet_data

# ### PID
# The class below , "SelfBalance" does the main job. In this class, we see function to tune the PID gains . 
# For PID controller function python code named "pidcontrol.py" from the project at [1](#pid) is used

class SelfBalance:
    '''
    Purpose:
    ---
    Class Describing the gains of LQR and various functions
    Functions:
    ---
        __init__ : Called by default to initilize the variables in PID
        callback : It takes the data from sensors/bots and accordingly predicts the next state and respecive action
        callback_Kp : It can be used to change the value of gains during execution
        callback_Ki : It can be used to change the value of gains during execution
        callback_Kd : It can be used to change the value of gains during execution
    Example initialization and function call:
    ---
    balance=SelfBalanceLQR()
    vel=balance.callback(data)
    '''
    def __init__(self):
        self.xvelMin=-.01
        self.xvelMax =0
        self.yMin = -0.01
        self.yMax = -0.001
        self.yPrev =0
        self.delY = 0
        self.Kp = 25
        self.Ki = 0.8
        self.Kd = 0.1
        self.controller=pid.PID_Controller(self.Kp,self.Ki,self.Kd)
        
    def callback(self,data):
        setpoint=0 #the required state / positon of bot 
        ##########################write your code here ##################################################
        #Varibale:y- It is the current state of the bot calculated from data
        #write here

        ###############################################################################################
        self.delY = y-self.yPrev # error calculation
        
        
        xvel = -self.controller.getCorrection(setPoint,y)#calling the class in "pidcontrol.py" and getting the correction


        #storing variables for evaluation
        if self.delY>self.yMax:
            self.yMax = self.delY
        elif self.delY<self.yMin:
            self.yMin = self.delY

        if xvel>self.xvelMax:
            self.xvelMax=xvel
        elif xvel<self.xvelMin:
            self.xvelMin = xvel
        
        if xvel >26:
            xvel =26
        elif xvel<-26:
            xvel =-26
        
        self.yPrev = y # storing previous state of variable
        
        return xvel
        #print "Max vel " + str(self.xvelMax) + " & Min vel " + str(self.xvelMin) + " Max delY " + str(self.yMax*180/3.1416) +" & Min delY" + str(self.yMin*180/3.1416)
    def callback_Kp(self,data):
        self.Kp = data.data
        self.controller=pid.PID_Controller(self.Kp,self.Ki,self.Kd)
    def callback_Ki(self,data):
        self.Ki = data.data
        self.controller=pid.PID_Controller(self.Kp,self.Ki,self.Kd)
    
    def callback_Kd(self,data):
        self.Kd = data.data
        self.controller=self.controllerpid.PID_Controller(self.Kp,self.Ki,self.Kd)


def synthesizeData(robot):
    '''
    Purpose:
    ---
    Calculate the current state(position , velocity , orienation etc.)
    Input Arguments:
    ---
    `robot` :  integer
        object id of bot spawned in pybullet

    Returns:
    ---
    `data` :  1D array 
        list of information required for calculation
    Example call:
    ---
    data=synthesizeData(robot)
    '''
    # print("----------------------------------------------------------------------------------------------------------------")
    # print("Dynamic Info of Base : ",p.getDynamicsInfo(robot, -1),end="\n")
    # #0->mass , 3->local inertial pos
    # print("Base position and Orientation : " , p.getBasePositionAndOrientation(robot),end="\n")
    # #1->orientation

    # com = p.getDynamicsInfo(robot, -1)
    # com += p.getBasePositionAndOrientation(robot)[0][2] 
    # print("Centre of mass - ", com)

    #information required yaw
    #imu sensor , kp ,ki ,kd
    #set cmd_vel 
    ########################### write your code here #######################################################
    # Variable: data - it contains the current state of bot that is sent to callback function for processing
    # For hints refer to statements above and choose an apt state variable
    #write here
         
     
    ########################################################################################################
    return data

# Main Function

if __name__ == "__main__":
    '''
    Purpose:
    ---
        Setup the pybullet environment and calculation of state variables and respective action to balance the bot
    '''
    id = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    plane = p.loadURDF("plane.urdf")
    p.setGravity(0, 0, -9.8)

    robot = p.loadURDF("../urdf/self_balance.urdf" , [0,0,0.2])

    # num = p.getNumJoints(robot)
    # for i in range(num):
    #     info = p.getJointInfo(robot, i)
    #     print(info,end="\n")
    #     link_name = info[12].decode("ascii")
    #     if link_name == "left_wheel": left_wheel = j
    #     if link_name == "right_wheel": wheel_foot = j

    left_joint=0
    right_joint=1
    maxForce = 0
    mode = p.VELOCITY_CONTROL
    p.setJointMotorControl2(robot, left_joint,controlMode=mode, force=maxForce)
    p.setJointMotorControl2(robot, right_joint,controlMode=mode, force=maxForce)


    balance=SelfBalance()
    while(True):
        data=synthesizeData(robot)#get data from simulation and bot 
        vel=balance.callback(data)#calculating torque to be applied on wheels
        # print(vel)
        p.setJointMotorControl2(robot, left_joint , p.TORQUE_CONTROL, force = -vel)
        p.setJointMotorControl2(robot, right_joint , p.TORQUE_CONTROL, force = vel)
        p.stepSimulation()
        time.sleep(0.01)



    # # Reference
    # [1] PyQuadSim [Repository](https://github.com/simondlevy/PyQuadSim/blob/master/pidcontrol.py)
