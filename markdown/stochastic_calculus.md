(stochastic_calculus)=
# Stochastic Calculus


(modelling_dynamical_systems)=
## Modelling dynamical systems

Introduction to generalities of modelling

Dynamical system: a set of variables that follow a time dynamics law

$$y = f(t,{X_t})$$ 

where $\{X_t\}$ is a set of external factors that influence the trajectory of the system.

Reasons: prediction, understanding, input to other problems
(optimization like pricing, etc)

The trajectory might be difficult to derive, sometimes it is easier to
derive the dynamics in small steps. Considering the case $y = f(t)$

$$\frac{dy}{dt} = g(t)$$

where $g(t) = \frac{df}{dt}$ and then integrate it

$$y(t) = y(0) + \int_0^t g(t) dt$$

In the more general case where there are external factors with their own time dynamics:

$$dy = \frac{\partial f}{\partial t}dt + \sum_{n=1}^N \frac{\partial f}{\partial X_{i,t}} d X_{i,t}$$

Modelization can be done empirically or using fundamental laws if available, we will see examples in next section

The dynamics of the system might not be deterministic. We can also model the dynamics of a stochastic system in the same way. For instance, a system without external drivers can be described by the following so-called stochastic differential equation:

$$dy = g(t) dt + k(t) d W_t$$ 

where $d W_t$ is the Wiener process (Brownian motion) that will be introduced later.

## Deterministic dynamical systems

Let us review some relevant deterministic differential equations that
come across in the modelization of dynamical systems.

### Example: Newton's Laws 

A first example comes from Newton's laws applied to the dynamics of particles in a gravitational field. The second law of Newton states:

$$F = m a$$ 

We consider an object of mass m drop at initial height
$h(0)$ with speed zero. It is only subjected to the gravitational force:
$F = m g$ where g is the gravitational constant close to Earth's surface: $g \approx 9.81 m/s^2$. The dynamics for the speed is therefore a first order differential equation with constant coefficients:

$$m \frac{d v}{d t} = - m g \rightarrow \frac{d v}{d t} = - g$$ 

where we have taken into account that the force is exerted in the opposite direction to which the height axis grows. This equation is simple to integrate: 

$$v(t) = v(0) - \int_0^t g dt = v(0) + g t = - gt$$ 

since in our case, $v(0) = 0$. The dynamics of the position reads:

$$\frac{d h}{dt} = v(t) = - g t$$ 

which can be again be easily integrated: 

$$h(t) = h(0) - \int_0^t g t' dt' = h(0) - g \frac{t^2}{2}$$

These are particular examples of a general family of differential
equations: 

$$\frac{d^n y}{d t^n} = f(t)$$ 

which can be simply integrated step by step by defining intermediate variables, e.g.:

$$z \equiv \frac{d^{n-1} y}{d t^{n-1}} \rightarrow \frac{d z}{dt} = f(t) \rightarrow z(t) = z(0) + \int_{t_0}^{t_1} f(t) dt$$

### Example: simple inflation targeting model 

A simple model of the dynamics of inflation takes into account Central Bank interventions using monetary policy in order to adjust inflation to a given target. When inflation deviates from the target, monetary policy
is used to bring it back to the target. This can be modelled using the following differential equation:

$$\frac{d \pi_t}{d t} = \theta (\hat{\pi} - \pi_t)$$ 

where $\pi$ is the current level of inflation, $\hat{\pi}$ is the inflation target, and $\theta > 0$ is a constant that models the speed at which monetary
policy takes effect. This is an example of a mean - reverting equation, a process whose dynamics is controlled by an external force that drives
back the system towards a stable level (the mean).

This equation is a particular example of a general family of differential equations which we call separable, with the form

$$\frac{d y}{d t} = g(y)f(t)$$ 

They can be solved by exploiting the
separability:

$$\int_{y_0}^{y_t} \frac{dy}{g(y)} = \int_{t_0}^t f(t') dt'$$

Coming back to the particular example of the mean reverting equation:

$$\begin{aligned}
\int_{\pi_{t_0}}^{\pi_t}\frac{d \pi}{\hat{\pi} - \pi} = \theta \int_{t_0}^t dt' \rightarrow -\log(\frac{\hat{\pi} - \pi_t}{\hat{\pi} - \pi_{t_0}}) = \theta (t - t_0) \\
\pi_t = \hat{\pi} + (\pi_{t_0}-\hat{\pi}) e^{-\theta(t-t_0)}
\end{aligned}$$ 

The solution shows as, as expected, a trajectory for the
inflation that decays to the target. The time scale for decay is independent of the size of the initial gap $\pi_{t_0} -\hat{\pi}$, depending exclusively on $\theta$, which is called the mean reversion speed. In analogy to the physical process of radioactive decay, which
can be described by a similar equation, we can define a half-life $\tau$, or time in which the gap is closed by half, as: $\tau = \frac{\log }{\theta}$ Alternatively, $1/\theta$ is the time it
takes to close the gap to $1/e \approx 0.369$

### Example: Free fall with friction 

We can again resort to Newton's laws to model the dynamics of an object in free fall in the atmosphere, where the air introduces an opposite resistance to the action of gravity. A simple model of such friction is
a force proportional to the speed of the object, namely $F = \eta v$, where $\eta$ is a coefficient that depends on the properties of the atmosphere. Using Newton's law, we have now: 

$$\begin{aligned}
m \frac{dv} {dt} = mg - \eta v \\
\frac{d h} {dt} = v
\end{aligned}$$ 

Which is a system of two equations. We can combine it to
get a differential equation on the particle's trajectory:

$$m \frac{d^2 h}{d t^2} + \eta \frac{dh}{dt} = mg$$ 

which is, particularly, a second order non-homogeneous ODE with constant coefficients. A general non-homogeneous linear ODE with constant coefficients reads:

$$a_n \frac{d^n y}{dt^n} + a_{n-1} \frac{d^{n-1} y}{dt^{n-1}} + ... + a_0 y = f(t)$$

To solve this equation first we find a general solution for the homogeneous equation, and then a particular solution for the non-homogeneous one.

For the general solution of the homogeneous we can actually exploit its connection to a system of first order differential equations, an example
of which we saw when introducing the problem of a particle in free-fall with friction. In general, we can define auxiliary variables
$y_i = \frac{d^i y}{dt^i}$ for $i < n$. We get the following system:

$$\begin{aligned}
 \frac{d y_{n-1}}{dt} + \frac{a_{n-1}}{a_n} y_{n-1} + ... + \frac{a_0}{a_n} y_0 = 0 \nonumber \\
\frac{d y_{n-2}}{dt} - y_{n-1} = 0 \nonumber \\
... \nonumber \\
\frac{d y_0}{dt} - y_1 = 0
\end{aligned}$$ 

which has the structure:

$$\frac{d {\bf y}}{dt} + A {\bf y} = 0$$ 

where ${\bf y} = (y_0, ..., y_{n-1})$ and A is the matrix form with the coefficients of the system of equations above. The general solution to this equation is: $${\bf y} =  e^{-A t} {\bf y_0}$$ This is the formal
solution, but to get a workable solution we need to diagonalize the matrix A, i.e. finding $A = C \Lambda C^{-1}$ where $\Lambda$ is a diagonal matrix with the eigenvalues of A, and C has its eigenvectors
$\vec{w}$ as columns. One can then project the solution in the space of eigenvectors:

$${\bf y_t} =  C C^{-1} e^{-A t} C C^{-1} {\bf y_0} = C e^{-\Lambda t} C^{-1} {\bf y_0}$$

This is equivalent to writing:

$${\bf y_t} = \sum_i w_i e^{-\lambda_i t}  {\bf c_i}$$ 

where ${\bf c_i}$ is the ith eigenvector with eigenvalue $\lambda_i$ and $w_i = (C^{-1} {\bf y_0})_i$ is the projection of the initial state into
the eigenvectors basis. In such basis, the dynamics is simple, driven by the exponential of its eigenvalue: $e^{-\lambda_i t}$

Coming back to the particle in free-fall, we can obtain the general solution of the homogeneous equation, namely:

$$\frac{d^2h}{dt} + \frac{\eta}{m} \frac{dh}{dt} = 0$$ 

by applying directly the ansatz $e^{\lambda t}$:

$$\lambda^2 + \frac{\eta}{m} \lambda = 0$$ 

which is equivalent to finding the eigenvalues of the matrix of the system of equations. This equation has two eigenvalues, $\lambda = 0$ and $\lambda = -\frac{\eta}{m}$, so the general solution reads:

$$h_t = C_0 + C_1 e^{-\frac{\eta}{m}t}$$ 

A particular solution is a linear function $h_t = \frac{m g}{\eta} t$. Therefore, the solution for
the full equation is:

$$h_t = \frac{m g}{\eta} t + C_0 + C_1 e^{-\frac{\eta}{m}t}$$ 

The speed is therefore:

$$v_t = \frac{m g}{\eta} - C_1 \frac{\eta}{m} e^{-\frac{\eta}{m}t}$$

Finally, by imposing initial conditions $h_0$ and $v_0 = 0$, then $C_1 = \frac{m^2 g}{\eta^2}$ and $C_0 = h_0 - C_1$, so:

$$h_t = h_0 + \frac{m g}{eta} t +  \frac{m^2 g}{eta^2} (e^{-\frac{\eta}{m}t} - 1)$$

Notice that the speed of the particle is then:

$$v_t = \frac{m g}{\eta} -\frac{m g}{\eta} h_0 e^{-\frac{\eta}{m}t}$$

which tends to a constant when $t \rightarrow \infty$,
$v_\infty = \frac{m g}{\eta}$, which is called the terminal velocity. At this speed, the friction force equates the gravitational pull and the
object no longer accelerates, therefore reaching a constant velocity. Another interesting observation is that the speed equation has also the
form of a mean reverting equation, in this case the mean being the terminal velocity, and the time-scale for mean reversion proportional to $m/\eta$.

### Numerical solutions of dynamical systems 

When closed form solutions are not available, one can resort to numerical schemes to simulate dynamical systems. The most popular one is the Euler method. First we discretize the time domain using a grid
$t_i = t_0 + \Delta * i$, $i = 0, .., N$, where
$\Delta = \frac{t_1 - t_0}{N}$. The differentials can be discretized over the grid as follows: 

$$\begin{aligned}
\frac{dy}{dt} \rightarrow \frac{y_{t_{i+1}}-y_{t_i}}{\Delta} \\
\frac{d^2y}{dt^2} = \frac{d}{dt} \frac{dy}{dt} \rightarrow \frac{y_{t_{i+1}}-2 y_{t_i} + y_{t_{i-1}}}{\Delta^2} \\
...
\end{aligned}$$ 

Notice that there is some ambiguity on where to evaluate
the derivatives in the grid. For instance the second order one could also be evaluated in a \"forward\" scheme instead of the \"central\"
used:

$$\frac{d^2y}{dt^2} \rightarrow \frac{y_{t_{i+2}}-2 y_{t_{i+1}} + y_{t_i}}{\Delta^2}$$

The same applies to the evaluation of functions in the equation. There are multiple schemes to do it. The most simple one is the forward method, where we evaluate functions at the initial point of the grid
step, $y(t) \rightarrow y_{t_i}$. In the backward case we evaluate it at the final point of the step, $y(t) \rightarrow y_{y_{i+1}}$. There other
possibilities, for example the Crank - Nicolson method uses an average of forward and backward:
$y(t) \rightarrow \frac{1}{2} (y_{t_i} + y_{y_{i+1}})$. In general all these methods with the exception of the forward one yield implicit discrete equations, which require more work to solve, but have usually
better convergence properties (speed, accuracy).

Let us see an example. Previously, we introduced the following model for inflation targeting:

$$\frac{d \pi_t}{d t} = \theta (\hat{\pi} - \pi_t)$$ 

A forward Euler scheme yields the following discrete equation:

$$\pi_{t_{i+1}} = \pi_{t_i} + \Delta \theta (\hat{\pi} - \pi_{t_i})$$

This equation is ready for simulation. Starting with an initial condition $\pi_{t_{i_0}}$ and a grid size $\Delta$, we can iteratively evaluate the trajectory of inflation.

The backward Euler scheme gives the following implicit equation:

$$\pi_{t_{i+1}} = \pi_{t_i} + \Delta \theta (\hat{\pi} - \pi_{t_{i+1}} )$$

In order to simulate it, we need to first solve for $\pi_{t_{i+1}}$. In this case this is simple:

$$\pi_{t_{i+1}} = \frac{\pi_{t_i} + \Delta \theta \hat{\pi}}{1 - \Delta \theta }$$

We leave as an exercise the solution of the Crank Nicholson scheme for this equation.

NUMERICAL EXAMPLE COMPARING SCHEMES AND EXACT

## The Wiener Process

### Definition

So far we have discussed models where we neglect any uncertainty in the trajectories of the dynamical systems we are modelling. However, in many situations, randomness is a dominant characteristic of the process and
we need tools to model such stochastic systems.

The Wiener process is the main building block when modelling stochastic dynamical systems which exhibit continuous trajectories. In order to
model discrete jumps we will introduce later another building block, the Poisson process.

Many introductory books motivate the Wiener process as the continuous limit of a random walk, e.g. a discrete dynamical process in which each step is decided by a random binary variable $Z_t = {1, -1}$ with
$p = 0.5$, i.e. analogous to flipping an unbiased coin. If we know that the process at time $t$ is $X_t$, then $X_{t+1} = X_t + Z_t$.

Here, we will instead introduce the Wiener process as a fundamental building block for the modelization of stochastic processes, i.e. a tool
that will allow us to capture certain observed or proposed behaviours of those systems in a model from which we can draw inferences. In such way,
we define a Wiener process as a type of stochastic process, i.e. an (in principle infinite) sequence of random variables $W_t$ indexed by time
$t$, with the following particular properties:

-   $W_0 = 0$

-   $W_{t+s} - W_s \sim N(0, s)$ where $N(0,s)$ is a Gaussian
    distribution with zero mean and variance $s$, i.e. the increments of
    the Wiener process are Gaussian

-   $W_t$ has independent increments, meaning that any
    $W_{t_1}-W_{t_2}$, $W_{t_3} - W_{t_4}$ where $t_1 < t_2 < t_3 < t_4$
    are independent

-   $W_t$ has continuous trajectories

### Connection to Gaussian Processes

The specific properties of the Wiener process make it part of the family of Gaussian processes, which are stochastic processes with the property that any finite set of them, $X_{t_1}, ..., X_{t_n}$ follow a joined
multivariate Gaussian distribution. The Gaussian process can be described then by a mean function $\mu_t = E[X_t]$ and a covariance function $k(t_1, t_2) = cov[X_{t_1}, X_{t_2}]$ that is usually referred as the kernel function of the Gaussian process.

The index for the stochastic process does not need to refer to time, another typical indexing is space, for instance. When using time as an
index, we talk about Gaussian Processes for time-series modelling. This is the case for the Wiener process, which is a Gaussian process with
mean $\mu_t = 0$ and kernel: 

$$\begin{aligned}
k(t_1, t_2) = cov[W_{t_1}, W_{t_2}] = E[W_{t_1} W_{t_2}] = \nonumber \\ \left(E[(W_{t_1} - W_{t_2}) W_{t_2}] + E[W_{t_2}^2]\right)1_{t_1 > t_2} + \nonumber \\ \left(E[W_{t_1}(W_{t_2} - W_{t_1})] + E[W_{t_1}^2]\right)1_{t_1 \leq t_2} = \nonumber \\
t_2 1_{t_1 > t_2} + t_1 1_{t_1 \leq t_2} = min(t_1,t_2)
\end{aligned}$$ 

In which sense it is useful to introduce this relationship? The theory of Gaussian processes has been pushed in the last years within the Machine Learning community, and there are multiple tools available for building, training and making inferences with these
models. Such toolkit can be useful when building models for dynamical systems using stochastic processes.

### Filtrations and the Martingale Property

The Wiener process satisfies the Martingale property, meaning that if we have a series of observations of the process $W_{t_1}, W_{t_2}, ... W_{t_n}$ then the expected value of an observation $t_{n+1} > t_n > ... > t_1$ conditioned to the previous observations only depends on the last observation:

$$E[W_{t_{n+1}}|W_{t_1}, W_{t_2}, ... W_{t_n}] = W_{t_n}$$ 

i.e., the information from previous observations is irrelevant. We can generalize the martingale property by introducing the notion of filtration $F_t$ at
time $t$, which contains all the information set available until time $t$. We can rewrite the Martingale property using the filtration as:

$$E[W_{t_{n+1}}|F_{t_n}] = W_{t_n}$$ 

We can prove the Martingale property using the defining properties of the Wiener process:

$$\begin{aligned}
E[W_{t_{n+1}}|F_{t_n}] = E[W_{t_{n+1}} - W_{t_n} + W_{t_n}|F_{t_n}] = \nonumber \\
 E[W_{t_{n+1}} - W_{t_n}|F_{t_n}]+ E[W_{t_n}|F_{t_n}] = W_{t_n}
\end{aligned}$$ 

where we have used that the increments of the Wiener
process have zero mean.

### The Tower Law

A useful property that exploits the concept of filtration in many applications is the so-called Law of Iterated Expectations or Tower Law. It simply states that for any random variable Y, if $t_m > t_n$:

$$E[E[Y|F_{t_m}]|F_{t_n}] = E[Y|F_{t_n}]$$ 

This is a useful property to compute expectations using a divide and conquer philosophy: maybe the
full expectation $E[Y|F_{t_n}]$ is not obviously tractable, but by conditioning it at intermediate filtrations
$E[E[E[...E[Y|F_{t_m}] ... |F_{t_{n+2}}|F_{t_{n+1}}|F_{t_n}]$ we can
work out the solution. We will see examples later on.

### The Feynman - Kac Theorem

WIP

### Multivariate Wiener process 

We can construct a multivariate Wiener process as a vector
${\bf W}_t= (W_{1t}, W_{2t}, ..., W_{Nt})$ with the following properties:

-   ${\bf W}_t = {\bf 0}$

-   ${\bf W}_{t+s} - {\bf W_t}_s \sim N(0, \Sigma s)$ where $\Sigma$ is a NxN correlation matrix. This means that the increments of the components of the multivariate Wiener process might be correlated

-   ${\bf W}_t$ has independent increments, meaning that any ${\bf W}_{t_1}-{\bf W}_{t_2}$, ${\bf W}_{t_3} - {\bf W}_{t_4}$ where $t_1 < t_2 < t_3 < t_4$ are independent

-   Each of the components of ${\bf W}_t$ has continuous trajectories

### Ito's Lemma

We have seen that given the trajectory of a deterministic dynamical system, $y_t = f(t, {X_t})$, its behaviour over a infinitesimal time-step is described by the following differential equation:

$$dy = \frac{\partial f}{\partial t}dt + \sum_{n=1}^N \frac{\partial f}{\partial X_{i,t}} d X_{i,t}$$

where $\{X_t\}$ is a set of deterministic external factors. But what if the external factors are Wiener processes, e.g. in the most simple case
$f(t,W_t)$?. We might be tempted to just reuse the previous equation:

$$dy = \frac{\partial f}{\partial t}dt + \frac{\partial f}{\partial W_t} dW_t$$

however, one of the peculiarities of the Wiener process is that this equation is incomplete, since there is an additional term at this order of the expansion. There are different ways to derive this result,
typically starting from the discrete Wiener process (random walk), but a simple non-rigorous argument can be made by expanding the differential to second order in the Taylor series:

$$dy = \frac{\partial f}{\partial t}dt + \frac{\partial f}{\partial W_t} dW_t +  \frac{1}{2}\frac{\partial^2 f}{\partial t^2}dt^2 + \frac{1}{2} \frac{\partial^2 f}{\partial W_t^2} dW_t^2 + \frac{\partial^2 f}{\partial t \partial W_t}dt dW_t$$

and take the expected value of this differential conditional to the
filtration at t: 

$$\begin{aligned}
E[dy|F_t] = \frac{\partial f}{\partial t}dt + \frac{\partial f}{\partial W_t} E[dW_t|F_t] +  \frac{1}{2}\frac{\partial^2 f}{\partial t^2}dt^2 \nonumber \\ + \frac{1}{2} \frac{\partial^2 f}{\partial W_t^2} E[dW_t^2|F_t] + \frac{\partial^2 f}{\partial t \partial W_t}dt E[dW_t|F_t] 
\end{aligned}$$ 

The key for the argument is that whereas $E[dW_t|F_t] = 0$, we have $E[dW_t^2|F_t] = dt$, getting:

$$E[dy|F_t] = \frac{\partial f}{\partial t}dt + \frac{1}{2}\frac{\partial^2 f}{\partial t^2}dt^2 + \frac{1}{2} \frac{\partial^2 f}{\partial W_t^2} dt$$

so if we keep only terms at first order in the expansion:

$$E[dy|F_t] = (\frac{\partial f}{\partial t} + \frac{1}{2} \frac{\partial^2 f}{\partial W_t^2})dt + O(dt^2)$$
we have an extra term coming from the variance of the Wiener process, whose expected value is linear in $dt$. This motivates us to propose the following expression for the differential of a function of the Wiener
process, the so-called Ito's lemma: 

$$\boxed{
dy = (\frac{\partial f}{\partial t} + \frac{1}{2} \frac{\partial^2 f}{\partial W_t^2})dt + \frac{\partial f}{\partial W_t} dW_t 
}$$ 

The same argument can be applied for a multivariate Wiener process. Let us for example analyze the case of a function of two correlated Wiener processes, $y = f(t, W_{1t}, W_{2t})$. Expanding to second order
in a Taylor series we get: 

$$\begin{aligned}
dy = \frac{\partial f}{\partial t}dt + \frac{\partial f}{\partial W_{1t}} dW_{1t} +   \frac{\partial f}{\partial W_{2t}} dW_{2t} \nonumber \\ + \frac{1}{2}\frac{\partial^2 f}{\partial t^2}dt^2 + \frac{1}{2} \frac{\partial^2 f}{\partial W_{1t}^2} dW_{1t}^2 + 
\frac{1}{2} \frac{\partial^2 f}{\partial W_{2t}^2} dW_{2t}^2  \nonumber \\
+ \frac{\partial^2 f}{\partial t \partial W_{1t}}dt dW_{1t} + 
\frac{\partial^2 f}{\partial t \partial W_{2t}}dt dW_{2t} +
\frac{\partial^2 f}{\partial W_{1t} \partial W_{2t}}d W_{1t} dW_{2t}
\end{aligned}$$ 

Now, using the expected value argument and keeping only
terms $O(dt)$: 

$$\begin{aligned}
E[dy|F_t] = \frac{\partial f}{\partial t}dt + \frac{1}{2} \frac{\partial^2 f}{\partial W_{1t}^2} dt + 
\frac{1}{2} \frac{\partial^2 f}{\partial W_{2t}^2} dt +
\frac{\partial^2 f}{\partial W_{1t} \partial W_{2t}} \rho_{12} dt
\end{aligned}$$ 

where we have used
$E[d W_{1t} dW_{2t} |F_t] = \rho_{12} dt$ as discussed in section [3.5](#MultivariateWiener){reference-type="ref"
reference="MultivariateWiener"}. This motivates the expression for the two-dimensional Ito's lemma: 

$$\begin{aligned}
d y = (\frac{\partial f}{\partial t} + \frac{1}{2} \frac{\partial^2 f}{\partial W_{1t}^2} + 
\frac{1}{2} \frac{\partial^2 f}{\partial W_{2t}^2}  +
\frac{\partial^2 f}{\partial W_{1t} \partial W_{2t}} \rho_{12}) d t  \nonumber \\ + \frac{\partial f}{\partial W_{1t}} d W_{1t} +  \frac{\partial f}{\partial W_{2t}} d W_{2t}
\end{aligned}$$

### Integrals of the Wiener process 

A firs relevant integral of the Wiener process is:

$$I_{1t} = \int_0^t f(u) dW_u$$ 

What is the distribution of $I_{1t}$? A simple way to deduce it is to discretize the integral and then take again the continuous limit:

$$I_{1t} = \lim_{\Delta \rightarrow 0} \sum_{i=0}^{N-1} f(u_i) (W_{u_{i+1}} - W_{u_i})$$

where $\Delta = t / N$, $u_i = \Delta i$. This is a sum of independent Gaussian random variables, since by definition the increments of the Wiener process are independent. Therefore its distribution is itself
Gaussian [^1]. Its mean is easily computed as:

$$E[I_{1t}|F_0] = \lim_{\Delta \rightarrow 0}  \sum_{i=0}^{N-1} f(u_i) E[(W_{u_{i+1}} - W_{u_i})|F_0] =$$

For the variance, we could simply use the result that the variance of independent variables is the sum of variances, but it is instructive to compute it directly over the discrete expression:

$$E[I_{1t}^2|F_0] = \lim_{\Delta \rightarrow 0} \sum_{i=0}^{N-1}  \sum_{j=0}^{N-1}   f(u_i)  f(u_j) E[(W_{u_{i+1}} - W_{u_i})(W_{u_{j+1}} - W_{u_j})|F_0]$$

The computation of $E[(W_{u_{i+1}} - W_{u_i})(W_{u_{j+1}} - W_{u_j})|F_0]$ needs to consider two cases. When $i \neq j$ the expectation is zero, since increments of the Wiener process are independent. This is no longer the
case of $i = j$, for which we have $E[(W_{u_{i+1}} - W_{u_i})^2|F_0] = u_{i+1} - u_i = \Delta$. Therefore:

$$E[(W_{u_{i+1}} - W_{u_i})(W_{u_{j+1}} - W_{u_j})|F_0] = \delta_{i,j} \Delta$$

Plugging this into the previous equation:

$$E[I_{1t}^2|F_0] = \lim_{\Delta \rightarrow 0} \Delta \sum_{i=0}^{N-1}  f^2(u_i) = \int_0^t f^2(u) du$$

Therefore, the distribution of $I_{1t}$ is given by:

$$I_{1t} \sim N(0, \int_0^t du f^2(u))$$ 

Notice that once we have motivated the solution by using a discretization of the equation, we can directly skip it and use the continuous version, for instance:

$$\begin{aligned}
E[I_{1t}^2|F_0] = \int_0^t \int_0^t f(u) f(u') E[dW_u dW_{u'}] \nonumber \\ = \int_0^t \int_0^t du du' f(u) f(u') \delta(u-u') du = \int_0^t f^2(u) du
\end{aligned}$$ 

Let us now move into the second relevant integral of the
Wiener process, namely: 

$$I_{2t} = \int_0^t du f(W_u)$$ 

What is the distribution of this random variable? In this case, applying the discretization argument does not provide a direct simple path to figure out the distribution, since we have a sum of correlated variables (e.g. $f(W_{u_i})$ and $f(W_{u_j})$ are correlated over the common paths shared by them, say if $u_i < u_j$, the path below $u_i$). We can use Ito's lemma to advance our comprehension:

$$d(u f(W_u)) = u df(W_u) + f(W_u) du$$ 

which being linear it does not have the Ito's convexity terms. Essentially we can then use integration by parts: 

$$\int_0^t du f(W_u) = t f(W_t) - \int_0^t u df(W_u)$$ 

Using again Ito's lemma, now on $f(W_u)$:

$$df(W_u) = \frac{\partial f}{\partial W_u} dW_u + \frac{1}{2} \frac{\partial^2f }{\partial W_u^2} du$$

we get:

$$\int_0^t du f(W_u) = t f(W_t) - \int_0^t u \frac{\partial f}{\partial W_u} dW_u - \frac{1}{2} \int_0^t u\frac{\partial^2 f}{\partial W_u^2} du$$

At this point we cannot proceed further in general unless we specify specific functions. For instance, the most simple non trivial case is the linear function $f(W_u) = W_u$. Applying this formulation:

$$\int_0^t W_u du = t W_t - \int_0^t u dW_u = \int_0^t (t - u) dW_u$$

which now we can identify as a specific case of the previous integral, with $f(u) = t - u$. The distribution is therefore:

$$\int_0^t W_u du \sim N(0, \frac{t^3}{3})$$ 

where we have used $\int_0^t (t-u)^2 du = \frac{t^3}{3}$

### Simulation of the Wiener process

#### Univariate processes

We can simulate the Wiener process using a discretization like the Euler scheme for deterministic processes. Again, defining a grid $t_i = t_0 + \Delta * i$, $i = 0, .., N$, where $\Delta = \frac{t_1 - t_0}{N}$, we can exploit directly the Wiener process properties to get:

$$dW_t \rightarrow W_{t_{i+1}} - W_{t_i} \sim N(0, \Delta)$$ 

So we can simulate numerically the Wiener process simply as:

$$W_{t_{i+1}} =  W_{t_i} + \sqrt{\Delta} Z$$ 

where $Z$ is a standard normal distribution.

SIMULATION DISCRETE

Alternatively, we can simulate complete paths of the Wiener process by exploiting its connection to Gaussian processes. Using a Gaussian process framework we get the following results:

SIMULATION GAUSSIAN PROCESS

#### Multivariate processes

Let us now simulate a multivariate Wiener process of dimension N. The strategy in this case is to start simulating N independent Wiener processes and then use them to generate the correlated paths. This can
be done using the Cholesky decomposition of the correlation matrix $\Sigma$. Since $\Sigma$ is symmetric and positive define, the decomposition reads: $$\Sigma = L L^T$$ where $L$ is a lower triangular matrix. If we now we have a vector of N uncorrelated Wiener increments
$d \hat{{\bf W_t}}$, we can obtain the correlated process by using $L$ such as $d {\bf W_t} = L d \hat{{\bf W_t}}$. We can see that this vector has the distribution of the multivariate Wiener process increment:

$$\begin{aligned}
E[d {\bf W_t} d {\bf W_t}^T] = E[L d \hat{{\bf W}}_{t} d \hat{{\bf W}}_{t}^T L^T]  \nonumber \\ = L E[d \hat{{\bf W}}_{t} d \hat{{\bf W}}_{t}^T] L = L L^T dt = \Sigma dt
\end{aligned}$$ 

where we have used $E[d \hat{{\bf W}}_{t} d \hat{{\bf W}}_{t}^T] = I dt$ where $I$ is the identity matrix.

It is illustrative to show the case for a two-dimensional multivariate Wiener process. The correlation matrix reads: 

$$\begin{aligned}
\begin{bmatrix}
1 & \rho  \\ \rho & 1
\end{bmatrix}
\end{aligned}$$ 

The Cholesky lower triangular matrix is simply:

$$\begin{aligned}
L = 
\begin{bmatrix}
1 & 0  \\ \rho & \sqrt{1-\rho^2}
\end{bmatrix}
\end{aligned}$$ 

Notice that, as expected: 

$$\begin{aligned}
L L^T = 
\begin{bmatrix}
1 & 0  \\ \rho & \sqrt{1-\rho^2}
\end{bmatrix}
\begin{bmatrix}
1 & \rho  \\ 0 & \sqrt{1-\rho^2}
\end{bmatrix} = 
\begin{bmatrix}
1 & \rho\\ \rho & 1
\end{bmatrix}
\end{aligned}$$ 

We can also write the decomposition in equations:

$$\begin{aligned}
d W_{1t} &=& d \hat{W}_{1t} \nonumber \\
d W_{2t} &=& \rho d \hat{W}_{1t} + \sqrt{1-\rho^2}  d \hat{W}_{2t}
\end{aligned}$$

## Basic stochastic processes

### Brownian motion with drift

The most simple stochastic process using the Wiener process as a building block is the Brownian motion with drift:

$$d S_t = \mu_t dt + \sigma_t d W_t$$ 

Here we are essentially shifting and rescaling the Wiener process to describe dynamical systems whose stochastic fluctuations have a deterministic non-zero mean $mu_t$
(drift) and arbitrary variance, the latter controlled by the so-called volatility $\sigma_t$. In practice, this is the process to use for any real application of stochastic calculus to model random time-series, since the simple Wiener process is simply too restrictive to describe
any real process. The name Brownian motion comes actually from the early application of this kind of process to describe the random fluctuations of pollen suspended in water observed by English botanist Robert Brown
in 1827. The actual modelling of this process would be pioneered by Albert Einstein [@EinsteinBrownian], in one of the four papers published in 1905, his \"annus mirabilis\", each of them transformative of its
respective field.

The distribution of $dS_t$ is easily derived by using the property that multiplying and summing scalars to a Gaussian random variable ($dW_t$) yields another Gaussian variable. Hence since $dW_t \sim N(0, t)$ then
we have: 

$$d S_t \sim N(\mu_t, \sigma_t^2 dt)$$ 

This stochastic differential equation can be integrated to get the solution for arbitrary times:

$$S_t = S_0 + \int_0^t \mu_u du + \int_0^t \sigma_u d W_u$$ 

which again follows a Gaussian distribution:

$$S_t \sim N(S_0 + \int_0^t \mu_u du, \int_0^t \sigma_u^2 du)$$ 

where we have used the properties of the stochastic integral discussed in section
[3.6.1](#IntegralWiener){reference-type="ref"
reference="IntegralWiener"}.

#### Connection to Gaussian processes

The Brownian motion is also a Gaussian process, since any finite set $X_{†_1}, X_{t_2}, X_{t_3}, ..., X_{t_n}$ follows a multivariate Gaussian process. The kernel of the Brownian process is simply to
derive: 

$$\begin{aligned}
k(t_1, t_2) = cov[X_{t_1}, X_{t_2}] = E[\int_0^{t_1} \sigma_u dW_u \int_0^{t_2} \sigma_v dW_v] = \int_0^{min(t_1, t_2}  \sigma_u^2 du
\end{aligned}$$ 

If $\sigma_t = \sigma$, i.e. is a constant, we hav simply:

$$\begin{aligned} k(t_1, t_2) = \sigma^2 min(t_1, t_2)
\end{aligned}$$ 

which is the kernel of the Wiener process rescaled by
$\sigma^2$, as expected given the construction of the Brownian process.

#### Simulation

Similarly to the Wiener process, simulation can be carried out using a discretization scheme. To improve numerical stability and convergence it is convenient to integrate first the distribution between points in the
simulation grid $t_0, ..., t_N$, $t_{i+1} = t_i + \Delta$, namely:

$$S_{t_{i+1}} |F_{t_n} \sim N(S_{t_i} + \int_{t_i}^{t_{i+1}} \mu_u du, \int_{t_i}^{t_{i+1}} \sigma^2_u du)$$

If we have a generator of standard Gaussian random numbers $Z$, we can perform the simulation using:

$$S_{t_{i+1}} = S_{t_i} + \int_{t_i}^{t_{i+1}} \mu_u du + \left(\int_{t_i}^{t_{i+1}} \sigma^2_u du \right)^{1/2} Z$$

If $\mu_u$ and $\sigma_u$ are smooth functions of time and $\Delta$ is small enough such that the variation in the interval is negligible, we can approximate the integrals:

$$S_{t_{i+1}} |F_{t_n} \sim N(S_{t_i} + \mu_{t_i} \Delta,  \sigma^2_{t_i} \Delta)$$

or simply:

$$S_{t_{i+1}} = S_{t_i} + \mu_{t_i} \Delta + \sigma_{t_i} \sqrt{\Delta} Z$$

SIMULATION DISCRETE

Alternatively, we can use the connection to Gaussian processes to perform the simulations using standard packages:

SIMULATION GAUSSIAN

#### Estimation

If we have a set of observations of a process $D = \{S_{t_0}, ..., S_{t_N}\}$ that we want to model as a Brownian
motion, we need to find the value of the parameters of the process that best fit the data.

Let us consider for simplicity that $\mu_t = \mu$ and
$\sigma_u = \sigma$. As discussed in the context of Bayesian models, a general estimation process models the parameters as random variables that capture our uncertainty about their exact values, which comes from
the fact that the sample is finite, or also in general because the data generation process will not necessarily be the one we are proposing, being models a simplification of reality. In this setup, the best
inference of the parameters is carried out by computing the posterior distribution $P(\mu, \sigma^2|D, I_P)$ where $I_P$ represents the prior information about the parameters.

Since as shown in the previous section we can write the process between observations as
$S_{t_{i+1}} - S_{t_i} = \mu \Delta + \sigma \sqrt{\Delta} Z$ with $Z\sim N(0,1)$, this is equivalent to fitting a Bayesian linear regression model om $S_{t_{i+1}} - S_{t_i}$ with an intercept $\mu \Delta$ and a noise term $\epsilon \sim N(0, \sigma^2 \Delta)$. As
we shown in chapter [\[ch:Bayesian\]](#ch:Bayesian){reference-type="ref"
reference="ch:Bayesian"}, if we model the prior distributions of the parameters as a Normal Inverse Gamma (NIG), meaning that:

$$\begin{aligned}
    \mu \Delta | \sigma^2 \Delta \sim N(\mu_0 \Delta, \sigma^2 \Delta V_0) \\
    \sigma^2 \Delta \sim IG(\alpha_0, \beta_0)
\end{aligned}$$ 

where $V_0$, $\mu_0$, $\alpha_0$, $\beta_0$ are parameters that define the prior, this distribution is a conjugate prior of the likelihood:

$$P(D|\mu \Delta, \sigma^2 \Delta, P_I) = \Pi_{n=1}^N \frac{1}{\sqrt{2\pi\Delta^2\sigma^2}} e^{-\frac{(S_{t_n} - S_{t_{n-1}} - \Delta \mu)^2}{2 \Delta^2 \sigma^2}}$$

Therefore, the posterior is also a NIG, with updated parameters:

$$\begin{aligned}
    \mu \Delta | D, \sigma^2  \Delta \sim N(\mu_N \Delta, \sigma^2 \Delta V_N) \\
    \sigma^2 \Delta | D \sim IG(\alpha_N, \beta_N)
\end{aligned}$$ 

To get the updated parameters from the general equations, bear in mind that in this representation with only an
intercept our feature-set can be seen as a N dimensional vector ${\bf X} = (1, ..., 1)$. Therefore: 

$$\begin{aligned}
    V_N = (V_0^{-1} + N)^{-1} \\
   \mu_N \Delta = \mu_0 \Delta \frac{V_N}{V_0} + \frac{1}{V_0^{-1} + N } \sum_{n=1}^N (S_{t_{n}} - S_{t_{n-1}})\\
   \alpha_N = \alpha_0 + N/2 \\
   \beta_N = \beta_0 + \frac{1}{2}\left(\sum_{n=1}^N(S_{t_n}-S_{t_{n-1}})^2 + \mu_0^2 \Delta^2 V_0^{-1} -\mu_N^2 \Delta^2 V_N^{-1} \right)
\end{aligned}$$ 

The predictive marginal for the $\mu \Delta$ parameter requires integrating out the $\sigma^2 \Delta$, resulting in:

$$\mu \Delta |D \sim T(\mu_N \Delta, \frac{\beta_N}{\alpha_N} V_N, 2 \alpha_N)$$

where $T$ is the Student's distribution.

Following our discussion in chapter [\[ch:Bayesian\]](#ch:Bayesian){reference-type="ref"
reference="ch:Bayesian"}, the best estimator of parameters extracted from the posterior in a mean squared error minimizing sense is to compute the mean of the posterior marginals. For $\sigma^2 \Delta$, we
have: 

$$\begin{aligned}
E[\sigma^2 \Delta |D, I_P] = \frac{\beta_N}{\alpha_N-1}=  \frac{\beta_0}{\alpha_0 -1 + N/2} + \nonumber \\ \frac{1}{2 \alpha_0 + N -1}\left(\sum_{n=1}^N(S_{t_n}-S_{t_{n-1}})^2+\mu_0^2 \Delta^2 V_0^{-1} -\mu_N^2 \Delta^2 V_N^{-1} \right) 
\end{aligned}$$ 

whereas for $\mu$ we have:

$$E[\mu \Delta|D, I_P] = \mu_N \Delta = \mu_0 \Delta \frac{V_0}{V_N} + \frac{1}{V_0^{-1} + N} \sum_{n=1}^N (S_{t_{n}} - S_{t_{n-1}}))$$

A special case deserved our attention: if we take the limit in the prior distribution $V_0\rightarrow\infty$ and
$\alpha_0, \beta_0 \rightarrow 0$, the prior distribution becomes a non-informative or Jeffrey's prior, with
$p(\sigma^2 \Delta) \sim 1/(\sigma^2 \Delta)$, and
$p(\mu\Delta|\sigma^2\Delta)$ becoming a flat prior. Jeffrey's prior is considered the best choice to describe non-informative priors of scale parameters as is the case of $\sigma^2 \Delta$. In this situation:

$$\begin{aligned}
E[\mu \Delta|D, I_P] \rightarrow \mu_{MLE}\Delta = \frac{1}{N} \sum_{n=1}^N (S_{t_{n}} - S_{t_{n-1}})\\ 
E[\sigma^2 \Delta|D, I_P] \rightarrow \frac{N}{N -1} \sigma_{MLE}^2 \Delta \nonumber \\ \frac{N}{N -1}\left(\frac{1}{N} \sum_{n=1}^N(S_{t_n}-S_{t_{n-1}})^2 -\left(\frac{1}{N} \sum_{n=1}^N (S_{t_{n}} - S_{t_{n-1}})\right)^2 \right) 
\end{aligned}$$ 

which are the maximum likelihood estimators (MLE) of the
mean and the variance of a Gaussian distribution [^2], which is expected for a non-informative prior since 1) for a Gaussian distribution the mean and the mode coincide, 2) maximizing the posterior with the
non-informative prior is equivalent to maximizing the likelihood. MLE estimators are the standard approach to learn the parameters of stochastic processes in many practical situations, since the Bayesian
estimations might become intractable for more complex processes as the Brownian motion. However, we must keep in mind their limitations, particularly that they neglect any prior information that might be useful in certain setups, and that they throw away the rest of the
information contained in the posterior distribution.

We will see in later chapters that keeping the full posterior distribution can be relevant when we want to incorporate model estimation uncertainty into the inferences that are derived using stochastic processes. For instance, in the presence of a non-negligible
estimation uncertainty of the parameters of our Brownian process, the correct predictive distribution of the next value of the process given its past history is actually given by:

$$S_{t_{N+1}}|S_{t_N}, D, I_P \sim T(\mu_N \Delta, \frac{\beta_N}{\alpha_N}(1+V_N), 2\alpha_N)$$

If we consider a non-informative prior, this becomes:

$$S_{t_{N+1}}|S_{t_N}, D, I_P \sim T(\mu_{MLE} \Delta, \sigma_{MLE}^2(1 + \frac{1}{N}), N)$$

This is to be compared with the inference using the MLE estimator, which would essentially plug the point MLE estimator into the Brownian process, yielding:

$$S_{t_{N+1}}|S_{t_N}, D, I_P \sim N(\mu_{MLE} \Delta, \sigma_{MLE}^2 \Delta)$$

The mean and the mode of both distributions is the same, namely $\mu_{MLE} \Delta$, but the Student distribution has fatter tails than the Gaussian distribution, reflecting the extra uncertainty coming from
the estimation error. Only in the case of having a very large data-set $N\rightarrow \infty$, both distributions converge, as in this limit the Student distribution becomes a Gaussian $N(\mu_{MLE} \Delta, \sigma_{MLE} \Delta)$. Another way of seeing this is to interpret the variance term of the Student distribution as the sum
of two terms: the first one coming from the intrinsic noise of the Brownian process, and the second one, the $1/N$ correction, coming from the estimation uncertainty.

#### Dimensional analysis

In order to reason about stochastic processes it is important to keep track or the units of their parameters. This can also be useful as a consistency check on the estimators derived, for instance. We will use a
brackets notation for dimensional analysis. For the case of the Brownian motion we write: $$= [\mu_t] [dt] + [\sigma_t] [dW_t]$$ In here, we know that $[dt]$ has time units, for instance seconds, hours, or days. We
denote them generically as $[t]$ The Wiener process being distributed as $dW_t \sim N(0, dt)$ has therefore units of $[t]^{1/2}$, i.e. the square root of time. Therefore, the parameters have the following units:

$$\begin{aligned}
= [S] / [t] //
    [\sigma_t] = [S] / [t]^{1/2}
\end{aligned}$$ 

where we have denoted generically $[S]$ as the units of
the process. If for instance $S$ is modelling a price of a financial instrument in a given currency like dollars, the units are dollars: $[dS_t] = \$$. If additionally we are using seconds as time units, $[t] = s$. then we have $[\mu_t] = \$ / s$ and $[\sigma_t] = \$ / s^{1/2}$. We can see that these units are consistent with the Gaussian distribution for the evolution of $S_t$: the argument
of the exponential should be a-dimensional. Applying the previous units to the expression we can see that it is indeed the case:

$$= ([S] - [\mu_t] [t])^2 / ([\sigma_t]^2 [t]^2) = 1$$

#### Applications

The Brownian motion model has plenty of applications. In the financial domain it can be used to model financial or economical indicators for which there is no clear pattern in the time-series beyond potentially a drift to motivate a more sophisticated modelling, i.e. the time-series
is mostly unpredictable. Notice that the Brownian motion has a domain that extends from $(-\infty, \infty)$, so indicators that have a more restrictive domain might not be suitable for being modelled using the
Brownian motion process. A typical example are prices of financial instruments, which cannot on general grounds be negative. However, there might be exceptions to this rule, for instance if we are modelling
prices in a time - domain such as the probability of reaching negative values is negligible, the model might be well suited. For instance, when modelling intraday prices.

### Geometric Brownian motion

The geometric Brownian motion is a simple extension of the Brownian motion that introduces a constraint in the domain of the process, allowing only positive values. The stochastic differential equation is
the following one: 

$$d S_t = \mu_t S_t dt + \sigma_t S_t d W_t$$ 

In order to find the distribution of $S_t$ for arbitrary times, let us apply Ito's lemma over the function $f(S_t) = \log S_t$. Such ansatz is motivated by looking at the deterministic part of the equation,
$dS_t = \mu_t S_t dt$, which can be rewritten as
$d \log S_t = \mu_t dt$. Coming back to the stochastic differential equation: 

$$\begin{aligned}
d \log S_t = \frac{1}{S_t} d S_t - \frac{1}{2}\frac{1}{S_t^2} \sigma_t^2 S_t^2 dt = \nonumber \\
= (\mu_t - \frac{1}{2} \sigma_t^2)dt + \sigma_t d W_t
\end{aligned}$$ 

This is the stochastic differential equation of the
Brownian motion, which we already now how to integrate from the previous section:

$$\log S_t = \log S_0 + \int_0^t du (\mu_u - \frac{1}{2} \sigma_u^2) +  \int_0^t \sigma_u d W_u$$

which means that $\log S_t$ follows a Gaussian distribution $\log S_t \sim N(\log S_0 + \int_0^t du (\mu_u - \frac{1}{2} \sigma_u^2), \int_0^u \sigma_u^2 du)$. The distribution of $S_t$ is the well studied Log-normal distribution,
which by definition is the distribution of a random variable whose logarithm follows a Gaussian distribution:

$$S_t \sim LN(\log S_0 + \int_0^t du (\mu_u - \frac{1}{2} \sigma_u^2), \int_0^u \sigma_u^2 du)$$

We can also simply write:

$$S_t = S_0 \exp(\int_0^t du (\mu_u - \frac{1}{2} \sigma_u^2) +  \int_0^t \sigma_u d W_u)$$

An interesting property of the Log-normal distribution is the simple solution for its moments: $$\begin{aligned}
X \sim LN(\mu, \sigma^2) \nonumber \\
E[X^n] = e^{n \mu + \frac{1}{2} n^2 \sigma^2}
\end{aligned}$$ 

In particular, the mean of the distribution is
$E[X] = e^{\mu + \sigma^2/2}$ which we will use in multiple applications. This means, coming back to the Geometric Brownian Motion, that:

$$E[S_t] = S_0 e^{\int_0^t du (\mu_u - \frac{1}{2} \sigma_u^2) +  \frac{1}{2} \int_0^t \sigma_u^2 du} = S_0 e^{\int_0^t \mu_u du}$$

### Arithmetic Average of the Brownian motion

As the name suggests, this is a derived process from the standard Brownian motion in which the latter is averaged continuously up to a certain time $T$: 

$$\begin{aligned}
M_t = \frac{1}{T-t}\int_t^T S_u du 
\end{aligned}$$ 

To derive its distribution we integrate by parts the
Brownian process: 

$$\begin{aligned}
M_t = \frac{T S_T - t S_t}{T-t} - \frac{1}{T-t}\int_t^T u d S_u = \nonumber 
= S_t + \int_t^T \frac{T-u}{T-t} dS_u
\end{aligned}$$ 

The result is the sum of two different parts, one is the
evolution of the Brownian motion up to time $t$, where averaging starts. The second averages the variations of the Brownian motion. Since both terms are independent and Gaussian their distribution is simply:

$$M_t \sim N(S_0, t +  \frac{1}{3} (T-t))$$ 

where we have used:
$$\int_t^T (\frac{T-u}{T-t})^2 du = \frac{1}{3} (T-t)$$ 

Notice that the variance of the averaged part is smaller than the variance up to t. This makes sense, since taking averages smooths out the random behaviour of
the process.

### Orstein-Uhlenbeck process

The Orstein - Uhlenbeck process is an extension of the Brownian motion process in which the drift term is modified to prevent large deviations from the mean $\mu$. This is achieved by making the drift penalize those
deviations: 

$$d S_t = \theta (S_t - \mu) dt + \sigma_t d W_t$$ 

The strength of the penalty is controlled by a parameter $\theta \leq 0$, which is called the mean reversion speed: the larger this parameter, the faster the process $S_t$ reverts to the mean. Such property of mean
reversion is not unique to the Orstein - Uhlenbeck process, but the latter is probably the most simple way to achieve this effect in a stochastic differential equation, allowing for the computation of
closed-form solutions for the probability distribution of the process. To derive it, we use the following ansatz: 

$$\begin{aligned}
d(e^{-\theta t} S_t) = -\theta e^{-\theta t} S_t dt + e^{-\theta t} dS_t = \nonumber \\
e^{-\theta t}(-\mu dt + \sigma_t dW_t)
\end{aligned}$$ 

Integrating this equation: 

$$\begin{aligned}
e^{-\theta t} S_t - S_0 = - (e^{-\theta t} - 1) \mu + \int_0^t e^{-\theta u} \sigma_u dW_u
\end{aligned}$$ 

Finally: 

$$S_t = S_0 e^{-\theta t} + \mu (1 - e^{-\theta t}) + \int_0^t e^{\theta (t-u)} \sigma_u dW_u$$

#### Other mean reverting processes

CIR $$d S_t = \theta (S_t - \mu_t) dt + \sigma_t S_t^{1/2} d W_t$$

### Brownian bridge

Another simple extension of the Wiener process is the Brownian bridge, that we denote as $B_t$. It defines a stochastic process within a time interval $[0,T]$ that behaves as a Wiener process with the exception of
having an extra constraint, namely that $B_T = 0$ (in addition to $B_0 = 0$ as in the Wiener process). Such process can be constructed from a single Wiener process $W_t$ as follows:

$$B_t =  W_t - \frac{t}{T} W_T$$ 

In order to derive the distribution of $B_t$, we decompose it in two independent Gaussian variables:

$$B_t =  W_t - \frac{t}{T} (W_T - W_t + W_t) = (1-\frac{t}{T})W_t - \frac{t}{T}(W_T - W_t)$$

where the two terms of the expression are independent by using the property that non overlapping differences of Wiener processes are independent. This is therefore the distribution of two independent Gaussian variables, which we know is also Gaussian:

$$B_t \sim N(0, t(1 - \frac{t}{T}))$$ 

where we have used:

$$\begin{aligned}
E[(1-\frac{t}{T})W_t|F_0]  - E[\frac{t}{T}(W_T - W_t)|F_0] = 0 \\
E[((1-\frac{t}{T})W_t)^2|F_0]  + E[(\frac{t}{T}(W_T - W_t))^2|F_0] = \nonumber \\ (1-\frac{t}{T})^2 t + (\frac{t}{T})^2 (T-t) = t(1 - \frac{t}{T})
\end{aligned}$$ 

The result fits well our expectation of such process:
for $t = 0$ and $t = T$, the process has no variance, since those points correspond to the constraints where the process is set to zero. Given those constraints, and the symmetry of the Brownian bridge with respect
to the transformation $t \rightarrow T-t$, we expect the maximum variance to be at the half-point $T/2$, which is indeed the maximum of the function $t(1-- \frac{t}{T})$

#### Connection to Gaussian processes

The Brownian bridge is also a Gaussian process, with the following kernel: 

$$\begin{aligned}
k(t_1,t_2) = cov[B_{t_1} B_{t_2}] = E[(W_{t_1} - \frac{t_1}{T} W_T])(W_{t_2} - \frac{t_2}{T} W_T)] = \nonumber \\ min(t_1, t_2) -  \frac{t_2}{T} t_1 -  \frac{t_2}{T} t_1 + \frac{t_1 t_2}{T} = min(t_1, t_2) - \frac{t_1 t_2}{T}
\end{aligned}$$

#### Simulation

TO DO

#### Applications

Brownian bridges or more realistic but similarly constructed processes (e.g. using the Brownian motion as the primitive instead of the Wiener process, or specifying fixed but non-zero boundaries), can be used to
model situations where there is no uncertainty about the final value of a stochastic process. This is for instance the case of financial instruments like bonds, in particular zero-coupon bonds, which are bonds
that simply return their principal at maturity without paying a coupon. They are also known to be more suitable for simulation than the underlying Wiener process, which can be written as a function of the
Brownian bridge simply as: 

$$W_t = B_t + \frac{t}{T} W_T$$ 

By simulating the Brownian bridge and a single standard Gaussian variable $Z\sim N(0,1)$, so that $W_T = \sqrt{T}Z$, we can generate samples of the Wiener process.

## Jump processes

WIP

## Exercises

1.  Derive the Crank - Nikolson scheme discretization of the inflation targeting model. Simulate it numerically and compare with the exact solution

2.  Use Ito's lemma to derive the differential of:

    -   $f(W_t) = W_t^2$

    -   $f(W_t) = t W_t$

    -   $f(W_t) = \exp(W_t)$

[^1]: The demonstration is relatively straight-forward by computing the characteristic function of a sum of independent random Gaussian variables

[^2]: Actually the bias corrected one, which can be achieved by the factor $N/(N-1)$ as it is well known that the MLE estimator of the variance of a Gaussian distribution is biased, i.e. $E[\sigma_{MLE}^2] = \frac{N-1}{N} \sigma^2$. The Bayesian derivation in this regard is more consistent than the MLE estimation. Notice that the MLE estimator actually corresponds to $\beta_N/\alpha_N$ in the case of a non-informative prior
