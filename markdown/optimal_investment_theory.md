(optimal_investment_theory)=
# Optimal Investment Theory

## Introduction

Chapter {ref}`quant_investment_fundamentals` classified investment strategies by economic hypothesis and practical methodology. This chapter provides the mathematical foundations for each strategy class. The goal is to move from the qualitative insight — "prices tend to revert to their mean" or "recent winners outperform recent losers" — to a precise formulation: how to detect the property, how to calibrate its parameters, how to derive the optimal entry and exit rules, and how to construct the portfolio.

We develop four blocks of theory, following the taxonomy of the preceding chapter. Section {ref}`sec:oit_meanrev` treats mean-reversion strategies in depth: the Ornstein-Uhlenbeck (OU) model and its discrete AR(1) representation, hypothesis tests for mean reversion (Dickey-Fuller, Augmented Dickey-Fuller, Hurst exponent), the half-life as a natural strategy timescale, and the extension to multi-instrument portfolios via cointegration (the Engle-Granger and Johansen tests). We also derive the Kalman filter update equations for a pairs-trading strategy with time-varying hedge ratio. Section {ref}`sec:oit_momentum` treats trend-following strategies: the statistical characterisation of momentum, MACD-style signal filters, and the relation between the Hurst exponent and the autocorrelation structure. Section {ref}`sec:oit_statarb` covers statistical arbitrage, focusing on the PCA-based factor decomposition approach of {cite:t}`avellaneda2010statistical`. Section {ref}`sec:oit_factor` develops the Arbitrage Pricing Theory and the Fama-French factor models. Finally, section {ref}`sec:oit_portfolio` derives the key results in portfolio optimisation: the efficient frontier, the maximum Sharpe ratio portfolio, risk parity, and the Black-Litterman framework.

Mathematical prerequisites are the stochastic calculus of chapter {ref}`stochastic_calculus` (Itô's lemma, Brownian motion, SDEs), the stochastic optimal control tools of chapter {ref}`stochastic_optimal_control` (Bellman equations, HJB), and the Bayesian inference tools of chapter {ref}`intro_bayesian` (Gaussian updates, prior-posterior analysis).

(sec:oit_meanrev)=
## Mean reversion strategies

### The Ornstein-Uhlenbeck model

The fundamental continuous-time model of mean-reverting dynamics is the **Ornstein-Uhlenbeck (OU) process**:

$$\boxed{dx_t = \theta(\mu - x_t)\,dt + \sigma\,dW_t}$$

where $\theta > 0$ is the **speed of mean reversion**, $\mu \in \mathbb{R}$ is the **long-run mean**, and $\sigma > 0$ is the **volatility**. Unlike geometric Brownian motion (the default model for non-mean-reverting prices), the OU process has a negative feedback term: when $x_t > \mu$, the drift is negative, pulling the process downward; when $x_t < \mu$, the drift is positive. The strength of this restoring force is proportional to $\theta$.

The OU SDE can be solved exactly (see chapter {ref}`stochastic_calculus`). Starting from $x_0$:

$$x_t = \mu + (x_0 - \mu)e^{-\theta t} + \sigma\int_0^t e^{-\theta(t-s)}\,dW_s$$

Taking expectations and variance:

$$\mathbb{E}[x_t] = \mu + (x_0 - \mu)e^{-\theta t}, \qquad \mathrm{Var}(x_t) = \frac{\sigma^2}{2\theta}\bigl(1 - e^{-2\theta t}\bigr)$$

The mean decays exponentially to $\mu$ with time constant $1/\theta$. The stationary distribution is $x_\infty \sim \mathcal{N}(\mu,\, \sigma^2/(2\theta))$.

**Half-life**: the time for the expected deviation from $\mu$ to halve:
$$\mathbb{E}[x_{t_{1/2}}] = \mu + \frac{x_0 - \mu}{2} \implies e^{-\theta t_{1/2}} = \frac{1}{2} \implies \boxed{t_{1/2} = \frac{\ln 2}{\theta}}$$
The half-life is a natural timescale for strategy design: holding periods should be of order $t_{1/2}$, and lookback windows for estimating the mean and standard deviation should span several half-lives to capture the stationary distribution.

**Autocovariance**: for the stationary process,
$$\mathrm{cov}(x_s, x_t) = \frac{\sigma^2}{2\theta}e^{-\theta|t-s|}$$
decaying exponentially with lag $|t-s|$. The autocorrelation function (ACF) is $\rho(\tau) = e^{-\theta\tau}$, which is always positive but decreasing — a distinguishing feature of OU versus a trend-following process (which would have $\rho > 0$ and potentially increasing autocorrelations at short lags).

### Discrete-time AR(1) representation

Discretising the OU SDE with time step $\Delta t$:
$$x_{k+1} = c + a\, x_k + b\,\epsilon_k, \qquad \epsilon_k \overset{\text{i.i.d.}}{\sim} \mathcal{N}(0, 1)$$
where the parameters map from the continuous OU as:
$$c = \theta\mu\Delta t, \qquad a = 1 - \theta\Delta t, \qquad b = \sigma\sqrt{\Delta t}$$
This is a first-order autoregressive model (AR(1)) with coefficient $a \in (0,1)$. Mean reversion requires $|a| < 1$; a random walk corresponds to $a = 1$ (no drift). Equivalently, the differences $\Delta x_k = x_{k+1} - x_k$ follow:
$$\Delta x_k = \underbrace{\theta\mu\Delta t}_{\alpha} + \underbrace{(-\theta\Delta t)}_{\beta}\, x_k + b\,\epsilon_k$$

The key insight: the difference $\Delta x_k$ is a *linear function of the level* $x_k$, with a *negative coefficient* $\beta = -\theta\Delta t$. Testing whether $\beta = 0$ (random walk) versus $\beta < 0$ (mean reversion) is the basis of the Dickey-Fuller test.

### Testing for mean reversion

#### The Dickey-Fuller and Augmented Dickey-Fuller tests

The **Dickey-Fuller (DF) test** {cite:p}`dickey1979distribution` regresses the first differences on the level:
$$\Delta x_k = \alpha + \beta\, x_k + \varepsilon_k$$
and tests the null hypothesis $H_0: \beta = 0$ (unit root / random walk) against the alternative $H_1: \beta < 0$ (mean reversion) using the t-statistic:
$$DF = \frac{\hat{\beta}}{\mathrm{SE}(\hat{\beta})}$$

Under $H_0$, the distribution of $DF$ is non-standard (not a normal or standard $t$ distribution), reflecting the non-stationarity of the random walk. Critical values at 5% significance are approximately $-1.95$ (no trend), $-2.86$ (with constant), and $-3.41$ (with constant and trend) for large samples. If $DF$ is more negative than the critical value, $H_0$ is rejected: the series is mean-reverting with statistical significance.

The **Augmented Dickey-Fuller (ADF) test** generalises the regression to include lagged differences to control for serial correlation in the residuals:
$$\Delta x_k = \alpha + \beta\, x_k + \gamma t + \sum_{j=1}^p \delta_j \Delta x_{k-j} + \varepsilon_k$$
The test statistic and critical values are the same. The lag order $p$ is chosen by information criteria (AIC, BIC). The ADF is the standard version used in practice, as the simple DF test can be over-sized in the presence of autocorrelation.

#### The Hurst exponent

The **Hurst exponent** $H$ {cite:p}`hurst1951long` quantifies the long-term memory of a time series. Define $z_t = \log(x_t)$ for a price series. The structure function scales as:
$$\bigl\langle |z(t+\tau) - z(t)|^2 \bigr\rangle \sim \tau^{2H}$$
The exponent $H$ is estimated by log-log regression of the variance of log-increments at different lags $\tau$ against $2\log(\tau)$. The three regimes are:
- $H = 0.5$: geometric random walk — no memory, increments are uncorrelated.
- $H < 0.5$: mean-reverting behaviour — the series diffuses *slower* than a random walk; positive increments are followed by negative ones on average.
- $H > 0.5$: trending behaviour — the series diffuses *faster* than a random walk; positive increments are followed by positive ones on average.

The Hurst exponent is complementary to the ADF test: the ADF is a formal hypothesis test for a unit root; the Hurst exponent is a descriptive statistic for the degree of memory. A series with $H = 0.3$ and a significant ADF test is a strong mean-reversion candidate; $H = 0.7$ is a strong trend-following candidate.

**Estimation**: the standard estimator is the **rescaled range** (R/S) method. Partition the series into $n$ blocks of length $m$. For each block, compute the range $R$ (max cumulative deviation from the block mean) and the standard deviation $S$. The statistic $R/S$ scales as $m^H$; regressing $\log(R/S)$ on $\log(m)$ yields $\hat{H}$.

### Z-score trading strategy

Given that a price series is mean-reverting with estimated parameters $\hat\mu$ and $\hat\sigma$ (rolling, computed over a half-life window), the **z-score** is:
$$z_t = \frac{x_t - \hat\mu}{\hat\sigma}$$

The canonical entry-exit rule:
- **Short entry**: $z_t > z_{\text{entry}}$ (e.g., $+1.96$) — price is high relative to mean, expect reversion down.
- **Long entry**: $z_t < -z_{\text{entry}}$ — price is low, expect reversion up.
- **Exit**: $|z_t| < z_{\text{exit}}$ (e.g., $0.5$) — price has returned sufficiently close to mean.
- **Stop loss**: $|z_t| > z_{\text{stop}}$ (e.g., $3.0$) — the deviation has grown so large that the mean-reversion thesis is questioned.

The strategy's expected holding period is related to the OU half-life: a half-life of 5 days implies typical holding periods of 5–15 days. Calibrating the thresholds $z_{\text{entry}}, z_{\text{exit}}, z_{\text{stop}}$ against the half-life and the distribution of the stationary OU process is a standard backtesting exercise.

### Cointegration and pairs trading

Mean-reversion strategies are most powerful when applied to a *portfolio* of instruments whose combination is mean-reverting, even if each individual series is non-stationary. This is the concept of **cointegration** {cite:p}`engle1987cointegration`.

**Definition**: a set of $I(1)$ time series $\{x^1_t, \ldots, x^d_t\}$ (i.e., each is a random walk individually) is **cointegrated** if there exists a vector $\boldsymbol{\beta} \in \mathbb{R}^d$ such that the linear combination $\boldsymbol{\beta}^T \mathbf{x}_t$ is $I(0)$ (stationary / mean-reverting). The vector $\boldsymbol{\beta}$ is called the **cointegrating vector**, and the stationary portfolio $\boldsymbol{\beta}^T\mathbf{x}_t$ is the **spread**.

**Economic intuition**: two instruments that share a common long-run trend — because they have fundamentally linked values (e.g., futures contract and its underlying basket, two large-cap equity indices with overlapping constituents) — will drift together in the long run even if they deviate temporarily. Cointegration formalises this co-movement without requiring the individual series to be stationary.

#### The Engle-Granger two-step procedure

For two series $(x_t, y_t)$:
1. **Regression**: regress $y_t$ on $x_t$ (and possibly a constant): $y_t = \hat\alpha + \hat\beta x_t + \hat\varepsilon_t$. The OLS estimate $\hat\beta$ is the hedge ratio of the cointegrating portfolio.
2. **ADF on residuals**: apply the ADF test to $\hat\varepsilon_t = y_t - \hat\alpha - \hat\beta x_t$. If the residuals are stationary (ADF rejects the unit root), the series are cointegrated.

Note: the direction of the regression matters — regressing $y$ on $x$ and $x$ on $y$ yield different hedge ratios. A symmetric alternative is the Johansen test.

#### The Johansen test

The **Johansen test** {cite:p}`johansen1991estimation` handles the multi-instrument case ($d \geq 2$) simultaneously and produces the cointegrating vectors as part of the test procedure. It fits a **Vector Autoregressive** (VAR) model to $\mathbf{x}_t = (x^1_t, \ldots, x^d_t)^T$:
$$\Delta\mathbf{x}_t = \boldsymbol{\mu} + A\mathbf{x}_{t-1} + \sum_{j=1}^p \Gamma_j\Delta\mathbf{x}_{t-j} + \mathbf{w}_t$$
and tests the rank $r$ of the matrix $A$. The rank equals the number of cointegrating relationships:
- $r = 0$: no cointegration (all series are independent random walks).
- $0 < r < d$: $r$ cointegrating vectors exist.
- $r = d$: all series are stationary.

The test uses two statistics: the **trace statistic** and the **maximum eigenvalue statistic**, both compared against critical values derived from Brownian motion theory. If rank $r > 0$ is established, the $r$ eigenvectors of $A$ corresponding to the $r$ largest eigenvalues define the $r$ cointegrating portfolios; the one with the largest eigenvalue is the *best* mean-reverting linear combination.

**Advantages over Engle-Granger**: the Johansen test works for $d \geq 2$ instruments, simultaneously estimates the hedge ratios and performs the hypothesis test (eliminating the two-stage bias), and provides a likelihood-based framework with better finite-sample properties.

### Kalman filter for time-varying hedge ratios

In practice, the cointegrating vector $\boldsymbol{\beta}$ is not fixed but evolves over time as market conditions change. Fixing $\boldsymbol{\beta}$ at a historical estimate (Engle-Granger or Johansen) causes the strategy to use a stale hedge ratio, increasing basis risk. The **Kalman filter** {cite:p}`kalman1960` provides an optimal solution to tracking time-varying hedge ratios.

For a pairs trading strategy with instruments $(x_t, y_t)$, model the relationship as:
$$y_t = \beta_t\, x_t + \varepsilon_t, \qquad \varepsilon_t \sim \mathcal{N}(0, \sigma_\varepsilon^2) \quad \text{(observation equation)}$$
$$\beta_t = \beta_{t-1} + \omega_t, \qquad \omega_t \sim \mathcal{N}(0, \sigma_\omega^2) \quad \text{(state transition equation)}$$

The hedge ratio $\beta_t$ is the latent state, modelled as a random walk. The Kalman filter optimal one-step update (see chapter {ref}`stochastic_optimal_control`, LQSC section) gives:

$$K_t = \frac{x_t^2\sigma_\omega^2 + P_{t-1}}{x_t^2(\sigma_\omega^2 + P_{t-1}) + \sigma_\varepsilon^2} \cdot x_t\sigma_\omega^2$$

$$\boxed{\beta_t = \beta_{t-1} + \frac{x_t\,\sigma_\omega^2}{x_t^2\sigma_\omega^2 + x_t^2 P_{t-1} + \sigma_\varepsilon^2}\bigl(y_t - \beta_{t-1}x_t\bigr)}$$

where $P_t$ is the posterior variance of $\beta_t$ given observations up to $t$. The ratio $\sigma_\omega^2/\sigma_\varepsilon^2$ controls the speed of adaptation: high $\sigma_\omega^2$ allows rapid updating (but introduces estimation noise); low $\sigma_\omega^2$ produces a slowly moving hedge ratio. These noise variances are estimated from historical data via maximum likelihood.

The spread used for trading is the residual $e_t = y_t - \hat\beta_t x_t$, which is z-scored and traded with the entry-exit rules of the previous section. Empirical studies consistently find that Kalman-filter pairs trading outperforms fixed-hedge-ratio strategies, particularly for pairs whose relationship drifts over months {cite:p}`chan2013algorithmic`.

The more general model with both intercept and slope time-varying is:
$$y_t = \begin{pmatrix} 1 & x_t \end{pmatrix}\begin{pmatrix}\alpha_t \\ \beta_t\end{pmatrix} + \varepsilon_t, \qquad \begin{pmatrix}\alpha_t \\ \beta_t\end{pmatrix} = \begin{pmatrix}\alpha_{t-1} \\ \beta_{t-1}\end{pmatrix} + \boldsymbol{\omega}_t$$
with $\boldsymbol{\omega}_t \sim \mathcal{N}(\mathbf{0}, Q)$. The Kalman filter generalises immediately to this two-dimensional state vector.

(sec:oit_momentum)=
## Trend following and momentum

### Time-series momentum

The empirical finding of {cite:t}`moskowitz2012time` is that the sign of the past 12-month return of a futures contract predicts the sign of the return over the next month. Define the time-series momentum (TSMOM) signal for instrument $i$ over lookback window $[t-L, t]$:
$$s_t^i = \mathrm{sign}\!\left(\sum_{\tau=1}^L r_{t-\tau}^i\right)$$
The strategy goes long (short) instrument $i$ if the signal is $+1$ ($-1$). The position is scaled by $1/\sigma_t^i$ (volatility-normalised) to equalise risk across instruments. Moskowitz, Ooi, and Pedersen show that an equally-weighted TSMOM strategy across 58 futures markets generates a Sharpe ratio of approximately 1.28 over 1985–2012, after transaction costs.

**Theoretical support**: TSMOM profits are consistent with the **slow adjustment hypothesis** — news is impounded into prices gradually rather than instantaneously, creating serial correlation. It is also related to the **behavioural underreaction** literature: investors initially underreact to news, with subsequent adjustment creating trends. The autocorrelation structure for a trending series is:
$$\mathrm{cov}(r_t, r_{t-1}) > 0$$
which corresponds to a Hurst exponent $H > 0.5$. The magnitude of TSMOM profits is proportional to the magnitude of the autocorrelation at the relevant lag.

### Cross-sectional momentum

Cross-sectional (or relative) momentum {cite:p}`jegadeesh1993returns` ranks $N$ instruments by their past $L$-period returns and forms a long-short portfolio: long the top decile, short the bottom decile, holding for $H$ periods. The canonical parameters (from the original Jegadeesh-Titman paper) are $L = 12$ months formation, $H = 1$ month holding, skipping the most recent month to avoid microstructure effects.

For a universe of $N$ stocks with returns $r^i_{t-L:t}$, the cross-sectional momentum score is the rank-transformed z-score:
$$s_t^i = \frac{\mathrm{rank}(r^i_{t-L:t}) - (N+1)/2}{\mathrm{std}(\mathrm{rank}(\cdot))}$$
The portfolio weights are proportional to $s_t^i$ (a dollar-neutral long-short portfolio). The key economic driver is not the same as TSMOM: cross-sectional momentum profits arise from relative underperformance — the bottom decile has negative alpha, not just lower-than-average returns.

### Detection: MACD and moving-average crossovers

In practice, trend-following strategies use **moving average convergence-divergence** (MACD) signals and moving-average crossovers rather than raw past returns. The exponential moving average (EMA) with decay rate $\alpha$ is:
$$\text{EMA}(t; \alpha) = \alpha\, r_t + (1-\alpha)\,\text{EMA}(t-1; \alpha)$$
The MACD signal is the difference between a fast and slow EMA:
$$\text{MACD}_t = \text{EMA}(t; \alpha_{\text{fast}}) - \text{EMA}(t; \alpha_{\text{slow}})$$
A positive MACD indicates recent returns exceed their long-term average — a bullish momentum signal. Moving-average crossover strategies trigger a long (short) entry when the fast MA crosses above (below) the slow MA. These signals are approximately proportional to the first difference of the MACD and are consistent with the TSMOM signal at the appropriate lag.

**Connection to autocorrelation**: it can be shown that the expected profit of a MA-crossover strategy is approximately proportional to the autocorrelation of returns at the lags spanned by the fast and slow MA windows. This provides a direct connection between the empirical autocorrelation structure (Hurst exponent) and the expected alpha of trend-following strategies.

(sec:oit_statarb)=
## Statistical arbitrage

### The no-arbitrage foundation

The law of one price states that two assets with identical payoffs must have the same price in an efficient market; otherwise a risk-free arbitrage exists. The no-arbitrage condition is the starting point for derivatives pricing (Black-Scholes, term structure models) and for the theoretical fair value of futures, forwards, and replication strategies.

In practice, true arbitrages — riskless profit opportunities — are extremely rare. The presence of transaction costs, liquidity differences, and execution risk means that even apparently model-free mispricings may not be exploitable profitably. The conversion of a true arbitrage into a **statistical arbitrage** occurs when:
1. The fair-value relationship involves *model assumptions* (e.g., a volatility surface arbitrage depends on the assumed dynamics of implied volatility).
2. There is a *basis* — a persistent, non-zero spread between the instrument and its theoretical value — due to liquidity premiums, contractual differences, or funding costs.
3. The convergence of the mispricing is not guaranteed within any fixed horizon.

A statistical arbitrage is characterised by positive expected return and small (but non-zero) variance: it profits on average across many repetitions but can lose on any individual trade.

### PCA-based statistical arbitrage

A powerful framework for equity StatArbs is the **factor decomposition** approach of {cite:t}`avellaneda2010statistical`. Each stock's log-return is decomposed into a systematic (factor) component and an idiosyncratic residual:
$$r_t^i = \sum_{k=1}^K \beta_{ik}F_t^k + \epsilon_t^i$$
where $F_t^k$ are the returns of the first $K$ principal components of the return covariance matrix, $\beta_{ik}$ are the factor loadings, and $\epsilon_t^i$ is the idiosyncratic residual. Principal component analysis (PCA) orthogonalises the factors.

**Statistical arbitrage strategy**: trade the idiosyncratic residuals $\epsilon_t^i$, which by construction are uncorrelated with the systematic market moves. If $\epsilon_t^i$ is mean-reverting (tested via ADF or Hurst), the strategy goes long stock $i$ when its cumulative residual $s_t^i = \sum_{\tau=1}^t \epsilon_\tau^i$ deviates negatively from its mean, and short when it deviates positively.

The intuition: the PCA factors capture the co-movements of all stocks (sector, size, beta effects); what remains is the idiosyncratic component, which reflects the stock-specific dynamics not explained by the market. If a stock has underperformed its factor model — i.e., its idiosyncratic return is negative — the strategy bets on a recovery.

The number of factors $K$ is chosen to balance explanatory power and dimensionality: too few factors and the residuals contain systematic risk; too many and the idiosyncratic component is diluted. In practice, $K = 15$–50 factors captures 50–70% of the variance of a large-cap equity universe.

### Risk-neutral model arbitrages

**Volatility surface arbitrage**: in options markets, the Black-Scholes implied volatility surface $\sigma_\mathrm{imp}(K, T)$ as a function of strike $K$ and maturity $T$ encodes the market's risk-neutral distribution of the underlying. Static no-arbitrage conditions constrain the surface: (i) call prices must be decreasing in $K$ (put-call parity), (ii) call prices must be decreasing in $K$ at rate bounded by the discount factor (butterfly spread must be non-negative), (iii) calendar spread must be non-negative. A violation of any of these conditions is a true arbitrage. Near-violations (surfaces near the boundary of the no-arbitrage region) are statistical arbitrages: the surface is likely to correct, but convergence is not instantaneous.

**Yield curve arbitrage**: the term structure of interest rates must satisfy no-arbitrage conditions relating spot rates, forward rates, and bond prices. Butterfly strategies — long the 5-year, short the 2-year and 10-year with duration-matched weights — are zero-cost portfolios that profit from convexity and curvature changes while hedging parallel and slope movements. These are classic StatArbs in rates markets.

(sec:oit_factor)=
## Factor models and factor investing

### The Arbitrage Pricing Theory

The **Arbitrage Pricing Theory** of {cite:t}`ross1976arbitrage` derives a linear factor model for expected returns from a no-arbitrage argument. Consider $N$ assets with returns $\mathbf{r}_t = (r_t^1, \ldots, r_t^N)^T$ generated by $K \ll N$ common factors $\mathbf{f}_t = (f_t^1, \ldots, f_t^K)^T$:

$$r_t^i = \alpha_i + \sum_{k=1}^K \beta_{ik}f_t^k + \epsilon_t^i$$

where $\mathbb{E}[\epsilon_t^i] = 0$, $\mathbb{E}[\epsilon_t^i f_t^k] = 0$ (idiosyncratic risk is uncorrelated with factors), and $\mathbb{E}[\epsilon_t^i\epsilon_t^j] \approx 0$ for $i \neq j$ (idiosyncratic risks are nearly uncorrelated with each other). Under the assumption that no asymptotic arbitrage exists — i.e., that no portfolio of idiosyncratic risks can generate riskless returns — it follows that:

$$\mathbb{E}[r^i] - r_f = \sum_{k=1}^K \beta_{ik}\lambda_k$$

where $\lambda_k = \mathbb{E}[f^k] - r_f$ is the **risk premium** of factor $k$. The expected excess return of asset $i$ is therefore a linear combination of its factor exposures, weighted by the factor risk premia.

**CAPM as a special case**: the Capital Asset Pricing Model is the APT with a single factor — the market portfolio. The CAPM risk premium is $\lambda = \mathbb{E}[r_M - r_f]$ (the equity risk premium), and $\beta_{i1} = \mathrm{cov}(r^i, r^M)/\mathrm{Var}(r^M)$ is the standard market beta.

### The Fama-French-Carhart four-factor model

{cite:t}`fama1993common` showed empirically that the CAPM fails to explain the cross-section of equity returns: small-cap stocks earn higher returns than predicted by CAPM, and high book-to-market (value) stocks earn higher returns than growth stocks. Their three-factor model adds two factors to the market factor:

$$r_t^i - r_f = \alpha_i + \beta_i^{\text{MKT}}(r_t^M - r_f) + \beta_i^{\text{SMB}}\,\text{SMB}_t + \beta_i^{\text{HML}}\,\text{HML}_t + \epsilon_t^i$$

where:
- **MKT** $= r_t^M - r_f$: market excess return.
- **SMB** (Small Minus Big): return of small-cap stocks minus large-cap stocks, capturing the *size premium*.
- **HML** (High Minus Low): return of high book-to-market stocks minus low book-to-market stocks, capturing the *value premium*.

{cite:t}`carhart1997persistence` extended the model with a momentum factor:

- **WML** (Winners Minus Losers): return of the top decile by 12-month return minus the bottom decile, capturing the *momentum premium*.

The four-factor Fama-French-Carhart model explains roughly 90–95% of the time-series variance of diversified equity portfolio returns. The $\alpha_i$ in the regression — the intercept, representing return unexplained by the four factors — is the asset's **true alpha** relative to these systematic risk premia.

### Factor exposure estimation and the factor zoo

For a given set of factor portfolios $(\mathbf{F}_t)$, the factor loadings $\boldsymbol{\beta}_i$ of asset $i$ are estimated by ordinary least squares on the time-series regression above. The standard errors account for heteroskedasticity and autocorrelation (HAC estimators).

**The factor zoo problem**: {cite:t}`lopezdeprado2022causal` surveys hundreds of factors proposed in the academic literature and argues that most are spurious. The hierarchy of evidence in financial research (from the lecture notes, AlgoTradingVII slide 15) ranks factor evidence by rigour:

| Type | Rigour | Example |
|------|--------|---------|
| Randomised controlled trials | Very high | Algo-wheel experiments |
| Natural experiments | High | Market-maker reaction to random spikes |
| Simulated interventions | Medium | Causal graph analysis of HML |
| Econometric (observational) studies | Low | Backtested factor strategies |
| Case studies | Very low | Broker analysis |
| Expert opinion | Anecdotal | Investment guru predictions |

Most factor research relies on econometric observational studies, which are vulnerable to multiple testing and selection bias. A causal validation approach — asking whether a factor represents a genuine, structurally interpretable source of risk rather than a data-mining artefact — substantially reduces the factor zoo. Chapter {ref}`intro_causal` provides the causal inference tools (do-calculus, back-door criterion) needed for this validation.

**Factor selection in practice**: the standard approach is to:
1. Require a theoretical rationale for the factor (risk-based or behavioural).
2. Require evidence across multiple markets, time periods, and asset classes.
3. Apply multiple-testing corrections (deflated Sharpe ratio, false discovery rate control).
4. Require the factor premium to survive transaction costs and to be estimable with low data requirements.

(sec:oit_portfolio)=
## Optimal portfolio construction

### Mean-variance optimisation

The **mean-variance optimisation** (MVO) of {cite:t}`markowitz1952portfolio` solves:
$$\max_{\mathbf{w}}\; \mathbf{w}^T\boldsymbol{\mu} - \frac{\lambda}{2}\mathbf{w}^T\boldsymbol{\Sigma}\mathbf{w}$$
subject to $\mathbf{1}^T\mathbf{w} = 1$ (and optionally $\mathbf{w} \geq \mathbf{0}$ for long-only). Here $\boldsymbol{\mu} \in \mathbb{R}^N$ is the vector of expected excess returns and $\boldsymbol{\Sigma} \in \mathbb{R}^{N\times N}$ is the return covariance matrix. The parameter $\lambda > 0$ is the risk-aversion coefficient.

The first-order conditions give the **analytical solution**:
$$\boxed{\mathbf{w}^* = \frac{1}{\lambda}\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu} - c\,\mathbf{1})}$$
where $c$ is the Lagrange multiplier for the budget constraint, determined by $\mathbf{1}^T\mathbf{w}^* = 1$. For an unconstrained (long-short) portfolio with zero-cost constraint ($\mathbf{1}^T\mathbf{w} = 0$), the solution simplifies to $\mathbf{w}^* \propto \boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}$.

**The efficient frontier**: as $\lambda$ ranges from $0$ to $\infty$, the solution $\mathbf{w}^*(\lambda)$ traces a curve in the (risk, return) space — the **efficient frontier**. Each point on the frontier is the portfolio with minimum risk for a given expected return (equivalently, maximum expected return for given risk). The relationship between risk $\sigma_p = \sqrt{\mathbf{w}^T\boldsymbol{\Sigma}\mathbf{w}}$ and return $\mu_p = \mathbf{w}^T\boldsymbol{\mu}$ traces a hyperbola in the $(\sigma_p, \mu_p)$ plane.

**Maximum Sharpe ratio portfolio**: the tangency portfolio maximises:
$$\text{SR}(\mathbf{w}) = \frac{\mathbf{w}^T\boldsymbol{\mu}}{\sqrt{\mathbf{w}^T\boldsymbol{\Sigma}\mathbf{w}}}$$
Its analytical solution (for a long-short portfolio with budget constraint $\mathbf{1}^T\mathbf{w}=1$) is:
$$\mathbf{w}^{\text{tan}} = \frac{\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}}{\mathbf{1}^T\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}}$$

**Instability and estimation error**: MVO is notoriously sensitive to errors in $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$. The covariance matrix $\boldsymbol{\Sigma}$ can be estimated with reasonable precision from historical data, but expected returns $\boldsymbol{\mu}$ are very noisy: the estimation error in $\boldsymbol{\mu}$ over typical historical windows is comparable in magnitude to $\boldsymbol{\mu}$ itself. The optimiser then amplifies small estimation errors into extreme portfolio weights. Common remedies:
- **Shrinkage estimators** for $\boldsymbol{\Sigma}$ (Ledoit-Wolf, factor models).
- **Robust optimisation** (worst-case constraints on the uncertainty set of $\boldsymbol{\mu}$).
- **Regularisation** (penalty on $\|\mathbf{w}\|_2^2$ or $\|\mathbf{w}\|_1$).
- **Black-Litterman** (Bayesian shrinkage of $\boldsymbol{\mu}$ toward a prior).

### Risk parity

**Risk parity** abandons expected return forecasts and focuses entirely on equalising the risk contribution of each asset to the portfolio. The **risk contribution** of asset $i$ is:
$$\text{RC}_i = w_i\cdot\frac{(\boldsymbol{\Sigma}\mathbf{w})_i}{\sqrt{\mathbf{w}^T\boldsymbol{\Sigma}\mathbf{w}}} = w_i\cdot\frac{\partial\sigma_p}{\partial w_i}$$
It measures how much asset $i$ contributes to total portfolio volatility $\sigma_p$. A risk-parity portfolio requires $\text{RC}_i = 1/N$ for all $i$ — each asset contributes equally to portfolio risk. For a diagonal $\boldsymbol{\Sigma}$ (uncorrelated assets), this reduces to $w_i \propto 1/\sigma_i$: inverse-volatility weighting.

For general $\boldsymbol{\Sigma}$, the risk-parity weights are found by solving the system:
$$w_i(\boldsymbol{\Sigma}\mathbf{w})_i = \frac{\mathbf{w}^T\boldsymbol{\Sigma}\mathbf{w}}{N}, \quad \forall i$$
This is a non-linear system without a closed-form solution in general, solved by iterative methods (Newton-Raphson, sequential quadratic programming).

**Advantages over MVO**: risk parity does not require expected return estimates (only covariance), which makes it much more stable. It naturally diversifies risk across assets, avoiding the concentration that plagues MVO. Its main limitation is that it does not account for return expectations — a lower-risk asset may have a higher (or lower) expected return per unit of risk than a higher-risk asset, and risk parity treats them identically.

### The Black-Litterman framework

The **Black-Litterman model** {cite:p}`black1992global` solves the estimation error problem of MVO by combining an equilibrium prior on expected returns with the investor's subjective views, using a Bayesian update.

**Step 1 — Equilibrium prior**: from the CAPM, the market-clearing expected excess return vector is:
$$\boldsymbol{\Pi} = \lambda_{\text{mkt}}\boldsymbol{\Sigma}\mathbf{w}_{\text{mkt}}$$
where $\mathbf{w}_{\text{mkt}}$ is the market-capitalisation weight vector and $\lambda_{\text{mkt}}$ is calibrated so that $\boldsymbol{\Pi}$ matches the empirical equity risk premium. This gives a reasonable prior on expected returns that is consistent with the market equilibrium and does not require forecasting.

**Step 2 — Views**: the investor expresses $K$ views on linear combinations of returns: $P\boldsymbol{\mu} = \mathbf{q} + \boldsymbol{\eta}$, where $P \in \mathbb{R}^{K\times N}$ selects the relevant assets, $\mathbf{q}$ is the expected return vector for each view, and $\boldsymbol{\eta} \sim \mathcal{N}(\mathbf{0}, \Omega)$ reflects the uncertainty in the views.

**Step 3 — Bayesian update**: combining the prior $\boldsymbol{\mu} \sim \mathcal{N}(\boldsymbol{\Pi}, \tau\boldsymbol{\Sigma})$ (with small $\tau$ reflecting confidence in the prior) and the view likelihood, the posterior expected return (see chapter {ref}`intro_bayesian` for the Gaussian update formula) is:
$$\boxed{\hat{\boldsymbol{\mu}}_{\text{BL}} = \bigl[(\tau\boldsymbol{\Sigma})^{-1} + P^T\Omega^{-1}P\bigr]^{-1}\bigl[(\tau\boldsymbol{\Sigma})^{-1}\boldsymbol{\Pi} + P^T\Omega^{-1}\mathbf{q}\bigr]}$$

The posterior $\hat{\boldsymbol{\mu}}_{\text{BL}}$ is a precision-weighted average of the equilibrium prior and the investor's views. It is then used as the expected return input to MVO, producing an optimal portfolio that tilts away from the market portfolio in proportion to the investor's views and confidence.

**Key properties**: if the investor has no views ($K=0$), the BL optimal portfolio equals the market portfolio. As views become more confident ($\Omega \to 0$), the portfolio tilts aggressively toward the views. The blending ensures that the portfolio is always a well-behaved tilt from a sensible baseline, avoiding the extreme weights that pure MVO produces.

**Connection to Bayesian inference**: the BL update is a special case of the Gaussian conjugate update derived in chapter {ref}`intro_bayesian`. The equilibrium CAPM return is the prior; the investor's views are the likelihood; the posterior is the BL expected return. This connection is particularly clean because both the prior and the views are modelled as Gaussian, making the update exact and closed-form.

## Exercises

1. **OU calibration.** A price spread $x_t$ has sample mean $\hat\mu = 1.2$ and is found to follow an AR(1) model with coefficient $\hat{a} = 0.92$, estimated on daily data ($\Delta t = 1$ day). (a) Estimate the OU parameters $\theta$, $\mu$, and $\sigma$ (assuming $\hat{b} = 0.08$). (b) Compute the half-life in trading days. (c) Compute the stationary standard deviation $\sigma_\infty = \sigma/\sqrt{2\theta}$. (d) How would you set the z-score entry threshold to achieve an expected holding period of roughly one half-life?

2. **Dickey-Fuller test.** You have 500 daily observations of a price spread. The OLS regression of $\Delta x_k$ on $x_k$ (with constant) gives $\hat\beta = -0.045$ with $\mathrm{SE}(\hat\beta) = 0.018$. (a) Compute the DF test statistic. (b) Is the null hypothesis of a unit root rejected at the 5% level? (c) If the regression also includes a time trend and gives $\hat\beta = -0.035$ with $\mathrm{SE}(\hat\beta) = 0.014$, what is the conclusion?

3. **Hurst exponent.** Log-log regression of the structure function $\langle|z(t+\tau)-z(t)|^2\rangle$ on $\tau$ gives a slope of $2H$. For three price series: (A) slope 1.0, (B) slope 0.7, (C) slope 1.4. Identify which series exhibits mean reversion, random walk behaviour, and trending behaviour. For which would a pairs-trading strategy be appropriate? For which a trend-following strategy?

4. **Cointegration and Johansen test.** Describe the key difference between the Engle-Granger two-step procedure and the Johansen test for detecting cointegration among a set of $d=3$ price series. Under what conditions would the two methods disagree about the number of cointegrating relationships? Which would you prefer in practice, and why?

5. **APT and factor premia.** An asset has factor loadings $\beta_1 = 1.1$ (market), $\beta_2 = 0.4$ (SMB), $\beta_3 = -0.2$ (HML). The factor risk premia are $\lambda_1 = 6\%$, $\lambda_2 = 2\%$, $\lambda_3 = 3\%$ (annualised). (a) Compute the expected excess return from the APT. (b) If the asset's actual average excess return is 8%, what is its four-factor alpha? (c) Interpret the sign of the HML loading economically.

6. **Black-Litterman with one view.** A universe of two assets has equilibrium returns $\Pi = (6\%, 8\%)^T$ and covariance $\Sigma = \begin{pmatrix}0.04 & 0.02 \\ 0.02 & 0.09\end{pmatrix}$. The market weights are $w_{\text{mkt}} = (0.6, 0.4)^T$ and $\tau = 0.05$. An investor holds one view: asset 1 will outperform asset 2 by 2% (i.e., $P = (1, -1)$, $q = 0.02$) with view uncertainty $\Omega = (0.01)^2$. (a) Write out the BL update formula and compute $\hat{\mu}_\text{BL}$. (b) Compare $\hat{\mu}_\text{BL}$ to the equilibrium prior $\Pi$. How has the investor's view shifted the expected returns?

7. **Risk parity.** A two-asset portfolio has standard deviations $\sigma_1 = 15\%$ and $\sigma_2 = 30\%$, and correlation $\rho = 0.3$. (a) Compute the inverse-volatility weights. (b) Verify that these weights are exactly risk-parity when the two assets are uncorrelated ($\rho=0$). (c) For $\rho = 0.3$, compute the exact risk contribution of each asset under the inverse-volatility weights — do they equalise risk contributions? If not, describe qualitatively how the weights would change to achieve exact risk parity.
