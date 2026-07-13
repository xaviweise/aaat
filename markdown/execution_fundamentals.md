(execution_fundamentals)=
# Execution fundamentals

## Introduction

As introduced in chapter {ref}`algorithmic_trading`, execution algorithms have a single mandate: to buy or sell a specified quantity of a financial instrument at the lowest possible total cost. Unlike investment algorithms—which decide *what* to trade—or market-making algorithms—which continuously provide liquidity by quoting two-sided prices—execution algorithms take the trading decision as given and focus exclusively on *how* to implement it efficiently. This makes execution a universal concern: every market participant, from portfolio managers rebalancing large equity books to banks hedging currency exposures, must at some point execute orders in the market.

The challenge of execution is fundamentally a consequence of market microstructure. In a hypothetical market with unlimited and instantaneous liquidity at a single price, every order would be filled at that price and transaction costs would reduce to simple commissions. In reality, liquidity at any given price level is finite, large orders move prices against the trader, and delay exposes the unexecuted portion to price uncertainty. Managing these effects—collectively known as *transaction costs*—is the central problem that execution algorithms are designed to solve.

This chapter develops the conceptual and quantitative framework for algorithmic execution. We examine the economic motivations for execution optimization ({ref}`sec:exec_objective`), catalogue the costs that arise when trading large orders ({ref}`sec:exec_risks`), and introduce the benchmarks used to evaluate and price execution quality ({ref}`sec:exec_benchmarks`). The section on execution strategies and tactics ({ref}`sec:exec_strategies`) provides an overview of the algorithmic landscape, which is treated in depth in the subsequent chapters: chapter {ref}`optimal_execution` derives optimal execution schedules mathematically, and chapter {ref}`execution_tactics` addresses the micro-level problem of optimal order placement. The quantitative models of limit order book dynamics that underpin tactic design — order arrival processes, fill probability, market impact, and short-term price prediction — are developed in Chapter {ref}`lob_models` of the preceding Advanced Analytics for Financial Markets block.

(sec:exec_objective)=
## The execution business objective

Algorithmic execution serves two primary economic purposes. The first is **internal**: ensuring that trading strategies remain profitable after accounting for the cost of implementing them in the market. The second is **commercial**: enabling broker-dealers and specialized execution providers to offer execution services to clients, competing on the quality and consistency of execution delivered.

### From profitable idea to profitable execution

A trading strategy generates returns only to the extent that the prices at which orders are actually executed are favorable relative to the prices at which the trading decision was made. When order sizes are small relative to market liquidity, execution costs are often negligible. However, institutional orders are frequently large relative to the depth of the limit order book. In these cases, naive execution—for instance, submitting a single large market order—moves prices significantly against the trader before the order is complete. The resulting transaction costs can partially or entirely offset the expected profit of the underlying strategy.

This problem is particularly acute for large asset managers—mutual funds, pension funds, and insurance companies—which must rebalance portfolios involving hundreds of millions or billions of dollars of assets. Banks hedging market risk exposures face similar challenges. For systematic hedge funds operating with tight signal-to-noise ratios, execution costs can determine whether a strategy is economically viable. A strategy that generates an expected alpha of 20 basis points is worthless if execution consistently costs 25 basis points.

### Execution as a business

Banks, broker-dealers, and specialized execution firms frequently execute orders on behalf of clients who prefer to delegate this function. This *agency execution* business is commercially significant: clients compensate providers through commissions, bid-offer spreads, or agreed benchmark-relative pricing arrangements.

In a competitive market for execution services, providers have a strong incentive to optimize their algorithms, since better execution allows more competitive pricing or higher margins. This competitive dynamic also creates a need for *transparency and measurement*: a client who delegates execution must be able to assess the quality of what was delivered. This requirement drives the use of standardized benchmarks—reference prices against which execution cost is measured—and gives rise to the practice of Transaction Cost Analysis (TCA), discussed in {ref}`sec:exec_tca`.

(sec:exec_risks)=
## Execution Risks and Tradeoffs

### Transaction costs

When executing a large order, a trader incurs a variety of costs beyond the nominal price of the instrument. Understanding the full cost structure is essential for algorithm design and performance evaluation. The principal components are:

- **Commissions**: payments to broker-dealers for order routing, execution, and related services. Typically negotiated bilaterally and vary by asset class and client relationship.

- **Fees**: exchange-mandated payments charged per executed order, covering clearing, settlement, and market access. These are set by the exchange or central counterparty.

- **Taxes**: government-imposed levies on trading activity or realized gains. Notable examples include the UK Stamp Duty Reserve Tax on equity purchases and Financial Transaction Taxes (FTTs) in France and Italy.

- **Rebates**: some exchanges operate a *maker-taker* model under which liquidity-providing orders (typically limit orders resting in the book) receive a rebate, while liquidity-consuming orders pay a fee. Under a *taker-maker* model the incentive is reversed. Rebates meaningfully affect the relative economics of aggressive versus passive order types.

- **Spreads**: the bid-ask spread is the implicit cost of consuming liquidity. A market order to buy executes at the ask price, which exceeds the theoretical fair-value mid-price by half the spread. The spread compensates market makers for inventory risk and adverse selection, and is directly related to the instrument's liquidity.

- **Delay cost**: the cost arising from the gap between the time a trading decision is made ($t_d$, at price $p_d$) and the time the first order reaches the market ($t_a$, at price $p_a$). During this interval, driven by processing latency and order routing, prices may move adversely.

- **Market impact**: adverse price movements caused by the trader's own orders. Market impact arises because large orders reveal information about trading intent and consume the available liquidity at favorable prices, forcing subsequent executions to occur at progressively worse levels.

- **Timing risk** (also called *price risk*): the uncertainty in execution costs arising from market conditions—price volatility, spread changes, and volume fluctuations—during the execution window. Unlike market impact, timing risk is stochastic: the market can move either favorably or unfavorably while an order is being worked.

- **Opportunity cost**: the cost of failing to execute the full order within the target time window. When an execution algorithm does not complete its mandate—because passive orders did not fill, or execution was halted—the unexecuted quantity must either be abandoned (foregone profit or avoided loss) or completed later at potentially worse prices.

The following figure illustrates the relationship between these cost components along the timeline of a typical buy order, from decision time through arrival at the market to final execution.

```{figure} figures/exec_cost_timeline.png
:name: fig:exec_cost_timeline
:width: 9in
Transaction cost components along the execution timeline of a buy order. At decision time $t_d$ the trader decides to buy at mid-price $p_d$. Delay cost arises from price movement between $t_d$ and arrival time $t_a$. Price risk captures the stochastic movement of the mid-price during the execution window. The spread is the half-width between the mid and the best ask. Market impact lifts the execution price $p_{exec}$ above the ask due to the order's own price pressure.
```

### Market impact

Market impact is the central challenge in algorithmic execution. Mathematically, it is defined as the difference between the actual price trajectory with the order and the counterfactual trajectory that would have occurred without it. Since this counterfactual is unobservable, market impact cannot be measured precisely; in practice it is estimated using pre- and post-trade price references.

Market impact is conventionally decomposed into two components:

- **Temporary market impact** is the immediate price concession required to absorb the order against the current limit order book. When a buyer demands more liquidity than is available at the best ask, they must accept progressively worse prices at deeper levels of the book. This cost is transient: once the order is filled, prices tend to partially revert as new orders replenish the consumed liquidity.

- **Permanent market impact** is the long-lasting price change that arises because the order reveals information to other market participants, who update their estimates of fair value and adjust their own quotes accordingly. Unlike temporary impact, permanent impact does not revert.

A classical and widely-used model for temporary market impact is the **square-root model** {cite:p}`grinold2000active`:

$$\Delta P = \text{Spread cost} + Y \sigma \sqrt{\frac{Q}{V}}$$

where $\sigma$ is the average daily volatility, $V$ is average daily volume, $Q$ is the order size, and $Y$ is a calibrated constant. The square-root functional form—as opposed to the linear form that is more analytically tractable—reflects an empirical regularity documented across a wide range of asset classes and order sizes: empirical studies show that the square-root model fits impact data over two to three orders of magnitude in relative order size $Q/V$ {cite:p}`toth2011anomalous`. The model can be generalized to a power law and enriched with intraday information (intraday spreads, predicted volume, realized volatility), at the cost of more complex calibration.

The square-root model is used as standard in many theoretical papers and in commercial implementations (e.g., Bloomberg's pre-trade analytics). A linear market impact model—$\Delta P = k q_i$—is less realistic empirically but considerably more tractable and is used extensively in the derivation of optimal execution strategies (see chapter {ref}`optimal_execution`). The three main applications of market impact models are:

- **Backtesting**: estimating the market impact of simulated orders in historical data, where actual impact is unobservable.
- **Pre-trade analysis**: forecasting the expected cost of a planned execution before it is launched.
- **Strategy derivation**: serving as the impact function in the objective of optimal execution problems such as Bertsimas and Lo {cite:p}`BERTSIMAS19981` and Almgren and Chriss {cite:p}`almgren2000optimal`.

### Timing risk

Timing risk encompasses the costs and profits arising from market uncertainty during the execution window. Three main sources contribute to it:

**Price volatility**: During the execution window, prices fluctuate due to new information arrivals and changing order flow. An algorithm that spreads an order over time to reduce market impact exposes the unexecuted portion to price movements over that horizon. If prices rise (for a buy order), execution cost increases; if prices fall, the reverse holds. The longer the execution window, the larger the cumulative exposure to price risk.

**Liquidity changes**: The bid-ask spread and available depth fluctuate intraday in response to news events, trading activity, and the presence of other large orders. Empirically, spreads tend to be widest at the open and narrowest in the middle of the session, following a U-shaped intraday pattern {cite:p}`cartea2015algorithmic`. These liquidity changes affect both the cost of aggressive orders (through the spread cost component of market impact) and the fill probability of passive orders resting in the book.

**Volume fluctuations**: The rate of market order arrivals—and thus the probability of filling a passive limit order—varies over the trading day. Volume profiles typically exhibit a U-shape or J-shape (concentrated at the open and close), and can be dramatically distorted on option and index expiration days, central bank announcement days, or around major scheduled events. This pattern has direct implications for VWAP and PoV strategies, which aim to track a proportion of market volume.

### The trader's dilemma

The fundamental trade-off in execution design arises from the opposing effects of the execution horizon on market impact and timing risk. This tension—sometimes called the **trader's dilemma**—is summarized as follows:

- **Market impact** is larger when the execution is compressed into a shorter time window, because each child order must consume more of the available liquidity per unit of time.
- **Timing risk** is larger when the execution is spread over a longer time window, because the unexecuted portion is exposed to price uncertainty for a longer period.

The resulting *efficient trading frontier* (introduced by Almgren and Chriss {cite:p}`almgren2000optimal` and popularized in practice by Kissell {cite:p}`kissell2014science`) traces the Pareto-optimal set of strategies in the (timing risk, market impact) plane, as illustrated in {numref}`fig:exec_frontier`. Any execution strategy that is simultaneously minimum-impact and minimum-risk is impossible. Strategies that lie above and to the right of the frontier—such as point D in the figure—are dominated: there exists a better strategy for the same level of risk.

```{figure} figures/exec_efficient_frontier.png
:name: fig:exec_frontier
:width: 7in
The efficient trading frontier in the market impact–timing risk plane {cite:p}`almgren2000optimal` {cite:p}`kissell2014science`. Point A (high impact, low risk) corresponds to aggressive, fast execution. Point C (low impact, high risk) corresponds to passive, slow execution. Point B lies on the frontier at an intermediate position. Point D lies above the frontier: it is a dominated strategy for which a lower-cost, lower-risk alternative exists.
```

The optimal position on the frontier depends on the **risk tolerance** of the trader. A risk-neutral trader who cares only about expected cost minimizes market impact by spreading the execution uniformly over the allowed window. A risk-averse trader accepts higher expected cost in exchange for lower variance—executing more aggressively early to avoid adverse price drift. The Almgren-Chriss framework, derived in chapter {ref}`optimal_execution`, formalizes this trade-off and produces optimal execution schedules parameterized by a risk aversion coefficient $\lambda$.

### What constitutes good execution

A rigorous definition of execution quality must acknowledge that transaction costs are random variables rather than deterministic quantities: they depend on market conditions unknown at the time the execution strategy is chosen. Formally, the total cost of a buy execution is:

$$TC = \sum_i p_i^{exec} q_i + \text{fees}$$

where $p_i^{exec}$ is the execution price of the $i$-th child order and $q_i$ is the corresponding quantity ($TC$ is negated for sell orders). Because transaction costs are stochastic, a strategy that minimizes expected $TC$ may still deliver unacceptably large costs in adverse scenarios due to timing risk. Practitioners therefore evaluate execution strategies by their full cost distribution: comparing not only means but also standard deviations, high quantiles (tail risk), and behavior across market regimes.

In practice, execution quality is also measured by comparison with **benchmarks**: reference prices constructed from market data that provide a market-wide baseline for what was achievable under ambient conditions. This is the subject of the next section.

(sec:exec_benchmarks)=
## Execution Benchmarks

An execution benchmark is a reference price constructed from market data that serves two purposes: evaluating the performance of an execution algorithm, and pricing the cost of an execution when delegated by a client to a specialist. Selecting an appropriate benchmark requires careful consideration of the trading objective, since different benchmarks reward different properties of the execution.

### Pricing an execution using a benchmark

When a client delegates a block order to a broker-dealer, a benchmark is used to fix the reference price for the execution cost charged to the client. The broker-dealer's pricing process is:

1. Use an execution algorithm designed to match or beat the chosen benchmark.
2. Construct, from historical performance data on similar orders, the empirical distribution of execution outcomes relative to the benchmark (in basis points).
3. Select a percentile of the loss tail—aggressive providers may target around the 50th percentile; conservative ones typically use between the 5th and 35th percentile—sufficient to make the business profitable on average.
4. Quote the client: **price = benchmark + selected percentile**.

This mechanism aligns the incentives of broker and client and allows objective performance reporting. The transparency it enables is also a regulatory requirement under best execution rules (see {ref}`sec:exec_tca`).

### Implementation Shortfall

The **Implementation Shortfall (IS)** benchmark {cite:p}`perold1988implementation` measures execution cost relative to the mid-price prevailing at the moment the trading decision was made. It captures the full *shortfall* between the paper portfolio performance (at the decision price) and the actual portfolio performance (at the execution prices).

For a buy order of total size $Q$ that is fully executed within the allowed window:

$$IS = \sum_i q_i p_i^{exec} + \text{fees} - Q p_0 = Q(p_{\text{avg}} - p_0) + \text{fees}$$

where $p_0$ is the mid-price at arrival time and $p_{\text{avg}} = Q^{-1}\sum_i q_i p_i^{exec}$ is the volume-weighted average execution price. When the algorithm does not complete the full order within the maximum time $T$, an opportunity cost for the unexecuted quantity must be added:

$$IS = \sum_i q_i (p_i^{exec} - p_0) + \left(Q - \sum_i q_i\right)(p_T - p_0) + \text{fees}$$

where $p_T$ is the mid-price at the end of the execution window and the second term prices the unexecuted residual at the market close. The IS P&L, expressed in basis points, is:

$$P\&L_{IS} = \text{side} \times \frac{p_0 - p_{\text{avg}}}{p_0} \times 10^4, \quad \text{side} = +1 \text{ (buy)}, -1 \text{ (sell)}$$

IS is the most conceptually complete benchmark: it accounts for all sources of execution cost, including the opportunity cost of unfilled quantity. It is the natural benchmark for traders with a specific target and timeline driven by investment or risk management needs, and its minimization is the objective of the Almgren-Chriss algorithm derived in chapter {ref}`optimal_execution`.

### Time Weighted Average Price

The **Time Weighted Average Price (TWAP)** benchmark is the arithmetic mean of market prices over the execution window, averaging first within each equal-length time sub-interval and then across intervals:

$$\text{TWAP} = \frac{1}{n} \sum_{i=0}^{n-1} p_i^{\text{twap}}, \quad p_i^{\text{twap}} = \frac{1}{N_{\text{trades}(i)}} \sum_{j \in \text{trades}(i)} p_j^{\text{avg}}$$

The TWAP cost measure and P&L are:

$$C_{\text{twap}} = Q(p_{\text{avg}} - p_{\text{twap}}) + \text{fees}$$
$$P\&L_{\text{twap}} = \text{side} \times \frac{p_{\text{twap}} - p_{\text{avg}}}{p_{\text{twap}}} \times 10^4$$

TWAP is a natural benchmark when the trader wants uniform participation in the market over a fixed window. The TWAP algorithm—splitting the order into equal-sized slices executed at equal time intervals—is also the optimal execution strategy for minimizing expected cost under a linear temporary market impact model and a random-walk price process, as shown by Bertsimas and Lo {cite:p}`BERTSIMAS19981` and derived in chapter {ref}`optimal_execution`. The solution is deterministic and does not depend on the specific realization of market impact or price dynamics, which makes TWAP robust and simple to implement.

### Volume Weighted Average Price

The **Volume Weighted Average Price (VWAP)** benchmark is the volume-weighted average of all market trade prices over the execution window:

$$\text{VWAP} = \frac{\sum_{i=0}^{n-1} v_i p_i^{\text{vwap}}}{\sum_{i=0}^{n-1} v_i}, \quad p_i^{\text{vwap}} = \frac{\sum_{j \in \text{trades}(i)} v_j p_j^{\text{avg}}}{\sum_{j \in \text{trades}(i)} v_j}$$

The corresponding cost measure and P&L are:

$$C_{\text{vwap}} = Q(p_{\text{avg}} - p_{\text{vwap}}) + \text{fees}$$
$$P\&L_{\text{vwap}} = \text{side} \times \frac{p_{\text{vwap}} - p_{\text{avg}}}{p_{\text{vwap}}} \times 10^4$$

VWAP is one of the most widely used benchmarks for broker-dealers executing equity orders on behalf of clients. Its appeal lies in the fact that it captures the representative price at which the market transacted over the window, weighted by activity: periods with high volume receive more weight, reflecting periods of particularly intense price discovery. VWAP is also a natural benchmark when the goal is to blend inconspicuously into market flow.

However, VWAP has a well-known conceptual issue for large orders: since the algorithm's own trades contribute to the benchmark, a strategy that executes aggressively can mechanically improve its measured VWAP performance by moving the benchmark itself. When order sizes are not negligible relative to market volume, the actual VWAP including own trades is:

$$\text{VWAP} = \frac{\sum_{i=0}^{n-1}(v_i p_i^{\text{vwap}} + |q_i| p_i^{\text{exec}})}{\sum_{i=0}^{n-1}(v_i + |q_i|)}$$

Optimal strategies that maximise own VWAP performance in this setting can produce behaviours tantamount to market abuse. For this reason, VWAP is used as a benchmark primarily when order sizes are small relative to market volume, so that own trades do not materially affect the benchmark. The VWAP execution algorithm—which tracks a predicted intraday volume curve—is derived in chapter {ref}`optimal_execution`, where it is also shown that, under a volume-proportional market impact model, the optimal VWAP strategy coincides with the IS-minimizing strategy {cite:p}`kato2017vwap`.

### Percentage of Volume

The **Percentage of Volume (PoV)** benchmark measures the algorithm's participation rate as a fraction of market volume at each time interval:

$$\text{POV}_i = \frac{q_i}{v_i}$$

A PoV strategy targets a constant participation rate $\rho$, executing $q_i = \rho v_{i-1}$ at each interval (using observed volume from the previous interval). Unlike IS, TWAP, and VWAP, the PoV benchmark does not specify a fixed completion time: the algorithm finishes when accumulated market volume is sufficient to absorb the full order. The PoV algorithm is discussed in chapter {ref}`optimal_execution`.

PoV is appropriate when the primary objective is minimizing market footprint without a strict deadline, and when the trader is willing to accept uncertainty around the completion time. The key limitation is that execution is not guaranteed within any finite window: if market volume is unexpectedly low, the order may not complete within the trading session, giving rise to opportunity cost that must be tracked and managed.

(sec:exec_strategies)=
## Execution strategies and execution tactics

The design of an execution algorithm naturally decomposes into two hierarchical levels, which correspond to the two dimensions of the execution problem: *when* to trade across the full execution window, and *how* to place individual orders in the limit order book at each selected moment.

**Execution strategies** (macro-strategies or execution schedules) determine the sequence of target sub-order sizes $q_1, \ldots, q_n$ to be executed in successive time windows of length $T/n$, given the total order $Q$, the horizon $T$, and the chosen objective. They operate at the scale of the parent order, balancing market impact against timing risk.

**Execution tactics** (micro-strategies) determine how to place each child order $q_i$ in the limit order book within its allocated window, deciding between market orders, limit orders, and combinations, at what price levels, and in what sequence. They operate at the scale of individual order events, managing the fill probability and price improvement of each slice.

This hierarchical decomposition is convenient and standard in practice, even if not globally optimal. It allows the two sub-problems to be designed and calibrated independently, and updated at different speeds—strategies at the timescale of minutes, tactics at the timescale of seconds or sub-seconds.

In fragmented markets, a third layer—**Smart Order Routing (SOR)**—sits between strategy and tactic, allocating each child order across multiple trading venues to minimize total cost given venue-specific fee structures, depths, and execution probabilities. SOR is discussed in chapter {ref}`execution_tactics`.

### Overview of execution strategies

The principal execution strategies used in practice are:

**TWAP**: Divides the total order into equal-sized slices executed at equal time intervals. The simplest possible execution schedule, and the optimal strategy under linear temporary market impact with a risk-neutral objective {cite:p}`BERTSIMAS19981`. Its deterministic, non-adaptive nature makes it predictable and thus potentially vulnerable to gaming by other market participants; more sophisticated strategies seek to add randomization.

**VWAP**: Allocates the order proportionally to a predicted intraday volume curve. Participates more heavily when market volume is high (typically at the open and close) and less when volume is low. Requires volume forecasting and tracks the VWAP benchmark. Under a volume-proportional market impact model, the static VWAP strategy is optimal for a risk-neutral trader minimizing IS {cite:p}`kato2017vwap`. Volume predictions are typically constructed using historical averages of intraday volume profiles, calibrated with time-series or machine-learning models {cite:p}`busseti2015vwap`.

**Implementation Shortfall (IS)**: Directly minimizes the expected implementation shortfall penalized by its variance, for a given risk aversion parameter $\lambda$. Front-loads the execution when risk aversion is high (to reduce timing risk), approaching aggressive execution at the limit; converges to a uniform schedule (TWAP) when risk aversion is low. The Almgren-Chriss framework {cite:p}`almgren2000optimal` provides the analytical closed-form solution.

**Percentage of Volume (PoV)**: Maintains a constant participation rate in market volume without specifying a fixed horizon. Appropriate when market impact control is the primary objective and there is no hard deadline for order completion.

### Overview of execution tactics

Execution tactics address order placement within the time window allocated by the strategy. The core decision is the choice between market orders, which guarantee immediate execution but consume liquidity and incur the full spread, and limit orders, which can achieve more favorable prices if filled but carry non-execution risk.

The optimal balance between passive and aggressive order types—and the optimal price level for limit orders—depends on remaining quantity, remaining time, current liquidity conditions, and market impact parameters. A simple model for this decision, developed by {cite:t}`cartea2015algorithmic`, places a limit order at $\delta$ ticks from the mid-price, where fill probability decays exponentially with $\delta$. The optimal $\delta$ is solved dynamically using stochastic optimal control, converging to increasingly aggressive placements as the deadline approaches. Chapter {ref}`execution_tactics` derives this framework in detail.

(sec:exec_tca)=
## Transaction Cost Analysis

Transaction Cost Analysis (TCA) is the systematic measurement, attribution, and reporting of execution costs. It serves both operational and commercial purposes: operationally, it provides feedback for algorithm improvement; commercially, it allows clients and regulators to verify that execution obligations were met.

### Pre-trade TCA

Pre-trade TCA estimates expected execution costs before a trade is submitted, enabling informed decisions about strategy, urgency, and timing. Key outputs include:

- **Market impact estimate**: Using a model such as the square-root formula, an estimate of the expected price impact from the planned order given its size relative to average daily volume and prevailing volatility.
- **Timing risk estimate**: A forecast of price volatility over the planned execution window, used to estimate the variance of execution cost and position the strategy on the efficient frontier.
- **Strategy comparison**: An assessment of how different execution strategies (TWAP, VWAP, IS, PoV) are expected to perform in current market conditions, enabling the selection of the appropriate strategy and risk setting before execution begins.

Pre-trade TCA is particularly important for large or complex orders where execution costs are material. The cost estimates it produces can also be used to decide whether it is worth executing the strategy at all, or whether it should be deferred to a more favorable liquidity environment.

### Post-trade TCA

Post-trade TCA measures the actual performance of a completed execution against benchmark references, and decomposes the total observed cost into its components. Standard metrics include:

- **IS performance**: Actual implementation shortfall relative to the arrival price, expressed in basis points. Captures the total execution cost including timing risk.
- **VWAP performance**: The algorithm's volume-weighted average execution price relative to the market VWAP, expressed in basis points.
- **TWAP performance**: The algorithm's average execution price relative to the market TWAP.
- **Fill rate**: The proportion of the order executed within the target window, relevant when passive orders with execution risk are used.

Post-trade TCA also supports **cost attribution**: decomposing total observed cost into spread cost, market impact, timing risk, and fees. This decomposition allows practitioners to identify which cost components are being controlled well and which represent opportunities for algorithm improvement.

### Regulatory context

Under MiFID II {cite:p}`MiFIDII2014`, investment firms must demonstrate *best execution* for client orders—a standard that requires considering multiple factors including price, costs, speed, likelihood of execution, and order size. TCA reports are a key tool for documenting best execution compliance. The requirement applies not only to the execution of specific orders but also to the ongoing review of execution arrangements and the selection of venues and algorithms. This makes systematic TCA both best practice and a regulatory obligation for firms operating under European market rules.

## Exercises

1. A portfolio manager wants to buy 500,000 shares of a stock with an average daily volume of 2,000,000 shares, average daily volatility of 1.5%, and an average bid-ask spread of 5 basis points. Using the square-root market impact model with $Y = 1$, estimate the expected market impact of executing the full order as a single market order. Compare this to a TWAP strategy that splits the order into 12 equal slices over a trading day.

2. An execution algorithm completed a buy order of 100,000 shares at a volume-weighted average price of €50.15. The arrival mid-price was €50.00 and the market VWAP over the execution window was €50.10. Fees amounted to €500. Calculate the IS cost, the VWAP cost, and the IS P&L in basis points.

3. Explain the trader's dilemma in your own words. Why is it generally impossible for an execution algorithm to simultaneously minimize expected market impact and expected timing risk? Under what conditions does the efficient frontier degenerate to a single point (a unique optimal strategy)?

4. A broker-dealer offers to execute a large equity order at a price of VWAP + 5 basis points. Describe the process by which the broker-dealer likely arrives at this quote. What does the "+5 basis points" represent in terms of the broker's historical performance distribution? What risk does the broker bear by offering this price?

5. Consider a PoV strategy targeting a participation rate of $\rho = 10\%$. In the first five minutes, the market trades 50,000 shares. How many shares does the algorithm execute? If the algorithm must complete 500,000 shares but total market volume for the day turns out to be only 3,000,000 shares, will the algorithm complete the order? How should the opportunity cost of the unexecuted residual be computed in the IS framework?

6. The VWAP benchmark is widely used but not without problems. Describe the self-referential issue that arises when an algorithm's own trades are large relative to market volume. Why might strategies designed to maximize measured VWAP performance in this setting constitute market abuse?
