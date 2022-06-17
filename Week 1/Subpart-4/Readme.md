In the last subpart, we looked upon what makes a system **stable**, but what if it isn't?

Its time to take matter in our own hands
<p align= "center">
<img width = "400" height = "300" src = "assets/control.jfif">
</p>

## Controlabillity
For Controlling the system, we introduce some external components called actuators to the system. Motors, hydraulics, heating elements are all examples of actuators. The main goal with placement is to bring over all stability.

<p align= "center">
<img width = "200" height = "100" src = "assets/linear.png">
<p align = "center">
<i>passive linear equation for the system</i>
</p>

With Actuators, the very same equation becomes
<p align= "center">
<img width = "300" height = "130" src = "assets/act.png">
<p align = "center">
<i>Bu is introduced as some external interfernece to the system.</i>
</p>

Here, B Matrix depends upo the actual arrangement of the actuators in the system and can be changed according to its contruction. u represents the amount of power that these actuators apply.

usually we take **u = -kx** in feedback control, x being the current state.

**The purpose to induce Bu is to change the real part of eigen values of the dynamics matrix (A in passive systems) to some negative number making our system stable and controllable.**

Consider the unstable inverted pendulum equations with an actuator at the hinge, equations after linearization are - 
<p align="center">
<img width="500" height = "120" src="assets\Invertedpendulum.png">
 <p align="center">
 <i></i><br>
</p>

After substituting u = -kx, 
<p align="center">
<img width="300" height = "60" src="assets\eigen eq.png">
 <p align="center">
 <i></i><br>
</p>
we get (A-Bk) as the new system matrix, now we just have to find k such that the new matrix now has stable eigen values.

## Some neccessary checks
We can put the eigen values of A-BK anywhere we want by deciding a good K but this is only possible if the matrices A and B together form a controllable system. Hence, to check if A and B form a controllable system or not, we check the controllability matrix.The  controllability of a linear system is determined entirely by the column space of the controllability matrix C:

<p align="center">
<img width="340" height = "60" src="assets\controlmatrix.png">
 <p align="center">
 <i></i><br>
</p>
If the matrix C has n linearly independent columns, so that it spans all of **R^n^**, then the system is controllable, that is to say of the rank of the matrix C is equal to n, then the system is controllable. 

**Note - Here nxn is the dimension of matrix A**

We hope that you have some idea about what the rank of a matrix means. Even if you don't, there is no need to worry. The rank can be obtained easily using numpy in python or matlab. Here, is a quick video explaining the rank of a matrix - 

[![Rank of a Matrix](https://img.youtube.com/vi/MxGJeli6qOc/0.jpg)](https://youtu.be/MxGJeli6qOc)

The following three conditions are equivalent if rank(C)=n:
1. System is *controllable*
2. *Arbitrary eigenvalue placement*. It is possible to design the eigenvalues of the closed-loop system through choice of feedback 
    u = −Kx. i.e for desired eigenvalues we can determine a value of K.
<p align="center">
<img width="300" height = "60" src="assets\eigen eq.png">
 <p align="center">
 <i></i><br>
</p>

3. *Reachability* of R^n^ . It is possible to steer the system to any arbitrary state x(t) = ξ ∈ R^n^ in a finite time with some actuation signal u(t).

<p align = "center">
    <img width = "300" height = "300" src = "assets/meme.jfif">
</p>   

## Intuition
The span of the columns in matrix C determine all the state vector directions in R^n^ which can be controlled. So rank(C)=n implies that all state vector directions in R^n^ are controllable. Thus, in addition to controllability implying arbitrary eigenvalue placement, it also implies that anystate ξ ∈ R^n^ is reachable in a finite time with some actuation signal u(t).

## maybe an Example
The notion of controllability is more easily understood by investigating a few simple examples. First, consider the following system:
<p align="center">
<img width="550" height = "100" src="assets\eg1.png">
 <p align="center">
 <i>The rank of the controllability matrix C is not equal 2 here (n=2).</i><br>
</p>
This system is not controllable, because the controllability matrix C consists of two linearly dependent vectors and does not span R^2^. Even before checkingthe rank of the controllability matrix, it is easy to see that the system won’t be controllable since the states x1 and x2 are completely decoupled and the actuation input u only effects the second state.
Modifying this example to include two actuation inputs makes the system controllable by increasing the control authority


<p align="center">
<img width="650" height = "80" src="assets\eg2.png">
 <p align="center">
 <i>Here the rank of controllability matrix is 2 (n=2).</i><br>
</p>
This fully actuated system is clearly controllable because x1 and x2 may be independently controlled with u1 and u2. The controllability of this system is confirmed by checking that the columns of C do span R^2^.

