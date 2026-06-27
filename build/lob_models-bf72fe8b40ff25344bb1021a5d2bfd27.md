(lob_models)=
# Modelling the Limit Order Book

## Introduction

The limit order book (LOB) is the core market mechanism in most modern electronic equity and derivatives markets. Understanding its statistical properties — how orders arrive, how they interact with existing quotes, and how prices emerge — is essential for designing execution algorithms, calibrating market impact models, and building realistic simulations for strategy backtesting.

This chapter develops models for the LOB from the ground up. We begin with **models for order arrival**: the stochastic processes (Poisson, Hawkes) that govern when and how orders reach the market, distinguishing visible orders from hidden ones. We then cover **market impact models** that quantify how individual trades move prices, and **volume prediction models** for anticipating the participation rate of the market at different times of day. The chapter continues with models for the **probability of filling a limit order** (key for smart order routing and passive execution strategies) and **short-term price prediction**, which underpins alpha signals on LOB data. We discuss models of **information asymmetry** in LOBs — the relationship between order flow, adverse selection, and price discovery. The chapter closes with a discussion of **LOB simulation**, covering both probabilistic generative models (which specify joint distributions over order types, sizes, and prices) and agent-based models (which populate the LOB with heterogeneous agents that interact via a matching engine), with particular reference to the McGroarty et al. framework {cite:p}`McGroarty2019`.

## Models for order arrival

### Visible and hidden orders

## Market impact models

## Volume prediction models

## Probability of filling a limit order

## Short term price prediction

## Information Asymmetry

## Simulation of LOBs

### Probabilistic generative models

As discussed in chapter {ref}`intro_bayesian`, a probabilistic generative model describes the joint probability distribution of the relevant variables of the problem. For a simulated limit order book, this means modelling the probability distribution of the orders, e.g. limit or market orders in limit order book. A typical way to construct these generative models is to proceed hierarchically: 

* First, we model the distribution of the arrival of orders to the market. These are point processes in continuous time, and a natural choice of models are the jump processes introduced in chapter {ref}`stochastic_calculus`. The most simple process is the Poisson process, in which orders arrive independently. More realistic choices are for instance Hawkes processes, that incorporate the empirical observation that orders tend to cluster in time, something that can be explained if they self-exciting. 

* Since a market has at least limit and market orders available, and possibly more, a second model can be used to choose the type of order conditional on the arrival of one order. This can be simply modelled with a categorical distribution (a generalization of a Bernoulli distribution for more than two discrete categories). Alternatively, a separate jump process can be modelled for each different order type. 

* Depending on the type of order, we have to model their parameters. The two simplest orders available in LOBs are limit and market orders. Limit orders have a side (buy or sell), a size and a price. Market orders only have side and size. 
  * The side can be modelled in the same lines as the type of order: as a Bernoulli random variable or by modelling separate point process for buy and sell. 
  * The size is a continuous positive variable. A log-normal distribution can be used to model sizes, although empirical distributions typically show heavy tails in the distribution, making power-law distributions, see for instance {cite:p}`gabaix2003theory`. Notice that depending on the exponent, power-laws are not well defined probability distributions. In those cases, though, maximum order sizes can be included to truncate then.
  * Finally, the distributions of limit order prices are typically constructed relative to the mid-price, and sign adjusted to make buy and sell distributions mostly positive. As discussed in {cite:p}`bouchaud2002statistical`, the are right-skewed and heavy tailed, peaking near the best bid and ask available. As with order size, a simple tractable distribution could be a log-normal distribution, potentially shifted to place some mass at least up to the opposite best (best ask for buy/bid orders, best bid for sell/ask orders). Log-normal distributions don't have heavy tails, so power-laws are also commonly used. 

Once we have a model for the generation of the orders, we need to couple it with a matching engine as the one described in chapter {ref}`market_microstructure`.

XXX Example

### Agent-based models

Agent-based models take a different path for simulation of the order book. In this case, we define a set of agents that seek to capture the stylized behaviour of real market players. These agents are algorithms that given market information make decisions about placing orders in the limit order book. Their internal logic is parametrized so their behaviour can be calibrated externally to generate dynamics that are representative of real markets. As with probabilistic generative models, they need to be coupled with a matching engine in order to execute a real simulation. 

To illustrate this paradigm, let us discuss the agent-based model from McGroarty et al. {cite:p}`McGroarty2019`. This model implements a fully functioning LOB populated by five agent types — market makers, liquidity consumers, momentum traders, mean reversion traders and noise traders — each designed to capture a distinct class of real-world market behaviour.

Time is pseudo-continuous: a simulated trading day is divided into a number of $T$ periods. At every period each agent is selected to act with a type-specific probability $\delta_i$, where $i$ indexes the type of agent. When selected, an agent may submit, modify or cancel an order, or do nothing — mirroring the discretion of real participants. For instance, in the original article, the calibrated action probabilities are

$$\delta_{\text{mm}} = 0.1,\quad \delta_{\text{lc}} = 0.1,\quad \delta_{\text{mr}} = 0.4,\quad \delta_{\text{mt}} = 0.4,\quad \delta_{\text{nt}} = 0.75.$$

Notice that higher $\delta$ corresponds to faster trading: noise traders are effectively ultra-high-frequency, while market makers and liquidity consumers act on a much slower timescale. 

#### Market makers

Market makers aim to earn the bid–ask spread by posting limit orders simultaneously on both sides of the LOB while keeping an approximately flat inventory. Their order placement is informed by a short-term directional signal: at each step they compute a $w$-period rolling mean of the order-sign time series to predict whether the next arriving order will be a buy or a sell. If they predict a buy, they size up their sell-side limit order , with a volume drawn from a uniform distribution $U(v_{\min}, v_{\max})$, where $v_{\min}$ and $v_{\max}$ are exogenous or calibrated minimum and maximum volumes. At the same time, they reduce their buy-side quote to a small residual volume $v^-$; the opposite applies when a sell is predicted. Executed orders are replaced the next time the agent is selected. This asymmetric quoting allows market makers to lean against anticipated flow and reduces adverse selection.

#### Liquidity consumers

Liquidity consumers model large institutional investors — pension funds, asset managers — who must buy or sell a substantial block of shares over the course of a day while minimising market impact and transaction costs. At the start of each day the agent is randomly assigned a direction (buy or sell with equal probability) and an initial order size drawn from a uniform distribution $h_0 \sim U(h_{\min}, h_{\max})$. Execution is purely passive and incremental: each time the agent is selected it checks the volume available at the opposing best quote $\Phi_t$. If the remaining order $h_t \leq \Phi_t$ it consumes exactly $h_t$; otherwise it takes all available $\Phi_t$. Only market orders are used, so every fill reduces the remaining balance until the block is fully executed.

#### Momentum traders

Momentum traders are the first of two intra-day investing agent types and represent the widespread belief that recent price trends persist. Their signal is the rate of change (ROC) over a look-back window of $n_r$ periods:

$$\text{roc}_t = \frac{p_t - p_{t-n_r}}{p_{t-n_r}}.$$

When $\text{roc}_t \geq \kappa$ the agent submits a buy market order; when $\text{roc}_t \leq -\kappa$ a sell market order. In both cases the order volume is proportional to the signal strength and the agent's current wealth $W_{a,t}$:

$$v_t = |\text{roc}_t| \cdot W_{a,t}.$$

This wealth-scaling makes the agent's footprint grow with realised profits, amplifying trending dynamics. Wealth is updated every time-period of the simulation valuing the shares at the current market price and adding the remaining cash available. 

#### Mean reversion traders

Mean reversion traders are the second intra-day investing agent type. They operate on the opposite belief: that prices tend to revert to a short-term historical average. Their anchor is an exponential moving average (EMA) updated at each tick:

$$\text{ema}_t = \text{ema}_{t-1} + \alpha\,(p_t - \text{ema}_{t-1}),$$

where $\alpha$ is a recency discount factor. If the current price is $k$ standard deviations above $\text{ema}_t$ the agent places a sell limit order one tick inside the best ask; if it is $k$ standard deviations below, a buy limit order one tick inside the best bid. Order volume is fixed at $v_{\text{mr}}$. By posting limit orders rather than market orders these agents add liquidity when prices overshoot, creating a restoring force.

#### Noise traders

Noise traders are typically the most active participants (as reflected in the original calibrated probabilities, $\delta_{\text{nt}} = 0.75$) and are intended to capture the residual, non-strategic order flow that is always present in real markets. Each time a noise trader is selected it first chooses a side (buy or sell with equal probability) and then randomly selects an action type: submit a market order (probability $\lambda_m$), submit a limit order ($\lambda_l$), or cancel the oldest outstanding order ($\lambda_c$). Order sizes are drawn from a log-normal distribution:

$$v_t = \exp(\mu + \sigma\, u_v), \quad u_v \sim U(0,1).$$

If a limit order is chosen, the price is determined by one of four sub-cases:

* **Crossing** (probability $\lambda_{\text{crs}}$): the order is placed at the opposing best price, guaranteeing immediate (possibly partial) fill, with any residual remaining in the book.
* **Inside spread** ($\lambda_{\text{inspr}}$): the price is drawn uniformly between the current best bid and ask.
* **At the spread** ($\lambda_{\text{spr}}$): the order is placed at the best price on the agent's side of the book.
* **Off-spread** ($\lambda_{\text{offspr}}$): the order is placed deeper in the book at a price drawn from a power-law distribution with minimum offset $x_{\min}$ and exponent $\beta$, fitted to empirical depth data.

The four probabilities sum to one ($\lambda_{\text{crs}} + \lambda_{\text{inspr}} + \lambda_{\text{spr}} + \lambda_{\text{offspr}} = 1$). Two safeguards prevent degenerate dynamics: market orders from noise traders cannot consume more than half of the total opposing volume, and noise traders will always ensure neither side of the book goes empty.

#### Calibration of the model

The model has twenty three input parameters in total. A LOB matching engine is used to handle the orders submitted by the agents. Once a simulation is run, the authors compute statistical properties using the synthetic market data generated by the simulated: the Hurst exponent of volatility, the mean autocorrelation
of mid-price returns, the mean first lag autocorrelation term of the order-sign series, and the best exponent $\beta$ of a price impact function modelled using a power law. The simulation is then run over a grid of parameters in order to find the outputs that best match realistic market dynamics.


