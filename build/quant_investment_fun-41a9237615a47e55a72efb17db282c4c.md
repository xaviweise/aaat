(quant_investment_fundamentals)=
# Quantitative Investment Fundamentals

## Introduction

Quantitative investment strategies aim to generate returns that are systematically repeatable, rigorously evaluated, and as free as possible from the arbitrary discretion that characterises traditional active management. The fundamental idea is simple: identify patterns in market prices, macroeconomic variables, fundamental data, or other information sources that predict future returns, and translate those patterns into automatic trading rules. The challenge lies in the word *systematically* — financial markets are competitive, non-stationary environments where patterns are discovered and exploited until they disappear, and where the boundary between genuine predictive signal and spurious data-mining artefact is notoriously difficult to draw.

This chapter provides the conceptual and practical foundations for quantitative investment. We begin by situating investment algorithms within the broader landscape of algorithmic trading ({ref}`sec:qi_landscape`), comparing them to execution and market-making algorithms discussed in earlier chapters. Section {ref}`sec:qi_types` presents a taxonomy of investment strategies — mean reversion, trend following, statistical arbitrage, factor investing, and portfolio optimisation — and characterises the economic rationale and typical operating timeframe of each. Section {ref}`sec:qi_lifecycle` describes the lifecycle of a quantitative strategy from ideation through live deployment. The core empirical discipline of the field, backtesting, is treated in {ref}`sec:qi_backtest`, covering data requirements, simulation fidelity, and the walk-forward validation framework. Section {ref}`sec:qi_metrics` collects the standard performance metrics used to evaluate and compare strategies. The chapter closes with a discussion of the most dangerous pitfalls in quantitative research — the systematic biases that produce strategies that look excellent in simulation but fail in production ({ref}`sec:qi_pitfalls`).

The mathematical foundations of each strategy class are developed in detail in chapter {ref}`optimal_investment_theory`. The present chapter focuses on intuition, classification, and practical methodology.

(sec:qi_landscape)=
## Algorithmic investment in context

The three pillars of algorithmic trading — execution, market making, and investment — share the same infrastructure (market data, order management, risk systems) but differ fundamentally in their objective and time horizon.

**Execution algorithms** (chapters {ref}`execution_fundamentals` and {ref}`optimal_execution`) accept a decision already made by a human or another algorithm — buy $N$ shares of IBM — and focus on minimising the cost of implementing it: slippage, market impact, opportunity cost. The alpha is external to the algorithm; its job is to lose as little of it as possible in the implementation.

**Market-making algorithms** (chapters {ref}`market_making_fundamentals` and {ref}`optimal_market_making`) do not form views on whether prices will go up or down. They extract the bid-ask spread from two-sided trading, managing inventory risk as the primary operational challenge. Their holding period is typically minutes to hours; their P&L comes from flow, not from price prediction.

**Investment algorithms** are in the business of *predicting price direction* — or, more precisely, predicting the risk-adjusted return of a position. They open positions expecting them to be profitable over a defined horizon (minutes to months, depending on the strategy) and close them when the expected return has been realised or the thesis invalidated. The quality of an investment algorithm is fundamentally determined by the quality of its predictive signal — its **alpha** — and the quality of its risk management.

The distinction is not always sharp. A market maker who tilts her quotes based on an Ornstein-Uhlenbeck (OU) model of the mid-price (chapter {ref}`optimal_market_making`, enriching section) is incorporating a directional alpha into her quoting. A VWAP execution algorithm that adapts its schedule based on intraday momentum is blurring the boundary between execution and investment. In practice, the three functions are often integrated in the same trading system, and the clean conceptual separation is a simplification that helps in understanding the purpose of each component.

The AI and machine learning taxonomy from the AlgoTrading lecture notes applies across all three domains but is particularly prominent in investment algorithms. Rules-based systems (technical analysis, fixed thresholds) dominated the early years of algorithmic investment. Mathematical optimisation models — mean-variance optimisation, Kalman filters, OU models — form the backbone of systematic funds today. Data-driven machine learning (classification and regression models for return prediction, reinforcement learning for strategy optimisation) is rapidly growing. Model-based causal approaches {cite:p}`lopezdeprado2022causal` represent the frontier of principled alpha generation.

(sec:qi_types)=
## A taxonomy of investment strategies

Investment strategies can be classified by the **economic hypothesis** they exploit, the **time horizon** over which the hypothesis operates, and the **instruments** used. The four major classes are summarised below and treated mathematically in chapter {ref}`optimal_investment_theory`.

(sec:qi_mean_reversion)=
### Mean reversion

**Economic hypothesis**: prices of one or more instruments tend to revert toward a long-run mean or fair value, so that deviations from that mean are temporary and therefore predictable.

**Intuition**: markets may overreact to news, creating transient mispricings that correct over minutes, hours, or days. In pairs of closely related instruments — such as CAC 40 and EUROSTOXX 50 futures, or two credit default swaps on the same issuer traded in different currencies — the long-run price relationship is determined by fundamentals (index composition, recovery rates, interest-rate levels), while short-term deviations reflect temporary imbalances in supply and demand.

The canonical mathematical model for mean-reverting prices is the **Ornstein-Uhlenbeck (OU) process** {cite:p}`cartea2015algorithmic`:
$$dx_t = \theta(\mu - x_t)\,dt + \sigma\,dW_t$$
where $\theta > 0$ is the speed of mean reversion, $\mu$ is the long-run mean, and $\sigma$ is the diffusion coefficient. The parameter $\theta$ implies a **half-life** $t_{1/2} = \ln 2\, /\,\theta$: the expected time for the deviation from $\mu$ to halve. A practical mean-reversion strategy measures the current z-score $z_t = (x_t - \hat{\mu})/\hat{\sigma}$ and enters a position when $|z_t|$ exceeds a threshold (typically $\pm 1.96$ standard deviations), profiting as $z_t$ reverts toward zero.

A very typical strategy is **pairs trading**: two correlated instruments are found to be cointegrated (their spread is mean-reverting); the strategy trades the spread, going long the relatively cheap leg and short the expensive one. The classic example in the literature {cite:p}`chan2013algorithmic` is the EWA (iShares MSCI Australia ETF) vs EWC (iShares MSCI Canada ETF) pair, whose price ratio fluctuated around a stable mean over several years. When the ratio deviates beyond two standard deviations, the pair is entered; it is exited when the ratio returns to the mean. More generally, the Johansen cointegration test identifies mean-reverting combinations of three or more instruments simultaneously.

**Typical instruments**: equity pairs, equity-index futures, FX cross-rates, interest-rate spread products (swap spreads, bond spreads), volatility surfaces.

**Timeframe**: intraday to days for equity pairs; days to weeks for macro spread products.

**Key risk**: the assumed mean may shift permanently (a **regime change**), turning a mean-reversion signal into a directional loss. Distinguishing a temporary deviation from a structural break is the central operational challenge.

(sec:qi_trend)=
### Trend following

**Economic hypothesis**: past price returns are positively autocorrelated over some horizon, so that buying recent winners and selling recent losers earns a positive expected return.

**Intuition**: trends arise from the slow diffusion of information into prices (not all participants react instantaneously to news), from the momentum of fund flows (large trend-following funds themselves reinforce the trends they exploit), from stop-loss cascade effects, and from the rebalancing flows of index-tracking and hedging portfolios {cite:p}`moskowitz2012time`. The classic empirical finding of {cite:t}`jegadeesh1993returns` documented that equity returns over 3–12 month horizons are strongly autocorrelated: stocks that outperformed over the past year tend to outperform in the following months. {cite:t}`moskowitz2012time` extended this to a broad set of asset classes — equities, bonds, commodities, FX — demonstrating **time-series momentum** as a near-universal phenomenon.

The standard detection tool is an autocorrelation analysis or, equivalently, the **Hurst exponent** $H$: for a price series with $H > 0.5$, the process diffuses faster than a random walk — a signature of trending behaviour. For $H < 0.5$, the diffusion is slower than a random walk, a signature of mean reversion. A standard random walk has $H = 0.5$. This single statistic thus classifies the time-series nature of any price sequence.

**Typical strategies**: trend-following (CTA) funds trade momentum signals across equities, fixed income, FX, and commodities using moving averages or time-series momentum scores. Intraday momentum exploits shorter-horizon signals — order-book imbalance (chapter {ref}`lob_models`), opening-gap patterns, news-driven sentiment shocks. Cross-sectional momentum ranks a universe of instruments by recent return and goes long the top decile while shorting the bottom.

**Timeframe**: intraday (HF momentum) to months (cross-sectional equity momentum).

**Key risk**: trend-following suffers sharp losses in market reversals. It is well known to perform well in trending markets and poorly in range-bound or volatile sideways environments. Managing the transition between regimes is the main challenge.

(sec:qi_stat_arb)=
### Statistical arbitrage

**Economic hypothesis**: a financial instrument (or portfolio of instruments) is mispriced relative to its theoretical fair value implied by no-arbitrage relationships, and the mispricing will correct.

**True vs statistical arbitrage**: a **true arbitrage** is a strategy that generates a positive return with zero risk — for instance, buying a futures contract and simultaneously selling the equivalent basket of underlyings when the futures price deviates from its fair value. In practice, true arbitrages are extremely rare and short-lived because they require: (i) a model-free fair value (so no model risk), (ii) perfectly liquid execution in both legs simultaneously, and (iii) no transaction costs. Common near-arbitrages include equity futures vs. index basket, FX triangular arbitrage (EURUSD × USDJPY × EURJPY ≠ 1), and put-call parity violations. In all of these, liquidity differences, transaction costs, and contractual details (dividend treatment, margin requirements) introduce a **basis** that converts the true arbitrage into a **statistical arbitrage** {cite:p}`avellaneda2010statistical`: a strategy with positive expected return and small but non-zero risk.

**StatArb sub-classes** include:
- *Risk-neutral model arbitrages*: volatility strategies (variance swaps, volatility surface arbitrage), yield-curve strategies (butterfly trades, swap spreads), mortgage derivative strategies.
- *Capital structure arbitrage*: long CDS vs short equity (or vice versa) on the same issuer, exploiting temporary divergences between credit and equity market assessments of company risk.
- *Machine-learning model arbitrages*: using ML models of fair value to identify mispricings. These are increasingly popular but prone to overfitting and require causal validation {cite:p}`lopezdeprado2022causal` to distinguish genuine economic signals from data artefacts.

**Timeframe**: milliseconds (cross-venue arbitrage) to days (volatility surface arbitrage).

**Key risk**: the basis persists or widens before converging. Capital structure arbitrages can lose severely if both legs move against the position — a credit event can cause CDS to widen *and* equity to collapse simultaneously. The 1998 collapse of Long-Term Capital Management (LTCM) is the canonical example of basis risk overwhelming a portfolio of statistical arbitrages.

(sec:qi_factor)=
### Factor investing

**Economic hypothesis**: the cross-sectional variation in expected returns is explained by a small number of **risk factors** — systematic sources of risk for which the market demands a premium.

**Theoretical foundation**: the **Arbitrage Pricing Theory** (APT) of {cite:t}`ross1976arbitrage` shows that in a no-arbitrage economy, expected returns satisfy $\mathbb{E}[r_i] = r_f + \sum_k \beta_{ik}\lambda_k$, where $\beta_{ik}$ are the factor exposures and $\lambda_k$ are the factor risk premia. The CAPM is the special case with one factor (the market). {cite:t}`fama1993common` identified three empirical factors that explain most of the cross-section of equity returns: the market factor (MKT), the size factor (SMB — small-minus-big), and the value factor (HML — high-minus-low book-to-market). {cite:t}`carhart1997persistence` added a momentum factor (WML — winners-minus-losers). Subsequent research has proposed hundreds of additional factors, prompting concerns about p-hacking and what {cite:t}`lopezdeprado2022causal` calls the **factor zoo** — a proliferation of factors that do not represent genuinely distinct causal risk sources but are instead artefacts of data mining.

**Factor strategies**: a systematic factor investor constructs portfolios with deliberate tilts toward premia-bearing factors (value, momentum, low-volatility, quality, carry) and away from unrewarded idiosyncratic risk. **Smart beta** products implement passive factor tilts at low cost. **Alpha factor** strategies in long-short equity funds seek to isolate idiosyncratic alpha net of factor exposures.

**Timeframe**: monthly rebalancing is standard for fundamental factors; daily for momentum and technical factors.

**Key risk**: factor premia are time-varying and can be negative over extended periods — value was a chronic underperformer from 2010 to 2020. Factor **crowding** — when many funds hold the same factor tilt — can cause sharp reversal events such as the August 2007 quant crisis, when systematic de-levering across crowded factor portfolios caused correlated losses across dozens of hedge funds simultaneously.

(sec:qi_portfolio_construction)=
### Portfolio construction and optimisation

The four strategy classes above are **alpha generation** mechanisms: they produce a set of investment views or signals. Converting those signals into actual trades requires **portfolio construction**: deciding how much to invest in each instrument, how to balance expected return against risk, and how to account for transaction costs.

The foundational framework is **mean-variance optimisation** (MVO) due to {cite:t}`markowitz1952portfolio`:
$$\max_{\mathbf{w}}\; \mathbf{w}^T\boldsymbol{\mu} - \frac{\lambda}{2}\mathbf{w}^T\boldsymbol{\Sigma}\mathbf{w} \quad \text{s.t.} \; \mathbf{1}^T\mathbf{w} = 1$$
where $\boldsymbol{\mu}$ is the vector of expected returns, $\boldsymbol{\Sigma}$ is the return covariance matrix, and $\lambda$ is the risk-aversion coefficient. The solution traces the **efficient frontier** — the set of portfolios offering maximum expected return for each level of risk. In practice, MVO has well-known instability problems: estimated $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ are noisy, and the optimiser amplifies estimation errors into extreme weights. Alternative approaches include **risk parity** (equal risk contribution per asset) and **Black-Litterman** {cite:p}`black1992global` (which incorporates manager views as Bayesian updates to equilibrium priors). Chapter {ref}`optimal_investment_theory` develops these methods in full.

(sec:qi_lifecycle)=
## The strategy development lifecycle

A quantitative investment strategy passes through a well-defined lifecycle from ideation to production deployment. Skipping or shortcutting any stage is a major source of underperformance and strategy failure in practice.

### Alpha ideation

The starting point is a **hypothesis** about why a pattern exists in market data and should persist. Strong hypotheses have an economic rationale — a risk premium, a structural market friction, a behavioural bias — that explains why other participants are not already arbitraging it away. Hypotheses without such a story are vulnerable to the "garbage in, garbage out" critique: a pattern found in data without economic underpinning is likely a statistical artefact.

Sources of alpha hypotheses include:
- *Theoretical models*: OU processes for mean reversion, APT for factor premia, no-arbitrage pricing for spread strategies.
- *Academic research*: the factor-investing literature, the microstructure literature on order flow and price impact.
- *Domain expertise*: practitioners who understand the institutional frictions, regulatory constraints, and flow dynamics that create persistent mispricings.
- *Alternative data*: satellite imagery of cargo volumes, credit-card spending data, web-traffic signals, sentiment extracted from news and social media by NLP models {cite:p}`denev2020alternative`.

### Signal construction

An alpha hypothesis must be translated into a quantitative **signal** $s_t$ — a number that, at each time $t$, scores each instrument in the universe by its expected return over the strategy horizon. Signals are typically normalised (e.g., z-scored across the universe) and may combine multiple raw predictors. Machine-learning models (ridge regression, random forests, gradient boosting, LSTM networks) — introduced in {ref}`data_driven_methods` — are widely used to combine signals, especially when the raw features are high-dimensional or non-linearly related to returns {cite:p}`dePrado2018`. A key discipline is ensuring that no future information leaks into the signal computation — the **lookahead bias** trap described in {ref}`sec:qi_pitfalls`.

### Strategy rules and execution

The signal is converted into **position rules** — how much to buy or sell, under what conditions, and how to scale position sizes. Rules typically include entry conditions (signal crosses a threshold), exit conditions (signal weakens, stop-loss triggered, maximum holding period expires), position sizing (proportional to signal strength, volatility-adjusted), and inventory limits. Investment algorithms are typically lower frequency than execution algorithms, but transaction costs remain critical to profitability. A strategy that generates a gross Sharpe ratio of 1.5 before costs may be marginally profitable after accounting for bid-ask spreads, market impact, and financing costs. Chapter {ref}`execution_fundamentals` provides the cost framework; chapter {ref}`optimal_execution` derives the optimal execution schedule.

### Monitoring and risk management

In production, an investment algorithm requires continuous monitoring of signal quality, position limits, P&L attribution, and risk exposures. Key operational controls include kill switches (automatic liquidation if daily P&L loss exceeds a threshold), regime detection (identification of market conditions in which the strategy should reduce activity), and factor exposure monitoring (ensuring the portfolio is not inadvertently concentrated in known risk factors outside its mandate).

(sec:qi_backtest)=
## Backtesting

Backtesting is the simulation of a strategy on historical data to evaluate its performance before risking real capital. It is the primary tool for quantitative strategy evaluation, but also the primary source of spurious results — overfit strategies that perform well in simulation and fail in production.

### The backtesting loop

A proper backtest simulates the exact sequence of decisions the algorithm would have made if deployed historically:
1. **At each time step $t$**: construct the signal $s_t$ using only data available at $t$ (no future data).
2. **Generate orders**: apply position rules to $s_t$ to determine the target portfolio $\mathbf{w}_t$.
3. **Simulate execution**: apply a realistic transaction cost model to determine achieved fill prices.
4. **Update P&L and positions**: record mark-to-market P&L and carry positions forward.
5. **Apply risk controls**: check position limits, stop-losses, margin requirements.

The notebook `notebooks/quant_investment.ipynb` implements a complete backtesting loop for pairs-trading and momentum strategies.

### In-sample / out-of-sample split and walk-forward analysis

The standard discipline is to divide the historical period into an **in-sample (IS)** training period (used to calibrate model parameters) and a reserved **out-of-sample (OOS)** test period. The strategy is applied to OOS with parameters fixed at their IS values, without any re-optimisation. A single IS/OOS split is insufficient when multiple parameter combinations are tried. **Walk-forward analysis** repeats the split at multiple time points, re-estimating parameters on each rolling IS window and evaluating on the subsequent OOS period. The composite OOS performance across all periods is a much more honest assessment of strategy robustness than any IS result.

### Transaction costs in backtests

Best practices include: use bid-ask spread at each execution point rather than mid-prices; model market impact for larger strategies using the square-root law (chapter {ref}`execution_fundamentals`); account for financing costs for leveraged and short positions; and add a one-period latency delay between signal generation and execution to simulate realistic information propagation.

(sec:qi_metrics)=
## Performance metrics

The output of a backtest is a time series of returns $r_t$. The standard metrics for evaluating a strategy are:

### Sharpe ratio

The **Sharpe ratio** is the central metric in quantitative investment, measuring risk-adjusted return:
$$\text{SR} = \frac{\mathbb{E}[r] - r_f}{\mathrm{std}(r)}, \qquad \text{SR}_{\text{ann}} = \sqrt{252}\cdot\text{SR}_{\text{daily}}$$
The hypothesis test $\text{SR}>0$ uses the statistic $t = \sqrt{T}\cdot\text{SR}$ {cite:p}`chan2013algorithmic`. A Sharpe ratio above 1.0 is generally considered acceptable; above 2.0 is considered very good for a systematic strategy.

### Sortino ratio and downside risk

The **Sortino ratio** replaces the standard deviation with the **downside deviation** computed only over periods when $r_t < r_f$, penalising downside risk without penalising upside volatility:
$$\text{Sortino} = \frac{\mathbb{E}[r] - r_f}{\sigma_{\text{downside}}}$$
More informative than Sharpe for strategies with a positive return skew (e.g., trend followers, which tend to have fat positive tails).

### Maximum drawdown and Calmar ratio

The **maximum drawdown** (MDD) measures the largest peak-to-trough decline in cumulative P&L:
$$\text{MDD} = \max_{t \leq s}\bigl(V_t - V_s\bigr)$$
It is the primary metric used by risk managers to assess worst-case capital at risk. The **Calmar ratio** is the annualised return divided by MDD — combining return and tail risk in one number.

### Information ratio

When a strategy benchmarks against a reference portfolio, the **information ratio** (IR) measures excess return over the benchmark per unit of tracking error:
$$\text{IR} = \frac{\mathbb{E}[r - r_{\text{bench}}]}{\mathrm{std}(r - r_{\text{bench}})}$$

### Turnover and capacity

**Turnover** (fraction of the portfolio traded per day) and the **average holding period** jointly determine the transaction cost burden. A strategy requiring 100% daily turnover with a 10bps bid-ask spread consumes roughly 250bps per year in costs alone. The **capacity** of a strategy — the maximum capital deployable before market impact erodes the alpha — depends critically on the liquidity of the instruments traded and the strategy's typical trade sizes relative to market volumes.

(sec:qi_pitfalls)=
## Common pitfalls and failure modes

Quantitative investment has a well-documented set of failure modes, most arising from some form of **data snooping** — using future information (directly or through implicit overfitting) that would not be available in real trading.

### Lookahead bias

**Lookahead bias** occurs when a signal or decision at time $t$ uses information that was not available until $t + \Delta t$. Common sources: computing a daily statistic and trading on it at the same-day close; using revised fundamental data (as-reported rather than point-in-time); including in the universe securities that did not exist at the time of decision. Lookahead bias typically produces large, stable-looking backtests that fail immediately in live trading.

### Survivorship bias

**Survivorship bias** occurs when the historical universe includes only instruments that survived to the present, excluding bankruptcies, delistings, and mergers. For equity strategies, this produces an optimistic return because stocks that performed badly enough to be delisted are never included in the losses. The bias can be several percentage points of annual return, severely inflating backtested Sharpe ratios.

### Overfitting and p-hacking

**Overfitting** is the selection of parameter settings that perform well in the backtest due to chance. With $K$ independent strategy variants tested on the same data, the probability that at least one produces a Sharpe ratio above the 5% critical value by chance is $1 - (1-0.05)^K$: with $K=14$ this already exceeds 50%. {cite:t}`dePrado2018` provides a framework for **deflated Sharpe ratios** and minimum backtest length that adjust for the multiple testing problem. Defences against overfitting include walk-forward validation, strict separation of model development from evaluation data, prior-based model selection, and rigorous hypothesis testing with multiple-testing corrections.

### Transaction cost neglect

Underestimating transaction costs is systematic in backtesting: the researcher optimises the signal for gross return without adequately penalising turnover. A signal requiring daily rebalancing with a 10bps bid-ask spread consumes $10\,\mathrm{bps} \times 250 = 250\,\mathrm{bps}$ per year in gross turnover alone — wiping out a 2.5% alpha.

### Regime instability

Financial markets are non-stationary: relationships that held for one decade may not hold for the next. Factor premia exhibit time-variation (the value premium was essentially zero for a decade post-GFC). High-frequency momentum strategies became less profitable as latency arms races compressed the exploitable signal duration. Robust strategies are designed with awareness of their regime dependency, include explicit regime-detection logic, and are tested across a variety of market environments including periods of stress.

## Practical examples

### Pairs trading: CAC 40 vs EUROSTOXX 50

The introductory slide in the AlgoTradingVI lecture notes shows the normalised price series of the CAC 40 and EUROSTOXX 50 futures over a period in which they traded highly correlated. A pairs-trading strategy observes that the two index futures are cointegrated because their compositions overlap substantially: when a temporary deviation opens — one rises while the other does not — the strategy goes long the underperformer and short the overperformer, expecting convergence. The position is closed when the z-score of the spread reverts toward zero. The notebook `notebooks/quant_investment.ipynb` implements this strategy on synthetic cointegrated data, including the Johansen test, half-life estimation, and a full backtest with transaction costs. The Kalman filter extension tracks a time-varying hedge ratio, substantially improving performance {cite:p}`chan2013algorithmic`.

### Cross-asset momentum in rates

A cross-sectional momentum strategy in the interest-rate space ranks a universe of sovereign bond markets by their 12-month total return, goes long the top quartile, and shorts the bottom quartile. This exploits the empirical finding of {cite:t}`moskowitz2012time` that momentum is pervasive across asset classes. Unlike equity momentum, rate momentum is partly driven by central bank policy cycles: economies with tightening monetary policy tend to outperform those in easing cycles, creating momentum in short rates that propagates across the curve.

## Exercises

1. **Strategy classification.** Categorise each of the following as mean reversion, trend following, statistical arbitrage, or factor investing: (a) buying the 10-year Italian BTP when its spread over German Bunds widens beyond 300bp; (b) buying a basket of stocks with the lowest price-to-book ratios in the S&P 500; (c) buying a crude oil futures contract when its 50-day moving average crosses above its 200-day moving average; (d) going long a convertible bond and short the underlying equity when the bond trades at a discount to its theoretical value.

2. **Sharpe ratio significance test.** A strategy produces a daily Sharpe ratio of 0.08 over a backtest of 500 trading days. Is the Sharpe ratio statistically significantly positive at the 5% level? How many additional days of data would be needed to achieve significance if the Sharpe ratio remains at the same level?

3. **Walk-forward validation design.** You are designing a walk-forward backtest for a mean-reversion pairs trading strategy. The strategy requires a minimum of 120 trading days to estimate stable parameters. The total available history is 2500 trading days. Design a reasonable walk-forward scheme, specifying the IS window length, the OOS window length, and the number of IS/OOS splits. How much total OOS data do you obtain?

4. **Transaction cost analysis.** A signal generates a daily Sharpe ratio of 0.12 on gross returns (before costs), with average daily turnover of 40% of the portfolio. The average bid-ask spread is 5bps per trade. (a) Compute the daily transaction cost drag. (b) Compute the net daily Sharpe ratio. (c) If you could reduce turnover to 20% by applying a 3-day momentum filter to the signal, would it improve the net Sharpe ratio assuming the filter reduces gross signal strength to an equivalent daily Sharpe of 0.09?

5. **Overfitting and deflation.** A researcher tests 50 independent trading rules on 3 years of daily data and reports the best-performing rule, which achieves an annualised Sharpe ratio of 2.2. (a) At what effective single-test significance level has the researcher implicitly tested? (b) Argue qualitatively why this reported result should be treated with scepticism. (c) What minimum backtest length would be required to conclude that the expected Sharpe ratio of the best rule is positive, under a conservative adjustment for the 50-rule search?

6. **Regime detection.** A momentum strategy performs well during trending markets and loses money in range-bound markets. Propose two quantitative indicators that could serve as a regime filter to switch the strategy off during unfavourable conditions, and describe how you would validate the filter in a backtesting framework without introducing lookahead bias.
