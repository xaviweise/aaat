(optimal_hedging)=
# Optimal Hedging

## Introduction

A dealer who provides liquidity to clients does not hold a balanced book. Every trade that she wins adds to her inventory — a residual position that exposes her to adverse price movements until the position is unwound through the opposite trade or through an explicit hedge. Managing this residual risk is the hedging problem, and it is central to the economics of market-making: the spread charged to clients must compensate for the expected cost of hedging the resulting inventory, and the quality of the hedge determines how much of that spread is retained as profit.

The hedging problem takes two structurally different forms depending on the nature of the instrument. For **flow products** — bonds, swaps, FX forwards, equity shares — the risk is linear: the P&L of the position is a linear function of the change in the underlying market variable, and the hedge is a position in a correlated instrument that offsets this linear exposure. The theory here is deeply connected to regression analysis and factor models, and the main challenges are statistical (estimating the hedge ratio from historical data) and operational (executing the hedge efficiently in the presence of transaction costs).

For **derivative instruments** — options and other nonlinear payoff structures — the risk is path-dependent and nonlinear. The theoretical benchmark is the **dynamic delta hedging** strategy derived in the Black-Scholes-Merton (BSM) framework, which we introduced in {ref}`fair_price_estimation`. In practice, BSM hedging is an idealization: continuous rebalancing is impossible, transaction costs are non-zero, and the model dynamics are at best approximate. The art of derivatives hedging consists in adapting this theoretical benchmark to the realities of market frictions, model error, and computational constraints.

A third dimension — particular to dealer markets — is the interaction between hedging and quote management. In the Avellaneda-Stoikov framework of {ref}`optimal_market_making`, the dealer manages inventory through **quote skewing**: biasing bid and ask prices to attract trades in the direction that reduces inventory. Hedging in the market and skewing in quotes are substitutes, each with its own cost, and the optimal policy combines both. The connection between these two approaches and the conditions under which one dominates the other is a key result of this chapter.

The chapter is organised as follows. We begin with **hedging flow products** ({ref}`sec:oh_flow`): minimum variance hedging ({ref}`sec:oh_mvh`), the compression of covariance structure via factor models and autoencoders ({ref}`sec:oh_factors`), sparse hedging under transaction costs ({ref}`sec:oh_lasso`), the pre-hedging decision when an anticipated client order is not yet executed ({ref}`sec:oh_prehedge`), and the unified analysis of skewing versus hedging ({ref}`sec:oh_skewhedge`). We then turn to **hedging derivatives** ({ref}`sec:oh_derivatives`): the discrete and transaction-cost-aware extension of BSM delta hedging ({ref}`sec:oh_bsm`), machine learning surrogates for large-scale Greeks computation ({ref}`sec:oh_ml`), and the model-free deep hedging framework ({ref}`sec:oh_deep`).

(sec:oh_flow)=
## Hedging Flow Products

Flow inventory arises naturally in any market-making operation: the dealer sells when clients buy, buys when clients sell, and holds the resulting imbalance until it is absorbed by the opposite flow or hedged away. Although the relationship between the inventory position and its market value is linear in the underlying price change, the problem of finding the best hedge is non-trivial for at least three reasons. First, the inventory is typically spread across many instruments — different bonds, tenors, or currency pairs — and their joint covariance structure must be estimated from noisy data. Second, the set of available hedging instruments may be far smaller than the set of instruments in the book, requiring the dealer to project exposures onto a smaller hedge basis. Third, every hedge transaction incurs a cost, so hedging more granularly is not always better.

(sec:oh_mvh)=
### Minimum Variance Hedging

The simplest formulation asks: given a position of size $q$ in instrument $X$, what static position $\mathbf{h} \in \mathbb{R}^K$ in a basket of $K$ liquid hedge instruments $\mathbf{H} = (H_1, \ldots, H_K)$ minimises the variance of the hedged P&L over a given horizon?

Over a short interval $\Delta t$, the unhedged P&L is $\pi_0 = q\,\Delta X$. The hedged P&L is:

$$\pi = q\,\Delta X - \mathbf{h}^T \Delta\mathbf{H}$$

where $\Delta X$ and $\Delta\mathbf{H}$ denote the price changes of the exposure and hedge instruments respectively. The variance of the hedged P&L is:

$$\text{Var}(\pi) = q^2\,\text{Var}(\Delta X) - 2q\,\mathbf{h}^T\boldsymbol{\sigma}_{XH} + \mathbf{h}^T\boldsymbol{\Sigma}_{HH}\,\mathbf{h}$$

where $\boldsymbol{\sigma}_{XH} = \text{Cov}(\Delta X, \Delta\mathbf{H}) \in \mathbb{R}^K$ and $\boldsymbol{\Sigma}_{HH} = \text{Cov}(\Delta\mathbf{H}) \in \mathbb{R}^{K\times K}$. Setting the gradient with respect to $\mathbf{h}$ to zero gives the minimum variance hedge:

$$\boxed{\mathbf{h}^* = q\,\boldsymbol{\Sigma}_{HH}^{-1}\boldsymbol{\sigma}_{XH} = q\,\hat{\boldsymbol{\beta}}_{X|H}}$$

The optimal hedge ratio is exactly the vector of OLS regression coefficients from regressing $\Delta X$ on $\Delta\mathbf{H}$. This identification — **hedging equals regression** — is fundamental. The minimum residual variance is:

$$\text{Var}(\pi^*) = q^2\,\text{Var}(\Delta X)\,(1 - R^2_{X|H})$$

where $R^2_{X|H}$ is the coefficient of determination from the regression. A perfect hedge ($R^2 = 1$) eliminates all variance; a hedge with $R^2 = 0.8$ leaves 20% of the variance unexposed. The unhedgeable residual $q^2\,\text{Var}(\Delta X)(1-R^2)$ represents **basis risk**: the component of the exposure's risk that is orthogonal to all available hedge instruments.

**Estimation.** In practice, the covariance matrix $\boldsymbol{\Sigma}_{HH}$ and the cross-covariance vector $\boldsymbol{\sigma}_{XH}$ must be estimated from historical data. The most common choices are:

- **Rolling sample covariance**: compute sample covariance over a window of $T$ past observations. A short window reduces the impact of stale data but increases estimation variance; a long window provides stability but assumes a stationary covariance structure.
- **Exponentially weighted moving average (EWMA)**: assign weight $\lambda^k$ to the $k$-th lag, with $\lambda \in (0,1)$. This is the RiskMetrics approach {cite:p}`wilmott2007introduces` and effectively sets the estimation window to $1/(1-\lambda)$ observations.
- **Bayesian shrinkage**: the Ledoit-Wolf estimator shrinks the sample covariance toward a structured target (e.g., the identity matrix), reducing the extreme eigenvalues that arise when $K$ is close to $T$.

The hedge ratio $\hat{\boldsymbol{\beta}}_{X|H}$ inherits the estimation error of the covariance estimator and is itself a random variable. Its estimation error introduces a systematic downward bias in the in-sample $R^2$ that inflates the apparent hedge quality: the hedging performance measured on the same data used to compute $\hat{\boldsymbol{\beta}}$ will be better than its true out-of-sample performance.

**Multi-instrument books.** When the dealer holds $N$ instruments $\mathbf{X} = (X_1, \ldots, X_N)$, each with position $q_i$, the total unhedged P&L is $\pi_0 = \mathbf{q}^T\Delta\mathbf{X}$. The hedged P&L with positions $\mathbf{h}$ in hedge instruments is $\pi = \mathbf{q}^T\Delta\mathbf{X} - \mathbf{h}^T\Delta\mathbf{H}$. The minimum variance hedge generalises to:

$$\mathbf{h}^* = \boldsymbol{\Sigma}_{HH}^{-1}\boldsymbol{\Sigma}_{HX}\mathbf{q}$$

where $\boldsymbol{\Sigma}_{HX} \in \mathbb{R}^{K\times N}$ contains the covariances between hedge and book instruments. Alternatively, the net exposure of the book in terms of the hedge instruments is $\boldsymbol{\beta}^T\mathbf{q}$, where $\boldsymbol{\beta}$ is the $N\times K$ matrix of regression betas, and this is the quantity to hedge.

(sec:oh_factors)=
### Factor Models and Compressed Hedging

In large books — a fixed income dealer might hold thousands of bond positions across many issuers and maturities — direct minimum variance hedging requires estimating an enormous covariance matrix. With $N = 1000$ instruments and $T = 250$ observations (one year of daily data), the sample covariance is not even invertible. Factor models address this by compressing the covariance structure into a small number of latent risk factors.

**The factor model.** Assume the returns on the $N$ book instruments are driven by $K \ll N$ common factors $\mathbf{f}_t \in \mathbb{R}^K$:

$$\Delta\mathbf{X}_t = \mathbf{B}\,\mathbf{f}_t + \boldsymbol{\epsilon}_t$$

where $\mathbf{B} \in \mathbb{R}^{N\times K}$ is the factor loading matrix and $\boldsymbol{\epsilon}_t$ is an idiosyncratic residual with $\text{Cov}(\boldsymbol{\epsilon}) = \mathbf{D}$ diagonal. The covariance matrix has the factor decomposition:

$$\boldsymbol{\Sigma}_{XX} = \mathbf{B}\,\boldsymbol{\Omega}_f\,\mathbf{B}^T + \mathbf{D}$$

where $\boldsymbol{\Omega}_f = \text{Cov}(\mathbf{f})$. The minimum variance hedge in factor space requires matching the **factor sensitivities** of the book: the net exposure to each factor is $(\mathbf{B}^T\mathbf{q})_k = \sum_i q_i B_{ik}$, and hedging means choosing $\mathbf{h}$ so that the hedge instruments absorb this exposure:

$$\sum_j h_j B_{jk}^{(\text{hedge})} = \sum_i q_i B_{ik}^{(\text{book})}, \qquad k = 1, \ldots, K$$

This is a system of $K$ linear equations in $K$ unknowns (assuming exactly $K$ hedge instruments), easily solved. When more hedge instruments are available, the system is under-determined and an additional criterion — minimum gross notional, minimum turnover, or maximum $R^2$ — is needed.

**PCA hedging of the yield curve.** In fixed income, the factors are naturally extracted from the principal components of the historical yield changes $\Delta\mathbf{r}_t \in \mathbb{R}^D$, where $D$ is the number of maturities on the curve. As shown in {ref}`sec:ddm_pca`, the PCA factors ordered by explained variance correspond to:

- **Level** ($k=1$): a near-parallel shift of the yield curve, explaining 70–85% of variance
- **Slope** ($k=2$): a steepening or flattening, explaining 10–15%
- **Curvature** ($k=3$): a butterfly, explaining 3–7%

Together, three factors typically explain over 95% of the joint variance of a developed-market yield curve.

For a bond with DV01 vector $\mathbf{d} \in \mathbb{R}^D$ (dollar sensitivity to a one-basis-point shift at each maturity), the P&L under a yield change $\Delta\mathbf{r}$ is $\text{PnL} = \mathbf{d}^T\Delta\mathbf{r}$. Projecting onto the PCA factors:

$$\text{PnL} \approx \sum_{k=1}^K (\mathbf{d}^T\mathbf{u}_k)\,f_k = \sum_{k=1}^K d^{(k)} f_k$$

where $d^{(k)} = \mathbf{d}^T\mathbf{u}_k$ is the **factor DV01** — the sensitivity to a unit move in factor $k$. Hedging the first three factors requires three liquid instruments (e.g., benchmark on-the-run bonds at 2-, 5-, and 10-year maturities) whose factor DV01s span the space, and the hedge ratios solve a $3\times3$ linear system. {numref}`fig:hedg_pca_factors` shows the first three PCA factors of a simulated yield curve and the hedge performance.

```{figure} figures/hedg_pca_factors.png
:name: fig:hedg_pca_factors
:width: 9in
Top row: sample yield curves (left) and the first three PCA eigenvectors (right), corresponding to level, slope, and curvature. Bottom row: out-of-sample P&L distribution for a bond position with no hedge (grey), a DV01-only hedge (blue), and a three-factor PCA hedge (orange). The PCA hedge substantially reduces variance; residual basis risk is the idiosyncratic component unexplained by the three factors.
```

**Autoencoders for nonlinear factor hedging.** The PCA decomposition is linear: it maps the yield curve into a linear subspace. When the yield curve dynamics contain significant nonlinearities — as they often do during stress periods when the curve can invert sharply or exhibit unusual curvature patterns — a linear projection into three factors can leave substantial unexplained variance that a nonlinear factor model would capture.

Autoencoders, introduced in {ref}`sec:ddm_autoencoders`, learn a nonlinear compressed representation. An autoencoder trained on a dataset of historical yield curves $\{\mathbf{r}_t\}$ learns:

- Encoder $f_\phi: \mathbb{R}^D \to \mathbb{R}^M$: compresses the yield curve to $M$ latent factors
- Decoder $g_\psi: \mathbb{R}^M \to \mathbb{R}^D$: reconstructs the curve from the factors

The factor sensitivities of a bond for hedging purposes follow by the chain rule through the decoder:

$$\frac{\partial\text{PnL}}{\partial z_k} = \sum_{j=1}^D d_j \frac{\partial r_j}{\partial z_k} = \mathbf{d}^T \frac{\partial g_\psi(\mathbf{z})}{\partial z_k}$$

computed by automatic differentiation. These nonlinear factor sensitivities replace the linear PCA projections $d^{(k)} = \mathbf{d}^T\mathbf{u}_k$ as inputs to the hedge ratio calculation. The procedure is otherwise identical: choose hedge instruments whose latent sensitivities match those of the book.

In practice, the autoencoder approach is most valuable when the number of effective risk dimensions is small but the manifold is curved — a setting where PCA uses many more components than the autoencoder to achieve the same reconstruction accuracy.

(sec:oh_lasso)=
### Hedging with Transaction Costs and Sparsity

The minimum variance hedge uses all $K$ available instruments, potentially with large notionals. In practice, each hedge position is executed with bid-ask spread cost and must be rebalanced periodically as market conditions change. A hedge that uses 50 instruments may consume more in transaction costs than it saves in variance reduction. The goal of **sparse hedging** is to find a small subset of instruments that provides most of the variance reduction, accepting a mild increase in residual variance in exchange for much lower transaction costs.

**The Lasso hedge.** The most natural formulation adds an $\ell_1$ penalty on the hedge positions to the minimum variance objective:

$$\min_{\mathbf{h}} \left[\frac{1}{2}\mathbf{h}^T\boldsymbol{\Sigma}_{HH}\mathbf{h} - q\,\mathbf{h}^T\boldsymbol{\sigma}_{XH}\right] + \lambda\|\mathbf{h}\|_1$$

The first bracket is the negative of the covariance between hedge and exposure — minimising it promotes variance reduction. The $\ell_1$ penalty encourages sparse solutions: for sufficiently large $\lambda$, many components of $\mathbf{h}$ are set exactly to zero, leaving a small subset of active hedge instruments. As shown in {ref}`sec:ddm_regularization`, the Lasso path traces out the solution as $\lambda$ varies from 0 (full minimum variance solution) to $\infty$ (zero hedge): instruments enter the active set one by one in decreasing order of their marginal contribution to variance reduction. The tuning parameter $\lambda$ is chosen by cross-validation or by explicit transaction cost accounting: set $\lambda = c \cdot \text{bid-ask}$, where $c$ is the expected frequency of rebalancing.

**Elastic net hedge.** An extension combines $\ell_1$ and $\ell_2$ penalties:

$$\min_{\mathbf{h}} \left[\frac{1}{2}\mathbf{h}^T\boldsymbol{\Sigma}_{HH}\mathbf{h} - q\,\mathbf{h}^T\boldsymbol{\sigma}_{XH}\right] + \lambda_1\|\mathbf{h}\|_1 + \frac{\lambda_2}{2}\|\mathbf{h}\|^2$$

The $\ell_2$ component (ridge penalty) stabilises the covariance estimate in the case of correlated hedge instruments, where the Lasso solution can be unstable (arbitrary allocation of weight among correlated instruments). The elastic net tends to select groups of correlated instruments together, which is desirable when several benchmark bonds are available and any of them would serve equally well.

**Transaction-cost-adjusted objective.** A more explicit treatment models the expected transaction cost of entering and maintaining the hedge. If the hedge is rebalanced $m$ times over the horizon $T$ and each rebalancing costs $c_j$ per unit in instrument $j$, the full cost of a hedge $\mathbf{h}$ is:

$$\text{Total cost} = \underbrace{\text{Var}(\pi^*)}_{\text{residual variance}} + \underbrace{m \sum_j c_j |h_j|}_{\text{transaction costs}}$$

Minimising over $\mathbf{h}$ gives a Lasso problem with $\lambda = m \cdot c_j$ for each instrument. This framing makes the dependence on rebalancing frequency explicit: a hedge that looks optimal at daily rebalancing may not be cost-effective at hourly rebalancing if transaction costs are high. {numref}`fig:hedg_lasso` shows the Lasso hedge path and the efficiency frontier of variance reduction versus gross notional for a fixed income book.

```{figure} figures/hedg_lasso.png
:name: fig:hedg_lasso
:width: 9in
Left: Lasso hedge path — coefficient values as a function of the regularisation parameter $\lambda$. Each line corresponds to one hedge instrument; instruments with stronger partial correlation to the exposure enter first. Centre: residual variance as a function of $\lambda$, normalised by the unhedged variance; the Lasso achieves near-minimum variance with a fraction of the instruments. Right: the efficiency frontier in the (gross notional, residual variance) plane; each point corresponds to a value of $\lambda$, and the Pareto-optimal region is shaded.
```

(sec:oh_prehedge)=
### Pre-hedging

The hedging frameworks above are **reactive**: they manage inventory that has already been accumulated. A dealer who anticipates a future client order faces a different decision: should she begin to hedge (or rather, position) in advance of the client trade? This is the **pre-hedging** problem, and it requires balancing the risk reduction from early positioning against the transaction cost of pre-trading.

**Setup.** At time $t=0$, the dealer learns — with probability $p \in (0,1]$ — that at time $T$ a client will request a trade of size $Q > 0$ (a sell order from the client, requiring the dealer to buy). Between $t=0$ and $t=T$, the dealer can build a position $x_t$ in the underlying at trading rate $v_t = \dot{x}_t$, subject to:

- **Linear transaction costs**: each unit of pre-trading costs $c > 0$ in bid-ask spread, contributing $c|v_t|$ per unit time
- **Inventory risk**: holding the pre-hedge position exposes the dealer to market risk, penalized at rate $\frac{\gamma}{2}\sigma^2 x_t^2$ per unit time (quadratic in position, consistent with the risk-averse objective in {ref}`optimal_market_making`)
- **Outcome**: if the order materialises (probability $p$), the dealer buys $Q$ from the client at $t=T$ with a net position $Q + x_T$; if it does not (probability $1-p$), the dealer holds the open pre-hedge position $x_T$ and must unwind it

The pre-hedging problem is therefore:

$$\min_{v_t} \mathbb{E}\left[\int_0^T \left(c|v_t| + \frac{\gamma}{2}\sigma^2 x_t^2\right) dt + \underbrace{p \cdot \text{Risk}(Q + x_T) + (1-p)\cdot \text{Risk}(x_T)}_{\text{terminal inventory risk}}\right]$$

This is a variant of the Almgren-Chriss execution problem ({ref}`optimal_execution`) with an uncertain terminal target: the dealer wants to arrive at $t=T$ with position $x_T = -pQ$ if she optimises entirely for the expected case, but deviations from this target in either direction carry inventory risk.

**Optimal pre-hedge fraction.** Under the linear-quadratic cost structure {cite:p}`muhlekarbe2023prehedge`, the optimal pre-hedge position at $t=T$ is a deterministic fraction of the client order:

$$x_T^* = -\phi^*(p,c,\gamma,\sigma,T)\cdot Q$$

where $\phi^*$ depends on the transaction cost $c$, risk aversion $\gamma$, volatility $\sigma$, and horizon $T$. The key limiting cases are instructive:
- **Zero transaction costs** ($c \to 0$): $\phi^* \to p$. The dealer pre-hedges the full expected order — rational given that pre-trading is free.
- **Zero risk aversion** ($\gamma \to 0$): $\phi^* \to 0$. The dealer does not pre-hedge since she is indifferent to inventory risk; pre-trading would be pure cost.
- **Large horizon** ($T \to \infty$): the pre-hedge can be built gradually and at lower market impact, so $\phi^*$ increases.
- **Certain order** ($p \to 1$): $\phi^* \to 1$; the dealer fully pre-hedges.

The pre-hedge is executed gradually, at a rate $v_t^*$ that is constant (linear schedule) under the symmetric linear-quadratic problem, analogous to the Almgren-Chriss VWAP strategy. {numref}`fig:hedg_prehedge` illustrates how the optimal pre-hedge fraction depends on the probability of the order and the ratio $c/(\gamma\sigma^2 T)$ of transaction costs to inventory risk.

```{figure} figures/hedg_prehedge.png
:name: fig:hedg_prehedge
:width: 9in
Optimal pre-hedge fraction $\phi^*$ as a function of the probability $p$ that the client order materialises (left) and as a function of the cost-to-risk ratio $c/(\gamma\sigma^2 T)$ (right). At low probabilities or high costs relative to risk, pre-hedging is minimal; at high probabilities and low relative costs, the dealer pre-hedges close to the full expected order.
```

**Regulatory and ethical dimensions.** Pre-hedging intersects with market conduct regulation. A dealer who trades ahead of a known client order in a way that disadvantages the client — for example, by moving the price before executing the client trade — may violate best execution obligations or front-running prohibitions. The legal and regulatory treatment of pre-hedging varies across jurisdictions and instruments: regulators distinguish between hedging anticipated risk (generally permissible) and trading ahead of a client to benefit from the client's subsequent market impact (generally not). The model above abstracts from these conduct dimensions but they are non-negligible in practice.

(sec:oh_skewhedge)=
### Skewing versus Hedging

The Avellaneda-Stoikov framework ({ref}`optimal_market_making`) provides one answer to inventory management: adjust the dealer's reservation price by $-\theta q$ (where $q$ is the net inventory and $\theta > 0$ is the GLF skew coefficient), effectively offering better prices on trades that reduce the book and worse prices on trades that add to it. This is inventory management through **skewing**: no transaction in the hedge market is required, but the dealer accepts a lower win rate on positions that increase inventory.

An alternative is **direct hedging**: leave the quotes unchanged and trade in the market to offset the inventory, paying the bid-ask spread on the hedge transaction. These two approaches are not mutually exclusive — the optimal policy typically mixes both — but their cost structures differ fundamentally.

**The cost of skewing.** When the dealer skews her reservation price by $-\theta q$, she offers a better price on the side that reduces inventory. This increases her win rate in the desired direction but reduces it on the other side, and the resulting trades are executed at a worse spread on average. The expected spread earned per trade decreases. If the arrival rate and price sensitivity are fixed, the dealer's expected revenue per unit time decreases by an amount proportional to $\theta^2 q^2$: skewing costs revenue.

**The cost of hedging.** A hedge trade of size $\Delta q$ incurs a one-way cost of $c |\Delta q|$ (bid-ask spread plus market impact). This is a direct cash cost paid regardless of subsequent market moves.

**The optimal policy.** The dealer minimises total cost — inventory risk + skewing revenue loss + hedging transaction costs — by choosing both the skew $\theta q$ and the hedging rate $v_t$ jointly. {cite:t}`barzykin2023skewhedge` derive the optimal policy in a continuous-time setting where the dealer receives order flow at a Poisson rate and can hedge at any time at proportional cost. The main results are:

1. **No-trade band**: there exists an inventory band $[-q^*, q^*]$ within which the dealer uses only skewing and does not hedge. Outside this band, both skewing and hedging are active simultaneously.

2. **Hedging threshold**: the threshold $q^*$ is increasing in transaction cost $c$ (wider band when hedging is more expensive) and decreasing in the arrival rate $A$ (narrower band when order flow is abundant, as skewing can quickly reduce inventory through the flow).

3. **Optimal skew**: inside the band, the optimal skew coefficient $\theta^*$ is identical to the GLF result; outside the band, the skew is reduced because the hedge absorbs part of the inventory correction, making aggressive skewing redundant.

4. **Substitutability**: when transaction costs are zero, the dealer hedges completely and never skews (the hedge is free, so skewing revenue loss is pure waste). When transaction costs are infinite, the dealer never hedges and sets the maximum admissible skew. For intermediate costs, the optimal policy is a weighted average.

The practical implication is that in liquid markets with tight bid-ask spreads (e.g., on-the-run government bonds, major FX pairs), hedging dominates and the dealer should maintain a small inventory through frequent market hedges. In illiquid markets (high-yield bonds, EM FX), hedging is expensive and the dealer should rely more heavily on quote skewing to attract the offsetting flow, tolerating larger inventory for longer. These qualitative prescriptions are consistent with standard market-making practice, and the {cite:t}`barzykin2023skewhedge` framework provides the quantitative ratios.

(sec:oh_derivatives)=
## Hedging Derivatives

The hedging of derivative positions presents qualitatively different challenges from flow hedging. A bond or FX position has a linear sensitivity to the underlying: the P&L is $q \Delta S$ and the hedge is a fixed notional in a correlated instrument. An option position has a sensitivity that changes continuously as the underlying moves, requiring the hedge to be adjusted dynamically. Moreover, the sensitivity depends not only on the current price of the underlying but also on time to expiry and on the level of volatility — inputs that are themselves uncertain and path-dependent.

(sec:oh_bsm)=
### Dynamic Hedging in the Black-Scholes Framework

The BSM theory ({ref}`fair_price_estimation`) establishes that a European option can be replicated by holding $\Delta_t = \partial C/\partial S$ units of the underlying and a corresponding cash position. As long as this position is rebalanced continuously and there are no transaction costs, the replicating portfolio earns the risk-free rate — the option is fully hedged. In practice, both conditions fail. Rebalancing is discrete, and every transaction incurs a bid-ask spread.

**The gamma-theta P&L identity.** The P&L of a delta-hedged option position over an infinitesimal interval $dt$ is:

$$d\text{PnL}^{\text{hedge}} = \underbrace{\frac{1}{2}\Gamma_t S_t^2 \sigma_R^2\,dt}_{\text{gamma earned}} - \underbrace{\frac{1}{2}\Gamma_t S_t^2 \sigma_I^2\,dt}_{\text{theta paid}}$$

where $\sigma_R$ is the **realised volatility** of the underlying and $\sigma_I$ is the **implied volatility** at which the option was purchased. This identity is the fundamental result of delta-hedging theory: a long option position (positive $\Gamma$) earns money when realized vol exceeds implied, and loses money otherwise. The dealer who buys an option and delta-hedges it is essentially taking a long position in realized variance $\sigma_R^2$ and short a fixed notional of implied variance $\sigma_I^2$. The net P&L over the life of the option is:

$$\text{PnL}_T^{\text{hedge}} = \frac{1}{2}\int_0^T \Gamma_t S_t^2 (\sigma_{R,t}^2 - \sigma_I^2)\,dt$$

**Discrete hedging error.** When the hedge is rebalanced at discrete intervals $\delta t$, the position is only delta-neutral at the rebalancing times and drifts in between. The hedging error per step arises from the second-order term in the Itô expansion:

$$\epsilon_t = -\frac{1}{2}\Gamma_t S_t^2 \sigma^2 \,\delta t \cdot (\xi_t^2 - 1), \qquad \xi_t = \frac{W_{t+\delta t} - W_t}{\sqrt{\delta t}} \sim \mathcal{N}(0,1)$$

The mean hedging error per step is zero (since $\mathbb{E}[\xi^2] = 1$), but the variance is:

$$\text{Var}(\epsilon_t) = \frac{1}{2}(\Gamma_t S_t^2 \sigma^2 \delta t)^2$$

The total hedging error variance over $T/\delta t$ steps scales as $(\Gamma S^2 \sigma^2)^2 \cdot T \cdot \delta t / 2$: hedging more frequently (smaller $\delta t$) reduces the variance quadratically. However, each rebalancing incurs a transaction cost, creating an explicit tradeoff.

**Transaction costs: the Leland adjustment.** {cite:t}`leland1985option` showed that in the presence of proportional transaction costs $c$ per unit of stock traded, BSM pricing still applies but with an effective volatility:

$$\tilde{\sigma}^2 = \sigma^2\left(1 + \text{sign}(\Gamma)\cdot\frac{c}{\sigma}\sqrt{\frac{2}{\pi\,\delta t}}\right)$$

For a dealer who sells an option (short $\Gamma$), the effective volatility is lower, reducing the replication cost. For a buyer of the option (long $\Gamma$), the effective volatility is higher — the option costs more to replicate because every rebalancing incurs a cost. The Leland adjustment provides a simple rule of thumb: multiply the transaction cost by $\sqrt{1/\delta t}$ to convert from per-trade cost to the annual cost embedded in the option price.

**The Whalley-Wilmott no-trade band.** {cite:t}`whalley1997optimal` extended Leland's result to the optimal rebalancing frequency. Rather than rebalancing at fixed intervals, they showed that the cost-minimizing strategy is to rebalance only when the current delta deviates from the Black-Scholes delta by more than a threshold $H_t$:

$$H_t = \left(\frac{3c}{2\gamma}\Gamma_t^2 S_t^2\right)^{1/3}$$

where $\gamma$ is the dealer's risk aversion. This **no-trade band** of width $2H_t$ around the BSM delta is wider when transaction costs $c$ are high, when the option is near expiry (when $\Gamma$ is large and the position moves quickly), and when risk aversion $\gamma$ is low. The intuition is that the dealer tolerates a larger deviation from the perfect hedge when the cost of closing the deviation exceeds the risk reduction achieved. {numref}`fig:hedg_delta_hedging` illustrates the P&L distribution under BSM delta hedging and the Whalley-Wilmott band for a European call option.

```{figure} figures/hedg_delta_hedging.png
:name: fig:hedg_delta_hedging
:width: 9in
Left: simulated P&L distribution for a short call position delta-hedged at different rebalancing frequencies (daily, weekly, monthly) and under the Whalley-Wilmott band policy (transaction cost $c = 0.1\%$). Daily hedging provides the tightest distribution but highest total transaction costs. Right: gamma-theta P&L decomposition over a simulated path; the realized variance exceeds implied in this scenario, resulting in a positive net P&L for the option seller.
```

**Greeks management in practice.** In a large derivatives book, the dealer does not hedge each option individually; she manages the aggregate **Greeks** of the book: net delta $\Delta_{\text{book}}$, net gamma $\Gamma_{\text{book}}$, net vega $\mathcal{V}_{\text{book}}$, and net theta $\Theta_{\text{book}}$. The delta is hedged by trading the underlying; vega is hedged by trading other options; gamma is harder to hedge cheaply (since liquid gamma-producing instruments are themselves options with their own bid-ask spreads). In a market-making context, the Greeks of each new trade are assessed relative to the existing book: a trade that reduces book gamma is valued at a tighter spread, while one that adds gamma is priced wider.

(sec:oh_ml)=
### Accelerating Hedge Computations with Machine Learning

A derivatives book with thousands of positions requires computing Greeks for each instrument, across all risk scenarios used in risk management and for each potential new trade. Even with analytical formulas (such as BSM), this scales as $O(N \cdot M)$ where $N$ is the number of instruments and $M$ is the number of scenarios. For exotic options or complex structured products where no analytical formula exists, the computation relies on Monte Carlo simulation, which is orders of magnitude slower.

Machine learning surrogates — functions learned from a training set of $(x, C(x))$ pairs, where $x$ represents the state variables (spot, strike, maturity, vol, rate) and $C(x)$ is the option price — offer a way to amortize the computational cost. Once trained, the surrogate can be evaluated in microseconds rather than milliseconds, and its derivative with respect to any input is obtained by automatic differentiation at negligible additional cost.

**Monotonicity constraints.** The key challenge for pricing surrogates is preserving **no-arbitrage monotonicity**: a call price must be non-increasing in strike $K$ (for fixed other parameters), non-decreasing in spot $S$, non-decreasing in volatility $\sigma$, and non-decreasing in time to maturity $T$ (for vanilla options without discrete cash flows). A standard neural network violates these constraints in regions of the input space where training data are sparse, producing negative deltas or decreasing prices as volatility rises — outputs that would imply arbitrage in the option book.

As discussed in {ref}`sec:ddm_monotone`, **monotone neural networks** enforce these constraints at the architectural level by restricting weight matrices to be element-wise non-negative for the inputs that require monotone behavior, combined with a non-decreasing activation function. The practical approach for option pricing:

1. Train a monotone network $\hat{C}_\theta(S, K, T, \sigma, r)$ on a grid of BSM prices (or on implied vol surface fits to market data)
2. Compute the delta via automatic differentiation: $\hat{\Delta} = \partial\hat{C}_\theta/\partial S$
3. Similarly obtain $\hat{\Gamma}$, $\hat{\mathcal{V}}$, $\hat{\Theta}$, and $\hat{\rho}$

The monotone constraint guarantees $\hat{\Delta} \in [0, 1]$ for calls, $\hat{\Delta} \in [-1, 0]$ for puts, and $\hat{\mathcal{V}} \geq 0$ everywhere — even far from the training distribution. This makes the surrogate safe for deployment in a live hedging system where out-of-sample inputs arise during stressed market conditions.

**Speed gains.** For a typical vanilla option portfolio with $N = 10{,}000$ positions evaluated across $M = 1{,}000$ market scenarios, a batched GPU evaluation of the neural network surrogate achieves speedups of $100\times$ to $1{,}000\times$ compared to individual BSM formula evaluations. For exotic options previously computed by Monte Carlo, the speedup can be much larger. The improved speed allows risk systems to run intraday or even in real-time, enabling faster hedging decisions.

**Local volatility and stochastic volatility surrogates.** Beyond BSM, surrogates are particularly valuable for models with no closed-form Greeks: local volatility models (where the vol surface is fitted to match all market prices), SABR, Heston, and rough volatility models. The training data is generated from calibrated model simulations, and the surrogate is trained to replicate the numerical Greeks across the full parameter space. The monotone architecture ensures the surrogate remains arbitrage-free in the interpolation and mild extrapolation regions.

(sec:oh_deep)=
### Deep Hedging

The preceding sections extend the BSM framework to accommodate transaction costs, discrete rebalancing, and computational speed. They remain, however, model-based: the hedge ratio is derived from a parametric price dynamics model. **Deep hedging** {cite:p}`buehler2019deep` takes a fundamentally different approach: it frames hedging as a learning problem and optimises the hedging strategy directly, without specifying a model for the underlying dynamics.

**Framework.** Consider a derivative with payoff $H_T$ at maturity $T$. A hedging strategy is a sequence of positions $\boldsymbol{\delta} = (\boldsymbol{\delta}_0, \boldsymbol{\delta}_1, \ldots, \boldsymbol{\delta}_{T-1})$ in a set of liquid hedging instruments $\mathbf{S} = (S^1, \ldots, S^d)$, where $\boldsymbol{\delta}_t \in \mathbb{R}^d$ is the vector of positions held between time steps $t$ and $t+1$. The hedged P&L at maturity is:

$$Z^{\boldsymbol{\delta}} = H_T + \sum_{t=0}^{T-1} \boldsymbol{\delta}_t^T(\mathbf{S}_{t+1} - \mathbf{S}_t) - \sum_{t=0}^{T-1} C_{t+1}(\boldsymbol{\delta}_t, \boldsymbol{\delta}_{t+1})$$

where $C_{t+1}(\boldsymbol{\delta}_t, \boldsymbol{\delta}_{t+1}) = \sum_i c_i |(\delta_{t+1}^i - \delta_t^i)| S_{t+1}^i$ captures the proportional transaction costs of rebalancing. The first term is the option payoff; the second is the gain from the hedging positions; the third is the transaction cost of all rebalancing transactions.

**Objective.** The dealer minimises a **convex risk measure** $\rho$ of the (negated) hedged P&L:

$$\min_{\boldsymbol{\delta}} \rho(-Z^{\boldsymbol{\delta}})$$

Common choices of $\rho$ and their implications:
- **Variance**: $\rho(-Z) = -\mathbb{E}[Z] + \frac{\lambda}{2}\text{Var}(Z)$. Under zero transaction costs, the variance-minimising strategy recovers the BSM delta — deep hedging is a strict generalization.
- **CVaR at level $\alpha$**: $\rho(-Z) = \text{CVaR}_\alpha(-Z) = \mathbb{E}[-Z \mid -Z \geq \text{VaR}_\alpha(-Z)]$. This focuses optimisation on the worst-$\alpha$ fraction of scenarios, producing a strategy that is robust to tail events at the expense of slightly worse median performance.
- **Entropic risk measure**: $\rho(-Z) = \frac{1}{\gamma}\log\mathbb{E}[e^{-\gamma Z}]$. For small $\gamma$ this approximates variance; for large $\gamma$ it becomes highly sensitive to tail losses.

**Neural network parameterisation.** The hedging policy $\boldsymbol{\delta}_t = \pi_\theta(I_t)$ maps an information state $I_t$ to hedge ratios. The information state includes the current price $\mathbf{S}_t$, the previous position $\boldsymbol{\delta}_{t-1}$ (needed to compute transaction costs), the time to expiry $(T-t)/T$, and any auxiliary features such as a volatility estimate or realised variance. A feedforward MLP or, for long horizons, an LSTM reads this state and outputs the hedge ratios.

Training proceeds by simulation:

1. **Generate paths**: simulate $M$ market scenarios $(\mathbf{S}_0^{(m)}, \ldots, \mathbf{S}_T^{(m)})$. These can come from a parametric model (GBM, Heston) for benchmarking, or from historical returns for a model-free approach.
2. **Roll out policy**: for each scenario, compute the strategy $\boldsymbol{\delta}_t^{(m)} = \pi_\theta(I_t^{(m)})$ and the hedged P&L $Z^{(m)}$.
3. **Compute risk measure**: evaluate $\rho$ across the $M$ scenarios.
4. **Gradient step**: compute $\nabla_\theta \rho$ via backpropagation through the rollout, and update $\theta$.

The gradient of a CVaR is estimated by identifying which scenarios fall in the tail and averaging the gradient over them — a standard technique in differentiable risk optimisation.

**Convergence to BSM.** Under GBM dynamics for the underlying, variance risk measure, and no transaction costs:

$$\pi_\theta(I_t) \xrightarrow{\text{training}} \Delta_t^{\text{BSM}} = N(d_1(S_t, K, T-t, \sigma, r))$$

where $N(d_1)$ is the BSM delta. This is both a theoretical validation — deep hedging recovers the known optimum in the classical setting — and a practical benchmark: on real data, any improvement over the BSM delta reflects genuine additional value from the machine learning component.

**Transaction costs and the no-trade band.** When transaction costs are nonzero, the optimal deep hedging policy learns a no-trade band analogous to the Whalley-Wilmott result: the policy does not trade when the current position is close to the BSM delta, and trades to bring the position back toward the delta only when the deviation becomes large. The width of the band is not imposed by the model but emerges from the optimisation — and it can adapt to the option's gamma profile, the current volatility regime, and the remaining time to expiry in a way that the fixed analytical formula cannot. {numref}`fig:hedg_deep_hedging` compares the P&L distributions and training dynamics.

```{figure} figures/hedg_deep_hedging.png
:name: fig:hedg_deep_hedging
:width: 9in
Left: P&L distribution of deep hedging versus BSM delta hedging for a short call option with proportional transaction costs ($c=0.1\%$, daily rebalancing, GBM underlying). Deep hedging achieves lower CVaR (0.95) by reducing rebalancing frequency. Centre: training curve — CVaR loss as a function of training epoch. Right: average hedge ratio as a function of moneyness, comparing the learned policy (solid) with the BSM delta (dashed); the deep hedging policy de-leverages slightly in-the-money (where $\Gamma$ is large and transaction costs are expensive to cover).
```

**Model-free hedging on historical data.** The most distinctive application is training the policy directly on historical market data rather than on simulated paths. In this setting, the resulting strategy captures empirical features of market dynamics — stochastic volatility clustering, jumps, liquidity effects — that no single parametric model fully reproduces. The key technical challenge is the small effective sample size: financial time series are short relative to the number of paths needed to train a reliable policy. Techniques such as data augmentation (generating synthetic paths that preserve statistical properties), bootstrapping, and variance reduction via control variates (e.g., using the BSM delta as a baseline surrogate) are used to improve sample efficiency.

**Limitations and open problems.** Deep hedging is powerful but not without limitations. The learned policy is specific to the market environment in which it was trained — a strategy optimised on low-volatility equity data may perform poorly during a vol spike. The choice of risk measure has a large impact on the hedging style, and the "right" risk measure for a given book depends on the dealer's capital structure and regulatory constraints. Finally, the computational and data requirements for training deep hedging models are substantially higher than for BSM Greeks computation, which constrains their practical use to the largest derivatives operations. Active research focuses on improving the sample efficiency, interpretability, and robustness of deep hedging policies.

## Exercises

1. Show that the minimum variance hedge ratio $\mathbf{h}^* = q\boldsymbol{\Sigma}_{HH}^{-1}\boldsymbol{\sigma}_{XH}$ can be derived equivalently by projecting $\Delta X$ onto the span of $\Delta\mathbf{H}$ in $L^2(\Omega)$ (the space of square-integrable random variables with inner product $\langle U, V \rangle = \text{Cov}(U, V)$). What does this projection interpretation say about basis risk?

2. A dealer holds a position in a 7-year bond and wants to hedge using 2-year and 10-year benchmark bonds. The DV01 vectors (sensitivities to yield changes at each maturity) and the PCA factors for the yield curve are given. Derive the hedge ratios that neutralise the first two PCA factors, and compare the resulting residual variance with the DV01-matched hedge.

3. Prove that the Lasso hedge path for the problem $\min_\mathbf{h} \frac{1}{2}\mathbf{h}^T\boldsymbol{\Sigma}_{HH}\mathbf{h} - q\mathbf{h}^T\boldsymbol{\sigma}_{XH} + \lambda\|\mathbf{h}\|_1$ is equivalent to the standard Lasso regression with design matrix $\boldsymbol{\Sigma}_{HH}^{1/2}$ and response $q\boldsymbol{\Sigma}_{HH}^{-1/2}\boldsymbol{\sigma}_{XH}$. What regularisation path algorithm applies?

4. Consider a dealer who delta-hedges a short call option with daily rebalancing. The option has $\Gamma = 0.05$, the underlying has $S = 100$, $\sigma = 20\%$. (a) Compute the standard deviation of the daily hedging error. (b) If transaction costs are $c = 0.1\%$ of the amount traded, compute the Whalley-Wilmott no-trade band width $H_t$ for $\gamma = 0.01$. (c) Discuss qualitatively how the band width evolves as the option approaches expiry.

5. In the deep hedging framework with variance risk measure and no transaction costs, show that the optimal policy $\pi^*_t(I_t) = N(d_1(S_t))$ (BSM delta) achieves the global minimum of the variance objective. *(Hint: use the fact that the BSM replicating portfolio achieves $Z^{\boldsymbol{\delta}} = 0$ almost surely under GBM dynamics.)*

6. Consider the skew-versus-hedge problem ({ref}`sec:oh_skewhedge`) with a single instrument and symmetric arrival rates. Show that the no-trade band threshold $q^*$ from {cite:t}`barzykin2023skewhedge` increases linearly in $c$ (the unit hedging cost) and decreases as $A^{-1/2}$ (the inverse square root of the order arrival rate). Explain the economic intuition behind each dependence.
