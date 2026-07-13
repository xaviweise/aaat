(market_making_fundamentals)=
# Market Making Fundamentals

## Introduction

A market maker occupies a distinctive role in the financial system: unlike most investors, who form a view on the future price of an asset and trade accordingly, a market maker *stands ready to trade* — continuously quoting prices at which she will buy and sell, regardless of her directional view. In doing so, she provides the market with **liquidity**: the ability of other participants to trade quickly and at known prices. This service is indispensable. Without liquidity providers willing to absorb the flow of investors and hedgers, markets would operate only when buyers and sellers coincidentally arrived at the same time. Bid-ask spreads would be wide, price discovery inefficient, and the real-economy benefits of financial markets — channelling savings into investment, distributing risk, and revealing fair values — would be severely impaired.

The compensation for providing this service is the **bid-ask spread**: the market maker quotes a price to buy (bid) that is slightly below her estimate of the fair value, and a price to sell (ask) that is slightly above it. If she trades on both sides symmetrically, she earns the spread on each round trip. In practice, achieving this symmetry is the central challenge of market making: the arrival of buy and sell orders is unpredictable, prices move continuously, and not all counterparties have the same information. Managing these realities is what makes market making a genuinely difficult optimization problem.

This chapter provides the conceptual and institutional foundations for the topic. We begin by characterizing the market-making business objective and the types of institutions that carry it out ({ref}`sec:mm_objective`). We then dissect the three fundamental risks that the bid-ask spread must compensate: order handling costs, inventory risk, and information asymmetry ({ref}`sec:mm_risks`). A simple but influential model for each of the last two risks — due to {cite:t}`grossman1988liquidity` and {cite:t}`glosten1985bid` respectively — illustrates the economic forces at work and provides the first quantitative relationships between spread, volatility, competition, and toxicity. The mathematical optimization underlying these models is developed in full in the following chapter, {ref}`optimal_market_making`. The foundational analytics for this block are all developed in the preceding Advanced Analytics for Financial Markets block: market structure models for limit order books ({ref}`lob_models`) and dealer-to-client RfQ markets ({ref}`rfq_models`), fair price estimation methods ({ref}`fair_price_estimation`), and liquidity measurement frameworks ({ref}`liquidity_modelling`). Section {ref}`sec:mm_strategy` then deconstructs a practical market-making strategy into its component decisions: fair price estimation, spread determination, skew management, and inventory hedging. Section {ref}`sec:mm_system` describes the architecture of a market-making system — the pricing engine, analytics, and risk management infrastructure that supports these decisions at operational scale. The chapter closes with a discussion of how market-making fits into the two dominant market structures — dealer-to-client platforms and limit order books ({ref}`sec:mm_microstructure`) — illustrated with concrete examples from interest rate swaps, equity index futures, and retail equity internalization.

(sec:mm_objective)=
## The market-making business objective

### Definition and rationale

A market maker is a trader who, on a continuous and regular basis, proposes prices at which she stands ready to buy and sell a given financial instrument {cite:p}`cartea2015algorithmic`. The distinguishing feature of market making is not that the market maker holds a view on the future price — she may or may not — but that she commits to trade at the prices she quotes, acting as a counterparty of last resort for other market participants who need to trade immediately.

The economic rationale is straightforward. Buyers and sellers rarely arrive at the market at the same time. A pension fund that needs to sell €500 million of government bonds to meet a redemption cannot wait for another investor who wants to buy exactly that amount. A market maker absorbs this *order imbalance* by buying the bonds at her bid price, holding them temporarily in inventory, and later selling them when a natural buyer appears. For this intermediation service — providing *immediacy to trade* — the market maker earns the bid-ask spread.

As described in chapter {ref}`market_microstructure`, this type of intermediation is fundamental in **quote-driven markets** (also called dealer markets), where prices are set by broker-dealers who quote firm bid and ask prices to clients. Corporate and government bond markets, interest rate swaps, foreign exchange, and credit derivatives operate predominantly as dealer markets. In **order-driven markets** (limit order books), the same function is performed by anyone who posts a limit order resting in the book — de facto acting as a liquidity provider, whether they call themselves a market maker or not. Modern equity markets blend both structures, with official market makers (Designated Market Makers on the NYSE, for instance) required to maintain orderly markets by a formal contractual obligation.

### Who makes markets

The market-making function is carried out by different types of institutions with distinct technology, risk appetite, and market focus:

**Investment banks and broker-dealers** — such as Goldman Sachs, J.P. Morgan, BNP Paribas, or BBVA — make markets across the broadest range of instruments and client types. They act as official market makers in many venues, quote firm prices to institutional clients in dealer-to-client platforms, and maintain inter-dealer books that they hedge via inter-dealer-broker networks. Their market-making desks are often supported by large balance sheets and deep client relationships, which give them access to natural two-way flow that helps balance inventory.

**Non-bank liquidity providers (NBLPs)** — firms such as Citadel Securities, Virtu Financial, or Jane Street — have become dominant in retail and ETF markets by exploiting technological advantages. They operate at high volume and low margin, focusing on the most liquid and electronically accessible instruments. Their business model depends on statistical edge and execution speed rather than client relationships or balance sheet capacity.

**High-frequency trading (HFT) firms** — overlapping with NBLPs but more narrowly focused on ultra-low latency — dominate market making in equity futures, spot FX, and other highly electronic markets. They hold very small inventories for very short holding periods, hedging residual risk continuously. They typically do not act as official market makers: they withdraw liquidity in stressed conditions rather than being obligated to maintain quotes.

These differences matter because they shape the spread, skew, and risk management practices that each type of market maker deploys. An investment bank with a long client relationship and access to natural netting can quote tighter spreads and tolerate larger inventory positions than an HFT firm that must manage every tick.

(sec:mm_risks)=
## Market-making risks and trade-offs

The bid-ask spread is not pure profit — it is compensation for three distinct categories of cost and risk. Understanding their origins is essential for understanding how spreads are determined and how market-making strategies are designed.

### Order handling costs

The first component is operational: the labour, technology, and capital required to quote prices, route and execute orders, and clear and settle trades. In fully automated electronic markets this cost has declined to near zero per transaction, but it is non-negligible for less liquid instruments traded manually or over the phone. In regulated markets, market makers also face balance sheet costs under capital adequacy rules (Basel III/IV), which constrain the size of the inventory they can hold and therefore affect the spreads they need to charge. For the purposes of modelling, order handling costs are typically treated as a fixed, instrument-specific floor on the spread.

### Inventory risk

When a market maker buys an asset at her bid price, she accumulates inventory that she cannot immediately unwind. During the period she holds this inventory, the asset's price may move adversely — downward if she is long, upward if she is short. This **inventory risk** is a direct consequence of providing the immediacy service: the market maker absorbs order imbalances, and the resulting inventory exposes her to market volatility.

The economic consequences of inventory risk are captured elegantly by the three-period model of {cite:t}`grossman1988liquidity`. The setup is deliberately stylized: there are $n$ identical market makers and a sequence of liquidity traders, with asset prices following a random walk with volatility $\sigma$. A liquidity trader arrives at $t=1$ needing to sell $i$ units immediately, and another arrives at $t=2$ wanting to buy $i$ units. The $n$ market makers compete to absorb the sell at $t=1$ and distribute it to the buyer at $t=2$. All agents have exponential utility $U(X) = -e^{-\gamma X}$ with risk-aversion coefficient $\gamma$.

In the competitive equilibrium, market makers will only absorb the inventory if compensated for the price uncertainty they bear between $t=1$ and $t=2$. Solving the market clearing conditions, the equilibrium bid price at $t=1$ is:

$$S_{\text{bid}} = S_{\text{fair}} - \frac{i \,\gamma\, \sigma^2}{n}$$

and symmetrically for the ask at $t=2$, giving a **bid-ask spread**:

$$\text{spread}_{\text{GM}} = \frac{2\,i\,\gamma\,\sigma^2}{n}$$

The formula captures the main economic determinants of inventory-driven spreads:

- **Volatility $\sigma^2$**: higher price uncertainty means greater inventory risk per unit time, so market makers demand a larger spread.
- **Order size $i$**: larger trades create more inventory imbalance; the spread increases proportionally.
- **Risk aversion $\gamma$**: more risk-averse market makers require greater compensation to hold inventory.
- **Competition $n$**: more market makers share the inventory burden, reducing the spread required from any one of them. As $n \to \infty$, spreads compress to zero — the perfectly competitive limit in which the market clears at the efficient price.

The full derivation of this result, including the utility maximization and market-clearing conditions, is covered in chapter {ref}`optimal_market_making`. The numerical illustration in the companion notebook (`notebooks/market_making.ipynb`) shows how the spread varies with each parameter.

### Information asymmetry

The second major risk is **adverse selection**: the risk that the counterparty initiating the trade has superior information about the asset's future value. If a market maker quotes a bid of 100 and an informed trader sells at that price because they know the asset will soon be worth 95, the market maker will suffer a loss that is not offset by trades with uninformed counterparties. The market maker cannot distinguish informed from uninformed flow at the moment of quoting — she must set a spread that accounts for the *possibility* of trading against informed counterparties.

This mechanism was formalized by {cite:t}`glosten1985bid`. Their model considers a single market maker (a specialist) quoting firm bid $b$ and ask $a$. A fraction $\alpha$ of all incoming orders are from informed traders who know the true asset value $v$ — either $V_H$ with prior probability $p$ or $V_L$ with probability $1-p$ — while the remaining fraction $1-\alpha$ are uninformed liquidity traders who buy or sell randomly. In a perfectly competitive equilibrium, the market maker earns zero expected profit:

$$\mathbb{E}[\pi \mid \text{buy}] = 0 \quad \text{and} \quad \mathbb{E}[\pi \mid \text{sell}] = 0$$

Solving these conditions yields equilibrium bid and ask prices:

$$a = \mu + \alpha(V_H - \mu), \qquad b = \mu - \alpha(\mu - V_L)$$

where $\mu = p V_H + (1-p)V_L$ is the prior expected value. The resulting bid-ask spread is:

$$\text{spread}_{\text{GL}} = a - b = \alpha\bigl[(V_H - \mu) + (\mu - V_L)\bigr] = \alpha(V_H - V_L)$$

The spread is a direct function of the **fraction of informed flow** $\alpha$ and the **magnitude of the informational asymmetry** $V_H - V_L$. With no informed traders ($\alpha = 0$), the competitive spread is zero. As $\alpha$ increases, the spread widens to allow the market maker to break even: profits on uninformed trades subsidize losses on informed ones. This result has a direct practical implication: market makers should quote wider spreads (or withdraw quotes entirely) when they detect elevated levels of informed flow — a concept central to *flow toxicity* analysis in modern electronic market making.

The full Glosten-Milgrom derivation with the zero-profit equilibrium conditions is covered in chapter {ref}`optimal_market_making`.

### The static and dynamic trade-offs

The two risks described above create two related trade-offs in market-making strategy:

**The static trade-off** concerns the choice of spread: a wider spread earns more per trade but reduces the arrival rate of orders (fewer clients will accept a wide bid-ask). The optimal spread balances these opposing forces. In the absence of inventory and information risk, this is equivalent to a monopoly pricing problem — the same unit-elasticity condition that appears in the dynamic pricing analysis of {ref}`rfq_models`. In practice, competition among market makers drives spreads toward the minimum needed to cover costs and risks.

**The dynamic trade-off** concerns inventory management over time. A market maker who quotes symmetric bid and ask prices around the fair value will, on average, receive balanced two-way flow. But random fluctuations in order arrival create inventory imbalances. A large long inventory in a volatile instrument is dangerous: prices may fall substantially before natural sellers appear to rebalance the book. The market maker must therefore *skew* her quotes — quoting more aggressively on the bid (or more conservatively on the ask) when she is long, to attract buyers and reduce inventory. This skewing is both a risk management tool and a revenue lever, and is the central dynamic decision in optimal market making.

(sec:mm_strategy)=
## Deconstructing a market-making strategy

Every market-making strategy can be decomposed into four sequential decisions, applied at the time of each quote:

$$\underbrace{p_{\text{bid}}}_{\text{bid quote}} = \underbrace{m_t}_{\text{fair price}} - \underbrace{\frac{\psi_t}{2}}_{\text{half-skew}} - \underbrace{\frac{s_t}{2}}_{\text{half-spread}}, \qquad \underbrace{p_{\text{ask}}}_{\text{ask quote}} = m_t + \frac{\psi_t}{2} + \frac{s_t}{2}$$

where $m_t$ is the fair price estimate, $s_t \geq 0$ is the bid-ask spread, and $\psi_t$ is the skew (positive when the ask is shifted up more than the bid, i.e. when the market maker is long and wants to attract sellers). The four decisions are: estimate $m_t$, determine $s_t$, determine $\psi_t$, and hedge the resulting inventory. We discuss each in turn.

### Fair price estimation

The fair price $m_t$ is the market maker's best estimate of the true value of the instrument at time $t$, net of any spread. Getting this estimate right is the most consequential decision: a consistently biased fair price will cause the market maker to transact at systematically disadvantageous levels, destroying value regardless of how well spread and skew are managed.

Chapter {ref}`fair_price_estimation` covers fair price models in depth. For the market-making context, two approaches are most relevant:

- **In liquid, centralized markets** — equity order books, liquid futures — the fair price is taken directly from the market: the mid-price of the limit order book (average of best bid and best ask), or a composite price from multiple venues. Statistical models such as the Kalman filter ({ref}`fair_price_estimation`) can be layered on top to smooth the mid-price and reduce noise from temporary order imbalances.

- **In fragmented or illiquid markets** — corporate and government bonds, interest rate derivatives, credit default swaps — there is no single authoritative mid-price. The fair price must be constructed from: indicative quotes from inter-dealer platforms or voice brokers, recent transaction prices (often stale), prices of liquid proxy instruments (hedges), and fundamental pricing models (e.g. discounted cash flow, Black-Scholes sensitivities, or yield curve models for fixed income). In practice, a hierarchical approach is used: start from the most liquid available reference, then apply model-based corrections for credit spreads, liquidity premiums, and instrument-specific features.

For instruments with measurable risk sensitivities — DV01 for bonds, delta/vega for options — the fair price also requires calculating these Greeks, which determine both the hedging strategy and the inventory risk metrics used by the risk management system.

### Spread determination

Given the fair price, the market maker chooses the bid-ask spread $s_t$. The spread must cover at minimum:

1. **Order handling costs**: fixed, instrument-level operational floor.
2. **Inventory risk premium**: from the Grossman-Miller result, the spread should be wider when $\sigma^2$ is large, when trades are large ($i$), or when competition is thin ($n$ small).
3. **Adverse selection premium**: from the Glosten-Milgrom result, the spread should be wider when the fraction of informed traders $\alpha$ is high.
4. **A profit margin**: competitive pressure may compress this to near zero in heavily competed instruments.

In practice, spread determination is often parametrized by a base spread (minimum competitive level) plus state-dependent adjustments:

$$s_t = s_{\text{base}} + \Delta s_{\text{vol}}(\sigma_t) + \Delta s_{\text{toxicity}}(\hat{\alpha}_t) + \Delta s_{\text{inventory}}(|q_t|)$$

where $\sigma_t$ is current volatility, $\hat{\alpha}_t$ is an estimate of current flow toxicity (discussed below), and $|q_t|$ is the absolute inventory level. Each adjustment reflects a distinct risk source: volatility increases inventory risk, toxicity signals informed flow, and large inventory increases the urgency to reduce exposure. Market analytics — real-time volatility estimates, flow classification models, and order book imbalance signals — feed these adjustments continuously.

The optimal spread from a dynamic stochastic control perspective (the Avellaneda-Stoikov framework {cite:p}`AvellanedaStoikov2008` and its extensions {cite:p}`gueant2012dealing`) derives these relationships formally by solving a utility maximization problem. The mathematical treatment is the subject of the next chapter.

### Skew and inventory management

The skew $\psi_t$ determines how the market maker's quotes shift relative to the fair price as a function of her inventory. The purpose of the skew is to create an asymmetric incentive for incoming orders: when the market maker is long (positive inventory $q_t > 0$), she wants to attract buyers and discourage sellers, so she shifts *both* prices downward — quoting a lower bid (making it less attractive to sell to her) and a lower ask (making it more attractive to buy from her). The net effect is a skew $\psi_t < 0$ (conventionally, the ask is shifted down more than the bid). The reverse applies when she is short.

The optimal skew is derived formally in {cite:t}`gueant2012dealing` by solving a stochastic control problem, and the closed-form solution is considerably richer than a simple rule: it depends on the risk-aversion coefficient $\gamma$, the asset volatility $\sigma^2$, the current inventory $q_t$, the average arrival rate and size of orders, and the price sensitivity of that flow (how steeply the hit probability falls with spread). The full derivation and the resulting formula are covered in chapter {ref}`optimal_market_making`. The qualitative message, however, is clear: the optimal skew is monotone in inventory — it increases in magnitude with $|q_t|$ — and its sensitivity to inventory grows with $\gamma$ and $\sigma^2$. A more risk-averse market maker facing a more volatile instrument should skew more aggressively to reduce inventory faster, and the exact rate at which she should do so also depends on the market's responsiveness to her quotes.

### Hedging the inventory

Skewing quotes reduces inventory gradually by attracting natural offsetting flow. But in volatile markets, or when natural flow is slow to arrive, the market maker must take a more active approach and **hedge** her inventory directly.

Hedging means taking an offsetting position in a correlated instrument that can be traded quickly and cheaply:

- **Same instrument, different venue**: hedging a corporate bond position by buying or selling the same bond in the inter-dealer market (e.g. via an inter-dealer broker).
- **Correlated instrument**: hedging a bond portfolio with interest rate futures (Bund futures for European rates, US Treasuries for USD rates); hedging an equity derivative position with the underlying stock or index ETF.
- **Proxy hedge**: when the exact instrument is unavailable or too costly to trade, hedging with a correlated substitute — e.g. a bond with similar duration and credit quality.

The quality of the hedge depends on the *basis risk*: the residual price risk that remains after the hedge is in place. A perfect hedge (same instrument, full size) eliminates inventory risk entirely at the cost of the transaction. A proxy hedge reduces risk but leaves residual exposure to the spread between the instrument and its proxy. Managing this basis risk is part of the risk management system's mandate.

Hedging execution itself uses the algorithms described in chapters {ref}`execution_fundamentals` and {ref}`optimal_execution`: the market maker effectively runs a continuous stream of small execution problems as she unwinds inventory positions.

(sec:mm_system)=
## Components of a market-making system

A production market-making system integrates four interconnected components:

### Pricing engine

The pricing engine computes the fair price $m_t$ and its sensitivities to risk factors (Greeks: delta, gamma, vega, DV01, etc.) for every instrument in the quoting universe. For a bank market-making thousands of instruments simultaneously, this requires high-performance infrastructure running pricing models at near-real-time frequency.

The pricing engine ingests market data — reference prices from electronic platforms, yield curves, volatility surfaces — and outputs a risk vector for each instrument. This risk vector feeds directly into both the spread/skew calculation and the inventory risk system.

### Analytics server

The analytics server provides the contextual information that drives state-dependent adjustments to spreads and skews. Two streams of analytics are typically maintained:

**Market analytics** — instrument-level signals derived from market data:
- Volatility estimation and forecasting (realized, implied, model-based)
- Short-term price trend signals (momentum, order imbalance)
- Liquidity conditions: market depth, recent trade frequency, bid-offer width in the inter-dealer market
- Regime alerts: detection of unusual market conditions (flash crashes, news releases, broad risk-off episodes)

**Client analytics** — relevant in dealer-to-client platforms where counterparty identity is known (see {ref}`rfq_models`):
- Client segmentation: grouping clients by their trading behaviour, information content, and flow toxicity
- Demand estimation: modelling client price sensitivity (elasticity of the hit rate in RfQ markets)
- Flow toxicity scoring: estimating $\hat{\alpha}_t$ (the probability that the current flow is informationally motivated) from short-term price impact statistics

### Market-making server

The market-making server combines fair prices and analytics to determine actual quotes and manage inventory:

**Quotes determination**: applies the spread and skew formulas to the fair price, incorporating all analytical inputs:
$$p_{\text{bid}} = m_t - \frac{\psi_t^*}{2} - \frac{s_t^*}{2}, \qquad p_{\text{ask}} = m_t + \frac{\psi_t^*}{2} + \frac{s_t^*}{2}$$

In electronic markets, quotes are streamed continuously and updated at sub-second frequencies. In voice or hybrid markets, the server pre-calculates indicative spreads and skews that human traders use as a starting point.

**Inventory hedging**: monitors the inventory vector $\mathbf{q}_t$ in real time and triggers hedging trades when inventory exceeds predefined thresholds or risk limits. Hedge selection is automated based on liquidity and correlation criteria; execution is routed through the execution algorithms discussed in {ref}`optimal_execution`.

**Performance monitoring**: tracks flow metrics — hit ratios, flow value by client and instrument, realized spread versus effective spread — to assess whether the quoting policy is generating value. The key metric is **flow value** or **round-trip P&L**: the average profitability of a trade computed over a round-trip horizon (the time to unwind the position), which captures both the spread earned and the mark-to-market impact of inventory movements. Persistently negative flow value on a specific client or time-of-day bucket signals toxic flow, triggering a spread adjustment.

### Risk management system

The risk management system operates in parallel, maintaining real-time positions and assessing their risk:

- **Inventory valuation**: marks all open positions to current fair prices, computing the full P&L in real time.
- **Risk factor sensitivities**: aggregates Delta, DV01, Vega, and other Greeks across all instruments to give a comprehensive view of the book's exposure to each risk factor.
- **Risk limits**: enforces pre-defined limits on position size, Greeks, and Value-at-Risk. Limit breaches trigger alerts to the market maker and, if critical, automatic inventory reduction.
- **Stress testing**: evaluates the portfolio under extreme market scenarios — large price moves, correlation breakdowns, liquidity crises — to identify tail risk exposures.

(sec:mm_microstructure)=
## Market-making and market microstructure

Market making looks different depending on the market structure in which it operates. The two dominant structures — dealer-to-client platforms and limit order books — impose different informational environments, different quoting mechanics, and different sources of inventory and adverse selection risk.

### Dealer-to-client platforms

In dealer-to-client (D2C) markets — including most bond, swaps, FX, and credit derivative markets — market making is organized around the Request-for-Quote (RfQ) process described in detail in chapter {ref}`rfq_models`. The key features from a market-making perspective are:

- **Client identity is known**: the dealer can condition her spread and skew on client characteristics — expected toxicity, historical demand patterns, relationship value. This is in stark contrast to anonymous order book markets.
- **Competition is explicit but limited**: the client sends RfQs to a small number of selected dealers simultaneously, and the dealer knows how many competitors she is facing. This affects her optimal spread (the larger $n$, the tighter the required spread to win the trade).
- **No continuous quoting obligation** (in most D2C markets): the dealer responds on a per-RfQ basis rather than maintaining live quotes. This changes the inventory dynamics significantly — positions accumulate in discrete jumps rather than continuously.
- **Information asymmetry is client-specific**: the probability that an RfQ is informationally motivated varies strongly by client, instrument, and market conditions. The analytics described above are particularly valuable in this context.

The causal framework from chapter {ref}`rfq_models` shows how the hit probability $P(\text{hit} \mid \text{do}(\delta))$ depends on the quoted spread $\delta$, and how optimal pricing maximizes expected flow value. This is the D2C analogue of the Avellaneda-Stoikov problem in limit order books.

**Example: Interest Rate Swaps.** The interest rate swap (IRS) market has an outstanding notional of approximately \$300 trillion worldwide, making it one of the largest derivatives markets. Dealers quote two-way prices for plain-vanilla fixed-to-float swaps at standard tenors (1Y, 2Y, 5Y, 10Y, 30Y). Clients send RfQs via D2C platforms (Bloomberg, Tradeweb) or by voice. The reference dealer hedges unmatched inventory in the inter-dealer market via platforms such as ICAP i-Swap or CME SwapStream, or by using government bond or futures positions to hedge the interest rate risk (DV01 hedging). The fair price is derived from the yield curve calibrated to traded liquid benchmarks; DV01 sensitivity is computed analytically from the swap's cash flow structure.

### Limit order books

In order-driven markets, market making takes the form of posting passive **limit orders** — orders to buy (or sell) at a specified price, resting in the limit order book until filled or cancelled. Limit order markets are discussed in chapter {ref}`lob_models`; here we focus on the market-making implications.

In a limit order book, the market maker must contend with:

- **Anonymous counterparties**: unlike D2C, she does not know who is trading against her passive orders. Adverse selection is harder to measure and control.
- **Queue priority and order placement**: even within a price level, orders are filled in time priority (first in, first out in most markets). Placing orders early earns better queue position but exposes the market maker to more adverse selection risk as the information environment evolves.
- **Continuous quote update obligation**: in active markets, a market maker posts and cancels orders at high frequency — tens to thousands of times per second for HFT market makers — to keep her quotes current as the fair price moves.
- **Make-take fee structures**: many exchanges reimburse liquidity providers with a *maker rebate* and charge a *taker fee* to liquidity consumers. This changes the effective spread economics and affects the optimal quoting strategy.

**Example: IBEX 35 Futures at MEFF.** The MEFF futures on the IBEX 35 index trade on a fully electronic limit order book during continuous market hours (8:00 am–8:00 pm). The nominal value per contract is €10 × index level (approximately €100,000 at current index levels). A market maker posts simultaneous bid and ask limit orders at or near the best bid-offer. When a buy order consumes her ask, she accumulates a short position and hedges by buying the IBEX 35 ETF (e.g. Lyxor IBEX 35) or the basket of 35 constituent stocks, or adjusts her outstanding bid to attract a seller. The round-trip P&L depends on how quickly she can rebalance and at what cost.

**Example: NYSE internalisation and payment for order flow.** Retail brokerage platforms such as Robinhood route most client order flow not to public exchanges but to **internalizers** — firms such as Citadel Securities, Virtu Financial, and Two Sigma — which execute orders against their own inventory at the National Best Bid and Offer (NBBO) or with a small price improvement. This practice, known as **payment for order flow (PFOF)**, compensates the broker for directing flow to the internalizer. The internalizer benefits because retail order flow is predominantly uninformed (low $\alpha$ in Glosten-Milgrom terms): customers trade for liquidity reasons — purchases of individual stocks, rebalancing, DCA — rather than on the basis of private information. This makes it profitable to offer price improvement (a tighter effective spread) while still earning a positive margin, and without the adverse selection risk of trading against institutional or informed flow.

## Exercises

1. In the Grossman-Miller model, a market maker operates in a market with asset volatility $\sigma = 2\%$ per day, risk aversion $\gamma = 10$, and competes with $n = 4$ other market makers. A liquidity trader arrives needing to sell $i = 100$ units. Compute the equilibrium bid-ask spread. How does it change if one market maker exits ($n = 3$)? What if volatility doubles?

2. In the Glosten-Milgrom model, suppose $V_H = 102$, $V_L = 98$, $p = 0.5$, and $\alpha = 0.2$. Compute the equilibrium bid and ask prices. What is the bid-ask spread? How does it change if the fraction of informed traders rises to $\alpha = 0.4$?

3. A market maker quotes bid = 99.8 and ask = 100.2 in a bond market (fair price = 100). During the day she executes 50 sells at the ask and 30 buys at the bid. What is her end-of-day inventory? If the fair price has moved to 99.9, what is her unrealized P&L on the inventory? What skew adjustment would help her reduce the inventory imbalance?

4. Consider a market maker facing both inventory risk and information asymmetry. She observes that her average flow value (round-trip P&L per unit) is negative for one particular client but positive for others. Using the frameworks in this chapter, explain the most likely cause and propose a remediation strategy (spread adjustment, skew adjustment, or quote withdrawal).

5. Explain the difference between a market maker "hedging in the market" versus "skewing quotes" as inventory management strategies. Under what market conditions is each approach more appropriate?
