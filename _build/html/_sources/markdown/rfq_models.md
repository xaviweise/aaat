# Modelling RfQs in Dealer to Client Markets

## Introduction

In the context of platforms where the client identity is known, like Dealer to Client platforms, the analysis of the client patterns of trading is relevant in order to fine-tune pricing and hedging models, or to optime the management of axes. 

## Probabilistic graphical model for RfQs

## Generative models for the request for quote activity

### Models for the arrival of RfQs

A dealer receives RfQs for different products from different clients every day or week. Each RfQ has a side, buy or sell, and a volume requested to be traded. A generative model that captures this distribution can be encoded by the following probability: 

$$p(\tau_{\text{RfQ}(\text{client = c, product = p, side = s, volume = v)}} \in [t, t+dt]|F_t)$$

where $\tau_{\text{RfQ}(\text{client = c, product = p, side = s, volume = v})}$ is a random variable that specifies the time at which a client $\text{c}$ requests a quote for product $\text{p}$ of side $\text{s}$ and volume $\text{v}$, and we have also a filtration $F_t$ that includes all relevant information up to t. Alternatively we can introduce $N_t^{\text{RfQ}(\text{client = c, product = p, side = s, volume = v)}}$ as the number of such RfQs up to time t. These two formulations are in fact equivalent:

$$p(\tau_{\text{RfQ}(\text{client = c, product = p, side = s, volume = v})} \in [t, t+dt]|F_t) = $$
$$ p(N_{t+dt}^{\text{RfQ}(\text{client = c, product = p, side = s, volume = v})} - N_t^{\text{RfQ}(\text{client = c, product = p, side = s, volume = v})} = 1|F_t)$$

From the Stochastic Calculus chapter we recognize this model as a **counting process**, whose probability distribution we can write as:

$$ p(\tau_{\text{RfQ}(\text{client = c, product = p, side = s, volume = v})} \in [t, t+dt]|F_t) = \lambda_t (...)dt$$

with the so-called intensity $\lambda_t$ being a general function of time, RfQ variables and any relevant information contained in $F_t$, for instances previous RfQs. If $\lambda_t = \lambda_t(c, p, s, v)$ then we have an instance of a non-homogeneous Poisson process, and if it depends on previous times of arrivals of RfQs, i.e. it is a self-exciting process, we have a Hawkes process. Such counting processes are natural candidates to model the arrival of RfQs.

DISCUSS RELATION TO MODEL WHERE SIDE, VOLUME ARE INDEPENDENT OF ARRIVAL WITH THEIR OWN DISTRIBUTIONS


### Attrition risk

Model from Fader et al, comment overall

## A Generative model for RfQs in negotiation

### Probability of winning the RfQ

### Probability of price discovery

### Information asymmetry and adverse flows

## Axe matcher


## Exercises
