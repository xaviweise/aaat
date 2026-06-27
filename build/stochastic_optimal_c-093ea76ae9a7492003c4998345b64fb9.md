(stochastic_optimal_control)=
# Stochastic Optimal Control

## Introduction

Stochastic optimal control (SOC) is the mathematical theory of making sequential decisions in systems whose state evolves stochastically over time. The agent observes the current state of the system, applies a control, and the system transitions to a new state according to a stochastic law. The goal is to choose a sequence of controls — a *policy* — that minimises an expected cumulative cost over a finite or infinite horizon. SOC extends classical optimal control theory, which addresses deterministic systems, to the regime where the state dynamics are driven by random processes such as the Wiener process introduced in chapter {ref}`stochastic_calculus`.

The mathematical tools developed in this chapter provide the foundation for two distinct classes of trading problems addressed later in this book: *optimal execution scheduling* (chapter {ref}`optimal_execution`) and *optimal market making* (chapter {ref}`optimal_market_making`). In the execution problem, the agent must liquidate an inventory at minimum expected cost while controlling timing risk; the state is the remaining inventory and the control is the trading rate. In the market making problem, the agent must quote bid and ask prices dynamically to maximise expected profit while managing inventory risk; the state is the inventory and the control is the spread quoted around the mid-price. Despite the different economic contexts, both problems share the same mathematical structure: a stochastic dynamical system, a cost functional, and a backward equation — the Bellman equation in discrete time, or the Hamilton–Jacobi–Bellman equation in continuous time — that determines the value of the optimal policy at each state and time.

The chapter is organised as follows. We begin with *discrete-time dynamic programming* ({ref}`sec:soc_dp`), which introduces Bellman's principle of optimality and the backward induction algorithm in the simplest setting. We then extend to *continuous-time* control ({ref}`sec:hjb`), where the state follows a stochastic differential equation and the optimal value function satisfies the Hamilton–Jacobi–Bellman (HJB) partial differential equation. We next present the *variational approach* ({ref}`sec:el`), which simplifies the optimisation to an ordinary differential equation when the stochastic noise enters the cost functional only through the trajectory of the state — a structure that appears in the Almgren–Chriss model. Finally, we derive the *Linear–Quadratic Stochastic Control* (LQSC) framework ({ref}`sec:lqsc`), which yields closed-form solutions via Riccati equations and is the method of choice for execution and market making problems with quadratic cost structures.

(sec:soc_dp)=
## Dynamic programming in discrete time

### Problem setup

We consider a system evolving over discrete time steps $k = 0, 1, \ldots, N$, where $N$ is the terminal time. At each step $k$ the system is in state $x_k \in \mathcal{X} \subseteq \mathbb{R}^n$ and the agent selects a control $u_k \in \mathcal{U}(x_k) \subseteq \mathbb{R}^m$ from a feasible set that may depend on the current state. The state then transitions according to the dynamics

$$x_{k+1} = f_k(x_k, u_k, w_k)$$

where $w_k$ is an exogenous random disturbance with known distribution that is independent of the past history of states and controls. Applying control $u_k$ in state $x_k$ incurs a running cost $c_k(x_k, u_k)$, and reaching terminal state $x_N$ incurs a terminal cost $\psi(x_N)$. The total cost of a sequence of controls $\mathbf{u} = (u_0, u_1, \ldots, u_{N-1})$ is

$$J(\mathbf{u}) = \sum_{k=0}^{N-1} c_k(x_k, u_k) + \psi(x_N)$$

This is a random variable because the state trajectory $(x_0, x_1, \ldots, x_N)$ depends on the random disturbances $(w_0, w_1, \ldots, w_{N-1})$. The objective is to find a *policy* $\pi = (\pi_0, \pi_1, \ldots, \pi_{N-1})$, where $\pi_k: \mathcal{X} \to \mathcal{U}$ maps states to controls, that minimises the *expected total cost*:

$$\min_\pi \, \mathbb{E}\left[\sum_{k=0}^{N-1} c_k(x_k, \pi_k(x_k)) + \psi(x_N) \,\Big|\, x_0\right]$$

A policy of this form — mapping the state to a control at each step — is called a *feedback* or *closed-loop* policy. The key result of dynamic programming is that the optimal policy has exactly this feedback structure: the optimal action at each step depends only on the current state, not on the full history of states and controls.

### Bellman's principle of optimality

The core insight behind dynamic programming is Bellman's *principle of optimality*: the tail of an optimal policy is itself optimal. Formally, if $(u_0^*, u_1^*, \ldots, u_{N-1}^*)$ is an optimal policy, then for any intermediate time $k$ and any state $x_k$ reachable under the optimal policy, $(u_k^*, u_{k+1}^*, \ldots, u_{N-1}^*)$ is an optimal policy for the sub-problem starting at time $k$ in state $x_k$.

This principle justifies decomposing the global optimisation into a sequence of local optimisations, solved backwards from the terminal time.

### The Bellman equation

Define the *value function* $V_k(x)$ as the minimum expected cost achievable from state $x$ at time $k$:

$$V_k(x) = \min_{\pi_k, \ldots, \pi_{N-1}} \mathbb{E}\left[\sum_{j=k}^{N-1} c_j(x_j, \pi_j(x_j)) + \psi(x_N) \,\Big|\, x_k = x\right]$$

The terminal value function is simply the terminal cost: $V_N(x) = \psi(x)$.

By the principle of optimality, applying the optimal first action $u_k^*$ and then following the optimal policy from the resulting state $x_{k+1}$ gives:

$$\boxed{V_k(x) = \min_{u \in \mathcal{U}(x)} \mathbb{E}_{w_k}\left[c_k(x, u) + V_{k+1}(f_k(x, u, w_k))\right]}$$

with $V_N(x) = \psi(x)$. This is the **Bellman equation** (or *dynamic programming equation*). It reduces the optimisation over sequences of controls into a sequence of single-step optimisations, each requiring only the value function at the next step. The optimal policy at step $k$ is recovered from the minimiser:

$$\pi_k^*(x) = \arg\min_{u \in \mathcal{U}(x)} \mathbb{E}_{w_k}\left[c_k(x, u) + V_{k+1}(f_k(x, u, w_k))\right]$$

### Backward induction algorithm

The Bellman equation defines a **backward induction** algorithm for computing the optimal value function and policy:

1. Initialise: set $V_N(x) = \psi(x)$ for all states $x$.
2. For $k = N-1, N-2, \ldots, 0$:
   - For each state $x \in \mathcal{X}$, compute:
     $$V_k(x) = \min_{u \in \mathcal{U}(x)} \mathbb{E}_{w_k}\left[c_k(x, u) + V_{k+1}(f_k(x, u, w_k))\right]$$
   - Record the minimiser as $\pi_k^*(x)$.

The algorithm sweeps backwards from the terminal time, propagating value information from the future into the current decision. Once all $V_k$ and $\pi_k^*$ are computed, the optimal forward trajectory is obtained by simulating the system under $\pi^*$ from $x_0$.

The feasibility of the algorithm depends on the structure of the problem. When $\mathcal{X}$ is finite and small, the expectation and minimisation can be computed explicitly. When $\mathcal{X}$ is continuous, the value function is defined over an uncountable domain, and special structure must be exploited to obtain tractable solutions. The LQSC framework in {ref}`sec:lqsc` provides one such tractable case.

### Example: discrete inventory liquidation

Consider a trader who must sell $X$ shares over $N$ time periods. Let the state be the remaining inventory $x_k \in \{0, 1, \ldots, X\}$ and the control be the number of shares sold in period $k$: $u_k \in \{0, 1, \ldots, x_k\}$. The inventory dynamics are $x_{k+1} = x_k - u_k$ (deterministic, no noise). The price in period $k$ is $S_k$ and the execution price is $P_k = S_k - \eta u_k$ (linear temporary impact). Suppose the price evolves as $S_{k+1} = S_k + \epsilon_{k+1}$ with $\epsilon_k$ i.i.d. zero-mean noise.

The total proceeds are $\sum_{k=0}^{N-1} u_k P_k = \sum_{k=0}^{N-1} u_k (S_k - \eta u_k)$, and we impose the constraint $\sum_{k=0}^{N-1} u_k = X$ (all shares must be sold). The expected total proceeds are:

$$\mathbb{E}\left[\sum_{k=0}^{N-1} u_k S_k - \eta \sum_{k=0}^{N-1} u_k^2\right]$$

Since prices follow a martingale ($\mathbb{E}[S_k] = S_0$) and the inventory $x_k = X - \sum_{j<k} u_j$ is determined by prior decisions, this problem has quadratic structure. Bertsimas and Lo {cite:p}`BERTSIMAS19981` show that the optimal policy under this formulation distributes the remaining inventory equally at each step: $u_k^* = x_k / (N - k)$, recovering the TWAP schedule. The value function is quadratic in the state, a structure that carries over to the continuous-time case and the LQSC framework.

(sec:hjb)=
## The Hamilton–Jacobi–Bellman equation

### From discrete to continuous time

The discrete-time Bellman equation can be extended to continuous time by taking the step size $\Delta t \to 0$. Consider the state dynamics

$$dX_t = \mu(X_t, u_t, t) \, dt + \sigma(X_t, t) \, dW_t$$

where $W_t$ is a standard Wiener process (see chapter {ref}`stochastic_calculus`), and the running cost $c(t, X_t, u_t) \, dt$ is incurred continuously. The state is $X_t \in \mathbb{R}^n$, the control is $u_t \in \mathcal{U}$, and the drift $\mu$ is allowed to depend on the control while the volatility $\sigma$ does not (for simplicity; this restriction can be relaxed). The value function is defined as:

$$J(t, x) = \min_{\{u_s\}_{t \leq s \leq T}} \mathbb{E}\left[\int_t^T c(s, X_s, u_s) \, ds + \psi(X_T) \,\Bigg|\, X_t = x\right]$$

and satisfies $J(T, x) = \psi(x)$. We seek the partial differential equation (PDE) that $J$ satisfies for $t < T$.

### HJB derivation

Applying the Bellman principle over the short interval $[t, t + dt]$:

$$J(t, x) = \min_{u \in \mathcal{U}} \, \mathbb{E}\left[c(t, x, u) \, dt + J(t + dt, X_{t+dt}) \,\Big|\, X_t = x\right]$$

Using Ito's lemma (chapter {ref}`stochastic_calculus`, {ref}`itos_lemma`) to expand $J(t + dt, X_{t+dt})$:

$$J(t + dt, X_{t+dt}) = J(t, x) + \frac{\partial J}{\partial t} dt + \frac{\partial J}{\partial x} dX_t + \frac{1}{2} \frac{\partial^2 J}{\partial x^2} (dX_t)^2$$

Taking expectations and using $(dX_t)^2 = \sigma^2(x,t) \, dt$ and $\mathbb{E}[dW_t] = 0$:

$$\mathbb{E}[J(t+dt, X_{t+dt}) | X_t = x] = J(t,x) + \left(\frac{\partial J}{\partial t} + \mu(x, u, t) \frac{\partial J}{\partial x} + \frac{1}{2}\sigma^2(x,t) \frac{\partial^2 J}{\partial x^2}\right) dt$$

Substituting back into the Bellman equation and rearranging:

$$\boxed{-\frac{\partial J}{\partial t} = \min_{u \in \mathcal{U}} \left[c(t, x, u) + \mu(x, u, t) \frac{\partial J}{\partial x} + \frac{1}{2}\sigma^2(x,t) \frac{\partial^2 J}{\partial x^2}\right]}$$

with terminal condition $J(T, x) = \psi(x)$. This is the **Hamilton–Jacobi–Bellman (HJB) equation**. It is a nonlinear PDE running backwards in time from the terminal condition. The optimal control $u^*(t,x)$ is the minimiser of the right-hand side at each $(t,x)$:

$$u^*(t, x) = \arg\min_{u \in \mathcal{U}} \left[c(t, x, u) + \mu(x, u, t) \frac{\partial J}{\partial x}\right]$$

Once the HJB PDE is solved for $J$ and the optimal control $u^*$ is obtained in feedback form, the optimal policy generates the optimal state trajectory by forward simulation under $u^*(t, X_t)$.

For multivariate states $X_t \in \mathbb{R}^n$ driven by a multivariate Wiener process $W_t \in \mathbb{R}^d$, with dynamics $dX_t = \mu(X_t, u_t, t) \, dt + \Sigma(X_t, t) \, dW_t$, the HJB equation generalises to:

$$-\frac{\partial J}{\partial t} = \min_{u \in \mathcal{U}} \left[c(t, x, u) + \mu(x, u, t)^T \nabla_x J + \frac{1}{2} \text{tr}\left(\Sigma \Sigma^T \nabla_{xx}^2 J\right)\right]$$

where $\nabla_x J$ is the gradient vector and $\nabla_{xx}^2 J$ is the Hessian matrix of $J$ with respect to $x$.

### Terminal conditions and boundary conditions

The HJB equation is solved backwards from the terminal condition $J(T, x) = \psi(x)$, which encodes the terminal cost at the end of the horizon. For execution problems, the most common terminal cost is a large penalty for failing to liquidate the full position:

$$\psi(x_T) = A \, x_T^2, \quad A \to \infty$$

which forces $x_T \approx 0$ in the limit. The terminal condition thus encodes the hard constraint that the position must be closed at the end of the trading horizon. In practice, a large but finite $A$ corresponds to the cost of liquidating any residual at market at time $T$.

### Connection to the Feynman–Kac theorem

Once the optimal control $u^*(t, x)$ is substituted back into the HJB equation, the resulting PDE is linear in $J$ and takes the form covered by the Feynman–Kac theorem (chapter {ref}`stochastic_calculus`, section {ref}`feynman_kac`):

$$\frac{\partial J}{\partial t} + \mu^*(x, t) \frac{\partial J}{\partial x} + \frac{1}{2}\sigma^2(x,t) \frac{\partial^2 J}{\partial x^2} - r \, J + c^*(t, x) = 0$$

where $\mu^* = \mu(x, u^*(t,x), t)$ and $c^* = c(t, x, u^*(t,x))$ are the optimal drift and cost. The Feynman–Kac theorem then identifies $J(t, x)$ with the expected discounted cost under the optimal dynamics:

$$J(t, x) = \mathbb{E}\left[\int_t^T e^{-r(s-t)} c^*(s, X_s) \, ds + e^{-r(T-t)}\psi(X_T) \,\Bigg|\, X_t = x\right]$$

This confirms the probabilistic interpretation of the value function and provides a Monte Carlo method for computing $J$ numerically when the PDE is not analytically tractable.

(sec:el)=
## The variational approach

### Calculus of variations

The calculus of variations studies functionals — real-valued functions whose argument is itself a function — and asks: for what function is a given functional minimised or maximised? In the control problems of interest, the functional is the expected total cost and the unknown is the trajectory of the state variable.

Consider minimising the functional

$$\mathcal{F}[x] = \int_0^T L(t, x_t, \dot{x}_t) \, dt$$

over smooth trajectories $x: [0, T] \to \mathbb{R}$ subject to fixed boundary conditions $x(0) = x_0$ and $x(T) = x_T$. The integrand $L(t, x, \dot{x})$ is called the *Lagrangian*. The trajectory $x^*$ that extremises $\mathcal{F}$ satisfies the **Euler–Lagrange equation**:

$$\frac{\partial L}{\partial x} - \frac{d}{dt}\frac{\partial L}{\partial \dot{x}} = 0$$

This is a second-order ordinary differential equation for $x_t$, solved subject to the two boundary conditions.

The variational approach applies directly to stochastic optimal control problems in which the noise enters the cost functional only through the trajectory of the state — not through the control variable itself. This occurs in the Almgren–Chriss model, where:
- the *expected* implementation shortfall depends deterministically on the trajectory $\{x_t\}$,
- the *variance* of implementation shortfall depends deterministically on $\{x_t\}$,
- the mean–variance objective is therefore a deterministic functional of the state trajectory.

In such cases, the stochastic optimisation reduces to a deterministic variational problem.

### Euler–Lagrange equation for execution

In the Almgren–Chriss model (derived in detail in chapter {ref}`optimal_execution`), the Lagrangian takes the form

$$L(x, \dot{x}) = \eta \dot{x}^2 + \lambda \sigma^2 x^2$$

where $\eta > 0$ is the temporary market impact coefficient, $\sigma$ is the price volatility, and $\lambda \geq 0$ is the risk-aversion parameter. The Euler–Lagrange equation gives:

$$\frac{\partial L}{\partial x} - \frac{d}{dt}\frac{\partial L}{\partial \dot{x}} = 2\lambda\sigma^2 x - 2\eta \ddot{x} = 0$$

equivalently,

$$\ddot{x} = \kappa^2 x, \quad \kappa \equiv \sqrt{\frac{\lambda \sigma^2}{\eta}}$$

This is a second-order linear ODE with constant coefficients. The general solution is:

$$x_t = A \sinh(\kappa t) + B \cosh(\kappa t)$$

where $A$ and $B$ are determined by the boundary conditions $x_0 = X$ (initial inventory) and $x_T = 0$ (complete liquidation). This yields the unique optimal trajectory:

$$x_t^* = X \, \frac{\sinh(\kappa(T-t))}{\sinh(\kappa T)}$$

The parameter $\kappa$ controls the shape of the trajectory: for $\kappa \to 0$ (risk-neutral, $\lambda \to 0$), the trajectory reduces to a linear decrease $x_t^* = X(1 - t/T)$ — the TWAP schedule. For large $\kappa$ (highly risk-averse), the trajectory front-loads aggressively, liquidating most of the position early and leaving only a small residual towards the end.

### Hyperbolic solution structure

The hyperbolic sine and cosine functions that appear in the solution have a natural interpretation. Define the half-life $\tau^* = 1/\kappa$ as the characteristic time over which the optimal strategy departs significantly from the risk-neutral uniform schedule. For $T \ll \tau^*$ (short horizon relative to the risk-aversion scale), the solution is approximately linear: $x_t^* \approx X(1 - t/T)$. For $T \gg \tau^*$, the solution approximates an exponential decay in the early portion, then abruptly falls to zero near $T$.

The trading rate is

$$v_t^* = -\dot{x}_t^* = \kappa X \, \frac{\cosh(\kappa(T-t))}{\sinh(\kappa T)}$$

This is a decreasing function of time: the optimal strategy sells most aggressively at time $t = 0$ and slows down as the horizon approaches — front-loading to reduce exposure to price risk from holding a large unexecuted inventory, at the cost of higher early market impact.

(sec:lqsc)=
## Linear–Quadratic Stochastic Control

### Problem setup

Linear–Quadratic Stochastic Control (LQSC) is a class of stochastic control problems in which:
- the state dynamics are **linear** in the state and control,
- the cost functional is **quadratic** in the state and control,
- the noise is **Gaussian** (additive, independent of state and control).

These three properties together guarantee that the value function is quadratic in the state, the optimal control is affine (linear plus a constant) in the state, and the optimal gains satisfy a backwards *Riccati equation* — a system of ODEs or recursions that can be solved analytically or efficiently numerically.

In discrete time, the LQSC problem is:

$$\min_{\{u_k\}} \mathbb{E}\left[\sum_{k=0}^{N-1} \left(x_k^T Q_k x_k + u_k^T R_k u_k + 2 q_k^T x_k + 2 r_k^T u_k\right) + x_N^T P_N x_N + 2 p_N^T x_N\right]$$

subject to the linear dynamics

$$x_{k+1} = A_k x_k + B_k u_k + c_k + w_k$$

where $x_k \in \mathbb{R}^n$ is the state, $u_k \in \mathbb{R}^m$ is the control, $w_k \sim \mathcal{N}(0, W_k)$ is a Gaussian disturbance independent of $x_k$ and $u_k$, $A_k \in \mathbb{R}^{n \times n}$, $B_k \in \mathbb{R}^{n \times m}$, $Q_k \succeq 0$, $R_k \succ 0$, and $P_N \succeq 0$.

### The quadratic value function ansatz

The key observation is that the Bellman equation preserves the quadratic structure of the value function. We postulate:

$$V_k(x) = x^T P_k x + 2 p_k^T x + q_k$$

and verify that this form is consistent with the Bellman equation. Substituting the ansatz into the Bellman equation and minimising over $u_k$ (which is unconstrained for simplicity):

The minimand is:

$$x^T Q_k x + 2q_k^T x + u^T R_k u + 2r_k^T u + (A_k x + B_k u + c_k)^T P_{k+1}(A_k x + B_k u + c_k) + \ldots$$

Taking the derivative with respect to $u$ and setting to zero:

$$2 R_k u + 2 B_k^T P_{k+1}(A_k x + B_k u + c_k) + 2(r_k + B_k^T p_{k+1}) = 0$$

Solving for the optimal control:

$$\boxed{u_k^* = K_k x_k + \ell_k}$$

where

$$K_k = -(R_k + B_k^T P_{k+1} B_k)^{-1} B_k^T P_{k+1} A_k$$

$$\ell_k = -(R_k + B_k^T P_{k+1} B_k)^{-1}(B_k^T P_{k+1} c_k + B_k^T p_{k+1} + r_k)$$

The optimal control is **affine in the state**: a linear feedback term $K_k x_k$ plus a constant correction $\ell_k$. The feedback gain $K_k$ depends only on the matrices of the problem, not on the realisation of noise.

### Riccati equations

Substituting the optimal control back into the Bellman equation yields recursions for the coefficients $P_k$, $p_k$, $q_k$, which are the **matrix Riccati equations**:

$$\boxed{P_k = Q_k + A_k^T P_{k+1} A_k - A_k^T P_{k+1} B_k (R_k + B_k^T P_{k+1} B_k)^{-1} B_k^T P_{k+1} A_k}$$

$$p_k = q_k + A_k^T p_{k+1} - A_k^T P_{k+1} B_k (R_k + B_k^T P_{k+1} B_k)^{-1}(B_k^T p_{k+1} + r_k) + A_k^T P_{k+1} c_k$$

with terminal conditions $P_N$ and $p_N$ given. The noise term $w_k$ contributes only to the scalar $q_k$, not to $P_k$ or $p_k$: this is the *certainty equivalence* property of LQSC — the optimal feedback gains are identical to those of the deterministic version of the problem (obtained by setting $w_k = 0$), and noise only increases the expected cost.

The computational cost of the Riccati recursion is $O(Nn^3)$ (matrix inversions at each of $N$ steps for $n$-dimensional state), which is tractable for the problem sizes arising in execution (state dimension 2–4, horizon $N$ = 20–400 time bins).

### Scalar LQSC: the Riccati recursion in closed form

For the scalar case ($n = m = 1$, $A_k = a$, $B_k = b$, $Q_k = q$, $R_k = r$), the Riccati recursion simplifies to:

$$P_k = q + a^2 P_{k+1} - \frac{a^2 b^2 P_{k+1}^2}{r + b^2 P_{k+1}}$$

This can be written as:

$$P_k = q + \frac{a^2 r P_{k+1}}{r + b^2 P_{k+1}}$$

which is a scalar nonlinear recursion that can be evaluated numerically with $P_N$ as the terminal condition. For the stationary case ($a$, $b$, $q$, $r$ constant), the recursion converges as $N \to \infty$ to the fixed point of the algebraic Riccati equation $P^* = q + a^2 r P^* / (r + b^2 P^*)$.

### Continuous-time LQSC

In continuous time, the LQSC problem is:

$$\min_{\{u_t\}} \mathbb{E}\left[\int_0^T \left(x_t^T Q_t x_t + u_t^T R_t u_t\right) dt + x_T^T P_T x_T\right]$$

subject to $dX_t = (A_t X_t + B_t u_t) \, dt + \Sigma_t \, dW_t$. The HJB equation is:

$$-\dot{P}_t = Q_t + A_t^T P_t + P_t A_t - P_t B_t R_t^{-1} B_t^T P_t$$

with terminal condition $P_T$ (matrix-valued). This is the **continuous-time matrix Riccati ODE**. The optimal control is $u_t^* = -R_t^{-1} B_t^T P_t x_t$ — a linear feedback policy with time-varying gain $K_t = -R_t^{-1} B_t^T P_t$. The certainty-equivalence property holds: the Riccati ODE does not depend on the noise covariance $\Sigma_t$, which affects only the expected cost, not the optimal gains.

### Structured extensions for execution problems

Both the VWAP execution problem and the market making problem introduce additional structure: the state vector includes not only the inventory but also a stochastic auxiliary state (the cumulative market volume for VWAP, or the asset price for market making) that is not directly controlled. The LQSC framework handles this naturally by extending the state vector and setting the corresponding control gain to zero.

More precisely, in the VWAP problem (chapter {ref}`optimal_execution`), the state is $x_k = (Q_k, V_k)^T$ where $Q_k$ is the cumulative order executed and $V_k$ is the cumulative market volume. The market volume $V_k$ evolves stochastically and independently of the control $q_k$ (shares executed in bin $k$). The Riccati recursion then produces gains $K_k = (K_{k,1}, K_{k,2})$ where $K_{k,1}$ governs feedback on the execution shortfall and $K_{k,2}$ governs adaptation to observed volume. This adaptive structure is what makes the dynamic VWAP strategy superior to its static counterpart.

## Exercises

1. Consider a one-dimensional control problem with dynamics $x_{k+1} = x_k - u_k$ (deterministic), cost $\sum_{k=0}^{N-1} u_k^2 + \lambda x_k^2$, and terminal cost $\psi(x_N) = A x_N^2$ with $A \to \infty$ (complete liquidation). Apply the LQSC backward recursion to find the optimal control $u_k^*(x)$ for $N = 3$ steps and $\lambda = 0$. Verify that the result is the equal-slicing TWAP schedule.

2. Derive the Euler–Lagrange equation for the Lagrangian $L(x, \dot{x}) = \frac{\dot{x}^2}{f(t)} + \lambda g(t) x^2$, where $f(t)$ and $g(t)$ are positive functions of time. Show that the resulting ODE reduces to the Almgren–Chriss equation when $f(t) = \eta$ and $g(t) = \sigma^2$ are constants.

3. Consider the HJB equation for a one-dimensional stochastic control problem with $dX_t = u_t \, dt + \sigma \, dW_t$, running cost $c(x, u) = u^2$ and terminal cost $\psi(x) = \lambda x^2$. Postulate $J(t, x) = a(t) x^2 + b(t)$ and derive the ODEs for $a(t)$ and $b(t)$ by substituting into the HJB equation. Solve for $a(t)$ and identify the optimal feedback control $u^*(t, x)$.

4. In the LQSC framework with scalar state, let $A = 1$, $B = 1$, $Q = 0$, $R = \eta$, and terminal condition $P_N = A_{\text{term}}$. Write the Riccati recursion and solve it exactly for $N = 1$ and $N = 2$. What is the optimal control $u_0^*$ in each case given $x_0 = X$?

5. Explain why the certainty-equivalence principle holds in LQSC: the optimal feedback gains are the same as in the deterministic version of the problem, regardless of the noise level $\sigma$. What structural property of the problem — linearity of dynamics, quadratic cost, Gaussian noise — is responsible for this? Would certainty equivalence still hold if the cost function were $|u_t|$ instead of $u_t^2$?

6. Write the HJB equation for the following problem: a market maker holds inventory $q_t$ and quotes a spread of $\delta_t$ around the mid-price $S_t$. Trades arrive from clients at a Poisson rate $\lambda(\delta_t)$ (decreasing in $\delta_t$), and each trade changes the inventory by $\pm 1$. The price $S_t$ follows a Brownian motion with volatility $\sigma$. The market maker maximises expected profit $\mathbb{E}[\int_0^T \delta_t \lambda(\delta_t) dt - \phi q_T^2]$ where $\phi$ is an inventory penalty. Identify the state variables, the control, and the structure of the HJB equation, without solving it. (This problem is treated in chapter {ref}`optimal_market_making`.)
