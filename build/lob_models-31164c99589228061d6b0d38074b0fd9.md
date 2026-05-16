(lob_models)=
# Modelling the Limit Order Book

## Introduction

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

To illustrate this paradigm, let us discuss the agent-based model from 


