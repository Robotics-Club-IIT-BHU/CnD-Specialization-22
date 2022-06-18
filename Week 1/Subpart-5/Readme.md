# Time to rule

After having a thourough understanding, its time for you to bring stablility to an unstable system

<p align="center">
<img  width="250" height="" src="assets/img1.jpg">
 <p align="center">
 <i></i><br>
</p>

You have seen the equation of a system with A dynamics matrix, B actuation matrix and control u.

<p align="center">
<img  width="250" height="" src="assets/act.png">
 <p align="center">
 <i></i><br>
</p>

When we change this u to feedback control i.e., the current control input u depends on the current state x of the system ( **u = -kx** ). Then we get the equation as - 

<p align="center">
<img  width="400" height="" src="assets/eigen eq.png">
 <p align="center">
 <i></i><br>
</p>

## Controlling the system

Now, A and B are fixed. If you want your system to be stable, you want to have stable eigen values. Here, K is a variable that we can choose for ourselves. Hence, this **K acts as the control knob**. 

Now, using K, we control the dynamics of the system. With proper selection of matrices, we can make our system converge to origin(or shifted origin in some case) by making our eigen values negative.

Softwares such as MATLAB can do this with one line commands passing the matrices A,B and eigen values.

**K = place(A, B, eigs)**

This is called **Pole Placement.**

The calculations include some mathematics from linear algebra but the computational tools help us to calculate such matrices pretty fast.

Once your system becomes stable, you can shift your origin anywhere you want and the system will converge to that point in some time. If the initial state of the system is that point then the control will make sure that the system maintains that state. The shift of origin is carried out like this - 

<p align="center">
<img  width="400" height="" src="assets/shift.png">
 <p align="center">
</p>

## The Big Question

**Now if we can put the eigen values where ever we want, what is the best place to put them to?**

<p align="center">
<img  width="400" height="" src="assets/meme2.jpg">
 <p align="center">
 <i></i><br>
</p>

Well, the following things depend on the position of eigen values:

* How fast the system converges to the required state.
* How much power the actuators use to get to the required state.
* How smoothly the system converges.

So, In control theory optimization algorithms are used to find optimal eigen values for a system and control it in the most efficient way. One of these control algorithms is LQR which is very popular.

# LQR control


Well, in LQR we introduce two matrices. Q and R.

These are cost matrices which are the parameters that we tune. These act as control knob for controlling the system.

1. The Q matrice is a diagonal matrix of nxn which contains the cost of each variable of the state. The higher the cost, the quickly the system needs to converge to that particular variable.

2. The R matric is a 1xz matrix where z is the number of actuators in the system. It decides how much cost is associated with each actuator. The higher the cost of an actuator, the lest power it must use.

For example, for the pendulum example that we saw earler - 

<p align="center">
<img  width="500" height="" src="assets/Invertedpendulum.png">
 <p align="center">
 <i></i><br>
</p>

The Q and R matrices would look something like - 

<p align="center">
<img  width="300" height="" src="assets/q.png">
 <p align="center">
 <i>Q matrix</i><br>
</p>


<p align="center">
<img  width="300" height="" src="assets/r.png">
 <p align="center">
 <i>R matrix</i><br>
</p>

Now, we introduce a cost function that calculates the cost associated with the converges of the system and tries to minimise it. This cost is given as - 

<p align="center">
<img  width="500" height="" src="assets/cost.png">
 <p align="center">
 <i>LQR cost</i><br>
</p>


Here, X and u are the state and actuator matrices at any time tau and the J is it's integration over a long time (equivalent to infinite amount of time).
What LQR does is it tries to produce a K matrix such that this J cost is minimum. This is an optimization problem and it's mathematics can't be covered here but modern control libraries in python and MATLAB can give you the K matrix with a single command, given you know values of A, B, Q and R.

**K = lqr(A, B, Q, R)**

Once we place the value of K into the dynamics, we get an optimal converging system which we can control and converge to any point that we like.

Well, that's all from our side for this week. Now you can also attempt the second task of the week. Best of Luck!!


<p align="center">
<img  width="300" height="" src="assets/meme4.jpg">
 <p align="center">
 <i></i><br>
</p>

## Further Readings - Extras

1. Here is a great playlist on basics of control that covers all that has taken place in this camp yet in great detail. Watch this if you are really interested in controls and want to become a controls expert -

[![Langrangian Mechanics](https://img.youtube.com/vi/Pi7l8mMjYVE/0.jpg)](https://youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m)

