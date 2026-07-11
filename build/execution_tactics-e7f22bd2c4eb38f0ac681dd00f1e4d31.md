(execution_tactics)=
# Execution Tactics

## Introduction

Chapter {ref}`optimal_execution` addressed the *scheduling* problem: given a large order to execute over a horizon $[0, T]$, what sequence of child order sizes $\{v_{t_i}\}$ minimises expected cost for a given level of risk aversion? The Almgren–Chriss model and its extensions produce optimal schedules that specify, at each time step $t_i$, a target volume $v_i$ to trade in the next slice $[t_i, t_{i+1}]$.

A slice, however, is not an execution. Sending a market order of size $v_i$ to the exchange is always an option, but it is rarely optimal: it consumes the spread and accelerates local price impact within the slice. **Execution tactics** are the micro-level algorithms that implement each slice in the limit order book, deciding dynamically whether to post a limit order (and at what price level), upgrade to a market order, or split the slice across multiple venues. Where strategies resolve the tension between market impact and timing risk at the scale of minutes to hours, tactics resolve the analogous tension between execution probability and price improvement at the scale of seconds to minutes.

This chapter develops the theory and practice of execution tactics. Section {ref}`sec:tact_fill` recalls the fill probability model from Chapter {ref}`lob_models` — the core stochastic ingredient for all tactic design. Section {ref}`sec:tact_single` formulates the single-market placement problem as an optimal stochastic control problem, derives the Hamilton–Jacobi–Bellman equation, and characterizes the solution as an **aggressiveness matrix** indexed by remaining time and remaining quantity. Section {ref}`sec:tact_sor` extends the framework to **smart order routing** across multiple venues. Section {ref}`sec:tact_heuristics` describes the menu of heuristic tactics offered by brokers and exchanges, and section {ref}`sec:tact_rl` develops the reinforcement learning approach to tactic design, which bypasses the need for explicit model calibration.

(sec:tact_fill)=
## Fill probability model

Section {ref}`sec:lob_fill_probability` of Chapter {ref}`lob_models` develops the fill probability model in full, including derivation, calibration, extensions with additional LOB features, and monotonicity constraints. Here we recall the key result needed for tactic design.

Following Avellaneda and Stoikov {cite:p}`AvellanedaStoikov2008` and Cont, Stoikov, and Talreja {cite:p}`cont2010stochastic`, fill events for a limit order placed $\delta$ ticks from the mid-price are modelled as a Poisson process with depth-dependent intensity:

$$\lambda(\delta) = A \, e^{-k\delta},$$

where $A > 0$ is the base fill rate and $k > 0$ is the depth sensitivity. The probability of a fill within a time window $\tau$ is:

$$P(\text{fill} \mid \delta, \tau) = 1 - e^{-\lambda(\delta)\tau} = 1 - \exp\!\left(-A e^{-k\delta} \tau\right).$$

In practice, $A$ and $k$ are calibrated from historical LOB data by regressing observed fill rates against placement depth, controlling for spread, order imbalance, and time of day (see Section {ref}`sec:lob_fill_probability`). Typical values for liquid equity markets are $A \sim 0.5$–$2.0$ fills per minute at zero depth and $k \sim 1$–$3$ per tick.

(sec:tact_single)=
## Single-market execution tactic

### Problem setup

We now formulate the tactic's control problem. The tactic is responsible for executing $Q$ shares (a sell order, without loss of generality) within a window $[0, T]$. The state at time $t$ is the remaining quantity $q_t \in \{0, 1, \ldots, Q\}$; the control is the placement depth $\delta_t \geq 0$ at which to post a limit sell order.

**Dynamics.** Fills arrive as a Poisson process with rate $\lambda(\delta_t)$; each fill reduces the remaining quantity by one unit:

$$q_{t^+} = q_t - 1 \quad \text{with intensity } \lambda(\delta_t)$$

We normalize the tick size to one, so a fill at depth $\delta$ yields proceeds of $\delta$ ticks above the mid-price.

**Terminal condition.** If any quantity remains at $T$ — because the limit orders did not fill — it must be sold immediately via a market order at an expected cost of $b$ ticks per unit below mid-price (the liquidation cost, capturing the spread and residual market impact):

$$\Pi_T^{\text{terminal}} = -b \, q_T, \qquad b > 0$$

**Objective.** The tactic maximises expected total proceeds relative to mid-price, over all admissible adapted placement policies $\{\delta_t\}_{0 \leq t \leq T}$. The value function is:

$$H(t, q) = \sup_{\{\delta_s\}_{s \geq t}} \mathbb{E}_t \!\left[\sum_{\text{fills}} \delta_{\text{fill}} - b \, q_T\right]$$

with boundary conditions $H(T, q) = -b\,q$ and $H(t, 0) = 0$ (no inventory left, no future proceeds).

### The HJB equation and optimal placement

Applying Bellman's principle over the short interval $[t, t + dt]$ and taking $dt \to 0$, the value function satisfies the **Hamilton–Jacobi–Bellman equation**:

$$-\partial_t H(t, q) = \max_{\delta \geq 0} \left\{ \lambda(\delta) \!\left[\delta + H(t, q-1) - H(t, q)\right] \right\}$$

The quantity in brackets, $\delta - \Delta H(t,q)$ where we define:

$$\Delta H(t, q) \equiv H(t, q) - H(t, q-1) \leq 0$$

is the net gain from a fill: the price improvement $\delta$ less the reduction in the value function from losing one unit of inventory. The sign of $\Delta H$ is non-positive because having more inventory to sell is never beneficial — it increases urgency and raises the probability of a costly terminal liquidation.

Substituting $\lambda(\delta) = Ae^{-k\delta}$ and taking the first-order condition with respect to $\delta$:

$$\frac{\partial}{\partial \delta}\left[A e^{-k\delta}(\delta - \Delta H)\right] = Ae^{-k\delta}\!\left[1 - k(\delta - \Delta H)\right] = 0$$

The unconstrained optimum is:

$$\delta - \Delta H(t, q) = \frac{1}{k} \qquad \Rightarrow \qquad \boxed{\delta^*(t, q) = \frac{1}{k} + \Delta H(t, q)}$$

This is the central result: **the optimal placement depth equals $1/k$ minus the absolute urgency $|\Delta H(t,q)|$**. As time runs out or inventory accumulates, $\Delta H$ becomes more negative (greater urgency), and the optimal level moves closer to the mid-price — or below it, triggering a market order. A market order is optimal when $\delta^*(t,q) < 0$, i.e., when $|\Delta H(t,q)| > 1/k$.

Substituting the optimal $\delta^*$ back into the HJB equation:

$$-\partial_t H(t, q) = \frac{A}{ek} \exp\!\left(-k\,\Delta H(t,q)\right)$$

where $e = \exp(1)$. Equivalently, in terms of time-to-go $\tau = T - t$ ($\partial_\tau = -\partial_t$):

$$\partial_\tau H(\tau, q) = \frac{A}{ek} \exp\!\left(-k\,\Delta H(\tau,q)\right)$$

This system of ODEs (one per inventory level $q$) is solved backwards from $H(0, q) = -bq$.

**Analytical solution for $q = 1$.** When only one unit remains, $H(\tau, 0) = 0$, so $\Delta H(\tau, 1) = -H(\tau, 1)$ and the ODE becomes:

$$\partial_\tau H(\tau, 1) = \frac{A}{ek} e^{kH(\tau, 1)}$$

This separable ODE has the solution (with initial condition $H(0,1) = -b$):

$$H(\tau, 1) = \frac{1}{k}\ln\!\left(e^{-kb} + \frac{A\tau}{e}\right)$$

The optimal placement depth for the last unit is:

$$\delta^*(\tau, 1) = \frac{1}{k}\!\left[\ln\!\left(e^{-kb} + \frac{A\tau}{e}\right) + 1\right]$$

As $\tau \to 0$: $\delta^*(0,1) = \frac{1}{k}(1 - kb) = \frac{1}{k} - b$, which is a market order when $b > 1/k$. As $\tau \to \infty$: $\delta^*(\tau,1) \to \frac{1}{k}\ln(A\tau/e)$, growing without bound — with plenty of time, the tactic posts very passively. For $q > 1$, the system must be solved numerically by backward induction on the grid $(\tau, q)$.

### The aggressiveness matrix

The solution $\delta^*(t, q)$ is most naturally displayed as a **two-dimensional look-up table** indexed by the normalised remaining time $t/T$ and the normalised remaining quantity $q/Q$ — the *aggressiveness matrix* of the tactic. Each cell of the matrix specifies the optimal placement depth in ticks at that (time, quantity) state.

```{figure} figures/tact_aggressiveness_matrix.png
:name: fig:tact_aggressiveness_matrix
:width: 10in
Aggressiveness matrices for three levels of terminal urgency $b$ (low: $b = 0.5$, moderate: $b = 2$, high: $b = 5$; with $A = 1$ fill/min, $k = 1.0$ per tick, $T = 10$ min). Colour indicates optimal placement depth in ticks: darker (blue) regions correspond to deeper, more passive placement; lighter (yellow/red) regions trigger aggressive or market orders. In all cases, the tactic becomes more aggressive (shallower depth) as time expires or as the remaining fraction $q/Q$ approaches 1. A higher urgency parameter $b$ shifts the entire matrix towards more aggressive placements.
```

Several properties of the aggressiveness matrix are economically intuitive:

- **Top-left corner** (early, little remaining): the tactic posts deep passive orders, harvesting price improvement with minimal urgency.
- **Bottom-right corner** (late, most remaining): the tactic posts at or near the best quote, maximising fill rate at the cost of price improvement.
- **Market order region**: the shaded region where $\delta^* < 0$ corresponds to states where the terminal liquidation cost is so imminent that immediate execution via a market order is optimal.

In practice, the matrix is pre-computed off-line using backward induction and stored as a look-up table. At each step of the tactic, the current state $(t, q)$ is mapped to the nearest grid cell, and the corresponding depth $\delta^*$ is read off. This makes real-time execution computationally trivial.

### Multi-order splitting

The single-order formulation posts one limit order at a time. In practice, it is common to **split the remaining quantity into $m$ simultaneous child orders**, each of size $q/m$, posted at (potentially different) price levels. The HJB equation for the multi-order case with $m$ simultaneous orders is:

$$-\partial_t H(t, q) = \max_{\delta_1, \ldots, \delta_m \geq 0} \sum_{j=1}^m \lambda(\delta_j)\!\left[\delta_j + H(t, q-1) - H(t, q)\right]$$

Because the objective is separable — each order's contribution depends only on its own $\delta_j$ and the common term $\Delta H(t,q)$ — the optimal $\delta_j^*$ are identical for all $j$:

$$\delta_j^*(t, q) = \frac{1}{k} + \Delta H(t, q) \quad \text{for all } j = 1, \ldots, m$$

All orders are placed at the same optimal depth as in the single-order case {cite:p}`cartea2015optimal`. The only effect of splitting is to multiply the effective fill rate: with $m$ orders at depth $\delta^*$, the aggregate fill rate is $m\lambda(\delta^*)$, reducing the expected time to the next fill by a factor of $m$. The aggressiveness matrix is therefore unchanged; only the inventory dynamics change (fills arrive $m$ times faster on average). Splitting reduces the risk of the tactic finishing the window with large residual inventory, at no cost to price improvement.

(sec:tact_sor)=
## Smart order routing

### Multi-venue framework

Modern financial markets are fragmented: the same instrument trades simultaneously on multiple lit exchanges, dark pools, and bilateral platforms with different liquidity profiles. A **Smart Order Router (SOR)** is a component that distributes the tactic's child orders across these venues, seeking to fill the required volume at the lowest total cost.

We model $K$ trading venues, each characterized by its own depth-dependent fill rate:

$$\lambda_k(\delta) = A_k \, e^{-k_k \delta}, \quad k = 1, \ldots, K$$

where $A_k$ is the base fill rate at venue $k$ and $k_k$ controls how steeply fill rates fall with depth. Venues with high $A_k$ (high volume) and low $k_k$ (book does not thin rapidly) are most liquid. The tactic simultaneously posts one limit order per venue, with depth $\delta^{(k)}_t$ at venue $k$.

### Optimal venue allocation

With multiple venues, the HJB equation becomes:

$$-\partial_t H(t, q) = \max_{\delta^{(1)}, \ldots, \delta^{(K)} \geq 0} \sum_{k=1}^K \lambda_k(\delta^{(k)}) \!\left[\delta^{(k)} + H(t, q-1) - H(t,q)\right]$$

The multi-venue objective is again separable across venues for a given $\Delta H(t,q)$. The first-order condition for each venue independently yields:

$$\delta^{(k)*}(t, q) = \frac{1}{k_k} + \Delta H(t, q), \quad k = 1, \ldots, K$$

The optimal depth at each venue follows the same formula as the single-venue case, with $1/k$ replaced by the venue-specific $1/k_k$. This has a direct economic interpretation: **venues where fill rates fall off slowly with depth (small $k_k$) attract deeper, more passive placements, while venues where fill rates fall off rapidly (large $k_k$) attract more aggressive placements**.

The substituted HJB becomes:

$$-\partial_t H(t,q) = \sum_{k=1}^K \frac{A_k}{e k_k} \exp\!\left(-k_k \, \Delta H(t,q)\right)$$

Intuitively, the SOR aggregates fill rate contributions from all venues and the tactic simultaneously harvests liquidity wherever it is available, without requiring an explicit allocation of a fixed fraction of volume to each venue.

```{figure} figures/tact_sor.png
:name: fig:tact_sor
:width: 9in
Smart order routing across two venues. *Left*: fill rates $\lambda_k(\delta)$ for a liquid venue (high $A_1$, low $k_1$; blue) and an illiquid venue (low $A_2$, high $k_2$; orange). The liquid venue attracts deeper passive placements; the illiquid venue is approached more aggressively. *Right*: simulated P&L distributions (10,000 runs, $Q = 100$, $T = 10$ min) comparing single-venue execution (liquid, illiquid) against the two-venue SOR. The SOR dominates both single-venue alternatives in both mean and variance.
```

### Practical considerations

Beyond the theoretical model, SOR design involves several practical dimensions:

**Dark pools.** Dark pools are off-exchange trading venues that do not display their order book; fills occur at the mid-price without market impact, but fill rates are uncertain and typically lower than on lit venues. The fill rate model for dark pools requires a different calibration — fills are generated by crossing contra-side orders, not by price movement. The seminal analysis of the dark pool problem is due to {cite:t}`ganchev2010censored`, who frame it as a censored exploration problem.

**Latency and queue position.** Fill rates in limit order books depend not only on depth but on queue position at each level. An order that arrives early at a given price level will be filled before later arrivals at the same level (price-time priority). The model above implicitly assumes the order is at the back of the queue; incorporating queue position leads to a richer state space and has been studied in the literature on optimal placement with latency {cite:p}`cont2010stochastic`.

**Price divergence across venues.** In fragmented markets, mid-prices can temporarily diverge across venues, especially at high frequency. A SOR that ignores this may place its order at the "wrong" venue. Best-execution regulations (MiFID II in Europe, Regulation NMS in the US) require systematic evaluation of execution quality across venues and oblige brokers to seek the best available price.

(sec:tact_heuristics)=
## Heuristic execution tactics

Beyond the model-based approaches above, a range of **heuristic tactics** are widely used in practice, supported natively by exchanges and prime brokers. These tactics encode practical execution intuitions that are simpler to implement than full HJB solutions, and serve as useful benchmarks.

### Pegged orders

A **pegged order** tracks a reference price dynamically, automatically re-pricing the order as market conditions change. The most common variants are:

- **Peg-to-mid**: the limit order is always posted $\delta$ ticks above (for a sell) or below (for a buy) the current mid-price. As the mid moves, the order reprices automatically, maintaining a constant spread to the centre of the market.
- **Peg-to-best (NBBO peg)**: the order is pegged to the national best bid/offer, posting at $\delta$ ticks above the best ask (for a sell) or below the best bid (for a buy). This keeps the order at a fixed distance from the best prevailing market price rather than the mid.
- **Primary peg**: the order is always posted exactly at the current best bid (for a sell) or best ask (for a buy), ensuring it is the first passive quote available.

Pegged orders reduce the operational complexity of managing limit orders in fast-moving markets: without pegging, a passive limit order placed at the mid at time $t_0$ may be far inside the book (or even outside the book entirely) by time $t_1$ if the price has moved. Pegging ensures the order remains continuously visible at the intended level without manual re-pricing.

### Iceberg and reserve orders

A large passive limit order that is fully displayed in the order book signals the trader's intention to other market participants, who may adjust their own behaviour — pulling displayed orders, widening spreads, or trading against the disclosed position — to extract rents from the informed side. **Iceberg orders** (also called reserve orders or hidden quantity orders) mitigate this information leakage by displaying only a small "tip" $q_{\text{tip}}$ in the public order book while reserving the remainder $q_{\text{hidden}} = Q - q_{\text{tip}}$ invisibly. When the tip is fully filled, the next tranche is automatically posted.

The trade-off in choosing the tip size is as follows. A larger tip signals more information to the market but earns better queue priority (since the displayed tip competes for fills on a first-come, first-served basis with its full size). A smaller tip minimises information leakage but may execute more slowly if queue priority is lost each time the tip is exhausted. Empirical evidence suggests iceberg orders execute at slightly better prices than equivalent market orders but slower than equivalent fully-disclosed limit orders, reflecting the information leakage channel {cite:p}`cartea2015algorithmic`.

### Liquidity seeking and sniping

**Liquidity seeking tactics** scan multiple venues simultaneously for executable liquidity at or better than a target price. When liquidity is detected — a visible limit order on the contra-side at a favourable price — the SOR fires a market order (or a marketable limit order) to capture it before it disappears. These tactics are opportunistic: they are passive in the absence of favourable liquidity and aggressive when it appears.

**Sniping** is a closely related strategy in which the tactic waits for a specific price level to be reached and then submits an aggressive order. In the context of execution tactics, a sniper may target a pre-specified price $S^* < S_0$ (for a buy) below which it activates, treating the price as a favourable entry point. The risk of sniping is adverse selection: the price may be moving rapidly to the target level precisely because informed traders are selling, making the achieved entry point worse in expectation than the target.

### Participation rate tactics

**Participation rate (PoV) tactics** constrain the execution rate to a fixed percentage $\pi$ of market volume, so that the tactic does not trade significantly faster than the prevailing market pace. Within each measurement interval $[t_i, t_{i+1}]$, the tactic computes the market volume $V_i$ and submits enough orders to have traded $\pi V_i$ shares in aggregate. If ahead of pace, it switches to passive limit orders; if behind pace, it switches to more aggressive orders or market orders.

PoV tactics are natural for VWAP strategies (see chapter {ref}`optimal_execution`): a constant participation rate $\pi = Q/V^{\text{day}}$ (where $V^{\text{day}}$ is the expected daily volume) approximates the VWAP schedule. In practice, the participation rate is adjusted intraday based on updated volume predictions from the volume models discussed in chapter {ref}`lob_models`.

(sec:tact_rl)=
## Reinforcement learning for execution tactics

### RL formulation

The optimal placement problem of section {ref}`sec:tact_single` rests on explicit assumptions: Poisson fill processes with exponential depth dependence, a known terminal liquidation cost, and a model that is stationary within the execution window. In practice, fill rates vary with LOB state, intraday patterns, and recent order flow in ways that are difficult to capture parsimoniously. **Reinforcement learning (RL)** provides an alternative that learns the optimal policy from simulated or historical experience, without requiring explicit model specification.

The tactic is formulated as a Markov Decision Process (MDP):

- **State** $\mathbf{s}_t = (\tau_t, \phi_t, \hat{\sigma}_t, I_t, \hat{A}_t)$: remaining time $\tau_t = T - t$, remaining fraction $\phi_t = q_t/Q$, recent volatility estimate $\hat{\sigma}_t$, order flow imbalance $I_t = (N^{\text{buy}}_t - N^{\text{sell}}_t)/(N^{\text{buy}}_t + N^{\text{sell}}_t)$, and estimated fill rate $\hat{A}_t$.

- **Action** $a_t \in \{-1, 0, 1, 2, \ldots, \delta_{\max}\}$: the placement depth in ticks. Action $a_t = -1$ corresponds to a market order; $a_t = 0$ is at the best ask (for a sell); $a_t = j > 0$ is $j$ ticks above the best ask.

- **Reward** $r_t$: proceeds from any fill at step $t$, minus the terminal liquidation cost at $T$. Formally:

$$r_t = \begin{cases} a_t & \text{if a fill occurs at step } t \\ -b \, q_T & \text{if } t = T \text{ and } q_T > 0 \\ 0 & \text{otherwise} \end{cases}$$

The RL agent learns a policy $\pi_\theta(\mathbf{s})$ (either a deterministic action or a probability distribution over actions) that maximises the expected discounted sum of rewards $\mathbb{E}[\sum_t \gamma^t r_t]$. This is precisely the same objective as the optimal control formulation, but the agent estimates $\pi$ from experience rather than from explicit HJB solution.

The RL framework is particularly powerful when (i) the state space is richer than just $(\tau, q)$ — including LOB features that are difficult to model analytically — and (ii) the fill rate model is non-stationary or has complex dependence structure.

### Q-learning and deep Q-networks

The seminal application of RL to execution tactics is due to Nevmyvaka, Feng, and Kearns {cite:p}`nevmyvaka2006reinforcement`, who applied tabular Q-learning to the order placement problem on NASDAQ data. Their state representation included remaining quantity, remaining time, bid-ask spread, and short-term price momentum. The action space was a discretized set of placement levels. Evaluated on 1.5 years of NASDAQ data, the RL policy outperformed TWAP by approximately 50 basis points on average for large-cap stocks — a significant improvement for institutional-scale executions.

In the tabular Q-learning approach, the action-value function $Q(\mathbf{s}, a)$ is maintained as a look-up table and updated via the Bellman recursion:

$$Q(\mathbf{s}_t, a_t) \leftarrow Q(\mathbf{s}_t, a_t) + \alpha\!\left[r_t + \gamma \max_{a'} Q(\mathbf{s}_{t+1}, a') - Q(\mathbf{s}_t, a_t)\right]$$

where $\alpha$ is the learning rate and $\gamma$ is the discount factor. The policy is $\epsilon$-greedy: with probability $\epsilon$ a random action is taken (exploration), and with probability $1-\epsilon$ the greedy action $\arg\max_a Q(\mathbf{s},a)$ is selected.

When the state space is continuous or high-dimensional, the tabular representation becomes infeasible. The **Deep Q-Network (DQN)** replaces the table with a neural network $Q_\theta(\mathbf{s}, a)$ parameterized by weights $\theta$, trained by minimising the Bellman residual loss:

$$\mathcal{L}(\theta) = \mathbb{E}\!\left[\left(r + \gamma \max_{a'} Q_{\bar{\theta}}(\mathbf{s}', a') - Q_\theta(\mathbf{s}, a)\right)^2\right]$$

where $Q_{\bar{\theta}}$ is a periodically updated **target network** that stabilises training by decoupling the moving target from the network being updated. A **replay buffer** stores historical transitions $(\mathbf{s}, a, r, \mathbf{s}')$, and mini-batches are drawn uniformly at random to break temporal correlations in the training data.

{cite:t}`ning2021double` apply a Double DQN architecture — which reduces Q-value overestimation by separating action selection from value evaluation — to execution with limit and market orders. Their model is trained on a calibrated synthetic LOB and evaluated against IS and VWAP benchmarks, showing that the learned policy adapts placement depth to real-time LOB features in a way that the static aggressiveness matrix cannot.

```{figure} figures/tact_rl_convergence.png
:name: fig:tact_rl_convergence
:width: 10in
Training a DQN execution tactic. *Left*: training curve — mean episodic reward per episode over 2,000 episodes (smoothed with a 50-episode rolling average). The agent progresses from random exploration to approximately optimal policy. *Right*: learned Q-values as a function of remaining time $\tau$ and remaining fraction $\phi$ for the action $a = 0$ (best ask placement), showing that the DQN has learned a representation qualitatively consistent with the theoretical aggressiveness matrix: higher Q-values (greener) at early times and low remaining fractions, lower Q-values (redder) at late times with large remaining fractions where more aggressive actions dominate.
```

### Policy gradient methods

Q-learning operates in a discretized action space. When the placement depth is treated as a continuous variable — or when the policy must be stochastic to handle exploration and variability in LOB conditions — **policy gradient** methods are more appropriate. The **Proximal Policy Optimisation (PPO)** algorithm {cite:p}`sutton2018reinforcement` maintains a parameterized policy $\pi_\theta(a|\mathbf{s})$ (e.g., a Gaussian over continuous depths) and updates it by ascending a clipped surrogate objective that prevents destabilising large policy updates:

$$\mathcal{L}^{\text{CLIP}}(\theta) = \mathbb{E}_t\!\left[\min\!\left(\rho_t(\theta)\hat{A}_t,\; \text{clip}(\rho_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t\right)\right]$$

where $\rho_t(\theta) = \pi_\theta(a_t|\mathbf{s}_t)/\pi_{\theta_{\text{old}}}(a_t|\mathbf{s}_t)$ is the probability ratio and $\hat{A}_t$ is the estimated advantage function.

**Actor-critic methods** (A2C, A3C) combine a policy network (actor) with a value network (critic) that estimates the expected return from each state. The critic reduces the variance of policy gradient estimates by providing a baseline for the advantage function. This structure mirrors the relationship between the optimal control value function $H(t,q)$ and the optimal policy $\delta^*(t,q)$: the critic approximates $H$ and the actor approximates $\delta^*$.

Recent developments in RL for execution have explored several directions. **Reward shaping** augments the terminal execution cost with intermediate milestones (e.g., rewarding the agent for maintaining pace relative to a VWAP schedule). **Multi-agent frameworks** model the interaction between the execution tactic and other market participants — momentum traders, market makers — explicitly, training the tactic in a game-theoretic rather than single-agent setting. **Offline RL** trains on historical order book data without an explicit simulator, avoiding the model misspecification that can occur when training on a stylised generative model. All of these extensions move in the direction of reducing the gap between the theoretical ideal and robust practical deployment.

## Exercises

* Verify the analytical solution $H(\tau, 1) = k^{-1}\ln(e^{-kb} + A\tau/e)$ by substituting into the HJB equation $\partial_\tau H(\tau, 1) = (A/ek) e^{kH(\tau,1)}$ and checking that the initial condition $H(0,1) = -b$ is satisfied. Interpret the limiting cases $\tau \to 0$ and $\tau \to \infty$ in terms of the optimal depth $\delta^*(\tau, 1) = k^{-1}\ln(e^{-kb} + A\tau/e) + 1/k$.

* In the single-market tactic, the optimal placement is $\delta^*(t,q) = 1/k + \Delta H(t,q)$ where $\Delta H = H(t,q) - H(t,q-1) \leq 0$. (a) Show that the optimal placement depth is always weakly smaller when $q$ is larger: $\delta^*(t, q) \leq \delta^*(t, q-1)$ for all $q \geq 1$. This is the "urgency is monotone in inventory" property. (b) Show that $\delta^*(t, q)$ is weakly decreasing in $t$ for fixed $q$ — the tactic becomes more aggressive as time runs out.

* In the two-venue SOR model with venues indexed $k = 1, 2$, venue 1 is liquid ($A_1 = 2$, $k_1 = 0.5$) and venue 2 is illiquid ($A_2 = 0.5$, $k_2 = 2.0$). (a) Compute the optimal depths $\delta^{(1)*}$ and $\delta^{(2)*}$ as functions of the marginal inventory cost $\Delta H$. (b) For $\Delta H = -1$ (moderate urgency), compute the aggregate fill rate $\lambda_1(\delta^{(1)*}) + \lambda_2(\delta^{(2)*})$ and compare it to the fill rate achievable on venue 1 alone if the same total aggression is concentrated there. (c) Interpret the result: why does the SOR outperform single-venue execution?

* Consider a pegged-to-mid sell order, so $\delta_t = \delta$ is held constant (not optimized) but the limit price tracks $S_t + \delta$ continuously. Assuming the mid-price $S_t$ follows an arithmetic Brownian motion with volatility $\sigma$ and no drift, and that fills occur when a market buy order arrives (at rate $\lambda$ per unit time, independently of the price level), show that the expected proceeds of the pegged order relative to the mid-price at the time of posting are equal to $\delta$ for any $\sigma$. Why does price volatility not affect expected proceeds in this case? Under what market microstructure assumptions does this result break down?

* Consider the RL formulation of the tactic. (a) Show that the tabular Q-learning algorithm converges to the optimal Q-function $Q^*(s, a)$ satisfying the Bellman equation $Q^*(s,a) = \mathbb{E}[r + \gamma \max_{a'} Q^*(s',a') \mid s, a]$ under the usual conditions (sufficient exploration, diminishing step sizes). (b) Explain why the function approximation version (DQN) does not generally converge to the exact Bellman solution, even with infinite data, and describe the two main stabilisation techniques (experience replay and target network) used to make the algorithm work in practice.

* **Iceberg order trade-off.** A sell order of $Q = 1000$ shares is to be executed passively over $T = 30$ minutes. Compare two strategies: (i) a fully visible limit order at depth $\delta = 1$ tick, filled at rate $\lambda = 0.5$ fills/min; (ii) an iceberg order with tip $q_{\text{tip}} = 100$ shares, where each tip fills at the same rate $\lambda = 0.5$ fills/min but the tactic must replenish the tip after each fill, incurring a 5-second queue re-entry delay. Compute the expected number of units filled in 30 minutes under each strategy, assuming fills are independent Poisson events. What tip size minimises the total expected time to complete the order?
