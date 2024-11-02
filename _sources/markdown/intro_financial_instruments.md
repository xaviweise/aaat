# Financial Instruments

## Introduction

## Stocks

## Bonds

### Derivatives

Derivatives are financial instruments whose value depends on the price of an underlying instrument, hence the name "derivative".

### Linear derivatives: Forwards, Futures and ETFs

### Options

Options are derivatives contracts that grant the holder the  the option (hence the name) to buy or sell (depending on the option) a given financial instrument (the underlying) at a price at time contingent to the clauses of the contract. The most simple option, the European option, pre-specifies a given time $T$, the expire, and price $K$, to exercise this option. But there are many other variations in the market. An option to buy a financial instrument is referred as a call option, and an option to sell is a put option. 

Let us consider european options of stocks. If the market price of the stock at the expiry is $S_T$, a call option will be exercised by a rational investor only if the price is higher than the strike $K$, making a profit of $S_T-K$, which in some cases is directly paid in cash, in others the actual stock is received, but of course it could be directly sold in the market at a favorable price. Therefore, the payoff of a call option can be written as:

$$C_T = (S_T-K)^+$$

where $(.)^+$ denotes the positive part of the argument. On the contrary, a put option will only be exercised if the market price is below the strike, hence the payoff is:

$$P_T = (K-S_T)^+$$

Options can be traded in regulated markets or be quoted by bank dealers. Since the investor that holds the option cannot lose money from it, such option does not come for free, and the question is how much is worth such option, which is called the premium of the option. At expiry, the price is naturally the payoff function. What at at time $t < T$ there is still  uncertainty about the price $S_T$ which will determine the final profit (if any), so the premium will be different. But how much? That is the subject of the theory of option pricing.
