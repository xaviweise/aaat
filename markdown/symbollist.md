(symbols)=

# Symbols

This page collects the mathematical notation used throughout the book. Symbols that carry chapter-specific meaning are listed under the relevant section below; general conventions apply everywhere.

## General conventions

| Symbol | Meaning |
|--------|---------|
| $\log(x)$ | Natural logarithm |
| $\mathbf{x}, \mathbf{y}$ | Vectors (bold lowercase); column vectors written $\mathbf{x}=[x_1,\dots,x_n]^T$ |
| $\mathbf{X}, \mathbf{Y}$ | Matrices (bold uppercase) |
| $X, Y$ | Random variables (uppercase Roman) |
| $\boldsymbol{\theta}$ | Model parameters (Greek lowercase) |
| $\hat\theta$ | Point estimate of $\theta$ |
| $\mathbb{E}[X \mid Y]$ | Expectation of $X$ given $Y$ |
| $\operatorname{Var}[X \mid Y]$ | Variance of $X$ given $Y$ |
| $\operatorname{Cov}[X, Y]$ | Covariance of $X$ and $Y$ |
| $\boldsymbol{\Sigma}$ | Covariance matrix |
| $X \sim p$ | Random variable $X$ is distributed as $p$ |
| $p(\cdot)$ | Probability density or probability mass function |
| $p(y \mid \mathbf{x})$ | Probability (density) of $y$ given $\mathbf{x}$ |
| $\mathbb{KL}(p \parallel q)$ | Kullback-Leibler divergence from $p$ to $q$ |
| $\mathcal{N}(\mu, \sigma^2)$ | Gaussian distribution with mean $\mu$ and variance $\sigma^2$ |
| $\mathbf{1}[\cdot]$ | Indicator function |
| $\mathbb{1}_A$ | Indicator of event $A$ |
| $\lVert \mathbf{x} \rVert$ | Euclidean norm of $\mathbf{x}$ |
| $\lVert \mathbf{x} \rVert_1$ | $L^1$ norm ($\sum_i |x_i|$) |
| $(\cdot)^+$ | Positive part: $\max(\cdot, 0)$ |

---

## Probability and statistics

| Symbol | Meaning |
|--------|---------|
| $p(\theta)$ | Prior distribution over parameters |
| $p(\theta \mid D)$ | Posterior distribution given data $D$ |
| $p(D \mid \theta)$ | Likelihood function |
| $p(D)$ | Marginal likelihood (model evidence) |
| $\hat\theta_\text{MLE}$ | Maximum likelihood estimate |
| $\hat\theta_\text{MAP}$ | Maximum a posteriori estimate |
| $\alpha, \beta$ | Beta/Dirichlet distribution shape parameters |
| $BF_{1,2}$ | Bayes factor $p(D\mid H_1)/p(D\mid H_2)$ |
| $\mathcal{GP}(\mu, k)$ | Gaussian process with mean $\mu$ and kernel $k$ |
| $k(x,x')$ | Kernel (covariance) function |
| $\lambda_\text{reg}$ | Regularisation hyperparameter (ridge/Lasso) |
| $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ | Multivariate Gaussian distribution |

---

## Stochastic calculus

| Symbol | Meaning |
|--------|---------|
| $W_t$ | Standard Brownian motion (Wiener process) |
| $\mathcal{F}_t$ | Filtration (information available at time $t$) |
| $dW_t$ | Brownian increment |
| $\mu$ | Drift coefficient (GBM, OU) |
| $\sigma$ | Diffusion coefficient / volatility |
| $\theta$ | Mean-reversion speed (OU: $dS_t = \theta(\mu-S_t)dt + \sigma\,dW_t$) |
| $\lambda_\text{Poi}$ | Poisson process arrival rate |
| $\phi$ | Hawkes process self-excitation amplitude ($\lambda(t) = \mu_0 + \sum_{t_i<t}\phi\,e^{-\beta(t-t_i)}$) |
| $\beta$ | Hawkes process decay rate |
| $\mu_0$ | Hawkes process baseline intensity |
| $N_t$ | Counting process (number of events by time $t$) |
| $\tau$ | Stopping time / time remaining |

---

## Financial instruments and markets

| Symbol | Meaning |
|--------|---------|
| $S_t$ | Asset price at time $t$ |
| $r$ | Risk-free interest rate |
| $y$ | Yield to maturity |
| $\mathcal{D}$ | Modified duration |
| $C$ | Option / instrument price; coupon payment (context-dependent) |
| $K$ | Strike price |
| $T$ | Maturity / terminal time |
| $F$ | Forward price |
| $\Delta$ | Option delta (sensitivity to underlying price) |
| $\Gamma$ | Option gamma (second derivative in price) |
| $\Theta$ | Option theta (time decay) |
| $\mathcal{V}$ | Option vega (sensitivity to volatility) |
| $R_i$ | Return of asset $i$ |
| $\beta_i$ | CAPM / factor beta of asset $i$ |
| $R_f$ | Risk-free rate |
| $\alpha_i$ | Jensen's alpha (excess return over CAPM benchmark) |

---

## Market microstructure and LOB

| Symbol | Meaning |
|--------|---------|
| $P^a_{best}$ | Best ask price |
| $P^b_{best}$ | Best bid price |
| $M_t$ | Mid-price: $M_t = \tfrac{1}{2}(P^a_{best}+P^b_{best})$ |
| $S$ | Bid-ask spread: $S = P^a_{best} - P^b_{best}$ |
| $I$ | Order imbalance: $I = (V^b_{best}-V^a_{best})/(V^b_{best}+V^a_{best})$ |
| $\text{TFI}_{t,\tau}$ | Trade flow imbalance over window $\tau$ |
| $V^b_{best}, V^a_{best}$ | Volume at best bid / best ask |
| $\lambda(t)$ | Point process intensity at time $t$ |
| $\lambda(\delta)$ | Fill intensity at depth $\delta$: $\lambda(\delta)=Ae^{-k\delta}$ |
| $A$ | Base fill rate (fill intensity at zero depth) |
| $k$ | Depth-sensitivity / demand-elasticity parameter |
| $P(\text{fill}\mid\delta,\tau)$ | Fill probability: $1-e^{-\lambda(\delta)\tau}$ |
| $\text{PIN}$ | Probability of Informed Trading: $\alpha\mu_{\text{PIN}}/(\alpha\mu_{\text{PIN}}+2\varepsilon)$ |
| $\text{VPIN}_t$ | Volume-synchronised PIN: $\frac{1}{n}\sum|V_i^B-V_i^S|/V$ |
| $\text{ILLIQ}_t$ | Amihud illiquidity: $\frac{1}{D}\sum|r_{t,d}|/V_{t,d}$ |
| $\lambda_K$ | Kyle's lambda: $\lambda_K=\sigma_v/(2\sigma_u)$ |
| $Y$ | Square-root impact coefficient: $\text{MI}\approx Y\sigma\sqrt{Q/V_{ADV}}$ |
| $V_{ADV}$ | Average daily volume |
| $\alpha_\text{inf}$ | Fraction of informed traders (Glosten-Milgrom; also written $\alpha$) |
| $V_H, V_L$ | High and low asset values (Glosten-Milgrom) |
| $p$ | Prior probability that asset value is $V_H$ |

---

## Execution algorithms

| Symbol | Meaning |
|--------|---------|
| $Q$ | Parent order size (initial inventory) |
| $q_t$ | Remaining inventory at time $t$ |
| $v_t$ | Trading rate: $v_t = -\dot{q}_t$ |
| $v_i$ | Quantity traded in discrete interval $i$ |
| $p_0$ | Arrival / decision price |
| $p_\text{avg}$ | Average execution price |
| $\text{IS}$ | Implementation shortfall: $Q(p_\text{avg}-p_0)$ |
| $\text{VWAP}$ | Volume-weighted average price: $\sum v_i P_i/\sum v_i$ |
| $\text{TWAP}$ | Time-weighted average price |
| $\eta$ | Temporary price-impact coefficient ($h(v)=\eta v$) |
| $\gamma_\text{perm}$ | Permanent price-impact coefficient ($g(v)=\gamma_\text{perm} v$) |
| $\rho$ | Risk-aversion coefficient in execution mean-variance objective |
| $\kappa$ | Almgren-Chriss trajectory decay rate: $\kappa=\sqrt{\rho\sigma^2/\eta}$ |
| $x_t$ | Remaining inventory in Almgren-Chriss (also written $q_t$) |

---

## Market making and optimal quoting

| Symbol | Meaning |
|--------|---------|
| $\delta^a, \delta^b$ | Ask-side and bid-side half-spreads (both non-negative) |
| $\delta^*(t,q)$ | Optimal half-spread (HJB / AS solution) |
| $r(t,q)$ | Reservation price: mid-point of optimal quotes |
| $\gamma$ | CARA risk-aversion coefficient ($U(W)=-e^{-\gamma W}$) |
| $\mathbf{q}_t$ | Inventory vector (multi-asset) |
| $H(t,q)$ | Value function in execution-tactic / AS HJB |
| $u(t,\mathbf{q})$ | Scalar indifference function (AS multi-asset) |
| $\boldsymbol{\Gamma}$ | Asset covariance matrix (market-making context) |
| $\text{spread}_\text{GL}$ | Glosten-Milgrom equilibrium spread: $\alpha(V_H-V_L)$ |
| $n$ | Number of competing market makers (Grossman-Miller) |
| $\Lambda^a, \Lambda^b$ | Ask-side and bid-side order arrival processes (Poisson rate $Ae^{-k\delta}$) |
| $\delta_\text{res}$ | Reservation half-spread (RfQ / dealer context) |
| $s$ | Side variable ($s=+1$ ask, $s=-1$ bid) in RfQ context |
| $P_m$ | Mid-price in RfQ context (equivalent to $M_t$) |

---

## Optimal control and dynamic programming

| Symbol | Meaning |
|--------|---------|
| $V(t,x)$ | Value function (cost-to-go or reward-to-go) |
| $J$ | Objective functional |
| $u_t$ | Control variable at time $t$ |
| $\mathcal{H}$ | Hamiltonian |
| $\mathbf{P}_t$ | Riccati matrix (LQSC solution) |
| $\lambda_\text{DP}$ | Risk-aversion / Lagrange multiplier in DP objectives |

---

## Machine learning and data-driven methods

| Symbol | Meaning |
|--------|---------|
| $\ell(y, \hat y)$ | Loss function |
| $R[f]$ | Expected (generalisation) risk |
| $\hat R[f]$ | Empirical risk (training loss) |
| $\mathbf{w}$ | Weight vector (neural network / linear model) |
| $f^*$ | Bayes-optimal decision function |
| $K$ | Number of classes; number of cross-validation folds (context-dependent) |
| $N$ | Number of training observations |
| $H$ | Hurst exponent ($H=0.5$ random walk, $H<0.5$ mean-reverting, $H>0.5$ trending) |
| $z_t$ | Z-score: $(x_t-\hat\mu)/\hat\sigma$ |
| $Q(s,a)$ | Action-value function (Q-learning) |
| $\pi$ | Policy (reinforcement learning) |

---

## Portfolio and investment

| Symbol | Meaning |
|--------|---------|
| $\mathbf{w}$ | Portfolio weight vector |
| $\boldsymbol{\mu}$ | Vector of expected returns |
| $\boldsymbol{\Sigma}$ | Asset covariance matrix |
| $S_a$ | Sharpe ratio: $\mathbb{E}[R_a-R_b]/\sigma_a$ |
| $\mathbf{h}^*$ | Minimum-variance hedge vector: $\boldsymbol{\Sigma}_{HH}^{-1}\boldsymbol{\sigma}_{XH}$ |
| $\beta_\text{hedge}$ | Hedge ratio (scalar, single hedge instrument) |
| $t_{1/2}$ | Mean-reversion half-life: $\ln 2/\theta$ |
