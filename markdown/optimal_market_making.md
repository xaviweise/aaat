(optimal_market_making)=
# Optimal Market Making

## Introduction

The market-making problem asks: given that you commit to quote firm bid and ask prices, how should those prices depend on your current inventory, the asset's price dynamics, the arrival rate and price-sensitivity of client orders, your risk preferences, and the liquidity cost of closing your position? Chapter {ref}`market_making_fundamentals` introduced the economic intuitions qualitatively. This chapter provides the mathematical answers.

We proceed in four stages. We begin with the **classic market-microstructure models** ({ref}`sec:omm_classic`) — Grossman-Miller {cite:p}`grossman1988liquidity` and Glosten-Milgrom {cite:p}`glosten1985bid` — and derive their key results in full, treating them as static equilibrium benchmarks that characterize inventory risk and information-asymmetry spreads respectively. We then move to the **single-trade model** ({ref}`sec:omm_single`): a dealer receives one RfQ, quotes a spread, and — if she wins — must liquidate the resulting inventory by end of day at market. This minimal dynamic problem captures all three spread components (static trade uncertainty, inventory risk, liquidity cost) in a single closed-form expression and extends cleanly to the multi-asset case via the covariance matrix of instrument prices.

The **Avellaneda-Stoikov (AS) framework** ({ref}`sec:omm_as`) generalises to a continuous stream of orders: the dealer posts live bid and ask prices that attract arrivals from a Poisson process with exponentially decreasing intensity. We derive the Hamilton–Jacobi–Bellman (HJB) equation in the general multi-asset setting, reducing the optimisation to a system of nonlinear ODEs for a scalar indifference function $u(t, \mathbf{q})$, and show how the optimal quotes depend on the first- and second-order discrete derivatives of $u$ with respect to inventory. Section {ref}`sec:omm_asym` then develops the **Guéant-Lehalle-Fernández-Tapia (GLF) infinite-horizon approximation** {cite:p}`gueant2012dealing`, which linearises the system and yields closed-form expressions for the optimal spread and inventory-skew, making the parameter dependences explicit.

Section {ref}`sec:omm_apps` discusses the application of the AS framework to both limit order books (the original context) and RfQ dealer markets. Finally, section {ref}`sec:omm_enrich` collects four extensions that enrich the baseline model: a **liquidity penalty** that closes the loop with the single-trade model; **Ornstein-Uhlenbeck mid-price dynamics** that incorporate relative-value beliefs; **asymmetric order flow** (flow imbalance); and **client segmentation** as treated in the D2C context of chapter {ref}`rfq_models`.

Mathematical prerequisites are the stochastic calculus of chapter {ref}`stochastic_calculus` (Itô's lemma, Poisson processes) and the stochastic optimal control tools of chapter {ref}`stochastic_optimal_control` (HJB equations, value functions).

(sec:omm_classic)=
## Classic market-making models

### Grossman-Miller: inventory risk

The model of {cite:t}`grossman1988liquidity` isolates inventory risk in a stylised three-period setting. There are $n$ identical market makers (MMs) and two waves of liquidity traders. At $t = 1$, a liquidity trader LT$_1$ needs to sell $i > 0$ units immediately. At $t = 2$, a second liquidity trader LT$_2$ needs to buy the same $i$ units. Time $t = 3$ is the terminal date at which all agents liquidate. MMs start at $t = 1$ with cash $W_0$ and zero inventory. The asset price follows

$$S_1 = \bar{S}, \qquad S_3 = S_2 + \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, \sigma^2)$$

where $S_2$ is to be determined in equilibrium, and $\varepsilon$ is unknown at $t = 1$. All agents have exponential (CARA) utility $U(W) = -e^{-\gamma W}$ with risk-aversion coefficient $\gamma > 0$.

**Equilibrium at $t = 2$.** When LT$_2$ arrives at $t = 2$, each MM holds $i/n$ units purchased at $t = 1$. Each MM's terminal wealth if she sells all her inventory at $S_2$ is deterministic: $W_0 + (S_2 - S_1) \cdot i/n$. If, instead, some inventory were carried to $t = 3$ at the risky price $S_3$, the MM would demand a risk premium. In competitive equilibrium with symmetric MMs, LT$_2$ absorbs the full supply $i$ at price $S_2 = S_1$ — MMs sell at the same price they bought, earning zero on the round trip {cite:p}`grossman1988liquidity`.

**Equilibrium at $t = 1$.** The MMs anticipate selling at $S_2 = S_1$ at $t = 2$, but $S_1$ itself is the quantity to be determined. Each MM purchases $q = i/n$ units at price $S_1 = p_{\mathrm{bid}}$. Her wealth at $t = 3$ if she unwinds at $t = 2$ is:

$$W = W_0 + (S_2 - p_{\mathrm{bid}}) \cdot q$$

Since $S_2$ is uncertain from the $t=1$ perspective (it depends on the new information arriving between $t = 1$ and $t = 2$, modelled as $S_2 = \bar{S} + \eta$ with $\eta \sim \mathcal{N}(0, \sigma^2)$), the MM faces price risk over the holding period. For CARA utility, the certainty equivalent of a normally distributed payoff $X \sim \mathcal{N}(\mu, \sigma^2)$ is

$$\mathrm{CE}[X] = \mu - \frac{\gamma}{2}\sigma^2$$

The MM's certainty equivalent of buying $q = i/n$ units at $p_{\mathrm{bid}}$ and selling them at the risky $S_2$ is:

$$\mathrm{CE}[W] = W_0 + \bigl(\bar{S} - p_{\mathrm{bid}}\bigr) \cdot \frac{i}{n} - \frac{\gamma}{2}\sigma^2 \cdot \left(\frac{i}{n}\right)^2$$

For the MM to be willing to absorb LT$_1$'s sale — i.e., $\mathrm{CE}[W] \geq W_0$ — the bid price must satisfy

$$p_{\mathrm{bid}} \leq \bar{S} - \frac{\gamma\sigma^2 \cdot (i/n)}{1} = \bar{S} - \frac{i\gamma\sigma^2}{n}$$

In competitive equilibrium, the bid is as large as possible consistent with MM participation, giving the **Grossman-Miller spread**:

$$\boxed{p_{\mathrm{bid}} = \bar{S} - \frac{i\,\gamma\,\sigma^2}{n}, \qquad \text{spread}_{\mathrm{GM}} = 2\,\frac{i\,\gamma\,\sigma^2}{n}}$$

The spread compensates the $n$ MMs collectively for bearing inventory risk on $i$ units for one period. It increases with volatility $\sigma^2$, trade size $i$, and risk aversion $\gamma$, and decreases with the number of competing MMs $n$ — compression to zero as $n \to \infty$ reflects perfect competition eliminating rents. Chapter {ref}`market_making_fundamentals` ({ref}`sec:mm_risks`) presents the economic interpretation; the notebook `notebooks/market_making.ipynb` illustrates the parameter sensitivities.

### Glosten-Milgrom: information asymmetry

The model of {cite:t}`glosten1985bid` isolates adverse selection. A single competitive MM quotes firm bid $b$ and ask $a$. The asset has a binary future value $v$:

$$v = V_H \text{ with probability } p, \qquad v = V_L \text{ with probability } 1-p, \quad V_H > V_L$$

with prior mean $\mu = p V_H + (1-p) V_L$. A fraction $\alpha \in [0,1]$ of all counterparties are **informed traders** who know $v$; the remaining fraction $1-\alpha$ are **uninformed liquidity traders** who buy or sell with probability $\frac{1}{2}$ each, regardless of prices. Informed traders act optimally: they buy if $v = V_H > a$, sell if $v = V_L < b$, and do nothing otherwise.

**Zero-profit ask.** By Bayes' theorem, the probability the counterparty is informed conditional on a buy order is:

$$P(\text{informed} \mid \text{buy}) = \frac{\alpha p}{\alpha p + (1-\alpha)/2}$$

The MM's expected profit on a buy is:

$$\mathbb{E}[\pi \mid \text{buy}] = a - \mathbb{E}[v \mid \text{buy}]$$

$$\mathbb{E}[v \mid \text{buy}] = \frac{\alpha p\, V_H + (1-\alpha)/2\, \cdot \mu}{\alpha p + (1-\alpha)/2}$$

Setting $\mathbb{E}[\pi \mid \text{buy}] = 0$ gives the zero-profit ask. Analogously for the bid. For the symmetric case $p = \frac{1}{2}$, so $\mu = \frac{V_H + V_L}{2}$ and both informed buy/sell flows are equally likely, the expressions simplify:

$$\mathbb{E}[v \mid \text{buy}] = \frac{\alpha/2 \cdot V_H + (1-\alpha)/2 \cdot \mu}{\alpha/2 + (1-\alpha)/2} = \alpha V_H + (1-\alpha)\mu = \mu + \alpha(V_H - \mu)$$

The **Glosten-Milgrom quotes** in the symmetric case are therefore:

$$\boxed{a = \mu + \alpha(V_H - \mu), \qquad b = \mu - \alpha(\mu - V_L), \qquad \text{spread}_{\mathrm{GL}} = \alpha(V_H - V_L)}$$

The spread is strictly proportional to $\alpha$ — the fraction of informed flow — and to the magnitude of the informational asymmetry $V_H - V_L$. With $\alpha = 0$ (no informed traders), competitive pressure eliminates the spread entirely. As $\alpha \to 1$, the ask approaches $V_H$ and the bid approaches $V_L$: the MM refuses to quote inside the full range of possible values because any trade would be a loss.

In the general asymmetric case ($p \neq \frac{1}{2}$), the ask and bid shift asymmetrically around $\mu$, but the qualitative message is identical: the spread compensates the MM for the expected loss on informed trades, funded by the expected gain on uninformed trades.

(sec:omm_single)=
## The single-trade model

Before tackling the full dynamic AS framework, we study the simplest non-trivial problem: a dealer receives one RfQ, quotes a half-spread $\delta$, and — if she wins — must unwind the resulting inventory by the end of the day $T$. This model connects directly to chapter {ref}`rfq_models` but adds the explicit inventory liquidation and its market-impact cost.

### Setup

The dealer holds an existing multi-asset inventory $\mathbf{q}_0 \in \mathbb{R}^d$ at time $t_0$. A client sends an RfQ for instrument $i$ of size $\bar{q}$ (e.g. a buy RfQ: the client wishes to buy $\bar{q}$ units). The multi-asset mid-price vector $\mathbf{S}_{t_0} = \mathbf{s}_0$ evolves as

$$d\mathbf{S}_t = \boldsymbol{\Sigma}\, d\mathbf{W}_t$$

where $\boldsymbol{\Sigma} \in \mathbb{R}^{d \times d}$ and $\mathbf{W}_t$ is a $d$-dimensional Brownian motion, so $\mathbf{S}_T - \mathbf{s}_0 \sim \mathcal{N}(\mathbf{0},\, \boldsymbol{\Gamma}(T-t_0))$ with covariance matrix $\boldsymbol{\Gamma} = \boldsymbol{\Sigma}\boldsymbol{\Sigma}^T \in \mathbb{R}^{d\times d}$.

If the dealer wins the RfQ with half-spread $\delta^i$ (she sells $\bar{q}$ units at $s_0^i + \delta^i$), her new inventory is $\mathbf{q}_1 = \mathbf{q}_0 - \bar{q}\,\mathbf{e}_i$. She then liquidates $\mathbf{q}_1$ by time $T$ at market, incurring a liquidity cost $\ell(\mathbf{q}_1)$ to account for the bid-offer spread and market impact of closing a position of that size. The client's RfQ hit probability is $f(\delta^i) = e^{-k\delta^i}$ (exponential demand, as in chapter {ref}`rfq_models`).

### Optimal spread

The dealer's terminal wealth if she wins is:

$$W_T^{\mathrm{hit}} = \bar{q}(s_0^i + \delta^i) - \bar{q}\,S_T^i + \mathbf{q}_1 \cdot \mathbf{S}_T - \ell(\mathbf{q}_1)$$

The first two terms represent the transaction: she sells at $s_0^i + \delta^i$ and eventually buys back at $S_T^i$ (which equals $s_0^i$ plus the Brownian increment). The third term is the mark-to-market of the residual position. Rearranging:

$$W_T^{\mathrm{hit}} = \bar{q}\,\delta^i + \mathbf{q}_0\cdot\mathbf{s}_0 + \mathbf{q}_1\cdot(\mathbf{S}_T - \mathbf{s}_0) - \ell(\mathbf{q}_1)$$

where $\mathbf{q}_1 \cdot (\mathbf{S}_T - \mathbf{s}_0) \sim \mathcal{N}(0,\, \tau\, \mathbf{q}_1^T \boldsymbol{\Gamma}\mathbf{q}_1)$ with $\tau = T - t_0$. Under CARA utility, the certainty equivalent is:

$$\mathrm{CE}[W_T^{\mathrm{hit}}] = \bar{q}\,\delta^i + \mathbf{q}_0\cdot\mathbf{s}_0 - \ell(\mathbf{q}_1) - \frac{\gamma\tau}{2}\,\mathbf{q}_1^T\boldsymbol{\Gamma}\mathbf{q}_1$$

The incremental gain from hitting the RfQ relative to not hitting (keeping inventory $\mathbf{q}_0$) is:

$$\Delta\mathrm{CE} = \bar{q}\,\delta^i - \underbrace{\bigl[\ell(\mathbf{q}_1) - \ell(\mathbf{q}_0)\bigr]}_{\Delta\ell} - \frac{\gamma\tau}{2}\underbrace{\bigl[\mathbf{q}_1^T\boldsymbol{\Gamma}\mathbf{q}_1 - \mathbf{q}_0^T\boldsymbol{\Gamma}\mathbf{q}_0\bigr]}_{\Delta(\mathbf{q}^T\boldsymbol{\Gamma}\mathbf{q})}$$

Expanding the quadratic difference $\Delta(\mathbf{q}^T\boldsymbol{\Gamma}\mathbf{q})$ with $\mathbf{q}_1 = \mathbf{q}_0 - \bar{q}\mathbf{e}_i$:

$$\Delta(\mathbf{q}^T\boldsymbol{\Gamma}\mathbf{q}) = -2\bar{q}\,(\boldsymbol{\Gamma}\mathbf{q}_0)_i + \bar{q}^2\,\Gamma_{ii}$$

The dealer maximises expected utility: $\max_{\delta^i} f(\delta^i)\,\Delta\mathrm{CE}$. With $f = e^{-k\delta^i}$, the first-order condition gives $\bar{q} = k\,\Delta\mathrm{CE}$, or equivalently:

$$\boxed{\delta^{i*} = \underbrace{\frac{1}{k}}_{\text{static}} + \underbrace{\frac{\Delta\ell}{\bar{q}}}_{\text{liquidity}} - \underbrace{\frac{\gamma\tau(\boldsymbol{\Gamma}\mathbf{q}_0)_i}{\bar{q}}}_{\text{cross-hedge skew}} + \underbrace{\frac{\gamma\tau\,\Gamma_{ii}}{2}\,\bar{q}}_{\text{new risk}}}$$

The third term carries a minus sign: when the existing inventory is positively correlated with instrument $i$ — meaning the new trade would add to risk — the cross-hedge term is positive and widens the spread; when the new trade reduces book risk it is negative, lowering the spread. This follows directly from the FOC $\bar{q} = k\,\Delta\mathrm{CE}$:

$$\delta^{i*} = \frac{1}{k} + \frac{\Delta\ell}{\bar{q}} - \frac{\gamma\tau(\boldsymbol{\Gamma}\mathbf{q}_0)_i}{\bar{q}} + \frac{\gamma\tau\,\Gamma_{ii}}{2}\,\bar{q}$$

The four components have natural interpretations:

1. **Static uncertainty** ($1/k$): even with zero price risk, the dealer incurs an option cost from the trade decision. The inverse of the demand elasticity $k$ is the unit spread needed to achieve the optimal trade frequency. This term is independent of risk or liquidity costs.

2. **Liquidity cost** ($\Delta\ell / \bar{q}$): the per-unit cost of closing the new inventory $\mathbf{q}_1$ at market, over and above the cost of closing the existing inventory $\mathbf{q}_0$. For linear spread costs $\ell(\mathbf{q}) = \sum_j \ell_j |q_j|$, this becomes $\pm\ell_i$ per unit (adding to the position adds cost; reducing it may save cost).

3. **Cross-hedging skew** ($-\gamma\tau(\boldsymbol{\Gamma}\mathbf{q}_0)_i / \bar{q}$): if the existing inventory $\mathbf{q}_0$ is positively correlated with instrument $i$ (and the new trade increases this exposure), the dealer demands a wider spread to compensate for incremental risk. If the new trade is a natural hedge against existing inventory, the spread narrows — the dealer offers a better price to reduce her book risk. This is the mathematical foundation for the inventory skew discussed qualitatively in chapter {ref}`market_making_fundamentals`.

4. **New-position risk** ($\gamma\tau\,\Gamma_{ii}\,\bar{q}/2$): the pure inventory risk premium from holding $\bar{q}$ units of instrument $i$ for the remaining horizon $\tau$, proportional to the instrument's variance $\Gamma_{ii}$, trade size $\bar{q}$, and the dealer's risk aversion $\gamma$.

**Single-asset specialisation.** For $d = 1$, $\mathbf{q}_0 = q_0$, $\Gamma_{11} = \sigma^2$:

$$\delta^* = \frac{1}{k} + \frac{\Delta\ell}{\bar{q}} - \gamma\tau\sigma^2\,\frac{q_0}{\bar{q}} + \frac{\gamma\tau\sigma^2}{2}\,\bar{q}$$

When $q_0 = 0$ (clean book), the formula reduces to the three-term result previewed in section {ref}`sec:omm_classic` and consistent with case 2 of the RfQ pricing formula in chapter {ref}`rfq_models`. The $q_0$-dependent skew term is the new ingredient: it shifts the entire quoted half-spread by $-\gamma\tau\sigma^2 q_0 / \bar{q}$, so a long existing inventory reduces the optimal half-spread on a sell-side RfQ (the dealer is willing to sell more cheaply to rebalance the book).

(sec:omm_as)=
## Beyond a single trade: the Avellaneda-Stoikov framework

The single-trade model fixes the quoting problem to a single event. In practice, a market maker faces a continuous stream of RfQs or limit-order-book arrivals, and her inventory $\mathbf{q}_t$ changes continuously. The Avellaneda-Stoikov framework {cite:p}`AvellanedaStoikov2008`, extended by {cite:t}`gueant2012dealing`, provides the dynamic stochastic control solution to this problem.

### Model setup

We work in the general $d$-asset setting. The state at time $t$ is the triple $(\mathbf{q}_t, \mathbf{S}_t, X_t)$ where $\mathbf{q}_t \in \mathbb{R}^d$ is the inventory vector, $\mathbf{S}_t \in \mathbb{R}^d$ is the mid-price vector, and $X_t \in \mathbb{R}$ is cash. The mid-price dynamics follow:

$$d\mathbf{S}_t = \boldsymbol{\Sigma}\, d\mathbf{W}_t, \qquad \boldsymbol{\Gamma} = \boldsymbol{\Sigma}\boldsymbol{\Sigma}^T$$

For each instrument $i = 1, \ldots, d$, the market maker posts a bid half-spread $\delta^{b,i}_t \geq 0$ and an ask half-spread $\delta^{a,i}_t \geq 0$:

$$p^{b,i}_t = S^i_t - \delta^{b,i}_t \quad \text{(bid)}, \qquad p^{a,i}_t = S^i_t + \delta^{a,i}_t \quad \text{(ask)}$$

Client orders arrive as independent Poisson processes $N^{b,i}_t$ (buy orders for instrument $i$, executed against the ask) and $N^{a,i}_t$ (sell orders, executed against the bid) with intensities:

$$\lambda^{b,i}(\delta^{b,i}) = A\,e^{-k\delta^{b,i}}, \qquad \lambda^{a,i}(\delta^{a,i}) = A\,e^{-k\delta^{a,i}}$$

The inventory and cash evolve according to:

$$dq^i_t = dN^{b,i}_t - dN^{a,i}_t$$

$$dX_t = \sum_{i=1}^{d}\Bigl[(S^i_t + \delta^{a,i}_t)\,dN^{b,i}_t - (S^i_t - \delta^{b,i}_t)\,dN^{a,i}_t\Bigr]$$

(Note: a client's buy order goes against the market maker's ask, adding to the MM's cash and reducing her inventory.)

### Objective and value function

The market maker maximises the expected CARA utility of terminal wealth including a quadratic inventory liquidation penalty $\ell(\mathbf{q}_T) = \frac{A_T}{2}\|\mathbf{q}_T\|^2$ (the cost of closing remaining inventory at market, generalising the single-trade penalty):

$$V(t, \mathbf{x}) = \sup_{\{\delta^{b,i}_s, \delta^{a,i}_s\}_{t \leq s \leq T}} \mathbb{E}\left[-e^{-\gamma\bigl(X_T + \mathbf{q}_T \cdot \mathbf{S}_T - \ell(\mathbf{q}_T)\bigr)}\right]$$

where $\mathbf{x} = (x, \mathbf{q}, \mathbf{s})$ collects the state variables. The terminal mark-to-market $X_T + \mathbf{q}_T\cdot\mathbf{S}_T$ is the total portfolio value; the penalty $\ell(\mathbf{q}_T)$ accounts for the cost of liquidating any remaining inventory.

### Ansatz and dimensionality reduction

The exponential utility and Gaussian mid-price dynamics suggest the **change-of-variable ansatz**:

$$V(t, x, \mathbf{q}, \mathbf{s}) = -e^{-\gamma\bigl(x + \mathbf{q}\cdot\mathbf{s} + u(t, \mathbf{q})\bigr)}$$

where $u(t, \mathbf{q})$ is a scalar function of time and inventory only — independent of cash $x$ (by the CARA structure) and of the mid-price $\mathbf{s}$ (because mid-price changes enter wealth only through $\mathbf{q}_T\cdot\mathbf{S}_T$, which is already accounted for in the $\mathbf{q}\cdot\mathbf{s}$ term of the ansatz). The function $u(t,\mathbf{q})$ is the **indifference value adjustment**: it measures how much the optimal pricing problem is worth relative to the mark-to-market of the current position.

The terminal condition on $u$ follows from $V(T, \cdot) = -e^{-\gamma(\cdot - \ell(\mathbf{q}))}$:

$$u(T, \mathbf{q}) = -\ell(\mathbf{q}) = -\frac{A_T}{2}\|\mathbf{q}\|^2$$

### The HJB equation

Substituting the ansatz into the HJB equation (see chapter {ref}`stochastic_optimal_control`, {ref}`sec:hjb`), the multi-asset diffusion term gives:

$$\frac{1}{2}\mathrm{tr}\bigl(\boldsymbol{\Sigma}\boldsymbol{\Sigma}^T \nabla^2_\mathbf{s} V\bigr) = V\cdot\frac{\gamma^2}{2}\,\mathbf{q}^T\boldsymbol{\Gamma}\mathbf{q}$$

For each instrument $i$, a bid arrival (buy order) transforms the state by $x \to x - (s^i - \delta^{b,i})$ and $q^i \to q^i + 1$, so the change in $V$ is:

$$V(t, x-(s^i-\delta^{b,i}), \mathbf{q}+\mathbf{e}_i, \mathbf{s}) = V \cdot e^{-\gamma\bigl(\delta^{b,i} + \Delta^+_i u\bigr)}$$

where $\Delta^+_i u = u(t, \mathbf{q}+\mathbf{e}_i) - u(t, \mathbf{q})$ is the forward finite difference of $u$ in dimension $i$. Analogously, an ask arrival (sell order) produces:

$$V(t, x+(s^i+\delta^{a,i}), \mathbf{q}-\mathbf{e}_i, \mathbf{s}) = V \cdot e^{-\gamma\bigl(\delta^{a,i} - \Delta^-_i u\bigr)}$$

where $\Delta^-_i u = u(t,\mathbf{q}) - u(t,\mathbf{q}-\mathbf{e}_i)$. Dividing the full HJB equation by $V$ (which is negative), the equation for $u$ is:

$$\partial_t u - \frac{\gamma}{2}\mathbf{q}^T\boldsymbol{\Gamma}\mathbf{q} + \sum_{i=1}^d \Bigl[\max_{\delta^{b,i}}\, A e^{-k\delta^{b,i}}\frac{e^{-\gamma(\delta^{b,i}+\Delta^+_i u)}-1}{\gamma} + \max_{\delta^{a,i}}\, A e^{-k\delta^{a,i}}\frac{e^{-\gamma(\delta^{a,i}-\Delta^-_i u)}-1}{\gamma}\Bigr] = 0$$

### Optimal half-spreads

Each inner maximisation involves only one decision variable. For the bid side, we maximise over $\delta^{b,i}$:

$$\max_{\delta^{b,i}} \; A e^{-k\delta^{b,i}}\bigl[e^{-\gamma(\delta^{b,i}+\Delta^+_i u)}-1\bigr]$$

Taking the derivative and setting to zero yields a single equation. Defining $\Phi^{b,i} = \delta^{b,i} + \Delta^+_i u$, the first-order condition is:

$$(k+\gamma)\,e^{-\gamma \Phi^{b,i}} = k \implies \Phi^{b,i} = \frac{1}{\gamma}\ln\!\left(1+\frac{\gamma}{k}\right)$$

Hence the **optimal bid half-spread**:

$$\boxed{\delta^{b,i*} = \frac{1}{\gamma}\ln\!\left(1+\frac{\gamma}{k}\right) - \Delta^+_i u(t,\mathbf{q})}$$

An identical calculation for the ask side yields $\Phi^{a,i} = \delta^{a,i*} - \Delta^-_i u = \frac{1}{\gamma}\ln(1+\gamma/k)$, so:

$$\boxed{\delta^{a,i*} = \frac{1}{\gamma}\ln\!\left(1+\frac{\gamma}{k}\right) + \Delta^-_i u(t,\mathbf{q})}$$

Defining the **static half-spread** $\eta := \frac{1}{\gamma}\ln(1+\gamma/k)$, the optimal quotes on instrument $i$ are:

$$p^{b,i*} = S^i_t - \delta^{b,i*} = S^i_t - \eta + \Delta^+_i u, \qquad p^{a,i*} = S^i_t + \delta^{a,i*} = S^i_t + \eta + \Delta^-_i u$$

The **reservation price** for instrument $i$ is the mid-point of the optimal bid and ask:

$$r^i_t := \frac{p^{a,i*} + p^{b,i*}}{2} = S^i_t + \frac{\Delta^-_i u + \Delta^+_i u}{2} = S^i_t + \frac{u(t,\mathbf{q}+\mathbf{e}_i) - u(t,\mathbf{q}-\mathbf{e}_i)}{2}$$

The **quoted spread** for instrument $i$:

$$p^{a,i*} - p^{b,i*} = 2\eta + \Delta^-_i u - \Delta^+_i u = 2\eta + \bigl[2u(t,\mathbf{q}) - u(t,\mathbf{q}+\mathbf{e}_i) - u(t,\mathbf{q}-\mathbf{e}_i)\bigr] = 2\eta - \Delta^2_i u$$

where $\Delta^2_i u$ is the second discrete derivative of $u$ in dimension $i$. For a concave $u$ (which is always the case here — the value function is concave in inventory due to risk aversion), $\Delta^2_i u < 0$ and therefore $2\eta - \Delta^2_i u > 2\eta$: the spread exceeds its static minimum, with the excess reflecting the curvature of the inventory risk.

### The equation for $u(t,\mathbf{q})$

Substituting the optimal half-spreads back into the HJB, and defining the constant $c = A(1+\gamma/k)^{-k/\gamma}/(k+\gamma)$, the value function satisfies:

$$\partial_t u = \frac{\gamma}{2}\mathbf{q}^T\boldsymbol{\Gamma}\mathbf{q} + c\sum_{i=1}^d \bigl[e^{k\Delta^+_i u} + e^{k\Delta^-_i u}\bigr]$$

with terminal condition $u(T, \mathbf{q}) = -\frac{A_T}{2}\|\mathbf{q}\|^2$. This is a coupled system of nonlinear ODEs in time (one per inventory state $\mathbf{q} \in \mathbb{Z}^d$), where the coupling arises through the discrete differences in $u$. The system can be solved numerically by backward integration from $T$ to $t_0$, typically by truncating $\mathbf{q}$ to a bounded grid $|q^i| \leq Q_{\max}$.

For the **single-asset case** ($d = 1$), the equation for $u(t, q)$ is:

$$\partial_t u(t,q) = \frac{\gamma\sigma^2 q^2}{2} + c\bigl[e^{k(u(t,q+1)-u(t,q))} + e^{k(u(t,q)-u(t,q-1))}\bigr]$$

The left side drives the concavity: for large $|q|$, the $\gamma\sigma^2 q^2/2$ term creates strong curvature in $u$ that translates into wide spreads and aggressive skewing.

(sec:omm_asym)=
## Asymptotic approximations

The nonlinear ODE system for $u$ has no closed-form solution in general. {cite:t}`gueant2012dealing` derive a tractable approximation valid for the **infinite-horizon (stationary) problem**, in which the horizon $T \to \infty$ and $u(t,\mathbf{q})$ converges to a time-independent function $u^\infty(\mathbf{q})$.

### The quadratic approximation

In the single-asset stationary problem, symmetry around $q = 0$ and the convexity structure of the ODE suggest the **quadratic ansatz**:

$$u^\infty(q) \approx u_0 - \frac{\theta}{2}q^2$$

for constants $u_0$ and $\theta > 0$. The discrete differences under this ansatz are:

$$\Delta^+u = u^\infty(q+1) - u^\infty(q) = -\theta q - \frac{\theta}{2}, \qquad \Delta^-u = u^\infty(q) - u^\infty(q-1) = -\theta q + \frac{\theta}{2}$$

**Reservation price.** From the AS formula derived above, $r^i = S^i + \frac{u(q+1)-u(q-1)}{2}$. Under the quadratic ansatz $u^\infty(q) = u_0 - \frac{\theta}{2}q^2$:

$$u(q+1) - u(q-1) = -\frac{\theta}{2}\bigl[(q+1)^2 - (q-1)^2\bigr] = -\frac{\theta}{2}\cdot 4q = -2\theta q$$

Therefore the **reservation price** and its **skew**:

$$\boxed{r^\infty = S - \theta q, \qquad \psi^\infty = -\theta q}$$

The quoted bid and ask are symmetric around $r^\infty$:

$$p^{a*} = r^\infty + \eta = S - \theta q + \eta, \qquad p^{b*} = r^\infty - \eta = S - \theta q - \eta$$

The **spread** is constant at $2\eta = \frac{2}{\gamma}\ln(1+\gamma/k)$, independent of inventory; the inventory effect appears entirely in the location of the bid-ask band.

### Determining $\theta$: the GLF result

Substituting the quadratic ansatz into the stationary HJB ($\partial_t u = 0$) and expanding at leading order in $q$:

$$0 = \frac{\gamma\sigma^2 q^2}{2} + 2c\cosh(k\theta/2) e^{-kq\theta}$$

This equation cannot hold for all $q$ simultaneously with the quadratic approximation. The GLF approach instead matches the equation at $q = 0$ and uses a linearisation in $\theta$ (valid for small $\theta$) to extract $\theta$. The result of this procedure is:

$$\boxed{\theta = \frac{\gamma\sigma^2}{\sqrt{2Ak^{-1}(1+\gamma/k)^{k/\gamma+1}}}}$$

or equivalently, in terms of the characteristic spread $\hat\eta = 2\eta = \frac{2}{\gamma}\ln(1+\gamma/k)$:

$$\theta = \gamma\sigma^2\sqrt{\frac{1}{2A\ln(1+\gamma/k)}} = \frac{\gamma\sigma^2}{\sqrt{2A\hat\eta\gamma}}$$

The full optimal GLF quotes in the single-asset stationary case are therefore:

$$\boxed{p^{a*} = S + \eta - \theta q, \qquad p^{b*} = S - \eta - \theta q}$$

$$\text{spread}^* = 2\eta = \frac{2}{\gamma}\ln\!\left(1+\frac{\gamma}{k}\right), \qquad \text{skew}^* = -\theta q = -\frac{\gamma\sigma^2}{\sqrt{2A\ln(1+\gamma/k)}}\,q$$

### Parameter dependences

The GLF formula makes the parameter dependences explicit and confirms the corrections introduced in chapter {ref}`market_making_fundamentals`:

| Component | Formula | Depends on |
|-----------|---------|------------|
| Static spread | $\frac{2}{\gamma}\ln(1+\gamma/k)$ | $\gamma$, $k$ |
| Skew per unit inventory | $\theta = \frac{\gamma\sigma^2}{\sqrt{2A\ln(1+\gamma/k)}}$ | $\gamma$, $\sigma^2$, $A$, $k$ |

The skew sensitivity $\theta$ is **not** simply $\gamma\sigma^2$ — it also depends on the arrival rate $A$ and the demand elasticity $k$. Higher order flow $A$ reduces $\theta$: a busy market maker can rebalance inventory quickly through trading, so she need not skew as aggressively for a given inventory imbalance. Higher demand elasticity $k$ also reduces $\theta$ (more responsive clients means tighter necessary skew) but amplifies the static spread component.

```{figure} figures/mm_as_sensitivities.png
:name: fig:mm_as_sensitivities
:width: 9in

**AS/GLF parameter sensitivities.** Top row: static spread $2\eta = \frac{2}{\gamma}\ln(1+\gamma/k)$ as a function of risk aversion $\gamma$ (left) and demand elasticity $k$ (centre), with the third panel showing how the optimal bid, ask and reservation price shift linearly with inventory $q$ at baseline parameters ($\sigma=2$, $A=140$, $k=1.5$, $\gamma=0.1$). Bottom row: skew coefficient $\theta$ as a function of volatility $\sigma$ (left), arrival rate $A$ (centre), and demand elasticity $k$ (right). The dashed vertical line marks the baseline parameter value in each panel.
```

### Multi-asset generalisation

In the multi-asset stationary problem, the quadratic approximation takes the form $u^\infty(\mathbf{q}) = u_0 - \frac{1}{2}\mathbf{q}^T\boldsymbol{\Theta}\mathbf{q}$ for a positive semi-definite matrix $\boldsymbol{\Theta} \in \mathbb{R}^{d\times d}$. The reservation price vector is:

$$\mathbf{r}^\infty = \mathbf{S} - \boldsymbol{\Theta}\mathbf{q}$$

so the skew in instrument $i$ depends on the **full inventory vector** through the off-diagonal elements of $\boldsymbol{\Theta}$:

$$r^{i,\infty} = S^i - \sum_j \Theta_{ij}\,q^j$$

The matrix $\boldsymbol{\Theta}$ is determined by the multi-asset analogue of the GLF equation, and its entries depend on $\boldsymbol{\Gamma}$, $A$, $k$, and $\gamma$. The key economic message is that correlated instruments share their inventory skew: being long in one instrument shifts the reservation price downward not only for that instrument but also for all positively correlated ones, reflecting the cross-hedging structure of the multi-asset covariance.

(sec:omm_apps)=
## Applications to LOBs and RfQs

### Limit order books

The AS framework was originally formulated for a market maker posting limit orders in a continuous limit order book {cite:p}`AvellanedaStoikov2008`. The original setting is the single-asset case ($d=1$) with the quoted mid-price following a zero-drift Brownian motion. The market maker maintains a bid and ask limit order and earns the spread whenever a market order arrives. The key assumption of exponential order arrival intensity $\lambda(\delta) = Ae^{-k\delta}$ approximates the empirical observation that the book thins out exponentially as orders are placed farther from the best bid and offer.

In the LOB context, the "hold-to-horizon" framework with a terminal liquidation penalty is appropriate when the market maker takes a position at the start of the day and manages it until a hard close. Intraday, the inventory $q_t$ fluctuates with each fill; the optimal quotes respond continuously via the finite-difference terms in $u$.

The GLF approximation is practically useful because it produces a simple real-time quoting formula: at any time $t$, compute the reservation price $r_t = S_t - \theta q_t$ (shifting the mid by the GLF skew) and quote bid $r_t - \eta$ and ask $r_t + \eta$. The formula depends only on the current mid price, the current inventory, and the two pre-computed constants $\eta$ and $\theta$.

### RfQ dealer markets

In dealer-to-client RfQ markets (chapter {ref}`rfq_models`), the single-trade model of {ref}`sec:omm_single` is directly applicable as the unit decision. The stream of RfQs maps to repeated single-trade problems, where between RfQs the inventory evolves (from hedges and prior trades) and the remaining horizon $\tau = T - t$ shrinks.

The connection between the single-trade formula and the AS framework is clearest in the **serial approximation**: treat each new RfQ as a fresh single-trade problem with the current inventory $q_t$ and remaining horizon $\tau_t = T - t$. The optimal spread is then:

$$\delta^*(t, q_t) = \frac{1}{k} + \frac{\Delta\ell}{\bar{q}} - \frac{\gamma\tau_t\sigma^2 q_t}{\bar{q}} + \frac{\gamma\tau_t\sigma^2\bar{q}}{2}$$

The third term $-\gamma\tau_t\sigma^2 q_t/\bar{q}$ is the skew: it grows with the remaining horizon $\tau_t$ (as in the AS finite-horizon formula) and shrinks toward zero at the end of the day as the urgency to rebalance the book increases. This formula can be used directly in a market-making system without solving the full HJB, at the cost of ignoring the interaction between the current RfQ and future arrivals.

### Backtesting and performance comparison

Theoretical optimality guarantees are derived under the model's own assumptions (Brownian mid-price, Poisson arrivals, CARA utility). To assess practical performance, {cite:t}`AvellanedaStoikov2008` propose a Monte Carlo back-test: simulate many independent trading days, record the terminal P&L after end-of-day liquidation, and compare strategies by the distribution of daily outcomes rather than by a single expected-utility number.

We implement three strategies under the baseline parameters ($\sigma = 2$, $A = 140$, $k = 1.5$, $\gamma = 0.1$, $T = 1$, $S_0 = 100$):

1. **GLF stationary**: quotes at $r_t = S_t - \theta q_t$ with constant half-spread $\eta$ — the closed-form approximation derived above.
2. **Single-trade (EOD)**: at each step uses the finite-horizon formula derived in {ref}`sec:omm_single`, with the current inventory and remaining horizon $\tau_t$. The spread widens early in the day (large inventory-risk premium) and narrows to $2/k$ at close.
3. **Symmetric benchmark**: fixed spread $2\eta$ around mid with no inventory management — a naive strategy that ignores the $u$-adjustment entirely.

A quadratic EOD liquidation penalty $A_{\mathrm{liq}}q_T^2$ (with $A_{\mathrm{liq}} = 1/(2k)$) accounts for the residual cost of crossing the market with any inventory remaining at close.

```{figure} figures/mm_as_simulation.png
:name: fig:mm_as_simulation
:width: 9in

**Single simulated trading day.** Left column: GLF stationary strategy. Right column: single-trade (EOD liquidation) strategy. Top row: mid-price trajectory (black) with shaded bid-ask band; the GLF band translates rigidly as inventory changes (constant width $2\eta$), while the single-trade band widens in the morning and narrows toward close. Middle row: inventory $q_t$ — the GLF strategy keeps the inventory closer to zero through continuous skewing; the single-trade strategy allows larger inventories early in the day. Bottom row: mark-to-market P&L.
```

```{figure} figures/mm_pnl_distribution.png
:name: fig:mm_pnl_distribution
:width: 9in

**Daily P&L distributions across 500 simulated trading days.** Left: kernel density estimates of terminal P&L for all three strategies (dashed vertical lines mark the mean). Right: box plots showing IQR and 5/95th percentiles. Both inventory-managing strategies (GLF and single-trade) substantially outperform the symmetric benchmark in both mean and tail risk — the symmetric strategy incurs large liquidation penalties from unchecked inventory drift. The GLF and single-trade strategies are comparable in mean P&L but differ in tail behaviour: the single-trade strategy controls inventory more conservatively (its wider early-day spread attracts fewer trades) and has slightly lighter tails; the GLF strategy fills more aggressively and achieves a higher mean at the cost of occasional larger left-tail outcomes.
```

The notebook `notebooks/market_making.ipynb` also produces a third figure (`mm_spread_dynamics.png`) showing the intraday spread schedule: the GLF spread is constant while the single-trade spread narrows monotonically from wide in the morning to $2/k$ at close, and the skew (difference between ask and bid half-spreads) vanishes at end of day for the single-trade strategy regardless of the current inventory level.

(sec:omm_enrich)=
## Enriching Avellaneda-Stoikov

### Liquidity: closing the position at market

The baseline AS framework with $\ell(\mathbf{q}_T) = \frac{A_T}{2}\|\mathbf{q}_T\|^2$ already introduces a liquidation cost at the terminal time. A natural extension for the dealer market is to allow partial liquidation throughout the day by trading at market with a spread cost.

Let $\delta^{\mathrm{mkt}}$ be the half-spread the dealer pays to cross the market (hedge in the inter-dealer book). Then the dealer has a continuous control: in addition to choosing the customer half-spreads $\delta^{b,i}$ and $\delta^{a,i}$, she can also execute a hedge of size $v^i_t$ at a cost of $\delta^{\mathrm{mkt}}|v^i_t|$ per unit. The cash and inventory dynamics gain the hedging terms:

$$dX_t^{\mathrm{hedge}} = -\sum_i (S^i_t \pm \delta^{\mathrm{mkt}}) v^i_t \, dt, \qquad dq^i_t \mathrel{+}= v^i_t \, dt$$

In the HJB, the hedging control $\mathbf{v}_t$ contributes an additional maximisation. For the quadratic penalty, the optimal hedge is:

$$v^{i*}_t = -\frac{1}{\delta^{\mathrm{mkt}}} \cdot \partial_{q^i} u(t, \mathbf{q}_t)$$

which drives inventory toward zero at a rate proportional to the indifference gradient divided by the hedging cost. When $\delta^{\mathrm{mkt}}$ is small (liquid inter-dealer market), the dealer hedges aggressively; when it is large (illiquid hedge), she relies more on skewing client quotes.

The unified model — optimising jointly over client quotes $\boldsymbol{\delta}$ and hedge trades $\mathbf{v}$ — is the framework of {cite:t}`gueant2017optimal` and of chapter 10 of {cite:t}`cartea2015algorithmic`. The single-trade formula of {ref}`sec:omm_single` corresponds to the limiting case $v = 0$ (no intraday hedging) with a one-shot terminal liquidation, i.e., $A_T = k\delta^{\mathrm{mkt}}/2$.

### Relative value: Ornstein-Uhlenbeck mid-price

The AS baseline assumes $d\mathbf{S}_t = \boldsymbol{\Sigma}d\mathbf{W}_t$ — mid prices are martingales with no drift. In spread products, pairs trading, or relative value strategies, the market maker may hold a mean-reverting view on the price. The natural model replaces the Brownian motion with a vector **Ornstein-Uhlenbeck (OU) process**:

$$d\mathbf{S}_t = \boldsymbol{\kappa}(\boldsymbol{\mu} - \mathbf{S}_t)\,dt + \boldsymbol{\Sigma}\,d\mathbf{W}_t$$

where $\boldsymbol{\kappa} \in \mathbb{R}^{d\times d}$ is the mean-reversion matrix and $\boldsymbol{\mu} \in \mathbb{R}^d$ is the long-run mean.

The HJB equation acquires a drift term. With the same CARA ansatz $V = -e^{-\gamma(x + \mathbf{q}\cdot\mathbf{s} + u(t,\mathbf{q},\mathbf{s}))}$, the reservation price becomes state-dependent:

$$r^i(t, \mathbf{q}, \mathbf{s}) = S^i + \partial_{q^i} u(t, \mathbf{q}, \mathbf{s})$$

The indifference function $u$ now satisfies a PDE in both $(t, \mathbf{q}, \mathbf{s})$ rather than just $(t, \mathbf{q})$. In the single-asset OU case, the solution has the form {cite:p}`cartea2015algorithmic`:

$$u(t, q, s) = A(t) s q + B(t) q^2 + C(t)$$

where $A$, $B$, $C$ satisfy a system of Riccati-type ODEs (see chapter {ref}`stochastic_optimal_control`, {ref}`sec:lqsc`). The reservation price becomes:

$$r(t, q, s) = s + A(t) q \cdot \frac{\partial s}{\partial q} + ... = s + A(t)s + 2B(t)q$$

and includes a directional component $A(t) s$: when $S_t > \mu$ (price above its mean), $A(t) < 0$ (for a mean-reverting process), so the reservation price shifts downward — the market maker expects the price to fall and quotes more aggressively on the sell side. This embeds a relative-value directional view into the quoting strategy without abandoning the optimal control framework.

### Flow imbalance

In the baseline AS model, the arrival rates of buy and sell orders are symmetric: $\lambda^b(\delta^b) = \lambda^a(\delta^a) = Ae^{-k\delta}$. In practice, order flow is often **imbalanced**: the rate of customer buy orders $A^b$ differs from the rate of sell orders $A^a$. This asymmetry may be persistent (a client base that predominantly sells, e.g., a corporate issuer hedging) or transient (intraday momentum in order flow).

Incorporating asymmetric intensities $\lambda^{b,i}(\delta^b) = A^b_i e^{-k\delta^b}$ and $\lambda^{a,i}(\delta^a) = A^a_i e^{-k\delta^a}$ modifies the HJB. After the same ansatz, the optimal half-spreads become:

$$\delta^{b,i*} = \eta - \Delta^+_i u, \qquad \delta^{a,i*} = \eta + \Delta^-_i u$$

where $\eta$ is unchanged (only $k$ and $\gamma$ enter the static half-spread), but the equation for $u$ picks up the asymmetry:

$$\partial_t u = \frac{\gamma}{2}\mathbf{q}^T\boldsymbol{\Gamma}\mathbf{q} + \sum_i\bigl[c^b_i\,e^{k\Delta^+_i u} + c^a_i\,e^{k\Delta^-_i u}\bigr]$$

where $c^b_i = A^b_i(1+\gamma/k)^{-k/\gamma}/(k+\gamma)$ and $c^a_i = A^a_i(1+\gamma/k)^{-k/\gamma}/(k+\gamma)$. When $A^b_i \neq A^a_i$, the stationary $u^\infty(q)$ is no longer symmetric around $q = 0$, and the optimal reservation price shifts in the direction of the dominant flow even at zero inventory.

Concretely, if $A^b_i > A^a_i$ (buy flow dominates), the market maker expects her inventory to drift negative (she sells more than she buys). The optimal response is to quote a slightly tighter ask (to attract the available buyers and prevent the drift from becoming too negative) and to widen the bid (since sellers are relatively rare). The flow imbalance thus introduces a **flow-driven skew** on top of the inventory-driven skew of the baseline model {cite:p}`cartea2015algorithmic`.

### Client segmentation in dealer-to-client markets

In dealer-to-client markets, unlike anonymous LOBs, the identity of each counterparty is known at the time of quoting. This information is economically valuable: different clients have different price sensitivities $k_c$, different flow toxicities $\alpha_c$ (the probability their trade is informationally motivated), and different average trade sizes $\bar{q}_c$. The AS framework can be extended to exploit this structure {cite:p}`gueant2019market`.

The key extension replaces the single arrival process with a superposition of $C$ client-class processes:

$$\lambda^{b,i}_c(\delta^b) = A_c\,e^{-k_c\delta^b}, \qquad c = 1, \ldots, C$$

Each client class $c$ has its own parameters $(A_c, k_c)$; the market maker observes the client identity before quoting and can therefore select a different spread $\delta^i_c$ for each client. The optimal quote for client $c$ is:

$$\delta^{i*}_c = \frac{1}{\gamma_c}\ln\!\left(1+\frac{\gamma_c}{k_c}\right) + \Delta^\pm_i u$$

where $\gamma_c$ is an effective risk-aversion coefficient that accounts for client toxicity: $\gamma_c = \gamma + \alpha_c \cdot k_c$ (the more toxic the client, the higher the effective risk aversion of the market maker toward that client's flow). The function $u$ itself remains common across clients — it reflects the total inventory risk, not the risk from any single client — but the optimal static component of the spread is client-specific.

The practical implications are significant. A market maker dealing with a highly informed institutional client should quote wider spreads ($\gamma_c$ large, so $\eta_c = \frac{1}{\gamma_c}\ln(1+\gamma_c/k_c)$ is wider) even when her current inventory is comfortable. Conversely, uninformed retail or corporate clients ($\alpha_c \approx 0$) receive tighter spreads, and the market maker can be more aggressive in winning their business to rebalance the book. This framework provides the mathematical foundation for the client analytics component of the market-making system described in chapter {ref}`market_making_fundamentals` ({ref}`sec:mm_system`).

In the multi-asset, multi-client setting, the full model becomes computationally challenging. {cite:t}`gueant2019market` develop a deep reinforcement learning approach that parametrises the value function with a neural network and optimises over client quotes directly, enabling solution of market-making problems with dozens of instruments and hundreds of clients.

## Exercises

1. **Grossman-Miller derivation.** Suppose $p = 1/2$ in the GM model and the price uncertainty between $t=1$ and $t=2$ is $\sigma^2_\text{intra}$ (not the full day volatility). The MM faces $n = 3$ competitors and the LT sells $i = 200$ units with $\gamma = 5$ and $\sigma_\text{intra} = 0.015$. Compute the equilibrium bid price and the bid-ask spread. How does the spread change if a fourth MM enters the market? What happens in the limit $n \to \infty$?

2. **Glosten-Milgrom full derivation.** Consider the asymmetric case with $p = 0.7$, $V_H = 105$, $V_L = 95$, and $\alpha = 0.3$. (a) Compute the prior $\mu$. (b) Derive the zero-profit ask and bid without the $p = 1/2$ simplification. (c) Compare the resulting spread to the symmetric-case formula. Does the spread depend on $p$ in the general case?

3. **Single-trade model — multi-asset skew.** A dealer has existing inventory $q_0^1 = 10$ (DV01 in EUR bonds) and $q_0^2 = -5$ (DV01 in USD bonds). The covariance matrix of daily returns is $\boldsymbol{\Gamma} = \begin{pmatrix} 4 & 2 \\ 2 & 3 \end{pmatrix} \times 10^{-4}$. She receives a buy RfQ for $\bar{q} = 8$ EUR bond DV01 with $\tau = 0.5$ (half-day remaining), $\gamma = 10$, $k = 20$, and liquidity penalty $\Delta\ell/\bar{q} = 0.002$. Compute the optimal spread $\delta^{1*}$. How does the cross-hedging from the USD inventory affect the spread relative to the clean-book case?

4. **Avellaneda-Stoikov optimal spreads.** In the single-asset AS model with $\sigma = 0.01$, $A = 2$ (arrivals per second), $k = 1.5$ (per unit spread), $\gamma = 0.1$, and $T - t = 1800$ seconds:
   (a) Compute the static half-spread $\eta = \frac{1}{\gamma}\ln(1+\gamma/k)$.
   (b) For inventory $q = 5$, compute the optimal bid and ask under the finite-horizon approximation $\delta^{b*} \approx \eta - (u(t,q+1)-u(t,q)) \approx \eta + \theta q$ (using the quadratic approximation for $u$).
   (c) Compute $\theta$ from the GLF formula and confirm the skew direction is consistent with the inventory.

5. **GLF parameter sensitivities.** A market maker uses the GLF approximation with $\gamma = 0.2$, $k = 1.0$, $\sigma = 0.012$, $A = 1.5$.
   (a) Compute the optimal spread and the skew coefficient $\theta$.
   (b) Suppose volatility doubles to $\sigma = 0.024$. How does the spread change? How does $\theta$ change?
   (c) Suppose the arrival rate $A$ doubles. How does $\theta$ change? Interpret the result economically.

6. **Client segmentation.** A dealer serves two client classes: (A) uninformed retail clients with $k_A = 3$, $\alpha_A = 0.05$; (B) sophisticated fund managers with $k_B = 1$, $\alpha_B = 0.4$. The dealer's risk aversion is $\gamma = 0.1$ and her inventory is currently flat.
   (a) Compute the effective risk aversion $\gamma_c = \gamma + \alpha_c k_c$ for each client class.
   (b) Compute the static half-spread $\eta_c$ for each class.
   (c) Explain how the optimal quotes would differ if the dealer has a large long position versus a flat book. Which client is more useful for rebalancing the book?
