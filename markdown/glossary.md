(glossary)=

# Glossary

**A**

**Adverse selection** ($\alpha$): The tendency for a market maker to trade against counterparties who possess superior information about future price movements, resulting in systematic losses on those trades. The fraction of informed counterparties $\alpha$ determines the magnitude of the adverse-selection component of the bid-ask spread. See {ref}`market_making_fundamentals` and {ref}`optimal_market_making`.

**Algorithmic trading**: The use of computer programs to generate, route, and manage orders automatically, encompassing execution algorithms, market-making algorithms, and investment algorithms. See {ref}`algorithmic_trading`.

**Almgren-Chriss model**: A stochastic optimal-control framework for optimal liquidation in which price impact has permanent ($\gamma v$) and temporary ($\eta v$) components; the optimal trading trajectory is $x_t^* = X\sinh(\kappa(T-t))/\sinh(\kappa T)$ where $\kappa = \sqrt{\lambda\sigma^2/\eta}$. See {ref}`sec:almgren_chriss`.

**Amihud illiquidity ratio**: A daily measure of price impact per unit of trading volume: $\text{ILLIQ} = \frac{1}{D}\sum_{d=1}^D |r_{t,d}|/V_{t,d}$, where $|r_{t,d}|$ is the absolute daily return and $V_{t,d}$ is dollar volume. High values indicate that small trades move prices substantially. See {ref}`sec:lob_asymmetry`.

**Arbitrage**: A trading strategy that generates a positive profit with zero risk and zero net investment, exploiting mispricings across related assets or markets. In practice, near-arbitrages carry residual basis risk and are more precisely termed statistical arbitrage. See {ref}`fair_price_estimation` and {ref}`quant_investment_fundamentals`.

**Arbitrage Pricing Theory (APT)**: A multi-factor model of expected returns asserting that the expected excess return of an asset equals the sum of its factor loadings times the corresponding factor risk premia, under no-arbitrage. See {ref}`optimal_investment_theory`.

**Ask price** ($P^a$): The price at which a market maker or the market is willing to sell; the lowest resting offer in the limit order book. See {ref}`market_microstructure`.

**Augmented Dickey-Fuller (ADF) test**: A hypothesis test for a unit root (random walk) in a time series, extending the Dickey-Fuller test by including lagged differences to control for serial correlation. Rejection of the null implies mean reversion. See {ref}`sec:oit_meanrev`.

**Avellaneda-Stoikov (AS) framework**: A continuous-time stochastic-control model for market making in which the dealer maximises CARA utility of terminal wealth, posting bid and ask quotes that attract Poisson-arriving client orders with exponential intensity $\lambda(\delta) = Ae^{-k\delta}$; solved via the HJB equation and a scalar indifference function. See {ref}`sec:omm_as`.

**Axe**: In dealer markets, a directional trading interest that a dealer is willing to share with clients, typically because the dealer holds inventory it wishes to reduce and can offer a preferential price. See {ref}`rfq_models`.

**B**

**Back-door criterion**: In causal inference, a condition on a set of variables $Z$ that blocks all non-causal (back-door) paths from $X$ to $Y$ in the causal DAG, enabling identification of the causal effect $P(Y|\text{do}(X=x))$ via the adjustment formula. See {ref}`intro_causal`.

**Backtesting**: The retrospective evaluation of a trading strategy on historical data. Reliable backtesting requires separate training, validation, and test sets; avoidance of look-ahead bias, survivorship bias, and data-snooping bias; and walk-forward validation. See {ref}`algorithmic_trading` and {ref}`quant_investment_fundamentals`.

**Basis risk**: The residual variance of a hedged position that cannot be eliminated with available hedge instruments; equal to $q^2\,\text{Var}(\Delta X)(1-R^2_{X|H})$. It arises from imperfect correlation between the exposure and the hedge. See {ref}`sec:oh_mvh`.

**Bayes factor** ($BF_{1,2}$): The ratio of marginal likelihoods $P(D|H_1)/P(D|H_2)$; a model-comparison statistic measuring how much more probable the data are under model $H_1$ than under $H_2$, without specifying a prior over models. See {ref}`intro_bayesian`.

**Bayes' theorem**: $P(H|D) = P(D|H)P(H)/P(D)$; the fundamental rule for updating a prior belief $P(H)$ to a posterior $P(H|D)$ given observed data $D$. See {ref}`intro_bayesian`.

**Bayesian information criterion (BIC)**: A model-selection criterion approximating the log-marginal-likelihood: $\text{BIC} = \log L(\hat\theta) - (d/2)\log N$; penalises model complexity in proportion to $\log N$. See {ref}`intro_bayesian`.

**Bayesian linear regression (BLR)**: Linear regression with a prior over weights; the posterior is analytically tractable under Gaussian or Normal-Inverse-Gamma priors. Ridge regression corresponds to MAP inference under a Gaussian prior; Lasso to MAP under a Laplace prior. See {ref}`blr-section`.

**Bellman equation**: The dynamic-programming recursion $V_k(x) = \min_{u}\{c_k(x,u) + \mathbb{E}[V_{k+1}(f(x,u,w))]\}$ characterising the value function of a stochastic optimal-control problem. See {ref}`sec:soc_dp`.

**Beta** ($\beta$): In CAPM, the sensitivity of an asset's excess return to the market excess return: $\mathbb{E}[R_i]-R_f = \beta_i(\mathbb{E}[R_m]-R_f)$. More generally, the OLS regression coefficient of asset returns on factor returns. See {ref}`sec:ifi_equities`.

**Bias-variance decomposition**: The identity $\mathbb{E}[(y-\hat{f})^2] = \text{Bias}^2 + \text{Variance} + \sigma^2_\text{noise}$; the fundamental tradeoff in statistical learning between systematic error (bias) and sensitivity to training data (variance). See {ref}`data_driven_methods`.

**Bid price** ($P^b$): The price at which a market maker or the market is willing to buy; the highest resting bid in the limit order book. See {ref}`market_microstructure`.

**Bid-ask spread** ($S$): The difference between the best ask and best bid prices: $S = P^a_{best} - P^b_{best}$. It is composed of inventory-risk, adverse-selection, and order-processing components. See {ref}`market_microstructure` and {ref}`optimal_market_making`.

**Black-Scholes-Merton (BSM) model**: An option-pricing model in which the underlying follows GBM; under the risk-neutral measure, options are priced by the BSM formula and hedged by continuous delta replication. See {ref}`sec:ifi_options` and {ref}`optimal_hedging`.

**Bond**: A fixed-income instrument representing a loan from the holder to the issuer, promising coupon payments and principal repayment at maturity; priced as the present value of future cash flows at the yield to maturity. See {ref}`sec:ifi_fixed_income`.

**Brownian motion / Wiener process** ($W_t$): A continuous-time stochastic process with independent Gaussian increments $W_t - W_s \sim \mathcal{N}(0, t-s)$, zero drift, and continuous sample paths; the fundamental building block of stochastic calculus. See {ref}`stochastic_calculus`.

**C**

**CARA utility**: Constant absolute risk aversion utility $U(W) = -e^{-\gamma W}$; produces risk premia that depend on the dollar variance of wealth, not its relative size. The risk-aversion coefficient $\gamma > 0$ scales the penalty for uncertainty. See {ref}`optimal_market_making`.

**CAPM** (Capital Asset Pricing Model): An equilibrium model asserting that the expected excess return of an asset is proportional to its market beta: $\mathbb{E}[R_i]-R_f = \beta_i(\mathbb{E}[R_m]-R_f)$. See {ref}`sec:ifi_equities`.

**Central limit order book (CLOB)**: An electronic order-matching system that ranks resting orders by price priority (then time priority) and matches incoming orders against the best available resting orders. See {ref}`market_microstructure`.

**Child order**: A smaller order split off from a parent order by an execution algorithm, routed to one or more venues. See {ref}`algorithmic_trading`.

**Cointegration**: A property of two or more non-stationary time series whose linear combination is stationary (mean-reverting). Cointegrated pairs form the basis of pairs-trading strategies. See {ref}`sec:oit_meanrev`.

**Conjugate prior**: A prior distribution closed under Bayesian updating for a given likelihood, yielding a posterior in the same family. The Beta distribution is conjugate to the Binomial; the Normal-Inverse-Gamma is conjugate to Gaussian regression. See {ref}`intro_bayesian`.

**Convexity**: The second derivative of a bond's price with respect to yield; a positive-convexity bond benefits from large yield moves in either direction. See {ref}`sec:ifi_fixed_income`.

**Cover price**: In a competitive RfQ, the second-best quote received by the client; used to assess whether a dealer won the trade at a profitable spread. See {ref}`market_microstructure` and {ref}`rfq_models`.

**Credit spread** ($s$): The yield differential between a risky bond and a risk-free bond of the same maturity; a measure of credit risk. See {ref}`sec:ifi_fixed_income`.

**Cross-validation ($K$-fold)**: A model-selection procedure partitioning training data into $K$ folds, training on $K-1$ and evaluating on the remaining fold, averaging $K$ estimates of generalisation error. See {ref}`data_driven_methods`.

**D**

**DAG (Directed Acyclic Graph)**: A graphical representation of a causal model in which nodes are variables and directed edges encode direct causal relationships; no directed cycles are permitted. See {ref}`intro_causal`.

**Dark pool**: A private trading venue that does not publish pre-trade order information, matching trades at or within the public bid-ask spread. See {ref}`intro_financial_markets`.

**Data-snooping bias**: The inflation of apparent strategy performance caused by implicitly fitting strategy parameters to the same data on which the strategy is evaluated; a form of multiple-testing bias. See {ref}`algorithmic_trading`.

**Delta** ($\Delta$): The sensitivity of an option's price to changes in the underlying asset price; the hedge ratio for delta-neutral positions. See {ref}`sec:ifi_options` and {ref}`optimal_hedging`.

**Depth**: One of the four dimensions of liquidity; the quantity available to trade at or near the current price without significantly moving the market. See {ref}`sec:liq_dimensions`.

**Do-operator** ($\text{do}(X=x)$): A formal notation in causal inference denoting an external intervention that sets variable $X$ to value $x$, distinct from conditioning on observing $X=x$; characterises interventional distributions $P(Y|\text{do}(X=x))$. See {ref}`intro_causal`.

**Duration** ($\mathcal{D}$): The modified duration of a bond: $\mathcal{D} = -(1/P)\partial P/\partial y$; approximates the percentage price change for a unit change in yield. See {ref}`sec:ifi_fixed_income`.

**Dynamic programming**: An optimisation method that solves multi-period problems by backward induction, expressing the optimal cost-to-go via the Bellman equation. See {ref}`sec:soc_dp`.

**E**

**Efficient frontier**: The set of portfolios that minimise variance for a given expected return (or maximise expected return for a given variance); the foundation of Markowitz portfolio theory. See {ref}`optimal_investment_theory`.

**Efficient trading frontier**: In execution, the curve tracing the minimum expected cost versus execution risk (timing risk) for all feasible trading strategies; the execution analogue of the Markowitz frontier. See {ref}`execution_fundamentals`.

**Empirical risk minimisation (ERM)**: The principle of selecting the model that minimises the average training loss $\hat{R}[f] = N^{-1}\sum_n \ell(y_n, f(\mathbf{x}_n))$ within a specified function class. See {ref}`data_driven_methods`.

**Exponential demand**: The model $\lambda(\delta) = Ae^{-k\delta}$ (or $f(\delta) = e^{-k\delta}$) for the rate at which client orders arrive as a function of the quoted half-spread $\delta$; used in the Avellaneda-Stoikov framework, execution tactics, and RfQ models. See {ref}`sec:lob_fill_probability`, {ref}`sec:tact_fill`, and {ref}`rfq_models`.

**F**

**Factor model**: A decomposition of asset returns into a small number of common factors plus an idiosyncratic component; used for risk management, portfolio construction, and hedging. See {ref}`sec:ifi_equities` and {ref}`optimal_investment_theory`.

**Fair value / fair price** ($M_t$): The theoretically correct price of an asset given all available information, modelled as a latent variable estimated via a Kalman filter from noisy trade observations. See {ref}`fair_price_estimation`.

**Feynman-Kac theorem**: A duality result linking solutions of linear second-order PDEs to conditional expectations of diffusion processes; used to convert HJB equations into expectations and to price derivatives. See {ref}`feynman_kac`.

**Fill probability** ($P(\text{fill}|\delta,\tau)$): The probability that a limit order posted at depth $\delta$ is executed within time $\tau$: $P(\text{fill}|\delta,\tau) = 1 - e^{-\lambda(\delta)\tau}$, where $\lambda(\delta) = Ae^{-k\delta}$. See {ref}`sec:lob_fill_probability`.

**Filtration** ($\mathcal{F}_t$): In stochastic calculus, the increasing family of sigma-algebras representing information available up to time $t$; formalises the notion of "no look-ahead." See {ref}`stochastic_calculus`.

**Forward contract**: A bilateral agreement to buy or sell an asset at a pre-agreed price $F = Se^{rT}$ at a future date $T$; the no-arbitrage forward price follows from the cost-of-carry relationship. See {ref}`sec:ifi_forwards`.

**Front-running**: The prohibited practice of trading in advance of a known client order to profit from the anticipated price movement caused by that order. See {ref}`algorithmic_trading`.

**G**

**Gaussian process (GP)**: A prior over functions specified by a mean function $\mu(x)$ and a covariance (kernel) function $k(x,x')$; any finite collection of function values is jointly Gaussian. GPs generalise Bayesian linear regression to infinite-dimensional function spaces. See {ref}`intro_bayesian`.

**Geometric Brownian motion (GBM)**: The SDE $dS_t = \mu S_t dt + \sigma S_t dW_t$ whose solution is $S_t = S_0 \exp((\mu-\sigma^2/2)t + \sigma W_t)$; the standard model for equity prices, ensuring positivity. See {ref}`stochastic_calculus`.

**Glosten-Milgrom model**: An equilibrium model of the bid-ask spread driven by adverse selection; with a fraction $\alpha$ of informed traders who know the asset value ($V_H$ or $V_L$ with prior mean $\mu = pV_H+(1-p)V_L$), the zero-profit spread is $\text{spread}_{\text{GL}} = \alpha(V_H - V_L)$. See {ref}`sec:omm_classic` and {ref}`sec:lob_asymmetry`.

**Greeks**: The partial derivatives of an option's price with respect to its inputs: $\Delta$ (delta, underlying price), $\Gamma$ (gamma, second derivative in price), $\Theta$ (theta, time decay), $\mathcal{V}$ (vega, volatility), $\rho$ (interest rate). See {ref}`sec:ifi_options`.

**Grossman-Miller model**: An equilibrium model of the bid-ask spread driven by inventory risk in a three-period setting; the competitive spread is $2i\gamma\sigma^2/n$ (declining in the number of market makers $n$, increasing in order size $i$ and volatility $\sigma$). See {ref}`sec:omm_classic`.

**H**

**Half-life** ($t_{1/2}$): The expected time for a mean-reverting process to halve its deviation from the long-run mean: $t_{1/2} = \ln 2 / \theta$. Provides the natural trading timescale for a mean-reversion strategy. See {ref}`sec:oit_meanrev`.

**Hamilton-Jacobi-Bellman (HJB) equation**: The continuous-time PDE characterising the value function of a stochastic optimal-control problem; the analogue of the Bellman equation in continuous time. See {ref}`sec:hjb`.

**Hawkes process**: A self-exciting point process in which past events increase the current arrival intensity: $\lambda(t) = \mu + \sum_{t_i < t}\phi\, e^{-\beta(t-t_i)}$; stationarity requires $\phi/\beta < 1$. Used to model order-flow clustering. See {ref}`sec:lob_order_arrival`.

**High-frequency trading (HFT)**: Algorithmic trading characterised by very high order-submission rates, extremely short holding periods (milliseconds to seconds), and minimal overnight positions; relies on co-location and low-latency infrastructure. See {ref}`algorithmic_trading`.

**Hit/miss ratio**: In RfQ markets, the fraction of trades won (hit) to total RfQs received; a key performance indicator for dealers. A miss occurs when the client trades with a competitor; a pass when the dealer declines to quote. See {ref}`market_microstructure` and {ref}`rfq_models`.

**Hurst exponent** ($H$): A scalar characterising the long-term memory of a time series: $H = 0.5$ (random walk), $H < 0.5$ (mean-reverting), $H > 0.5$ (trending). Estimated by the rescaled-range (R/S) method. See {ref}`sec:oit_meanrev`.

**I**

**Iceberg order**: A large order whose full size is hidden from the public order book; only a small visible portion ("peak") is displayed, with the hidden quantity refreshed as the visible portion executes. See {ref}`lob_models`.

**Immediacy**: One of the four dimensions of liquidity; the ability to execute a trade quickly without a substantial price concession. See {ref}`sec:liq_dimensions`.

**Implementation shortfall (IS)**: The difference between the paper portfolio value at the decision price $p_0$ and the actual portfolio value after execution: $IS = Q(p_\text{avg} - p_0) + \text{fees}$. The primary benchmark for measuring execution quality. See {ref}`sec:exec_benchmarks`.

**Informed trader**: In microstructure models, a trader who possesses private information about an asset's true value and trades profitably against the market maker. The fraction $\alpha$ of informed traders drives adverse-selection spreads. See {ref}`market_making_fundamentals` and {ref}`optimal_market_making`.

**Inventory risk**: The risk borne by a market maker from holding an unbalanced position in a volatile asset; a key component of the bid-ask spread in the Grossman-Miller model. See {ref}`market_making_fundamentals`.

**Inventory skew**: The adjustment to a market maker's quoted prices to attract trades that reduce an unwanted inventory position; in the Avellaneda-Stoikov model, the optimal reservation price shift is $\gamma\sigma^2(T-t)q$. See {ref}`sec:omm_single` and {ref}`sec:omm_as`.

**Itô's lemma**: The stochastic chain rule: for $y = f(W_t, t)$, $dy = (\partial_t f + \frac{1}{2}\partial^2_{WW} f)dt + \partial_W f\, dW_t$; the key tool for deriving SDEs for functions of Brownian motion. See {ref}`itos_lemma`.

**K**

**Kalman filter**: A recursive Bayesian estimator for the state of a linear Gaussian state-space model; produces the minimum-variance unbiased linear estimate of the latent state given all observations. Used for fair-value estimation and pairs trading with time-varying hedge ratios. See {ref}`fair_price_estimation` and {ref}`sec:oit_meanrev`.

**Kernel function** ($k(x,x')$): In Gaussian process regression and kernel methods, a positive semi-definite function measuring the similarity between two inputs; encodes smoothness and periodicity assumptions. See {ref}`intro_bayesian` and {ref}`data_driven_methods`.

**Kyle's lambda** ($\lambda_K$): The price-impact coefficient in Kyle's model of strategic informed trading: $\lambda_K = \sigma_v/(2\sigma_u)$; the slope of the price schedule set by the market maker as a function of order flow. See {ref}`sec:lob_market_impact`.

**L**

**Laplace approximation**: A method for approximating a posterior distribution by a Gaussian centred at the MAP estimate, with covariance equal to the inverse Hessian of the negative log-posterior. See {ref}`intro_bayesian`.

**Lasso regression**: Linear regression with an $L^1$ penalty on coefficients ($\lambda\sum_j|\beta_j|$), promoting sparsity; equivalent to MAP estimation under a Laplace prior. See {ref}`blr-section` and {ref}`sec:oh_lasso`.

**Layering**: A form of market manipulation in which large non-bona-fide orders are placed and quickly cancelled to create a false impression of supply or demand. See {ref}`algorithmic_trading`.

**Limit order**: An order to buy or sell at a specified price or better; it rests in the order book until matched against an incoming aggressive order. See {ref}`market_microstructure`.

**Linear-Quadratic Stochastic Control (LQSC)**: A special case of stochastic optimal control in which dynamics are linear and the cost is quadratic; admits an analytic solution via the Riccati equation. See {ref}`sec:lqsc`.

**Liquidity**: The ease with which an asset can be bought or sold without significantly affecting its price; measured along four dimensions: tightness (spread), depth, immediacy, and resiliency. See {ref}`sec:liq_dimensions`.

**M**

**MAP estimator** (Maximum A Posteriori): The mode of the posterior distribution $\hat{\theta}_\text{MAP} = \arg\max_\theta \log p(D|\theta) + \log p(\theta)$; a regularised point estimate that reduces to MLE when the prior is flat. See {ref}`intro_bayesian`.

**Market impact**: The adverse price movement caused by the execution of a trade; decomposed into temporary impact (reverting after the trade) and permanent impact (lasting). The empirical square-root law $\text{MI} \approx Y\sigma\sqrt{Q/V_{ADV}}$ is a widely used approximation. See {ref}`execution_fundamentals` and {ref}`sec:lob_market_impact`.

**Market maker**: A dealer who continuously quotes firm bid and ask prices, providing liquidity to the market in exchange for the bid-ask spread, while managing inventory risk and adverse selection. See {ref}`market_making_fundamentals`.

**Market order**: An order to buy or sell immediately at the best available price; it executes against resting limit orders and "takes" liquidity. See {ref}`market_microstructure`.

**Martingale**: A stochastic process $\{M_t\}$ satisfying $\mathbb{E}[M_t|\mathcal{F}_s] = M_s$ for all $s \leq t$; the mathematical formalisation of a "fair game." Brownian motion is a martingale. See {ref}`stochastic_calculus`.

**Maximum likelihood estimator (MLE)**: The parameter value that maximises the likelihood $L(\theta) = p(D|\theta)$; equivalent to MAP with a flat (uninformative) prior. See {ref}`intro_bayesian`.

**Mean reversion**: The tendency of a process to return toward a long-run mean after deviations; modelled by the Ornstein-Uhlenbeck process with $\theta > 0$. See {ref}`stochastic_calculus` and {ref}`sec:oit_meanrev`.

**Mid-price** ($M_t$): The average of the best bid and best ask prices: $M_t = \frac{1}{2}(P^a_{best} + P^b_{best})$; used as an estimate of the fair market price. See {ref}`market_microstructure` and {ref}`fair_price_estimation`.

**MiFID II**: The Markets in Financial Instruments Directive II; EU regulation governing trading venues, transparency requirements, best execution, and algorithmic trading controls. See {ref}`intro_financial_markets` and {ref}`algorithmic_trading`.

**Minimum variance hedge** ($\mathbf{h}^*$): The position in hedge instruments that minimises the variance of a hedged P&L: $\mathbf{h}^* = \boldsymbol{\Sigma}_{HH}^{-1}\boldsymbol{\sigma}_{XH}$; identical to the OLS regression coefficients of the exposure on the hedge instruments. See {ref}`sec:oh_mvh`.

**Momentum**: The tendency of recent asset returns to persist over short to medium horizons; quantified by the Hurst exponent ($H > 0.5$). See {ref}`quant_investment_fundamentals` and {ref}`optimal_investment_theory`.

**N**

**Normal-Inverse-Gamma (NIG) distribution**: The conjugate prior for Bayesian linear regression with unknown noise variance; enables closed-form posterior inference for regression weights and noise level jointly. See {ref}`blr-section`.

**O**

**Opportunity cost**: In execution, the cost incurred when a portion of the order remains unexecuted at the end of the trading window, measured against the arrival price; one component of implementation shortfall. See {ref}`execution_fundamentals`.

**Optimal depth** ($\delta^*(t,q)$): The optimal limit-order placement depth in the execution-tactics HJB model: $\delta^*(t,q) = 1/k + \Delta H(t,q)$, where $\Delta H$ is the finite difference of the value function $H$ with respect to inventory. See {ref}`sec:tact_single`.

**Order imbalance** ($I$): The normalised difference between bid-side and ask-side depth at the best quotes: $I = (V^b_{best} - V^a_{best})/(V^b_{best} + V^a_{best}) \in [-1,1]$; a short-term price-direction predictor. See {ref}`market_microstructure` and {ref}`sec:lob_features`.

**Order-to-trade ratio (OTR)**: The number of orders submitted per trade executed; a measure of the aggressiveness of order-submission activity. Under MiFID II, regulators monitor OTR to detect market manipulation. See {ref}`algorithmic_trading`.

**Ornstein-Uhlenbeck (OU) process**: The mean-reverting SDE $dS_t = \theta(\mu - S_t)dt + \sigma dW_t$ with stationary distribution $\mathcal{N}(\mu, \sigma^2/(2\theta))$; used to model spread processes, fair-value deviations, and mean-reversion strategies. See {ref}`stochastic_calculus` and {ref}`sec:oit_meanrev`.

**Overfitting**: The phenomenon in which a model fits training data so closely that it fails to generalise to new data; associated with high model complexity relative to the number of observations. See {ref}`data_driven_methods` and {ref}`algorithmic_trading`.

**P**

**Pairs trading**: A market-neutral strategy that goes long the relatively underpriced and short the relatively overpriced member of a cointegrated pair; profits from mean reversion of the spread. See {ref}`sec:oit_meanrev`.

**Parent order**: The full quantity of an asset that a trader wishes to buy or sell; decomposed into child orders by an execution algorithm. See {ref}`algorithmic_trading`.

**Particle filter**: A sequential Monte Carlo method for non-linear, non-Gaussian state-space models; approximates the filtering distribution with a set of weighted particles. See {ref}`fair_price_estimation`.

**Permanent market impact**: The portion of market impact that persists after a trade, permanently shifting the asset's equilibrium price; modelled as $g(v) = \gamma v$ in Almgren-Chriss. See {ref}`optimal_execution`.

**PIN (Probability of Informed Trading)**: A structural measure of the fraction of order flow that is information-motivated: $\text{PIN} = \alpha\mu_{\text{PIN}}/(\alpha\mu_{\text{PIN}} + 2\varepsilon)$, estimated by MLE from daily buy/sell counts. See {ref}`sec:lob_asymmetry`.

**Poisson process**: A counting process with independent, stationary increments and exponentially distributed inter-arrival times; the canonical model for order arrivals. See {ref}`stochastic_calculus` and {ref}`sec:lob_order_arrival`.

**Posterior distribution**: $p(\theta|D) \propto p(D|\theta)p(\theta)$; the updated belief about parameters after observing data $D$, combining the likelihood and the prior via Bayes' theorem. See {ref}`intro_bayesian`.

**Pre-hedging**: The act of trading in advance of an anticipated client order to reduce the expected inventory risk; raises regulatory concerns about information misuse. See {ref}`sec:oh_prehedge`.

**Prior distribution** ($p(\theta)$): The probability distribution encoding beliefs about model parameters before observing data. See {ref}`intro_bayesian`.

**Probabilistic graphical model (PGM)**: A framework combining graph theory and probability to represent complex joint distributions compactly; includes Bayesian networks (directed) and Markov random fields (undirected). See {ref}`sec:rfq_pgm`.

**Put-call parity**: The no-arbitrage relationship $C - P = S - Ke^{-rT}$ between European call ($C$) and put ($P$) option prices with the same strike $K$ and maturity $T$. See {ref}`sec:ifi_options`.

**Q**

**Q-table / Q-learning**: A model-free reinforcement learning algorithm that estimates the action-value function $Q(s,a)$ (expected discounted return from state $s$, action $a$) and derives the greedy policy $\pi^*(s) = \arg\max_a Q(s,a)$. See {ref}`sec:tact_rl` and {ref}`data_driven_methods`.

**R**

**Regularisation**: The addition of a penalty term $\lambda\Omega(f)$ to an empirical risk objective, discouraging overly complex models; has a Bayesian MAP interpretation where the penalty corresponds to the negative log-prior. See {ref}`data_driven_methods` and {ref}`intro_bayesian`.

**Reinforcement learning (RL)**: A framework for sequential decision-making in which an agent learns a policy to maximise cumulative reward through interaction with an environment modelled as a Markov decision process; relevant for execution and market-making optimisation. See {ref}`data_driven_methods`.

**Request for Quote (RfQ)**: A trading protocol in which a client solicits price quotes from one or more dealers; common in fixed income, credit, and OTC derivative markets. See {ref}`market_microstructure` and {ref}`rfq_models`.

**Reservation price** ($r(t,q)$): In market-making models, the price at which the market maker is indifferent between trading and not; the mid-point of the optimal bid and ask quotes. In the Avellaneda-Stoikov model, $r(t,q) = M_t - q\gamma\sigma^2(T-t)$. See {ref}`sec:omm_single`.

**Reservation spread** ($\delta_\text{res}$): The minimum half-spread at which a dealer is willing to trade given her current inventory and risk aversion. See {ref}`rfq_models`.

**Resiliency**: One of the four dimensions of liquidity; the speed at which the order book recovers to its normal depth and spread after a large trade. See {ref}`sec:liq_dimensions`.

**Ridge regression**: Linear regression with an $L^2$ penalty ($\lambda\|\boldsymbol{\beta}\|^2$), shrinking coefficients toward zero; equivalent to MAP estimation under a Gaussian prior. See {ref}`blr-section`.

**Risk parity**: A portfolio-construction approach that allocates capital so that each asset contributes equally to overall portfolio risk rather than by capital weight. See {ref}`optimal_investment_theory`.

**S**

**Self-excitation**: The property of a Hawkes process whereby past events increase the probability of future events; models order-flow clustering and volatility clustering. See {ref}`sec:lob_order_arrival`.

**Sharpe ratio** ($S_a$): The ratio of expected excess return to volatility: $S_a = \mathbb{E}[R_a - R_b]/\sigma_a$; the primary risk-adjusted performance metric. See {ref}`algorithmic_trading`.

**Smart order routing (SOR)**: An algorithm that automatically routes child orders across multiple trading venues to achieve best execution, minimising total cost by accounting for venue liquidity, fees, and latency. See {ref}`sec:tact_sor`.

**Spoofing**: A form of market manipulation in which a trader places large orders with no intention of executing them, to create a false impression of supply or demand, then cancels before execution. See {ref}`algorithmic_trading`.

**Square-root market-impact law**: The empirical relationship $\text{MI} \approx Y\sigma\sqrt{Q/V_{ADV}}$, where $Y$ is a dimensionless constant, $\sigma$ is daily volatility, $Q$ is trade size, and $V_{ADV}$ is average daily volume; widely used for pre-trade cost estimation. See {ref}`execution_fundamentals` and {ref}`sec:lob_market_impact`.

**State-space model (SSM)**: A dynamical model with latent state $\mathbf{x}_t$ evolving via a transition equation and observed via a measurement equation; provides the general framework for Kalman filtering and fair-value estimation. See {ref}`fair_price_estimation`.

**Statistical arbitrage**: A strategy that exploits mispricings relative to a model-implied fair value, accepting small residual risk that the mispricing will correct. See {ref}`quant_investment_fundamentals`.

**Stochastic differential equation (SDE)**: An equation of the form $dX_t = \mu(X_t,t)dt + \sigma(X_t,t)dW_t$ describing the evolution of a continuous-time random process driven by Brownian motion. See {ref}`sde`.

**Stochastic discount factor (SDF)**: A random variable $M$ such that the price of any asset equals $\mathbb{E}[M \cdot \text{payoff}]$; the fundamental object of arbitrage-free pricing theory, also called the pricing kernel. See {ref}`fair_price_estimation`.

**Structural causal model (SCM)**: A formal representation of a causal system as a collection of functions $X_i = f_i(\text{pa}(X_i), U_i)$, where $\text{pa}(X_i)$ are the causal parents and $U_i$ exogenous noise variables. See {ref}`intro_causal`.

**Survivorship bias**: The error of evaluating a strategy only on assets that survived to the end of the sample period, omitting those that delisted or failed; upward-biases apparent performance. See {ref}`algorithmic_trading`.

**Swap**: A bilateral derivative contract exchanging two cash-flow streams; in an interest rate swap (IRS) one party pays a fixed rate in exchange for a floating rate (e.g., SOFR). See {ref}`sec:ifi_swaps`.

**T**

**Temporary market impact**: The portion of market impact that reverts after a trade is completed; modelled as $h(v) = \eta v$ in Almgren-Chriss and causes an instantaneous adverse price shift during execution. See {ref}`optimal_execution`.

**Tick size**: The minimum price increment for an instrument in a given market; affects the granularity of the order book and the minimum possible bid-ask spread. See {ref}`market_microstructure`.

**Tightness**: One of the four dimensions of liquidity; the cost of a round-trip transaction of minimal size, approximated by the bid-ask spread. See {ref}`sec:liq_dimensions`.

**Timing risk**: In execution, the variance in execution cost arising from price uncertainty during the execution window; increases with execution horizon and asset volatility, creating the trader's dilemma against market impact. See {ref}`execution_fundamentals`.

**Trade flow imbalance (TFI)**: The difference between buyer-initiated and seller-initiated volume over a window, normalised by total volume; a higher-frequency analogue of order imbalance measuring directional pressure in recent trades. See {ref}`sec:lob_features`.

**Trader's dilemma**: The fundamental tradeoff in execution between minimising market impact (trade slowly) and minimising timing risk (trade quickly); the efficient trading frontier traces the Pareto-optimal solutions. See {ref}`execution_fundamentals`.

**Transformer architecture**: A deep learning architecture based on scaled dot-product attention mechanisms and positional encodings; the foundation of modern large language models and the basis of DeepLOB-style LOB predictors. See {ref}`generative_ai` and {ref}`sec:lob_short_term`.

**TWAP** (Time-Weighted Average Price): An execution benchmark equal to the arithmetic average of prices over a time interval; also the execution algorithm that trades equal-sized child orders at regular intervals. See {ref}`algorithmic_trading` and {ref}`sec:exec_benchmarks`.

**U**

**Uninformed trader / liquidity trader**: A counterparty who trades for exogenous reasons (portfolio rebalancing, hedging, liquidity needs) unrelated to private information; the source of profit for the market maker in Glosten-Milgrom. See {ref}`optimal_market_making`.

**V**

**Value function** ($V(t,x)$, $H(t,q)$): In stochastic optimal control, the expected optimal cost-to-go (or reward-to-go) from state $x$ at time $t$; satisfies the Bellman equation (discrete) or HJB equation (continuous). See {ref}`sec:soc_dp` and {ref}`sec:hjb`.

**VPIN (Volume-synchronized PIN)**: A high-frequency measure of order flow toxicity: $\text{VPIN}_t = \frac{1}{n}\sum_{i=t-n+1}^t |V_i^B - V_i^S|/V$, where volumes are computed over equal-size volume buckets. Elevated VPIN signals one-sided, potentially informed flow. See {ref}`sec:lob_asymmetry`.

**VWAP** (Volume-Weighted Average Price): The average execution price weighted by trade volume: $\text{VWAP} = \sum v_i P_i / \sum v_i$. Used as both an execution benchmark and an execution algorithm targeting a participation rate proportional to market volume. See {ref}`algorithmic_trading` and {ref}`sec:exec_benchmarks`.

**W**

**Walk-forward validation**: A backtesting methodology in which the model is trained on a rolling or expanding window of past data and tested on the immediately following out-of-sample period; reduces look-ahead and overfitting risks. See {ref}`quant_investment_fundamentals`.

**Wash trading**: A prohibited practice in which a party simultaneously buys and sells the same instrument to create artificial volume or price activity. See {ref}`algorithmic_trading`.

**Y**

**Yield to maturity (YTM)** ($y$): The internal rate of return of a bond held to maturity: the discount rate $y$ such that the present value of all cash flows equals the current market price. See {ref}`sec:ifi_fixed_income`.

**Z**

**Z-score** ($z_t$): The standardised deviation of a mean-reverting process from its estimated long-run mean: $z_t = (x_t - \hat{\mu})/\hat{\sigma}$; used as the entry/exit signal in mean-reversion strategies. See {ref}`sec:oit_meanrev`.

**Zero-coupon bond**: A bond that makes no periodic coupon payments; its price equals the present value of a single payment at maturity, directly revealing the discount factor for that maturity. See {ref}`sec:ifi_fixed_income`.
