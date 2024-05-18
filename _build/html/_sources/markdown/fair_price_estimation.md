# Fair price estimation

## Introduction

## Pricing of flow products

For flow products that are relatively liquid, we can aim at extracting all the pricing information from price indications and trades in the market, without having to resort to economic theories of fair value. In this setup, we consider their price the one that market participants are willing to pay for. 

The issue, though, is that price indications and trades cannot be considered themselves pure observations of fair price, since they might be affected by market frictions: bid ask spreads, particularities of the negotiation mechanism, liquidity fluctuations, specific needs of market participants at a given time, etc. When instruments trade in limit order books, a popular estimation of the fair price is using the mid-price, the arithmetic average of the best bid and ask. However, if bid-ask spreads are wide of liquidity is thin in the first levels, such estimation is not necessary very precise. Trades provide a lot of information, since they are real transaction and not indications of interests, the larger they are in principle the more information. Still, they are subject to the aforementioned market frictions that reduce their reliability. 

These makes all these price observations noisy estimates of the fair price, so if we want to estimate a fair price out of them we need to be able to separate the signal from the noise, or in other words, filter those observations. This is precisely what a Kalman filter does. 

### The Kalman Filter model for pricing

The Kalman filter was introduced in chapter ... 

#### Two correlated instruments

In this case, the Kalman gain has the following structure:

$$\begin{aligned}
K_t = \frac{1}{(\sigma_{v,1}^2 + (\sigma_{1,t}^{t-1})^2)(\sigma_{v,2}^2 + (\sigma_{2,t}^{t-1})^2) -  (\rho_t^{t-1}\sigma_{1,t}^{t-1}\sigma_{2,t}^{t-1})^2} \nonumber \\
\begin{pmatrix} 
(\sigma_{1,t}^{t-1})^2 \sigma_{v,2}^2 + (\sigma_{1,t}^{t-1})^2(\sigma_{2,t}^{t-1})^2(1- (\rho_t^{t-1})^2) &  \rho_t^{t-1} \sigma_{1,t}^{t-1}\sigma_{2,t}^{t-1}\sigma_{v,1}^2 \\ 
  \rho_t^{t-1} \sigma_{1,t}^{t-1}\sigma_{2,t}^{t-1}\sigma_{v,1}^2 & (\sigma_{2,t}^{t-1})^2\sigma_{v,1}^2 + (\sigma_{1,t}^{t-1})^2 (\sigma_{2,t}^{t-1})^2)(1-(\rho_t^{t-1})^2)
  \nonumber \\
\end{pmatrix}
\end{aligned}$$

For the case in which $\sigma_{v,2} = 0$ let us see the effect of the
observation of the second instrument on the first one: $$\begin{aligned}
\hat{P}^{t}_{1,t} = \hat{P}^{t-1}_{1,t} + \frac{1}{1-(\rho_t^{t-1})^2 + (\frac{\sigma_{v,1}}{\sigma_{1,t}^{t-1}})^2}\left((1-(\rho_t^{t-1})^2)(O_{1,t} - \hat{P}^{t}_{1,t}) + \rho_t^{t-1} \frac{\sigma_{v,1}^2}{\sigma_{1,t}^{t-1} \sigma_{2,t}^{t-1}}(O_{2,t} - \hat{P}^{t}_{2,t})  \right)  \nonumber \\
\end{aligned}$$

### Pricing sources and models

#### Composites

#### RfQs

#### Trades

#### LOBs

#### HitMiss

#### Correlated instruments

## Derivatives pricing

Derivatives are financial instruments whose value depends on the price of an underlying instrument, hence the name "derivative". It is therefore logic to assume that their pricing should be somehow restricted by that of the underlying. Of course if a derivative trades in relatively liquid markets, to compute its fair price we can simply resort to the techniques discussed above, unless we are trying to identify arbitrage opportunities so we aim at challenging those market prices. Of course, precisely because of the existence of investors that seek to capitalize on those opportunities, one could expect that in those cases markets tend to reflect, at least on average, prices that are consistent with such "relative pricing models". In the absence of liquidity, though, such models become critical to be able to quote prices of derivatives to clients. 

A comprehensive description of techniques for derivatives pricing is out of the scope of this book. Let us concentrate on some of the most popular and liquid contracts, which are more relevant for algorithmic trading

### Statistical pricing of derivatives

Let us consider a simple derivative contract that pays off $P_T = f(S_T)$ at a given expiry date $T > t$, being $t$ the present time. For ease of exposition, we consider $T$ to be determinist, but it could also be contingent to a certain event detailed in the derivative's contract. The pay-off function $P_T$ depends on the value of the underlying $S_T$ at the expiry time $T$. It can also depend on other parameters that are deterministic. For instance, for an European call option we have $P_T = C_T = (S_T-K)^+$, where $K$ is the strike.

The derivative pays in the future a quantity that is contigent to the future value of the underlying, whose value is known today but is uncertain in the future. Therefore, the future pay-off is uncertain, so  which the price would a rational investor be willing to accept to get into this contract, the so-called premium of the derivative? To get an estimation, we need to use probability theory to put some bounds to our uncertainty, so we characterize $S_T$ by a random distribution function $g(S_T)$. As we saw in chapter {ref}`stochastic_calculus`, a popular model that allows us to compute such future distribution is a random walk model or a geometric random walk, the latter being a natural choice for prices that cannot be negative. In those cases the future distribution can be computed, being a normal distribution in the first case, and a log-normal distribution in the second, e.g. in the case of stocks. Although for short expiries the random walk can also be a good model for stocks. These models allow us to get sometimes closed-form solutions, but more realistic models that capture better empirical distributions of prices can be used. 

We can now use the theory of a rational risk-averse investor to compute the value of the premium. We consider that investors might be risk averse, meaning that they need to be compensated increasingly more to take extra risk. In chapter XXX we saw that such behaviour is described by utility functions. And since the derivative's payoff is uncertain before the expiry, we need to compute expected utilities to characterize the value that the investor places on the contract. Using exponential utility, this means:

$$ \mathbb{E}[U] = 1- \mathbb{E}[e^{-\gamma_i \left(e^{-r(T-t)}f(S_T)\right)}] $$

where $\gamma_i$ is the risk aversion coefficient of the investor. We have discounted the payoff at $T$ by the discount factor $e^{-r(T-t)}$ in order to consider the opportunity cost of holding the cash in a deposit or money-market fund. For simplicity, we have considered the interest rate $r$ as constant and determinist up to $T$, but the model can be extended to cover non-deterministic interest rates. 

If the investor needs to pay (or be paid) a premium $P_t$ to enter into the derivative's contract today, the utility calculation changes, since it needs to take into account the premium:

$$ \mathbb{E}[U] = 1- \mathbb{E}[e^{-\gamma_i \left(e^{-r(T-t)}f(S_T) -P_t\right)}] $$

When modelling rational risk-averse agents with utility functions, we model their decisions as those that maximize the expected utility. However, in this case this cannot be used to compute the premium, since naturally the premium that maximizes utility is $P_t = -\infty$!. The problem is, of course, that it does not take into account the utility maximization of the dealer selling the derivative, who would not enter into the contract at this premium. Of course, the same framework could be used to model the dealer's payoff, which is the reverse from the investor, albeit with a different dealer's risk aversion, $\gamma_d$:

$$ \mathbb{E}[U] = 1- \mathbb{E}[e^{-\gamma_d \left(P_t - e^{-r(T-t)}f(S_T) \right)}] $$

but even introducing the dealer's utility function, how could we compute the value of the premium?

For the answer, we need first to frame the problem in other terms: what is the maximum premium that the investor would be willing to pay to enter into the contract? Since the alternative to not entering into the contract implies a zero payoff with total certainty, whose expected utility in this framework is $\mathbb{E}[U_0] = 0$, we can argue that the investor would be willing to buy the derivative as far as the premium makes him/her better off, i.e. $E[U] > 0$. For a value of the premium such that $\mathbb{E}[U] = 0 = \mathbb{E}[U_0]$, the investor is indifferent to buy or not buy. This value of the premium is called the <em>reservation price</em> or the <em>utility indifference price</em> of the investor. Of course the same computation could be done for the dealer, obtaining a different reservation price. An agreement will only happen if the maximum premium that the investor is willing to pay is above the minimum premium that the dealer is willing to receive. 
 
Let us first see the problem from the dealer's point of view. In real situations, it is typically the investor who comes to the dealer and request a price for the derivative. The minimum premium that the dealer would be willing to accept to provide the contract as a reference for derivatives pricing, i.e. the reservation price of the dealer, is the one that solves:

$$ 1- \mathbb{E}[e^{-\gamma_d \left(P_t - e^{-r(T-t)}f(S_T) \right)}] = 0$$

We can now obtain a general expression for the premium:

$$ P_t^d =  \frac{1}{\gamma_d} \log \mathbb{E}[e^{\gamma_d \left(e^{-r(T-t)}f(S_T)\right)}] = \frac{1}{\gamma_d} \log \int dS_T g(S_T) e^{\gamma_d \left(e^{-r(T-t)}f(S_T)\right)} $$ 

For those dealers that have zero risk aversion, i.e. they are <em>risk neutral</em>, by taking the limit $\gamma_d \rightarrow 0$ we get:

$$ P_{0,t} = \mathbb{E}[ e^{-r(T-t)}f(S_T)] = \int dS_T g(S_T) e^{-r(T-t)}f(S_T)$$ 

And for small, but positive risk aversion:

$$ P_t^d = P_{0,t} +  \frac{\gamma_d}{2}\int dS_T g(S_T) e^{-2r(T-t)}f^2(S_T) + O(\gamma_d^2)$$ 

We can derive the same expression for a investor we get:

$$ P_t^i =  -\frac{1}{\gamma_i} \log \mathbb{E}[e^{-\gamma_i \left(e^{-r(T-t)}f(S_T)\right)}] = -\frac{1}{\gamma_i} \log \int dS_T g(S_T) e^{-\gamma_i \left(e^{-r(T-t)}f(S_T)\right)} $$ 

If the investor has a small but positive risk aversion:

$$ P_t^i = P_{0,t} - \frac{\gamma_i}{2}\int dS_T g(S_T) e^{-2r(T-t)}f^2(S_T) + O(\gamma_i^2)$$ 

We see immediately that $P_t^i \leq P_d^i$, so there is only agreement if both investor and dealer are risk neutral, or at least one is risk prone, which is not a normal situation. Therefore, according to this theory of pricing, there would not be trading of derivatives! However, we know empirically that it is not the case. So what was wrong in our theory? We will see that the dealer is not simply taking the opposite bet than the investor, and therefore we need to modify this analysis. Before that, though, let us see particular examples of the computation of the premium for investors.

#### Example: pricing of a simple contingent claim 
A contingent claim is a contract that pays off only under the realization of an uncertain event. Many derivatives contracts like options are contigent claims. The most simple contingent claim pays 1$ under the realization of a specific uncertain event, and zero in all other cases. These contingent claims are called Arrow-Debreu securities, and have a theoretical interest since we could in principle decompose any contingent claim as a linear combination of these securities. Therefore, if we know the prices (premiums) of Arrow-Debreu securities, we could price any contingent claim.

For our purposes, though, we just want to discuss a simple example of reservation prices. Let us consider a contingent claim in which the dealer pays the investor 1$ if we get heads when tossing a fair coin in the present. In our framework, the underlying now is the side of the coin, heads or tails, with probabilities $p_H = p_T = 1/2$. We also make $T = t$ since we toss the coin in the present. The value of the reservation price for the investor reads then:

$$ P_t^i = -\frac{1}{\gamma_i} \log \left(\frac{1}{2}e^{-\gamma_i} + \frac{1}{2} \right) = \frac{1}{2} - \frac{1}{\gamma_i}\log \cosh \left(\frac{\gamma_i}{2}\right)$$

For a risk-neutral investor, by making $\gamma_i \rightarrow 0$, we get simply $P_t^i = 1/2$, which makes sense: the investor is willing to pay 0.5$ to make the game <em>fair</em>. Or in other terms, to make the expected value of the game zero. A fully risk averse investor for whom $\gamma_i \rightarrow \infty$ has $P_t = 0$, i.e. only is willing to buy the contract when there is guarantee of no losses under any scenario. In the middle, the premium lies between those two values: the investor will be willing to pay more than 0$ to trade, as far as the payoff is skewed in its favor. 

#### Example: European Call Options

Let us now focus in a more realistic case, and find the premium for an European Call option on a stock, which has the payoff:

$$ f(S_T) = (S_T - K)^+ $$

where $K$ is the strike of the option. The risk-averse investor will be willing to pay the dealer a maximum premium of:

$$ P_t^i = -\frac{1}{\gamma_i} \log \int dS_T g(S_T) e^{-\gamma_i \left(e^{-r(T-t)}(S_T-K)^+\right)} \$$ 

In the limit of a risk-neutral investor, the premium is:

$$ P_{0,t}^i = \int dS_T g(S_T) e^{-r(T-t)} (S_T-K)^+ \$$ 

Let us consider the case of a non-dividend paying stock, which we model as Geometrical Brownian Motion to ensure non-negative prices are allowed:

$$d S_t = \mu S_t dt + \sigma S_t d W_t$$

where $\mu$ and $\sigma$ are the drift and volatility of the stock, respectively, and $W_t$ a Wiener process. Integrating this SDE up to T:

$$ S_T = S_t e^{(\mu - \frac{\sigma^2}{2})(T-t) + \sigma \sqrt{T-t} Z} $$

where $Z \sim N(0,1)$. We can further decompose the expression of the premimum as:

$$ P_{0,t}^i = \int_0^\infty dS_T g(S_T) e^{-r(T-t)}  (S_T-K)^+ = \int_K^\infty dS_T g(S_T) e^{-r(T-t)}  (S_T - K) $$ 

$$= e^{-r(T-t)} \left(\int_K^\infty dS_T g(S_T) S_T - K \int_K^\infty dS_T g(S_T)\right) $$

Let us now change variables from $S_T$ to $Z$ in the integration. The first integral becomes: 

$$ \int_K^\infty dS_T g(S_T) S_T = S_t \int_{\frac{1}{\sigma \sqrt{T-t}} \left(\log \frac{K}{S_t} - (\mu - \frac{\sigma^2}{2})(T-t)\right)}^\infty \frac{dZ}{\sqrt{2\pi}} e^{-\frac{Z^2}{2}} e^{(\mu - \frac{\sigma^2}{2})(T-t) + \sigma \sqrt{T-t} Z}$$

$$ = S_t e^{(\mu - \frac{\sigma^2}{2})(T-t)} \int_{-d_2(\mu)}^\infty \frac{dZ}{\sqrt{2\pi}} e^{-\frac{Z^2}{2}} e^{ \sigma \sqrt{T-t} Z} = S_t e^{\mu (T-t)} \int_{-d_2(\mu)-\sigma\sqrt{T-t}}^\infty \frac{dZ}{\sqrt{2\pi}} e^{-\frac{(Z-\sigma \sqrt{T-t})^2}{2}}$$

$$ = S_t e^{\mu (T-t)} \left(1-N(-d_1(\mu))\right)$$

where we have defined the functions:

$$d_1(\mu) = \frac{1}{\sigma \sqrt{T-t}} \left(\log \frac{S_t}{K} + (\mu - \frac{\sigma^2}{2})(T-t)\right) $$

$$d_2(\mu) = \frac{1}{\sigma \sqrt{T-t}} \left(\log \frac{S_t}{K} + (\mu + \frac{\sigma^2}{2})(T-t)\right) $$

and $N(x)$ is the cumulative distribution function of the standard normal distribution. The second integral is then:

$$ \int_K^\infty dS_T g(S_T) = \int_{-d_2(\mu)}^\infty \frac{1}{\sqrt{2 \pi}} e^{-\frac{Z^2}{2}} = 1-N(-d_2(\mu))$$

Wrapping up all we get:

$$P_{0,t}^i=S_t e^{(\mu-r)(T-t)}N(d_1(\mu))-K e^{-r(T-t)} N(d_2(\mu)) $$

where we have used the property $1-N(-x) = N(x)$. Let us analyze this formula, which recall is the maximum premium that a investor is willing to pay for the call option. It depends on the following parameters:

* Current stock price $S_t$: as the current stock price increases, the premium increases. This is because the call option gives the right to buy the stock at the strike price, so a higher current stock price makes this option more valuable.

* Strike price $K$: as the strike price increases, the premium decreases. A higher strike price makes the option less valuable since it would cost more to exercise the option.

* Time to maturity $T-t$: as the time to maturity increases, the premium  increases. More time to maturity means more opportunity for the stock price to move favorably.

* Risk-free interest rate $r$: as the risk-free interest rate increases, the premium decreases. A higher risk-free rate reduces the present value of the option payoff, making the option less attractive.

* Stock drift $\mu$: as the stock drift increases, the premium increases, since it is more likely that the option will be exercised. 

* Volatility $\sigma$: as volatility increases, the premium increases. Higher volatility increases the probability of the stock price moving significantly, which benefits the option holder.

We plot those dependencies in the following picture:

```{figure} figures/option_indifference_premium.png
:name: fig:option_indifference_premium
:width: 4in
Dependencies of a call option premium for a risk neutral investor, derived as the maximum premium the investor is willing to pay (reservation or indifference price). We use the parameters $S_t=100$, $K =100$, $T-t = 1$ in years, $r = 0.05$, $\mu = 0.1$, $\sigma = 0.2$.
```

### The Black & Scholes model



## Exercises
