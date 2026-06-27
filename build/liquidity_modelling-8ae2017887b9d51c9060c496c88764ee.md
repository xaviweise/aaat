(liquidity_modelling)=
# Liquidity Modelling

## Introduction

Liquidity is one of the most consequential and yet elusive properties of a financial instrument or market. The classical economic definition describes liquidity as the ease with which an asset can be converted into cash without significantly affecting its price. This seemingly simple notion conceals a rich and multidimensional concept: a liquid market is one where large trades can be executed quickly, at low cost, and without materially moving prices. An illiquid market, by contrast, imposes frictions that manifest as wide bid-ask spreads, scarce depth, slow execution, and elevated price sensitivity to individual trades.

The importance of liquidity for the topics covered in this book is pervasive. For market makers, as discussed in chapter {ref}`optimal_market_making`, the liquidity of the instruments they quote directly determines the risk of holding inventory, since illiquid instruments are harder and more costly to unwind, more difficult to hedge with proxy instruments, and more likely to exhibit unstable correlations. For execution algorithms, covered in chapters {ref}`execution_fundamentals` and {ref}`optimal_execution`, liquidity determines the cost and feasibility of completing large orders: the market impact and bid-ask spread costs that define the execution problem are direct manifestations of the liquidity conditions of the market. For portfolio managers and systematic traders, liquidity constrains which instruments can be held at scale and affects the statistical properties of returns.

Quantifying liquidity from observable market data is non-trivial because there is no single direct measure. Instead, practitioners compute a battery of proxies—each illuminating a different facet of liquidity—and then aggregate them into a composite score. These proxies require different types of data: transaction-level trade records, dealer quotes, or static instrument attributes. The literature and industry practice have converged on a set of well-established indicators, which we organize in this chapter by the dimension of liquidity they capture and the data they require.

The chapter proceeds as follows. We first discuss the multiple dimensions along which liquidity can vary ({ref}`sec:liq_dimensions`), and how they relate to the market structures described in chapter {ref}`market_microstructure`. We then present structural predictors of liquidity ({ref}`sec:liq_structural`) and a taxonomy of market-data-based liquidity indicators: activity-based measures ({ref}`sec:liq_activity`), price impact estimators ({ref}`sec:liq_impact`), and transaction cost estimators ({ref}`sec:liq_tce`). We next discuss methodologies for aggregating these indicators into a composite liquidity score ({ref}`sec:liq_scoring`). We close with a discussion of the connection between liquidity and market making through the concept of inventory rotation time ({ref}`sec:liq_marketmaking`) and of the dynamic properties of liquidity, including intraday patterns and behavior under market stress ({ref}`sec:liq_dynamics`).

(sec:liq_dimensions)=
## The dimensions of liquidity

The academic literature has identified four primary dimensions along which the liquidity of a market can vary {cite:p}`kyle1985`:

- **Tightness** refers to the cost of executing a small trade, typically measured by the bid-ask spread. A tight market is one where the gap between the best bid and ask prices is small, so that a round-trip buy-and-sell transaction can be completed at low cost. Tightness is the most directly observable dimension of liquidity and is the primary concern for small, frequent traders.

- **Depth** refers to the volume of orders available at or near the current price. A deep market can absorb large trades without significant price movement. As discussed in chapter {ref}`lob_models`, depth is a structural property of the limit order book and can be measured at different price levels. A market may be tight at the best bid and ask but shallow beyond that, meaning that only small orders can be executed at favorable prices.

- **Immediacy** refers to how quickly a trade can be arranged and executed at the prevailing price. In a market with high immediacy, a trader can find a counterparty almost instantly, as in a liquid electronic order book. In illiquid markets—particularly in over-the-counter environments where trading proceeds through request-for-quote protocols, as described in chapter {ref}`market_microstructure`—finding a counterparty may require time and negotiation.

- **Resiliency** refers to how quickly prices recover to their equilibrium level after a transient disturbance caused by a large trade. A resilient market absorbs the temporary impact of a trade and reverts quickly; an illiquid market is one where the price impact is long-lasting and the recovery is slow.

These four dimensions do not always move together. An instrument may display a narrow quoted spread (high tightness) while simultaneously lacking depth—meaning the spread widens dramatically for orders above a certain threshold. Immediacy varies substantially across instrument classes: equities on an electronic exchange offer near-instantaneous execution, while a corporate bond in an OTC market may take hours to find a counterparty willing to trade.

These distinctions also interact with market structure. In quote-driven markets, such as the OTC bond markets described in chapter {ref}`market_microstructure`, tightness is determined by dealer spreads and immediacy by the speed and willingness of dealers to respond; depth and resiliency emerge from the aggregate inventory capacity and risk appetite of the dealer community. In order-driven markets with a central limit order book, all four dimensions are simultaneously visible in the book's structure—tightness from the best bid-ask, depth from the full book profile, and resiliency from the post-trade dynamics.

(sec:liq_structural)=
## Structural predictors of liquidity

Before examining indicators derived from market and trading data, it is useful to consider observable instrument characteristics that are predictive of liquidity without directly quantifying it. These structural features are typically determined at issuance or change slowly over time, making them useful as priors when market data is limited or unreliable.

**Outstanding notional** is the total nominal amount of an instrument in circulation. For bonds, larger issues attract more investors, dealers, and trading interest, generally leading to better liquidity. The relationship is particularly pronounced in fixed-income markets, where small issues may trade only sporadically and lack a natural two-way market.

**Time since issuance** is an especially important predictor in bond markets. Newly issued bonds—known as *on-the-run* securities—are typically highly liquid because they represent the most recent benchmark, attract initial investor flows, and form the basis for derivative pricing and index replication. As time passes and new instruments are issued, older bonds become *off-the-run* and lose trading interest even if their financial characteristics are otherwise unchanged. The *on-the-run / off-the-run* premium is one of the most well-documented liquidity phenomena in fixed-income markets {cite:p}`krishnamurthy2002bond`: off-the-run Treasuries trade at a yield premium to identical-maturity on-the-run bonds, reflecting purely a liquidity discount.

**Benchmark status** amplifies the time-since-issuance effect. Certain bonds are designated as pricing benchmarks for derivatives, index construction, or futures contract settlement. Benchmark bonds attract a disproportionate share of trading activity and systematic rebalancing flows, making them more liquid than neighbouring issues even when their maturity and credit characteristics are similar.

**Credit quality** affects liquidity because high-grade instruments attract a broader and more diverse investor base and can be more readily pledged as collateral in repurchase (repo) transactions (see chapter {ref}`intro_financial_instruments`). Investment-grade bonds are generally more liquid than high-yield bonds; sovereign bonds are more liquid than comparably-dated corporate bonds. The connection runs in both directions: liquidity premia and credit spreads interact, particularly during periods of stress when illiquidity premia widen alongside credit risk {cite:p}`duffie2001liquidity`.

These structural features establish a prior expectation of liquidity that is then updated with real-time market and trading data.

(sec:liq_activity)=
## Activity-based liquidity indicators

Activity-based indicators measure how frequently and in what volume an instrument is traded. They are among the most intuitive proxies for liquidity and require data on actual transactions. In fixed-income markets, such data is available from regulatory reporting systems (such as TRACE in the United States), from inter-dealer brokering platforms, or from dealers' own records of executed transactions.

### Trading frequency and volume

The most direct measure of activity is the **average number of trades per day**, computed over a rolling estimation window. The choice of window length involves a trade-off between statistical stability (favouring longer windows) and responsiveness to changes in liquidity regime (favouring shorter windows); windows of four to eight weeks are common in practice.

Related to this is the **percentage of days traded**—the fraction of trading sessions in which at least one transaction occurred. For very illiquid fixed-income instruments, this ratio can be substantially below one: some bonds may trade only a handful of times per month. The **average period between trades** provides the same information in a more intuitive form: a short inter-trade interval indicates active and continuous liquidity; a long one indicates that traders must wait, bearing market risk, before finding a counterpart.

**Turnover** normalizes trading volume by the size of the issue:

$$\text{Turnover} = \frac{\text{Total volume traded over estimation period}}{\text{Outstanding notional}}$$

By expressing volume relative to the outstanding supply, turnover removes the mechanical relationship between issue size and raw trading volume. An instrument with a small outstanding amount but high absolute volume may still be illiquid if that volume merely reflects the limited supply available to trade. Conversely, high turnover is a strong positive signal of liquidity: it indicates that the outstanding stock of the instrument changes hands frequently, implying an active and two-way market.

**Average trade size** also provides information about liquidity, though its interpretation is less straightforward. In liquid markets, investors tend to break their orders into smaller pieces because finding counterparties is cheap and fast; the average observed trade size is thus smaller. In illiquid markets, traders consolidate activity into fewer, larger transactions to amortize the fixed costs of finding a counterparty, producing a larger average trade size. This effect is sometimes masked by the fact that illiquid instruments also attract larger institutional investors with large minimum order sizes, so the indicator should be interpreted in context.

(sec:liq_impact)=
## Price impact measures

Price impact measures quantify the relationship between trade volume and subsequent price movements. They are closely related to the market impact models discussed in chapter {ref}`execution_fundamentals`, but are applied here to characterize the *inherent* liquidity of an instrument rather than to model the cost of a specific execution strategy. A high price impact per unit of volume is a symptom of illiquidity.

### The Amihud illiquidity ratio

The Amihud illiquidity ratio {cite:p}`amihud2002illiquidity` is the most widely used empirical proxy for price impact. It is defined as the average ratio of the absolute return of a transaction to its volume:

$$\text{Amihud} = \frac{1}{K} \sum_{k=1}^{K} \frac{|\Delta P_k / P_k|}{Q_k}$$

where $K$ is the number of transactions in the estimation window, $\Delta P_k / P_k$ is the percentage price change associated with trade $k$, and $Q_k$ is the volume of that trade. Overnight returns are excluded to avoid confounding the intraday liquidity signal with market-wide overnight information arrivals.

The intuition is immediate: in a liquid market, large trades have a small effect on price because abundant depth absorbs them. In an illiquid market, even modest volume creates substantial price movement. A high Amihud ratio—indicating that small volumes are associated with large returns—is therefore a symptom of illiquidity. Originally proposed for equity markets {cite:p}`amihud2002illiquidity`, the measure has since been adapted for bond markets {cite:p}`bao2011illiquidity`, where it is computed using transaction prices from centralized reporting systems.

The Amihud ratio has a natural connection to the square-root market impact model discussed in chapter {ref}`execution_fundamentals`: if $\Delta P / P \propto \sqrt{Q/V}$ for some daily volume $V$, then the Amihud ratio behaves as $1/\sqrt{Q \cdot V}$, and the measure aggregated across all trades is related to $1/V$. More liquid instruments—with higher daily volume—thus exhibit lower Amihud ratios.

### Hasbrouck's lambda

Hasbrouck's lambda {cite:p}`hasbrouck2009trading` estimates the price impact coefficient via a regression of trade-by-trade returns on signed volume. The specification is:

$$\frac{\Delta P_k}{P_k} = \lambda D_k Q_k + \varepsilon_k$$

where $D_k \in \{-1, +1\}$ is the trade direction (buyer-initiated trades have $D_k = +1$; seller-initiated trades $D_k = -1$), $Q_k$ is the volume, and $\varepsilon_k$ captures other drivers of price change. The estimated coefficient $\hat{\lambda}$ measures the average percentage price impact per unit of signed volume: a larger $\hat{\lambda}$ indicates that a given volume moves prices more, which is a signal of illiquidity.

This specification is the empirical implementation of Kyle's {cite:p}`kyle1985` theoretical model of price impact in a market with informed and uninformed traders. In Kyle's model, the equilibrium price impact slope is proportional to the ratio of informed to uninformed order flow, making it a structural measure of adverse selection—the degree to which price-sensitive, information-based trading drives market-maker losses. Hasbrouck's lambda therefore captures not just market depth but the information content of the order flow, making it particularly relevant for instruments where information asymmetry between dealers and clients is significant.

(sec:liq_tce)=
## Transaction cost estimators

Transaction cost estimators recover the effective bid-ask spread or round-trip trading cost from observable transaction prices. Unlike the price impact measures above, which focus on how much prices move in response to volume, these estimators are designed to capture the *cost of crossing the spread*—the tightness dimension of liquidity—without requiring access to dealer quotes or order book data.

### The Roll estimator

Roll {cite:p}`roll1984` proposed a simple measure of the effective bid-ask spread based on the serial correlation of transaction price changes. The idea is that if transactions alternate between the bid and ask sides of the market, successive price changes will exhibit negative correlation: a buy at the ask (pushing price up) is followed by a sell at the bid (pushing price down), creating a negative autocorrelation that reflects the bid-ask bounce.

Formally, suppose the unobservable mid-price follows a random walk $m_t = m_{t-1} + u_t$ with $u_t$ i.i.d., and the observed transaction price is $P_t = m_t + c D_t$ where $D_t \in \{-1, +1\}$ is i.i.d. trade direction and $c > 0$ is the half-spread. Then:

$$\text{Cov}(\Delta P_k, \Delta P_{k-1}) = -c^2$$

giving the Roll estimator of the half-spread:

$$\hat{c}_{\text{Roll}} = \sqrt{-\text{Cov}(\Delta P_k, \Delta P_{k-1})}$$

and a round-trip spread estimate of $2\hat{c}_{\text{Roll}}$. This estimator requires only a time series of transaction prices, making it applicable in markets where dealer quote data is unavailable—which is typical in many OTC bond markets outside regulated reporting regimes. Its main limitation is that it is only well-defined when the price-change covariance is negative: positive covariance can arise from momentum in mid-prices or from measurement noise, and in those cases the estimator is undefined.

### Price dispersion

Price dispersion {cite:p}`bao2011illiquidity` measures how much transaction prices deviate from a benchmark mid-price reference, weighted by volume:

$$\text{Price dispersion} = \frac{2}{\sum_k Q_k} \sum_{k=1}^{K} \left| \frac{P_k - P^m_{t_k}}{P^m_{t_k}} \right| Q_k$$

where $P^m_{t_k}$ is the mid-price benchmark at the time of transaction $k$ (such as a composite dealer quote or a model-based fair value estimate), and $Q_k$ is the transaction volume. In a liquid market, trade prices cluster tightly around the prevailing mid-price: buyers and sellers transact close to fair value, implying narrow bid-ask spreads. In an illiquid market, buyers pay well above the mid and sellers receive well below it, producing high price dispersion. A higher dispersion value therefore indicates less liquidity.

Unlike the Roll estimator, which exploits the time-series pattern of price changes, price dispersion uses a cross-sectional comparison between transaction prices and an external benchmark. This makes it more robust to persistent price trends but requires a reliable mid-price reference.

### The Schultz regression estimator

A regression-based approach {cite:p}`schultz2001bond` recovers an implied spread by regressing the deviation of transaction prices from the mid-price benchmark on a signed trade indicator:

$$P_k - P^m_{t_k} = \alpha + \beta D_k + \varepsilon_k$$

where $D_k \in \{-1, +1\}$ is the trade direction (positive for dealer sells to client, negative for dealer buys from client), and a positivity constraint $\alpha > 0$ is imposed to prevent negative spread estimates. The estimated intercept $\hat{\alpha}$ captures the average half-spread, so that $2\hat{\alpha}$ is the implied round-trip transaction cost. By pooling all transactions over the estimation window into a single regression, this estimator is more stable than individual matched-pair approaches when transaction flow is sparse.

### Round-trip transaction cost

The round-trip transaction cost directly measures the cost of a complete buy-and-sell cycle. For each pair of a buy trade and a sell trade of equal volume in the same instrument occurring within a short time window (typically a single trading session), the round-trip cost is twice the difference between the buy price and the sell price, normalized by the mid-price. Averaging over all matched pairs in the estimation window gives:

$$\text{Round-trip cost} = \frac{1}{N_{\text{pairs}}} \sum_{j=1}^{N_{\text{pairs}}} \frac{2(P^{\text{buy}}_j - P^{\text{sell}}_j)}{P^m_j}$$

This measure directly captures what a dealer or investor would pay for a round trip. Its limitation is that it requires that matched buy-sell pairs of comparable volume actually occur within the window—a condition that is easily satisfied for liquid instruments but may yield few observations for illiquid ones.

### Quoted and effective spreads

When dealer quote data is available, liquidity can be measured from quoted prices directly. The **quoted spread** is the difference between the best ask and best bid at a given point in time, and the **relative quoted spread** normalizes it by the mid-price:

$$\text{Relative quoted spread} = \frac{P^a_t - P^b_t}{(P^a_t + P^b_t)/2}$$

The **effective spread** captures actual trading costs more precisely than the quoted spread, using the actual execution price relative to the prevailing mid-price:

$$\text{Effective half-spread} = D_k (P_k - P^m_{t_k})$$

where $D_k = +1$ for a buy and $D_k = -1$ for a sell. The effective spread can be lower than the quoted spread (if orders receive price improvement) or higher (if large orders walk up multiple price levels). In bond markets, composite dealer quotes—when available—provide a useful mid-price benchmark for effective spread calculations. The time-series **volatility** of composite prices is also used as a liquidity proxy: illiquid instruments tend to show higher price volatility for the same information flow, because each transaction moves prices more and price discovery is noisier.

(sec:liq_scoring)=
## Aggregating indicators into a liquidity score

The indicators described above capture distinct dimensions of liquidity and may be available from different data sources. Individual metrics are imperfect proxies: each captures only one aspect of liquidity and is subject to its own measurement noise. The practitioner's goal is to combine them into a composite **liquidity score** that provides a stable, comprehensive ranking of instruments. Three broad methodologies are used for this aggregation.

### Ranking aggregation

The simplest approach ranks each instrument by each metric and averages the ranks. For $M$ metrics and $N$ instruments in the universe:

1. For each metric $m$, compute the rank $r_{i,m} \in \{1, \ldots, N\}$ of instrument $i$, assigning rank 1 to the most liquid. For metrics where higher values indicate less liquidity (such as the Amihud ratio), invert the metric before ranking.
2. Compute the average rank for each instrument: $\bar{r}_i = M_i^{-1} \sum_m r_{i,m}$, where $M_i$ is the number of metrics available for instrument $i$. Missing metrics are excluded from the average.
3. Normalize to the $[0, 1]$ interval:

$$l_i = \frac{\bar{r}_i - \min_j \bar{r}_j}{\max_j \bar{r}_j - \min_j \bar{r}_j}$$

The resulting score $l_i$ is interpretable as a relative liquidity rank: an instrument with $l_i = 1$ is the most liquid in the universe, and one with $l_i = 0$ is the least liquid. The advantages are simplicity, interpretability, robustness to outliers (since ranks are bounded), and natural tolerance of missing data. The key limitation is that the score is purely relative: it depends on the composition of the universe and is not directly comparable across portfolios or across time unless the universe is held constant.

### PCA-based aggregation

A more data-driven approach uses Principal Component Analysis (PCA) to extract a composite factor from the joint distribution of liquidity metrics. If all metrics are imperfect proxies of the same underlying latent construct, the first principal component should align with the common liquidity signal, as it captures the direction of maximum variance across the cross-section.

Let $\mathbf{X}$ be the $N \times M$ matrix of standardized metrics (each column $z$-scored to zero mean and unit variance across the universe at a given date). The PCA decomposition $\mathbf{X} = \mathbf{U \Sigma V}^T$ identifies the directions of maximum variance. The liquidity score is the projection onto the first right singular vector $\mathbf{v}_1$:

$$\mathbf{l} = \mathbf{X} \mathbf{v}_1$$

The sign of $\mathbf{v}_1$ must be checked: if it loads negatively on metrics that should be higher for more liquid instruments (such as turnover), the sign of the resulting score should be flipped. Final scores are typically expressed as $z$-scores relative to the cross-section.

The PCA approach weights metrics according to their common variance, which can provide information about which indicators are most informative. It also produces a score on an absolute scale (within a given cross-section), so that the distribution of scores across instruments is interpretable. The limitation is that PCA maximizes explained *variance*, not explained *liquidity signal*: if some metrics are particularly noisy, PCA may overweight them simply because they contribute more variance.

### Machine learning approaches

A predictive approach uses a supervised model to forecast one target liquidity metric from the others. The fitted model's feature importances then provide weights for combining the input metrics into a composite score.

For example, one may train a regularized linear model (such as Lasso regression; see {ref}`sec:ddm_regularization`) or an ensemble model (such as a random forest; see {ref}`sec:ddm_trees`) to predict an observable forward-looking liquidity indicator—such as future turnover or future trading frequency—from current activity, price impact, and spread metrics. A shared model trained across all instruments provides a consistent calibration. Feature importances from the fitted model determine the relative weights of each input in the composite score, which is then normalized for comparability.

The advantage of this approach is that weights reflect actual predictive relevance—an empirically grounded criterion for what matters for future liquidity. Its disadvantages include the requirement for sufficient historical data to train and validate the model, and the risk that the composite score is biased toward the specific target metric chosen, rather than reflecting liquidity in a broader sense.

(sec:liq_marketmaking)=
## Liquidity and market making: inventory rotation

A particularly useful application of liquidity modelling in the context of this book is the estimation of the **inventory rotation time**: the expected time for a market maker to eliminate an open inventory position through the natural flow of incoming client orders. Unlike market-wide liquidity metrics, the inventory rotation time measures liquidity from the perspective of a specific dealer operating in a specific instrument, conditioning on the flow of requests that dealer receives.

### Motivation

As discussed in chapter {ref}`optimal_market_making`, a market maker in a dealer market (such as an OTC bond market) earns revenue by quoting bid and ask prices to clients requesting trades. By the nature of this business, the dealer may accumulate inventory when more clients wish to sell than to buy (or vice versa) within a given period. This inventory position carries risk: the dealer is exposed to adverse price movements until the position is unwound. The cost of carrying inventory is a central input in the optimal spread-setting problem.

The inventory rotation time quantifies how long a dealer can expect to wait, under an optimal pricing policy, for incoming client flow to naturally reverse the position—without requiring an active hedge at an unfavorable price. A short rotation time indicates that client flow is sufficient to quickly net out the position; a long rotation time implies that the dealer must either tolerate prolonged inventory risk or actively hedge in the market at potentially adverse prices.

### Dependence on liquidity characteristics

Within the Avellaneda-Stoikov framework detailed in chapter {ref}`optimal_market_making`, the inventory rotation time $\tau_{1/2}$ (defined as the expected time for inventory to be reduced to half its initial size under optimal quoting) can be derived analytically. The result depends on the following parameters:

- **$A$**: the rate of incoming client requests (requests per unit time). A higher flow rate means the market maker can expect to find a natural counterpart sooner, reducing the rotation time.
- **$\bar{x}$**: the average size of each request. Larger trade sizes reduce the number of trades needed to rotate a given inventory level.
- **$\alpha$**: the clients' price sensitivity coefficient. In the exponential win-probability model $p(\text{win} \mid \delta) = p_0 e^{-\alpha \delta}$, a larger $\alpha$ means clients are more sensitive to the quoted spread. Highly price-sensitive clients will only accept tight spreads, which limits the dealer's ability to quote asymmetrically to attract flow on the desired side.
- **$\sigma$**: the volatility of the instrument. Higher volatility increases the cost of holding inventory and forces the dealer to quote wider spreads to compensate, reducing the win probability and slowing inventory rotation.
- **$p_0$**: the baseline probability of winning a client request at the mid-price. This encodes the competitive intensity of the dealer's market: a dealer with a strong client franchise that wins frequently even at mid has a lower effective rotation time.

The key qualitative insight is that liquid instruments—characterized by high $A$, large $\bar{x}$, high $p_0$, and low $\sigma$—have short rotation times and thus low inventory risk per trade, allowing the dealer to quote tighter spreads. Illiquid instruments have long rotation times, imply high inventory risk, and justify wider spreads. This provides a principled link between liquidity measurement (as described in the earlier sections of this chapter) and optimal market-making behaviour.

### Connection to the liquidity score

The parameters that determine the inventory rotation time—arrival rate $A$, average size $\bar{x}$, and volatility $\sigma$—are directly related to the activity-based and spread-based liquidity indicators discussed earlier. A high trading frequency (low $A^{-1}$) and high turnover directly reduce the rotation time. A low price dispersion or tight effective spread indicates that clients trade near the mid, corresponding to a high $p_0$ and low effective cost. This connection means that a well-constructed liquidity score should be broadly predictive of the inventory rotation time, making it a natural input to the optimal spread models of chapter {ref}`optimal_market_making` and to the enrichments of the Avellaneda-Stoikov model discussed in section {ref}`sec:omm_enrich`.

(sec:liq_dynamics)=
## Dynamic properties of liquidity

Liquidity is not a static property: it varies within the trading day, across market conditions, and over longer horizons. Understanding these dynamics is essential for both market-making and execution.

### Intraday liquidity patterns

Empirical studies consistently document systematic intraday variation in liquidity, mirroring the volume patterns discussed in chapter {ref}`execution_fundamentals`. Bid-ask spreads are typically wide at the market open, as dealers face uncertainty about the overnight information set and initial order imbalances have not yet cleared. Liquidity tends to improve through the morning as information is incorporated into prices and two-way flow from a diverse range of participants balances the book. In many markets, a second period of elevated activity and tighter spreads occurs near the close, driven by end-of-day portfolio rebalancing, benchmark hedging, and index replication flows {cite:p}`cartea2015algorithmic`.

These intraday patterns have direct implications for execution algorithm design: consuming liquidity is cheaper at certain times of day, and strategies that are sensitive to spread costs—such as aggressive market orders—should preferentially execute during high-liquidity windows.

### Liquidity and volatility

Liquidity and volatility are closely connected. The bid-ask spread that a rational market maker quotes must compensate for the risk of holding inventory, which is proportional to the volatility of the instrument (see chapter {ref}`optimal_market_making`). As a result, spreads widen when volatility rises. This relationship works in both directions: wider spreads increase the effective cost of trading, which can reduce order flow and further widen spreads in a self-reinforcing dynamic.

The connection is also visible in the Amihud ratio: since the numerator is $|\Delta P / P|$ and the denominator is volume $Q$, the Amihud ratio is elevated whenever price volatility is high relative to trading activity. Care must therefore be taken when interpreting activity-based and price-impact liquidity indicators in periods of market stress: deteriorating scores may reflect genuine illiquidity or may partially reflect elevated market-wide volatility.

### Liquidity during market stress

Liquidity is procyclical: it tends to deteriorate precisely when market participants most need it. During periods of market stress—characterized by sharp price moves, increased correlation across assets, and heightened uncertainty—bid-ask spreads widen, depth declines, and resiliency weakens. This deterioration reflects the rational response of liquidity providers who face greater adverse selection risk (clients with superior information are more likely to trade in stressed conditions) and higher inventory hedging costs {cite:p}`duffie2001liquidity`.

A practical consequence is that liquidity scores estimated from trailing historical data may be misleadingly optimistic during the onset of a stress event. This argues for incorporating real-time liquidity signals—such as current quoted spreads, recent transaction frequency, or measures of dealer inventory pressure—as complements to the backward-looking composite scores. The combination of structural, activity-based, and real-time liquidity information provides the most complete picture of an instrument's current liquidity conditions.

## Exercises

1. Using simulated trade data in which a market maker alternates between bid and ask executions, verify that the Roll estimator correctly recovers the half-spread. Examine what happens to the estimator when the underlying mid-price has a non-zero drift.

2. Compute the Amihud illiquidity ratio on a simulated series of trades with a known price impact function. Verify that the Amihud ratio is inversely related to market depth. How does the estimator behave when trade sizes are clustered (e.g., power-law distributed)?

3. Apply ranking aggregation, PCA, and a machine learning approach (e.g., Lasso regression predicting forward turnover) to a panel of simulated liquidity metrics. Compare the composite scores produced by each method. Under what conditions do the methods agree, and when do they diverge?

4. In the context of the inventory rotation time, examine how the expected half-life of inventory changes as a function of each of the parameters $A$, $\bar{x}$, $\alpha$, $\sigma$, and $p_0$. What combination of parameter values would best represent an on-the-run sovereign bond? An off-the-run corporate bond?

5. Using intraday transaction data, construct a time series of the Amihud ratio at hourly frequency over a trading day. Characterize the intraday pattern and discuss its implications for the design of an execution algorithm that seeks to minimize market impact.
