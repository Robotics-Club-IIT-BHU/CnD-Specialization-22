# Why  LQR if we already have PID? 

The application of industrial robots has greatly increased in recent  years making production systems more and more efficient. With this in  mind, increasingly efficient controllers are needed for those robots. 

<p align="center">
<img  width="" height="" src="https://user-images.githubusercontent.com/56964828/126338592-12198b94-8ab3-4935-a49a-062eda016648.png">
 <p align="center">
 <i></i><br>
</p>

LQR control is a trade-off between highly optimized controls and reduced complexity such as in PID control.

LQR controllers are robust and produce a very low steady state error, However there are sometimes huge transition delays when working with multiple feedback gains, making them non-ideal to apply on fast response systems or those with no direct access to all states. On the other hand, a PID controller gives a faster response but not with robust gains as the previous controller. [[1]](https://fei.edu.br/~psantos/PID2737725.pdf)

Therefore, which controller to use depends upon the system and operating conditions as well.


<p align="center">
<img  width="400" height="" src="https://indianmemetemplates.com/wp-content/uploads/matlab-aisa-bilkul-immediate-nahi-soche-hai-but-sochenge.jpg">
 <p align="center">
 <i>*le control Engineer</i><br>
</p>


# Root of all systems, the Inverted Pendulum

#### Pendulums are Everywhere

![Real -world application of an inverted pendulum - the Segway](https://www.quanser.com/wp-content/uploads/2019/09/Segway-200x300.jpg)

*The inverted pendulum DOES represent many real-world systems*. Examples include the Segway, the human posture systems, the launching  of a rocket, and so on. Basically, any system that requires vertical  stabilization has dynamics that are similar to an inverted pendulum.  Sure, the dynamics in these real-world systems are more complex, but  they are related. The work involved in modeling and controlling an  inverted pendulum carries over to many engineering areas. [[2]](https://www.quanser.com/blog/why-is-the-pendulum-so-popular/)

Also the maths is easy .

# Second task for the week

## Goals for the challenge

1. Implement a LQR based controller to balancing the self balancing bot  using Torque Control.
2. Develop a LQR controller to make the bot stay upright.
3. Calibrate the Gains to get the best performance and minimum turbulence.
4. Infer from the exercise how different error coefficients affect the performance and stability.


# INSTRUCTIONS 

1. Download this folder.
2. The code in folder "exercise" has to  be edited.
3. You have two controller options although submission for only LQR will be taken.
4. You are free to make any changes you like based on your algo.
5. "test_lqr.py" and "test_urdf" are just for you to get familiar with the function used and the environment.
6. **Hint** - Consider the self balancing bot as a inverted pendulum on a pole (cartpole) problem.
7. Refer to **CartPole_help** subfolder in order to get some help in calculating the A and B matrices for the problem. 


Once you have completed the challenge, *record a video with your bot in simulation*, zip it with your *SelfBalance_withLQR.py* file and submit at the link below- 

[Weekly Challenge 2 - Submission](https://forms.gle/Gris7FD4psogJ3yDA)

<p align = "center">
<img width = "500" height = "" src = "https://media.makeameme.org/created/hurrah-all-done.jpg">
<p align = "center">
<i>You made it! Will see you next week :)</i>
</p>





