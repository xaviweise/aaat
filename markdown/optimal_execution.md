(optimal_execution)=
# Optimal Execution Theory

## Introduction

Chapter {ref}`execution_fundamentals` established the economic motivations and practical vocabulary of algorithmic execution: why large orders generate market impact, how different benchmarks measure execution quality, and how the tension between market impact and timing risk creates the trader's dilemma. This chapter builds on that foundation by providing the mathematical theory that underlies optimal execution algorithms. The central question is: given a large order to execute over a fixed time horizon, what sequence of child order sizes minimises the expected cost of execution for a given level of risk tolerance?

Answering this question rigorously requires casting execution as an optimal control problem — a framework developed in chapter {ref}`stochastic_optimal_control`. The agent's state is the remaining inventory $x_t$, the control is the trading rate $v_t$, and the cost functional combines expected market impact with the variance of the execution cost. The solution yields a complete characterisation of the *efficient frontier* of execution strategies, parametrised by risk aversion. This frontier generalises naturally to multiple assets traded simultaneously, where correlations between price movements allow natural hedging during execution.

The chapter is organised as follows. Section {ref}`sec:exec_design` formalises the execution problem as an optimal control problem, introducing the price dynamics, market impact model, and cost functional. Section {ref}`sec:almgren_chriss` derives the Almgren–Chriss solution {cite:p}`almgren2000optimal`: the optimal continuous-time trajectory, its efficient frontier, and its discrete-time implementation. Section {ref}`sec:is_target` discusses the IS algorithm and the connection to the Bertsimas–Lo result {cite:p}`BERTSIMAS19981`. Section {ref}`sec:vwap_target` develops the theory of VWAP-optimal execution, from the static proportional schedule through the dynamic adaptation of {cite:t}`busseti2015vwap`. Section {ref}`sec:portfolio_execution` extends the framework to portfolio execution with cross-asset impact and natural hedging.

(sec:exec_design)=
## Designing execution algorithms

### The execution problem as an optimal control problem

Consider an agent who must buy (or sell) a total of $X > 0$ shares of an asset over a time horizon $[0, T]$. We formulate this as a continuous-time optimal control problem with state $x_t$ (remaining inventory) and control $v_t$ (trading rate):

- **State variable**: $x_t$ = number of shares still to be executed at time $t$, with $x_0 = X$ and the constraint $x_T = 0$ (full execution by time $T$).
- **Control variable**: $v_t \geq 0$ = rate of execution (shares per unit time). The state evolves as

$$\dot{x}_t = -v_t \qquad \Rightarrow \qquad x_t = X - \int_0^t v_s \, ds$$

so that the constraint $x_T = 0$ is equivalent to $\int_0^T v_t \, dt = X$.

The trader is liquidating (selling) throughout, so $v_t \geq 0$ and $x_t$ is non-increasing.

### Price dynamics

Absent any trading, the mid-price $S_t$ follows a diffusion process. In the Almgren–Chriss framework {cite:p}`almgren2000optimal`, the price is modelled as an arithmetic Brownian motion modified by the permanent market impact of the trader's own activity:

$$dS_t = \sigma \, dW_t - g(v_t) \, dt$$

where $\sigma > 0$ is the price volatility (constant for simplicity), $W_t$ is a standard Wiener process, and $g(v_t) \geq 0$ is the *permanent impact function* — the irreversible price depression caused by the trader's sell flow. The price process is a martingale in the absence of trading ($v_t = 0$), consistent with the efficient market hypothesis, and is depressed by the accumulated permanent impact of all prior trading.

The choice $g(v) = \gamma v$ (linear permanent impact) is the primary tractable case, yielding a clean closed-form solution. More general impact functions can be handled variationally but typically require numerical methods.

### Linear market impact model

When $v_t$ shares are sold per unit time, the actual *execution price* received for each share is not $S_t$ but $S_t$ adjusted downward by the *temporary market impact* — the immediate price concession needed to absorb the flow against the current order book:

$$P_t^{\text{exec}} = S_t - h(v_t)$$

where $h(v) \geq 0$ is the temporary impact function. The key modelling choice, motivated in chapter {ref}`execution_fundamentals`, is the **linear temporary impact model**:

$$h(v) = \eta v$$

where $\eta > 0$ is the temporary impact coefficient (units: price per trading rate). This means the execution price is depressed by $\eta v_t$ relative to the prevailing mid-price, in addition to the permanent depression already reflected in $S_t$. The temporary impact is transient: it disappears as soon as the order flow stops.

The two-component linear model (linear permanent $g(v) = \gamma v$ and linear temporary $h(v) = \eta v$) is less empirically accurate than the square-root model for large orders but is the standard in theoretical work because it yields analytical closed-form solutions. It is the model used by Almgren and Chriss {cite:p}`almgren2000optimal` and Bertsimas and Lo {cite:p}`BERTSIMAS19981`.

### Cost functional: implementation shortfall

The total proceeds from selling $X$ shares are:

$$\Pi = \int_0^T v_t P_t^{\text{exec}} \, dt = \int_0^T v_t (S_t - h(v_t)) \, dt$$

The *implementation shortfall* (IS) — the cost of execution relative to the paper portfolio value at the arrival price $S_0$ — is:

$$IS = X S_0 - \Pi = X S_0 - \int_0^T v_t (S_t - h(v_t)) \, dt$$

Since $S_t = S_0 + \sigma W_t - \gamma \int_0^t v_s \, ds$, we can write $S_t - S_0 = \sigma W_t - \gamma \int_0^t v_s \, ds$, so:

$$IS = \int_0^T v_t \left[(S_0 - S_t) + h(v_t)\right] dt = \int_0^T v_t \left[\gamma \int_0^t v_s \, ds - \sigma W_t + \eta v_t\right] dt$$

The IS is a random variable whose distribution depends on the price path. The objective is to choose the trading schedule $\{v_t\}_{0 \leq t \leq T}$ to minimise a risk-adjusted expected cost. Following Almgren and Chriss {cite:p}`almgren2000optimal`, the objective is the **mean–variance combination**:

$$\min_{v_t: \, \int_0^T v_t dt = X, \, v_t \geq 0} \mathbb{E}[IS] + \lambda \, \text{Var}[IS]$$

where $\lambda \geq 0$ is the risk-aversion parameter. This corresponds to minimising the expected cost of a risk-averse agent with CARA utility, as shown in {cite:p}`almgren2000optimal`.

(sec:almgren_chriss)=
## The Almgren–Chriss model

### Expected implementation shortfall

Using the linear permanent impact $g(v) = \gamma v$ and linear temporary impact $h(v) = \eta v$, the expected IS can be computed explicitly. First, integrating by parts:

$$\int_0^T v_t \gamma \int_0^t v_s \, ds \, dt = \frac{\gamma}{2} \left(\int_0^T v_t \, dt\right)^2 = \frac{\gamma X^2}{2}$$

This shows that the *permanent impact cost* $\frac{\gamma}{2} X^2$ is path-independent for linear permanent impact: it equals the same constant regardless of how the order is scheduled. This is a key property of linear permanent impact that makes the optimisation tractable — only the temporary impact term and the variance term depend on the schedule.

Taking expectations of the IS (the Brownian term $\sigma W_t$ has zero mean):

$$\mathbb{E}[IS] = \eta \int_0^T v_t^2 \, dt + \frac{\gamma X^2}{2}$$

The first term is the expected *temporary impact cost*, which is minimised by spreading the order as slowly as possible (reducing $v_t^2$ by smoothing). The second term is fixed.

### Variance of implementation shortfall

The stochastic part of the IS arises from the Brownian term $-\sigma \int_0^T v_t W_t \, dt$. The variance of the IS is:

$$\text{Var}[IS] = \sigma^2 \, \text{Var}\left[\int_0^T v_t W_t \, dt\right]$$

Using the stochastic integral result $\text{Var}[\int_0^T f(t) W_t \, dt] = \int_0^T \left(\int_0^T f(s) \min(s,t) \, ds\right) dt$ and integration by parts:

$$\text{Var}[IS] = \sigma^2 \int_0^T x_t^2 \, dt$$

This has a natural interpretation: the variance of execution cost is proportional to the sum of squared *inventory exposures* $x_t^2$. Holding a large unexecuted inventory for a long time exposes the trader to large timing risk; reducing the inventory quickly cuts this exposure at the cost of higher impact.

### The mean–variance objective

Since the permanent impact term $\frac{\gamma}{2} X^2$ is constant across strategies, the mean–variance objective reduces to:

$$\min_{x: \, x_0 = X, \, x_T = 0} \left\{\eta \int_0^T \dot{x}_t^2 \, dt + \lambda \sigma^2 \int_0^T x_t^2 \, dt\right\} + \frac{\gamma X^2}{2}$$

where we have written $v_t = -\dot{x}_t$. This is a **deterministic variational problem** in the trajectory $x_t$: minimise a functional of the form $\int_0^T L(x, \dot{x}) \, dt$ subject to fixed boundary conditions $x_0 = X$ and $x_T = 0$, where:

$$L(x, \dot{x}) = \eta \dot{x}^2 + \lambda \sigma^2 x^2$$

The stochastic nature of the problem has been fully absorbed into the variance term $\sigma^2 \int_0^T x_t^2 \, dt$, leaving a classical calculus-of-variations problem amenable to the Euler–Lagrange approach.

### Optimal trajectory

Applying the Euler–Lagrange equation from chapter {ref}`stochastic_optimal_control` (section {ref}`sec:el`) to the Lagrangian $L(x, \dot{x}) = \eta \dot{x}^2 + \lambda\sigma^2 x^2$:

$$\frac{\partial L}{\partial x} - \frac{d}{dt}\frac{\partial L}{\partial \dot{x}} = 2\lambda\sigma^2 x_t - 2\eta \ddot{x}_t = 0$$

This yields the second-order linear ODE:

$$\ddot{x}_t = \kappa^2 x_t, \quad \kappa = \sqrt{\frac{\lambda\sigma^2}{\eta}}$$

with boundary conditions $x_0 = X$ and $x_T = 0$. The general solution is $x_t = A \sinh(\kappa t) + B \cosh(\kappa t)$. Applying boundary conditions:

- $x_0 = X$: $B = X$
- $x_T = 0$: $A \sinh(\kappa T) + X \cosh(\kappa T) = 0 \Rightarrow A = -X \cosh(\kappa T)/\sinh(\kappa T)$

Substituting and simplifying using the hyperbolic identity $\sinh(a-b) = \sinh a \cosh b - \cosh a \sinh b$:

$$\boxed{x_t^* = X \, \frac{\sinh(\kappa(T-t))}{\sinh(\kappa T)}}$$

The optimal **trading rate** is:

$$v_t^* = -\dot{x}_t^* = \kappa X \, \frac{\cosh(\kappa(T-t))}{\sinh(\kappa T)}$$

This is a monotonically decreasing function of time: the strategy sells most aggressively at $t = 0$ and tapers towards $T$. The degree of front-loading is governed by $\kappa = \sqrt{\lambda\sigma^2/\eta}$: higher risk aversion (larger $\lambda$) or higher volatility (larger $\sigma$) relative to temporary impact cost (smaller $\eta$) produces more aggressive front-loading.

### Properties of the optimal solution

**Risk-neutral limit** ($\lambda \to 0$, $\kappa \to 0$): Using $\sinh(\kappa(T-t)) / \sinh(\kappa T) \to (T-t)/T$ as $\kappa \to 0$, the optimal trajectory becomes:

$$x_t^* \to X\left(1 - \frac{t}{T}\right) \quad \Rightarrow \quad v_t^* \to \frac{X}{T}$$

This is the **TWAP schedule**: sell at a constant rate $X/T$ throughout the horizon. The risk-neutral agent cares only about expected impact and not timing risk, and the impact-minimising strategy is to distribute the order uniformly to avoid quadratically costly bursts. This recovers the Bertsimas–Lo result {cite:p}`BERTSIMAS19981` as a special case.

**Infinitely risk-averse limit** ($\lambda \to \infty$, $\kappa \to \infty$): The optimal inventory collapses to $x_t^* \to 0$ for all $t > 0$, meaning the entire order is liquidated instantaneously at $t = 0$. The trader eliminates all timing risk by accepting the maximum possible market impact.

**General case**: For intermediate $\lambda$, the trajectory $x_t^*$ is convex (the Almgren–Chriss trajectory): it decays faster than the TWAP at the start and slower near the end. The front-loading increases monotonically with $\lambda$.

The figure below illustrates the Almgren–Chriss trajectory for different values of $\kappa T$.

```{figure} figures/ac_trajectories.png
:name: fig:ac_trajectories
:width: 10in
Almgren–Chriss optimal inventory trajectories for different risk-aversion levels (parametrised by $\kappa T$). The TWAP schedule ($\kappa T = 0$) is the straight line; higher $\kappa T$ produces increasingly front-loaded trajectories.
```

### The efficient frontier

For each risk aversion $\lambda$ (equivalently, each $\kappa$), the optimal strategy achieves a specific pair $(\mathbb{E}[IS], \text{Var}[IS])$. Substituting the optimal trajectory into the cost expressions:

$$\mathbb{E}[IS^*] = \frac{\gamma X^2}{2} + \frac{\eta \kappa X^2}{2} \coth\!\left(\frac{\kappa T}{2}\right)$$

$$\text{Var}[IS^*] = \frac{\sigma^2 X^2}{2\kappa} \coth\!\left(\frac{\kappa T}{2}\right) \left[1 - \frac{\kappa T / 2}{\sinh^2(\kappa T/2)}\right]$$

A simplified and commonly used approximation for the variance uses only the leading term:

$$\text{Var}[IS^*] \approx \frac{\sigma^2 X^2}{2\kappa} \coth\!\left(\frac{\kappa T}{2}\right)$$

As $\kappa$ varies from $0$ to $\infty$, the pair $(\mathbb{E}[IS^*], \text{Var}[IS^*])$ traces out a curve in the (variance, expected cost) plane — the **Almgren–Chriss efficient frontier**. Every point on this frontier is the optimal strategy for some risk-aversion level $\lambda$; any strategy not on the frontier is dominated. The figure below shows the frontier.

```{figure} figures/ac_frontier.png
:name: fig:ac_frontier
:width: 9in
The Almgren–Chriss efficient frontier in the $(\sqrt{\text{Var}[IS]}, \mathbb{E}[IS])$ plane. The bottom-left of the frontier corresponds to the risk-neutral TWAP (low expected cost, high variance); the top-right corresponds to aggressive immediate execution (high expected cost, low variance). Each colour marks a different risk-aversion level $\kappa T$.
```

The shape of the frontier has important practical implications. Moving from the TWAP point towards aggressive execution reduces variance rapidly at first (by eliminating the bulk of timing risk), but at increasing marginal cost in expected impact. This reflects the convexity of the temporary impact cost $\eta \int_0^T v_t^2 \, dt$ in the trading rate: executing faster always costs more in impact, but the benefit in risk reduction diminishes as the inventory is already small.

### Liquidation Value at Risk

In addition to the mean–variance efficient frontier, Almgren and Chriss {cite:p}`almgren2000optimal` introduce the *Liquidation Value at Risk* (L-VaR), defined as the worst-case implementation shortfall at a given confidence level $\alpha$:

$$\text{L-VaR}_\alpha = \mathbb{E}[IS^*] + z_\alpha \sqrt{\text{Var}[IS^*]}$$

where $z_\alpha$ is the $\alpha$-quantile of the standard normal distribution. L-VaR provides a risk measure compatible with Value-at-Risk frameworks used in risk management. Minimising L-VaR for a given $\alpha$ corresponds to choosing a specific risk aversion $\lambda = z_\alpha / (2\sqrt{\text{Var}[IS^*]})$, which gives an endogenous way to calibrate $\lambda$ from a risk budget constraint.

### Discrete-time implementation

In practice, the continuous-time trajectory is discretised into $N$ time intervals of length $\tau = T/N$. The agent sells $n_k$ shares in interval $k$ ($k = 1, \ldots, N$), with remaining inventory $x_k = X - \sum_{j=1}^{k-1} n_j$. The discrete analogue of the mean–variance objective is:

$$\min_{\{n_k\}} \left\{\frac{\eta}{\tau} \sum_{k=1}^N n_k^2 + \lambda \sigma^2 \tau \sum_{k=1}^N x_k^2\right\} + \frac{\gamma X^2}{2}$$

subject to $\sum_{k=1}^N n_k = X$. The optimal discrete trades satisfy the second-order linear recursion {cite:p}`almgren2000optimal`:

$$n_{k+1} = \frac{\tau(\lambda\sigma^2\tau + 2\eta/\tau)}{2\eta/\tau} n_k - n_{k-1}$$

which is the discrete approximation of the continuous-time Euler–Lagrange equation $\ddot{x} = \kappa^2 x$. As $\tau \to 0$ with $N\tau = T$ fixed, the discrete solution converges to the continuous-time trajectory $x_t^* = X \sinh(\kappa(T-t))/\sinh(\kappa T)$.

The discrete version is what is implemented in practice. The schedule is computed once at the start of execution using current parameter estimates and then executed deterministically (the static IS algorithm). Dynamic adaptation — re-solving the optimal schedule intraday as new price and volume information arrives — is a natural extension but changes the objective and solution, as discussed in {ref}`sec:is_target`.

(sec:is_target)=
## Implementation Shortfall target

### Risk-neutral optimality: the Bertsimas–Lo result

Bertsimas and Lo {cite:p}`BERTSIMAS19981` derive the optimal execution strategy using dynamic programming in discrete time with a purely risk-neutral objective ($\lambda = 0$ in the mean–variance framework). Their model uses the price dynamics $S_{k} = S_{k-1} + \theta n_{k-1} + \epsilon_k$, where $\theta$ is the permanent impact coefficient and $\epsilon_k$ are i.i.d. zero-mean shocks.

The value function for the problem of maximising expected execution proceeds has the *quadratic form* $V_k(x_k, S_k) = a_k x_k^2 + b_k x_k S_k + c_k$, where the coefficients $\{a_k, b_k, c_k\}$ satisfy backward recursions. The optimal policy at each step is:

$$n_k^* = \frac{x_k}{N - k + 1}$$

This is the **TWAP schedule**: at each step, sell an equal fraction of the remaining inventory. The result is consistent with the Almgren–Chriss $\lambda \to 0$ limit and establishes TWAP as the optimal IS-minimising strategy under linear permanent and temporary impact with i.i.d. price innovations.

When the price process has predictable components (non-zero expected returns), the optimal strategy departs from TWAP. Bertsimas and Lo show that with a linear return predictor $\hat{\mu}_k$ (observable at time $k$), the optimal policy takes the form:

$$n_k^* = \frac{x_k}{N - k + 1} + \phi_k \hat{\mu}_k$$

where $\phi_k$ are coefficients that increase the trade size when the price is expected to fall (for a sell order) and reduce it when the price is expected to rise. This *signal-adaptive execution* is a direct generalisation of TWAP that incorporates short-horizon alpha signals into the execution decision — an important consideration for systematic strategies where residual alpha is present during execution.

### Risk aversion and front-loading

The key insight of the Almgren–Chriss model {cite:p}`almgren2000optimal` is that a risk-averse trader does not implement TWAP even when returns are unpredictable. The optimal IS strategy for $\lambda > 0$ front-loads execution relative to TWAP, sacrificing expected cost to reduce the variance exposure from holding large inventory in a volatile market.

The degree of front-loading can be quantified by comparing the initial sell rate to the TWAP rate:

$$\frac{v_0^*}{X/T} = \frac{\kappa T / \sinh(\kappa T)}{\tanh(\kappa T/2) / (\kappa T/2)} = \kappa T \coth(\kappa T)$$

For $\kappa T = 1$, the initial rate is about 1.31 times the TWAP rate; for $\kappa T = 2$, about 1.93 times. This front-loading effect is consistent with the practical behaviour of IS algorithms in equities, which typically execute 30–60% of the order in the first third of the scheduled window.

### The IS algorithm in practice

In a production IS algorithm, the continuous-time trajectory is pre-computed at launch and then executed via the tactics layer (chapter {ref}`execution_tactics`). The key parameters required are:

- **Volatility $\sigma$**: estimated from recent realised or implied volatility, typically at the intraday time scale of the execution window.
- **Temporary impact coefficient $\eta$**: estimated from execution data, typically calibrated using the square-root model as $\eta \approx \alpha \sigma / \sqrt{V}$ where $V$ is average daily volume and $\alpha$ a market-specific constant.
- **Risk aversion $\lambda$**: set by the institution's risk tolerance, either directly or derived from an L-VaR target. A common practice is to parametrise $\lambda$ through the *execution horizon* $T$, which is set by specifying a *participation rate* — a target fraction of market volume — and using the predicted total volume to derive the horizon.

The IS algorithm is inherently **static**: the schedule is computed once from current parameter estimates. Dynamic variants re-solve the optimal schedule at each time step using updated estimates of volatility and the remaining horizon, trading additional computation for improved adaptation.

(sec:vwap_target)=
## VWAP target

### IS and VWAP under volume-proportional impact

Under certain conditions, the VWAP-optimal strategy coincides with the IS-optimal strategy. {cite:t}`kato2017vwap` shows that when the market impact of trading is proportional to the fraction of market volume traded — $h(v_t) = \eta v_t / V_t$, where $V_t$ is the market trading rate — the risk-neutral IS-optimal strategy is to trade proportionally to the market volume profile. This is the static VWAP schedule: $v_t^* = (X / V_T) V_t$, where $V_T = \int_0^T V_t \, dt$ is the total market volume. The two benchmarks therefore share the same optimal strategy under the natural assumption that temporary impact is proportional to participation rate.

In practice, the two targets differ when impact deviates from this proportional form and particularly when timing risk is relevant: VWAP is agnostic to the trader's risk aversion, while IS front-loading reflects the risk of adverse price movements. The VWAP target is more appropriate for agency execution where the goal is to blend into market flow, while IS is more appropriate for proprietary execution where the investor bears timing risk directly.

### Static VWAP schedule

The simplest VWAP strategy is the **static schedule**: at time 0, estimate the daily volume profile $m_t = V_t / V_T$ from historical data, and allocate the order proportionally:

$$v_t = X \cdot m_t$$

so that the participation rate $v_t / V_t = X / V_T$ is constant across all time bins. The static schedule perfectly tracks VWAP if the realised volume profile matches the forecast; its tracking error arises from deviations between actual and predicted volume.

Volume profiles exhibit strong intraday patterns — the well-known U-shape — that are stable on average but noisy on any given day. The key sources of volume forecast uncertainty are:
- **Total daily volume**: the aggregate number of shares traded that day, which can deviate significantly from its historical average on news or macro event days.
- **Intraday distribution**: the shape of the volume curve within the day, which can shift due to scheduled economic releases, index rebalancing flows, or other events.

### Dynamic VWAP: the Busseti–Boyd framework

{cite:t}`busseti2015vwap` cast the VWAP tracking problem as a *Linear–Quadratic Stochastic Control (LQSC)* problem (chapter {ref}`stochastic_optimal_control`, section {ref}`sec:lqsc`) and derive a dynamic strategy that adapts the execution schedule as volume information is revealed intraday.

**Setup**: the trading period is divided into $M$ bins of equal length. Let $q_n$ be the number of shares executed in bin $n$, $v_n$ the market volume in bin $n$ (random), $V_M = \sum_{n=0}^{M-1} v_n$ the total daily volume, and $m_n = v_n / V_M$ the realised volume fraction. The VWAP slippage relative to the market VWAP is:

$$S = \frac{\sum_{n=0}^{M-1} q_n p_n - \Pi \cdot p_{\text{vwap}}}{\Pi \cdot p_{\text{vwap}}}$$

where $p_n$ is the mid-price in bin $n$ and $\Pi$ is the total order size. Neglecting market impact and using a driftless geometric random walk for prices, the expected slippage is zero and the variance simplifies to:

$$\text{Var}[S] = \sum_{n=1}^{M-1} \sigma_n^2 \, \mathbb{E}_0\!\left[\left(\frac{V_n}{V_M} - \frac{Q_n}{\Pi}\right)^2\right]$$

where $V_n = \sum_{j<n} v_j$ is the cumulative market volume, $Q_n = \sum_{j<n} q_j$ is the cumulative executed quantity, and $\sigma_n$ is the per-bin price volatility. The objective $\min_{\{q_n\}} \text{Var}[S]$ is quadratic in $q_n$, fitting the LQSC structure.

**State space**: the state vector is $x_n = (Q_n, V_n)^T$, combining the cumulative executed quantity and the cumulative market volume. The state dynamics are $x_{n+1} = x_n + (q_n, v_n)^T$, which is linear in the control $q_n$ and the noise $v_n$.

**Riccati solution**: since the cost is quadratic in the state and the dynamics are linear, the LQSC backward recursion from chapter {ref}`stochastic_optimal_control` applies. The optimal control at each step is affine in the current state:

$$q_n^* = K_n x_n + \ell_n$$

where the gains $K_n$ and $\ell_n$ are computed backwards from the terminal condition via Riccati equations. The resulting **dynamic VWAP strategy** is:

$$\boxed{q_n^* = \Pi \cdot \frac{V_n + \mathbb{E}_n[v_n]}{\mathbb{E}_n[V_M]} - Q_n}$$

This elegant formula has a direct interpretation: at each bin $n$, compute the expected total market volume $\mathbb{E}_n[V_M]$ (updated using all information available through bin $n-1$), determine what fraction of $\Pi$ should have been executed by the end of bin $n$ to track the VWAP exactly, and execute the difference between that target and what has actually been executed so far. The strategy thus **corrects for cumulative volume forecast errors one bin at a time**, catching up all accumulated deviations immediately at the next opportunity.

**Static fallback**: if no intraday information is used (only the information available at $n=0$), the optimal strategy reduces to:

$$q_n^{\text{static}} = \Pi \cdot \frac{\mathbb{E}_0[v_n]}{\mathbb{E}_0[V_M]}$$

the proportional static schedule where the allocation to each bin is the predicted fraction of daily volume. This is the static VWAP schedule from the previous section.

**Performance**: Busseti and Boyd report that the dynamic strategy reduces VWAP tracking error (root mean squared slippage) by approximately 10% relative to the static schedule on a sample of DJIA stocks, with execution cost savings of approximately $50 on a $1 million order.

### Volume modelling

The quality of the dynamic VWAP strategy depends critically on the quality of the volume forecasts $\mathbb{E}_n[v_n]$ and $\mathbb{E}_n[V_M]$. {cite:t}`busseti2015vwap` model the intraday volume profile $(m_0, \ldots, m_{M-1})$ as a multivariate log-normal distribution, capturing:

- **Intraday seasonality**: the U-shaped average volume profile, which concentrates at the open and close.
- **Stock-specific scaling**: each stock has a characteristic volume level captured by a stock-specific factor.
- **Cross-bin correlations**: volume is correlated across adjacent bins (high volume in one bin predicts higher volume in the next), captured by a low-rank plus banded covariance matrix.

Given partial observations of the realised volume through bin $n-1$, the conditional distribution of the remaining volume profile follows a log-normal distribution whose parameters are updated via standard conditional Gaussian formulas (Schur complement). The required expectations $\mathbb{E}_n[v_\tau]$ and $\mathbb{E}_n[V_M]$ are computed as log-normal moments using these updated parameters.

In practice, volume models are calibrated from 20–60 days of historical intraday data, discriminating by features such as day of the week, expiration dates, and macro announcement calendars to avoid mixing volume patterns from structurally different days.

(sec:portfolio_execution)=
## Portfolio execution

### Multi-asset extension

Consider simultaneously executing orders in $d$ assets, with target sizes $X^{(i)}$ for $i = 1, \ldots, d$. The state is now a vector $\mathbf{x}_t = (x_t^{(1)}, \ldots, x_t^{(d)})^T$ of remaining inventories and the control is the vector of trading rates $\mathbf{v}_t = (v_t^{(1)}, \ldots, v_t^{(d)})^T$.

Asset prices evolve as a multivariate arithmetic Brownian motion with cross-impact:

$$dS_t^{(i)} = \sigma^{(i)} dW_t^{(i)} - \sum_j g_{ij} v_t^{(j)} \, dt$$

where $G = (g_{ij})$ is the **cross-permanent-impact matrix**: selling asset $j$ at rate $v_t^{(j)}$ moves the price of asset $i$ by $g_{ij} v_t^{(j)}$. The Wiener processes $W_t^{(i)}$ are correlated with instantaneous correlation $\rho_{ij}$, giving the *covariance matrix* $\Sigma$ with $\Sigma_{ij} = \rho_{ij} \sigma^{(i)} \sigma^{(j)}$.

The execution price for asset $i$ is:

$$P_t^{(i),\text{exec}} = S_t^{(i)} - h_{ii} v_t^{(i)}$$

where temporary impact is assumed diagonal (each asset's temporary impact depends only on its own trading rate; cross-asset temporary effects are typically negligible at practical order sizes).

### Portfolio cost functional

The multi-asset mean–variance objective is:

$$\min_{\mathbf{v}_t} \left\{\mathbb{E}[IS_{\text{portfolio}}] + \frac{\lambda}{2} \text{Var}[IS_{\text{portfolio}}]\right\}$$

where $IS_{\text{portfolio}} = \sum_{i=1}^d \left(X^{(i)} S_0^{(i)} - \int_0^T v_t^{(i)} P_t^{(i),\text{exec}} \, dt\right)$.

The expected cost separates into asset-specific temporary impact costs plus a path-independent permanent impact term $\frac{1}{2} \mathbf{X}^T G \mathbf{X}$. The variance of cost is:

$$\text{Var}[IS_{\text{portfolio}}] = \int_0^T \mathbf{x}_t^T \Sigma \, \mathbf{x}_t \, dt$$

This is the key cross-asset term: the variance of the portfolio's execution cost depends on the *joint* inventory trajectory through the covariance matrix $\Sigma$. Correlated assets contribute positively to the total variance, but can be managed jointly to reduce it.

The multi-asset mean–variance objective then reduces to:

$$\min_{\mathbf{x}_t: \, \mathbf{x}_0 = \mathbf{X}, \, \mathbf{x}_T = \mathbf{0}} \left\{\int_0^T \dot{\mathbf{x}}_t^T H \dot{\mathbf{x}}_t \, dt + \lambda \int_0^T \mathbf{x}_t^T \Sigma \, \mathbf{x}_t \, dt\right\}$$

where $H = \text{diag}(\eta^{(1)}, \ldots, \eta^{(d)})$ is the diagonal temporary impact matrix.

### The matrix Euler–Lagrange equation

Applying the Euler–Lagrange equation to the vector Lagrangian $L(\mathbf{x}, \dot{\mathbf{x}}) = \dot{\mathbf{x}}^T H \dot{\mathbf{x}} + \lambda \mathbf{x}^T \Sigma \mathbf{x}$:

$$\frac{\partial L}{\partial \mathbf{x}} - \frac{d}{dt} \frac{\partial L}{\partial \dot{\mathbf{x}}} = 2\lambda \Sigma \mathbf{x}_t - 2H \ddot{\mathbf{x}}_t = 0$$

giving the **matrix ODE**:

$$\ddot{\mathbf{x}}_t = K^2 \mathbf{x}_t, \quad K^2 = \lambda H^{-1} \Sigma$$

The matrix $K^2$ couples the trajectories of all $d$ assets through the covariance matrix $\Sigma$ and the impact matrix $H^{-1}$. The general solution involves *matrix exponentials*:

$$\mathbf{x}_t^* = \sinh(K(T-t)) [\sinh(KT)]^{-1} \mathbf{X}$$

where the matrix $K = \sqrt{\lambda H^{-1} \Sigma}$ (principal square root of the positive semi-definite matrix $\lambda H^{-1} \Sigma$) can be computed via eigendecomposition of $H^{-1} \Sigma$.

For practical implementation, the matrix ODE is solved numerically on a discrete grid using either the matrix exponential or forward Euler integration of the first-order system.

### Natural hedging during execution

The coupling through $\Sigma$ has an important economic interpretation: **correlated assets should be liquidated jointly**. If two assets have positive correlation ($\rho > 0$), selling both simultaneously is better than selling them sequentially, because the price risk of holding residual inventory in one asset is partially hedged by the comovement with the other.

More precisely, consider two perfectly correlated assets ($\rho = 1$, $\sigma^{(1)} = \sigma^{(2)} = \sigma$, $\eta^{(1)} = \eta^{(2)} = \eta$). The joint portfolio trajectory $X^{(1)} x_t^{(1)} + X^{(2)} x_t^{(2)}$ is perfectly hedged against price movements as long as the two inventory trajectories track each other proportionally — if one asset's price moves adversely, the other's moves identically. The optimal strategy therefore schedules both assets with identical normalised trajectories, and the portfolio execution cost is no higher than executing either asset alone.

For imperfectly correlated assets ($0 < \rho < 1$), partial hedging is still possible: the optimal joint trajectory front-loads the more volatile asset and holds the less volatile one longer, exploiting the natural hedge to reduce total variance at lower impact cost.

### Proxy instruments

A powerful extension of multi-asset portfolio execution is the use of **proxy instruments**: highly liquid instruments that are correlated with the portfolio but not themselves in the target portfolio (e.g. index futures for a basket of equities). A proxy instrument can be traded at low cost and high liquidity to hedge the portfolio's price risk during execution, effectively extending the execution window without increasing timing risk.

In the framework above, proxy instruments enter the optimisation with boundary conditions $x_0^{(\text{proxy})} = 0$ and $x_T^{(\text{proxy})} = 0$: they carry no net position change but can be used as intermediaries to reduce portfolio-level risk during the execution window. The optimizer freely uses them as they appear in the covariance matrix $\Sigma$ and their use is only constrained by their boundary conditions. This allows the algorithm to temporarily take on a proxy position to hedge inventory risk, then unwind it as the primary positions are completed.

## Optimal execution using Reinforcement Learning

See my KB
Add some references

## Exercises

1. Derive the formula $\mathbb{E}[IS] = \eta \int_0^T v_t^2 \, dt + \frac{\gamma}{2} X^2$ from the definition of implementation shortfall and the price model $dS_t = \sigma \, dW_t - \gamma v_t \, dt$ with execution price $P_t^{\text{exec}} = S_t - \eta v_t$. Confirm that the permanent impact term $\frac{\gamma}{2}X^2$ is path-independent by computing $\int_0^T v_t \gamma \int_0^t v_s \, ds \, dt$ using integration by parts.

2. Verify that the variance of implementation shortfall is $\text{Var}[IS] = \sigma^2 \int_0^T x_t^2 \, dt$ by computing the variance of $-\sigma \int_0^T v_t W_t \, dt$ using the stochastic integral formula $\text{Var}[\int_0^T f(t) W_t \, dt] = \int_0^T (\int_t^T f(s) \, ds)^2 dt$.

3. Solve the Euler–Lagrange equation $\ddot{x} = \kappa^2 x$ with boundary conditions $x(0) = X$ and $x(T) = 0$ to obtain the Almgren–Chriss trajectory $x_t^* = X \sinh(\kappa(T-t))/\sinh(\kappa T)$. Verify that $x_0^* = X$ and $x_T^* = 0$.

4. Consider an Almgren–Chriss execution with $\sigma = 0.02$ (daily volatility), $\eta = 10^{-5}$ ($/\text{share}^2 \cdot \text{day}$), $\lambda = 10^{-4}$ ($\text{day}^{-1}$), $T = 1$ day, and $X = 10^6$ shares. Compute $\kappa$, $\kappa T$, and the ratio of the initial trading rate to the TWAP rate. What fraction of the order is executed in the first quarter of the horizon?

5. Show that the IS cost at the TWAP limit ($\kappa \to 0$) is $\mathbb{E}[IS^*] \to \frac{\gamma X^2}{2} + \frac{\eta X^2}{T}$ and $\text{Var}[IS^*] \to \frac{\sigma^2 X^2 T}{3}$. Interpret each term: why does variance grow with $T$ while expected impact shrinks with $T$?

6. In the dynamic VWAP strategy (Busseti–Boyd), show that the formula $q_n^* = \Pi (V_n + \mathbb{E}_n[v_n])/\mathbb{E}_n[V_M] - Q_n$ reduces to the static schedule $q_n^{\text{static}} = \Pi \cdot \mathbb{E}_0[v_n]/\mathbb{E}_0[V_M]$ when no intraday volume information is available (i.e. $V_n = 0$, $Q_n = 0$, and $\mathbb{E}_n[\cdot] = \mathbb{E}_0[\cdot]$ for all $n$).

7. Consider a two-asset portfolio execution problem with $X^{(1)} = X^{(2)} = X$, $\sigma^{(1)} = \sigma^{(2)} = \sigma$, $\eta^{(1)} = \eta^{(2)} = \eta$, and correlation $\rho$. Write the matrix $K^2 = \lambda H^{-1} \Sigma$ explicitly and compute its eigenvalues. Show that the eigenmodes correspond to the sum and difference of the two inventory trajectories, and identify which mode is more aggressive and why.
