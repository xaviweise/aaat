(algorithmic_trading)=
# Algorithmic Trading

## Introduction

Algorithmic trading refers to the use of computer programs to automate the process of making trading decisions and executing orders in financial markets. Although the term is widely used, its precise meaning can vary depending on the context and the regulatory framework. Two influential definitions are the following:

* Bank for International Settlements (BIS, 2016){cite:p}`BIS2016ElectronicTradingFixedIncome`:
*Trading technology in which order and trade decisions are made electronically and autonomously.*

* MiFID II (Directive 2014/65/EU, Article 4, Definition 39){cite:p}`MiFIDII2014`:
 *Trading in financial instruments where a computer algorithm automatically determines individual parameters of orders such as whether to initiate the order, the timing, price or quantity of the order or how to manage the order after its submission, with limited or no human intervention.*

Notice that we use the terms algorithmic trading and automated trading as synonyms. In some references, algorithmic trading is used more narrowly to denote algorithmic execution, a specific form of automated trading focused on the optimal execution of predefined orders.

A relevant point to notice is that those definitions don't necessarily imply full automation, particularly in the order submission. Although early interpretations of these definitions suggested that any order that has to be confirmed by a human is immediately out of the scope of algorithmic trading: in 2026, ESMA has clarified that if order parameters, like price and volume, are computed by an algorithm, the final confirmation by a human does not exclude the order to be classified as algorithmically generated {cite:p}`esma2026algotrading` . 

Algorithmic trading can be viewed as a subset of *systematic trading*, which refers to any trading strategy defined in a rule-based, methodical manner. It is also a subset of *quantitative trading*, where trading decisions follow the principles of the scientific method. In this framework, we first construct a scientific model of the trading environment—for example, a stochastic process such as a random walk—to represent market dynamics. This model is then used to derive inferences about quantities of interest, such as the likely range or direction of future prices. These inferences serve as inputs to mathematical optimization procedures, which determine the optimal trading actions—such as when and at what levels to trade—under given objectives and constraints.

The MiFID II definition is intentionally broad. It encompasses both complex, fully automated trading strategies and simpler automated rules, such as dynamic stop-loss orders or RfQ auto-negotiation rules. The exception being complex orders that are directly implemented within a exchange, which are considered part of the market infrastructure. 
In the following discussion, we will adopt the first, more restrictive definition, focusing on more advanced algorithmic strategies where automation plays a central role in decision-making and execution.
 
 ### High-Frequency Trading

High-Frequency Trading (HFT) is a subset of algorithmic trading distinguished by extremely short holding periods, rapid order submission and cancellation, and technological infrastructures designed to minimize latency. According to the Bank for International Settlements {cite:p}`BIS2016ElectronicTradingFixedIncome`, HFT is a “subset of automated trading in which orders are submitted and trades executed at high speed, usually measured in microseconds, and a very tight intraday inventory position is maintained.” Such strategies seek to gain advantage from the ability to process information on market conditions and react almost instantaneously, typically resulting in a very large number of small trades, held for short periods, and generating substantial message traffic. To achieve this, HFT firms tend to place their trading servers physically close to the electronic market’s matching engines—a practice known as co-location—to minimize transmission delays or latency.

At the European regulatory level, MiFID II (Directive 2014/65/EU, Article 4(1)(40)) {cite:p}`MiFIDII2014` defines HFT as an algorithmic trading technique that relies on infrastructure designed to minimize latency, such as co-location, proximity hosting, or high-speed direct electronic access, and in which individual trades or orders are initiated, generated, routed, or executed by systems without human intervention. It also specifies that such activity typically involves high intraday message rates consisting of orders, quotes, or cancellations.

In practice, low-latency infrastructures are at the core of HFT. Co-location refers to hosting trading servers directly within or adjacent to an exchange’s data center to reduce round-trip latency to microseconds. Examples include Equinix LD4 in Slough (London) and NY4 in Secaucus (New Jersey), which host a large portion of global financial trading infrastructure. Proximity hosting involves maintaining servers in nearby facilities linked via dedicated fiber, while high-speed network access often relies on optimized fiber or microwave connections between major trading hubs (for instance, London–Frankfurt or New York–Chicago routes). Even marginal reductions in latency—on the order of microseconds—can yield significant competitive advantages in markets where prices evolve continuously and across fragmented venues.

HFT strategies themselves vary in scope and complexity. Common approaches include electronic market making, where firms continuously quote bid and ask prices and manage risk within very short horizons; statistical and cross-venue arbitrage, which exploit fleeting price discrepancies between related instruments or exchanges; latency arbitrage, which reacts faster than competitors to public information or order book events; and smart order routing, which optimizes execution quality across multiple venues, sometimes also to capture fee rebates or queue priority. These strategies generate immense volumes of order messages and depend critically on precise market data, optimized software, and sophisticated risk controls.

From a regulatory perspective, MiFID II and MiFIR introduced a harmonized framework for algorithmic and high-frequency trading, elaborated through Regulatory Technical Standard 6 (RTS-6) {cite:p}`ESMA_RTS6_2016`, which defines organizational, risk-control, and testing requirements. As with all European directives, MiFID II provisions must be transposed into national law, and implementation may differ across jurisdictions. For example, Germany’s High-Frequency Trading Act {cite:p}`BaFinHFTAct2013` introduced an explicit authorization regime for HFT firms and added an additional criterion based on the speed of the connection, ensuring that firms not genuinely engaged in high-frequency activity would not fall under the same regulatory burden. These frameworks impose significant obligations on HFT firms, including mandatory system testing, kill switches, message-rate controls, record-keeping, and stringent resilience standards—all of which contribute to higher compliance costs and operational complexity.

Despite their efficiency benefits, HFT firms have attracted public and regulatory scrutiny. Critics argue that practices such as latency arbitrage or preferential access to dark pools create an uneven playing field, eroding confidence in market fairness. Michael Lewis’s Flash Boys {cite:p}`Lewis2014FlashBoys` popularized this perception by portraying HFT as exploiting microscopic speed advantages to anticipate and “front-run” slower participants, contributing to the view that HFT is inherently predatory. Although many of these practices are fully compliant with market rules, they raise ethical and transparency questions, particularly in fragmented markets where access to speed and information is uneven.

Regulators are also concerned about the systemic implications of HFT. The Flash Crash of May 6, 2010 {cite:p}`CFTC_SEC2010FlashCrash` illustrated how rapid, automated interactions among algorithms could amplify volatility and cause temporary dislocations. Two main risks are frequently cited {cite:p}`ESMAHFT2019` {cite:p}`BIS2018HFTRisks`: false liquidity—where HFT appears to provide deep liquidity in normal conditions but withdraws it abruptly during stress—and algorithmic herding, when many algorithms respond similarly to the same signals, creating self-reinforcing price dynamics. To mitigate these risks, regulators have implemented safeguards such as circuit breakers, message-rate limits, and system testing obligations.

Yet, it is important to balance these concerns against the structural role HFT plays in modern markets. By continuously arbitraging prices across venues, narrowing spreads, and enhancing price consistency, HFT contributes to market efficiency and liquidity provision under most conditions. The regulatory challenge is therefore not to constrain speed itself, but to ensure that technological advantages do not compromise fairness or stability. In this sense, HFT embodies both the promise and the tension of modern market microstructure: the pursuit of efficiency through automation, bounded by the need to maintain integrity and resilience in the face of ever-faster financial systems.
 
## Algorithmic Trading Growth

The growth of algorithmic trading is closely tied to the broader electronification of financial markets, since of course algorithms can only in principle operate when markets provide electronic protocols for submitting, routing, and cancelling orders automatically. Traditionally, this requirement limited algorithmic participation to venues with fully electronic limit-order books or standardized API-based access. However, this constraint may gradually weaken with the emergence of [Generative AI](generative_ai.md) models—large language models, multimodal systems, and real-time audio models—that could enable algorithmic strategies to interact with voice, chat, and email-based trading workflows. Such systems may eventually allow automation to extend into execution channels that historically relied on human-to-human communication, potentially reshaping parts of OTC, RFQ, and relationship-driven markets.

Across major markets, empirical studies consistently show a structural transition from manual and voice-based execution to electronic and then algorithmic execution. SEC market-structure analyses report that by the late 2010s much of U.S. trading activity in the capital markets is executed electronically, with automated execution constituting a large portion of activity {cite:p}`SEC2020AlgoTrading`. Measurements of algorithmic and HFT share vary depending on methodology—whether based on order messages, trade count, or value traded—but most empirical work places algorithmic/HFT participation in U.S. equities in the range of 40–60% during the 2010s. Studies using more recent data at millisecond or microsecond granularity reveal that while HFT’s share of displayed liquidity peaked in the mid-2010s, algorithmic activity remains central to U.S. market functioning. A recent reconstruction of HFT participation from 2012 to 2023 shows persistent, high algorithmic involvement across the full universe of listed stocks {cite:p}`Boehmer2024HFT`

In Europe, ESMA’s empirical reviews of MiFID markets confirm that algorithmic trading expanded rapidly after 2007, driven by fragmentation and the introduction of new trading venues. While HFT participation in European equities is generally found to be lower than in the United States —often around one-third of trading depending on the metric—, algorithmic order submission and cancellation rates are substantial, and similar structural patterns emerge: high electronic venue reliance, dense order-book activity, and widespread use of automated execution by intermediaries and buy-side institutions {cite:p}`ESMA2014HFT` {cite:p}`ESMAHFT2021`. ESMA’s multi-year datasets also document significant cross-country heterogeneity, with markets such as the UK and the Netherlands exhibiting higher algorithmic intensity than smaller or less-fragmented continental venues.

In the Asia–Pacific region, algorithmic trading expanded at a later stage but has shown strong growth wherever electronic limit order-book infrastructure is well developed. Empirical studies on the Tokyo Stock Exchange report substantial algorithmic and HFT participation from the mid-2010s onward, driven by improvements in exchange matching technology {cite:p}`Hosaka2014`. Similar patterns appear in Australia, Korea, and, increasingly, select Chinese markets. The region is more heterogeneous than Europe or the United States: in several Asian jurisdictions the persistence of voice or hybrid OTC mechanisms constrains the penetration of high-speed algorithmic strategies. Where low-latency access and co-location are available, algorithmic trading tends to scale rapidly.

The growth of algorithmic trading also differs markedly across asset classes. Equities exhibit the deepest empirical record: numerous studies show that algorithmic execution and HFT reshaped equity microstructure by increasing order-book depth, tightening spreads, and raising message traffic. Futures and derivatives markets have experienced a similarly strong expansion. CFTC-backed studies show that between 2012 and 2018 many major U.S. futures contracts saw sharp increases in HFT share, in some cases more than doubling relative to early-2010s baselines {cite:p}`CFTCFuturesAutomated`. Derivatives markets, being fully electronic and centrally cleared, are particularly conducive to high-speed algorithmic strategies, and empirical work documents widespread cross-asset and cross-venue arbitrage activity.

FX markets present a more complex case due to their predominantly OTC structure. BIS fact-finding studies nonetheless show rising algorithmic and HFT presence in electronic spot-FX platforms such as EBS and Reuters venues {cite:p}`BIS2011`. Here, algorithmic trading is concentrated in highly liquid currency pairs (G10 countries) and in segments where anonymous, central-limit-order-book trading is available; elsewhere, voice trading and relationship-based bilateral execution remain dominant. 

In fixed income markets the evidence points to a steady but uneven rise in automation. ICMA and New York Fed research finds that electronification, especially on all-to-all corporate bond platforms and electronic interdealer Treasury markets, has enabled algorithmic strategies to scale. However, voice and RFQ mechanisms continue to retain significant market share in many bond categories. Algorithmic market making in bond futures has grown particularly quickly, mirroring the pattern observed in equity index futures {cite:p}`Bech2016` {cite:p}`NYFed2021Treasuries`.

Finally, cryptocurrency markets have undergone one of the fastest transitions to algorithmic execution. Empirical studies using millisecond-level data show that, from the mid-2010s onward, many large crypto exchanges experienced rapid growth in latency-sensitive strategies, cross-venue arbitrage, and automated market making. Fragmentation across exchanges, low latency APIs, and continuous trading environments have resulted in market microstructures that resemble early electronic equities: high message traffic, narrow spreads in liquid pairs, and a strong role for algorithmic intermediaries {cite:p}`Makarov2020CryptoHFT`.

Taken together, empirical research shows that algorithmic trading expands most rapidly in markets that have electronic order books, provide direct or low-latency access, and standardize market data and clearing processes. Regional patterns differ: U.S. markets lead, Europe follows with strong regulatory oversight, and Asia expands heterogeneously, but the underlying trajectory is similar. Across asset classes, algorithmic activity is most advanced in equities and futures, growing in FX and fixed income as electronification proceeds, and already dominant in many crypto venues. The result is a global, multi-asset shift in which algorithmic strategies have become a central mechanism for price formation, liquidity provision, and execution quality in modern markets.

## Reasons to use Algorithmic Trading

The widespread adoption of algorithmic trading across financial markets is driven by a combination of technological, economic, and organisational factors. At its core, algorithmic trading enables market participants to operate more efficiently, consistently, and at scale than would be possible through purely manual processes.

A primary motivation for using trading algorithms is **speed**. Computer algorithms can submit orders and react to changes in market conditions in timeframes far shorter than those accessible to human traders. In electronic markets, where prices and liquidity can change within milliseconds, this speed advantage is often essential, particularly for strategies that rely on short-lived opportunities or rapid risk adjustments.

Closely related to speed is the ability of algorithms to perform **large-scale information processing**. Trading algorithms can simultaneously monitor and analyse multiple data sources, including prices, order books, volumes, and derived indicators across many instruments and markets. This parallel processing capability allows algorithms to detect patterns and respond to market signals that would be difficult or impossible for a human trader to observe in real time.

Algorithmic trading also provides **scalability**. Once developed, an algorithm can be deployed across a large number of instruments, markets, or client orders with minimal incremental cost. This enables firms to increase trading activity and market coverage without a proportional increase in human headcount. Scalability is particularly important for institutions managing large portfolios, operating multiple strategies concurrently, or providing execution and liquidity services to many clients.

Another key advantage is the promotion of **systematic trading**. Algorithms enforce a disciplined and repeatable decision-making process, reducing the influence of emotions such as fear, overconfidence, or hesitation. This systematic approach facilitates rigorous evaluation of strategy performance using historical data, allows meaningful comparisons between alternative strategies, and supports continuous improvement through testing and refinement. While systematic trading is not exclusive to algorithms, automation makes it far easier to apply consistently over time and at scale.

Trading algorithms are also naturally aligned with a **quantitative approach** to trading, so much than in {cite:p}`BIS2011`, they are defined as "the use of computers and *advanced mathematical models* to make decisions about the timing, price and quantity of a market order". They enable the explicit formulation of objectives—such as minimising execution costs, controlling inventory risk, or maximising profit and loss—within a mathematical or statistical framework. By doing so, algorithms can optimise trading decisions in a consistent manner, subject to clearly defined constraints. This is particularly evident in execution algorithms that seek to minimise transaction costs and in market-making algorithms that aim to balance profitability against inventory and risk limits.

Finally, algorithmic trading helps to reduce human errors. Manual trading is susceptible to operational mistakes, such as incorrect order sizes, prices, or instruments, often referred to as “fat-finger” errors. By automating order generation and routing, algorithms can significantly lower the incidence of such errors. At the same time, it is important to recognise that automation introduces its own set of risks, including software bugs, model errors, and system failures. These risks do not negate the benefits of algorithmic trading, but they do require robust governance, testing, and monitoring frameworks, which are addressed in later chapters.

## A Brief History of Algorithmic Trading

The evolution of algorithmic trading is deeply intertwined with the broader digitisation of financial markets. In the 1970s and 1980s, exchanges began computerising order workflows, while quantitative finance—particularly the Black–Scholes framework {cite:p}`black1973pricing`—rapidly entered trading practice. Black–Scholes provided a replicating-portfolio logic that could be encoded into dynamic rules, enabling strategies such as portfolio insurance, which sought to mimic a put option by mechanically selling futures as markets fell. As computers automated these adjustments, model-driven execution became one of the first large-scale uses of electronic trading logic. During the 1987 crash, the pro-cyclical behaviour of these strategies—selling as prices declined—was widely seen as amplifying market stress, revealing how model-based, computerised trading could interact with volatility in destabilising ways.

Through the 1990s, electronic trading accelerated. Several U.S. exchanges migrated to fully electronic execution, and new electronic communication networks (ECNs) such as Island and Archipelago fostered a more competitive, fragmented market structure. Decimalisation in 2001 further reduced tick sizes and compressed spreads, creating conditions that favoured automation. Early statistical arbitrage strategies, including pairs trading, became prominent in this era, with pioneering work at Morgan Stanley and subsequent developments by David Shaw, James Simons, and others who would later build systematic hedge funds. At the academic frontier, Bertsimas and Lo {cite:p}`BERTSIMAS19981`, followed by Almgren and Chriss {cite:p}`almgren2000optimal`, created a rigorous mathematical foundation for optimal trade execution, establishing the framework that still underpins institutional execution algorithms today.

The 2000s saw rapid advances in connectivity, co-location, and message-handling infrastructure. As latency budgets shrank, high-frequency trading (HFT) grew from a niche practice into a major component of equity-market activity. Regulatory changes—in particular Regulation NMS in the United States and MiFID I in Europe—encouraged venue competition and liquidity fragmentation, making automated smart order routing essential for best execution. Around the same period, Avellaneda and Stoikov (2008) {cite:p}`AvellanedaStoikov2008` introduced a dynamic framework for limit-order-book market making, which became one of the theoretical cornerstones of modern electronic liquidity provision.

By the end of the decade, HFT accounted for a substantial share of U.S. equity volumes, though competition subsequently reduced margins. The “Flash Crash” of 6 May 2010 demonstrated the speed and interconnectedness of automated strategies: a large sell algorithm interacting with aggressive HFT flows produced a rapid, self-reinforcing price collapse across multiple asset classes before markets recovered minutes later. After 2010, firms increasingly pushed for technological edge through specialised hardware such as FPGAs and—critically—through the deployment of microwave and later millimetre-wave transmission networks. These reduced Chicago–New Jersey latency close to the physical limit achievable in the atmosphere.

During the 2010s, automated ingestion of unstructured data emerged as another frontier. Firms began deploying real-time news analytics, and by 2012 platforms such as Dataminr enabled machine-readable detection of market-relevant events from public information flows. Twitter-based signals were incorporated into professional terminals, although early episodes such as the 2013 hacked Associated Press tweet showed the risks inherent in embedding fast-reaction systems into the market ecosystem. Meanwhile, crypto-asset markets developed their own microstructures, with HFT-style market making and arbitrage quickly dominating trading on major exchanges by the mid-2010s.

The late 2010s brought an increase in experimentation with machine learning in execution optimisation, short-horizon prediction, and market-making parametrisation. Reinforcement learning, in particular, attracted academic and industry attention, although deployment into truly latency-critical or autonomous production systems remained limited. Most firms adopted ML in peripheral or advisory capacities—signal generation, short-term prediction, and parameter tuning—rather than placing machine learning models directly “in the loop” for continuous order submission.

The 2020s introduced several structural developments. Cloud-based trading infrastructure matured, allowing firms to shift large-scale analytics, simulation, and historical data processing to scalable cloud compute while continuing to run their latency-sensitive components on dedicated hardware. Alternative datasets, spanning geospatial indicators, mobility traces, supply-chain data, and ESG-linked information, became integrated into quantitative research pipelines, further blurring the boundary between traditional quant signals and broader data science.

Generative AI technologies, including large language models, began to influence research, monitoring, and operational workflows. Firms are actively experimenting with these tools—for example in news classification, documentation analysis, surveillance, and compliance—but there is little evidence of LLMs being embedded directly into production trading engines. Their role remains largely complementary: accelerating research, aiding supervision, or supporting decision-making rather than autonomously driving order flow.

Events such as the extreme volatility during the COVID-19 market shock reinforced the centrality of algorithmic trading to market functioning: automated execution models proved adaptable under stress, yet liquidity provision by HFT market makers contracted at critical moments, widening spreads and exposing structural fragilities. In crypto-asset markets, the 2022 crisis offered a parallel demonstration of algorithmic microstructure dynamics—latency races, liquidity evaporation, and execution-layer vulnerabilities—within a largely unregulated environment.

Across these decades, algorithmic trading evolved from a narrow automation tool into a comprehensive technological discipline encompassing market microstructure, optimisation, data engineering, and increasingly advanced machine learning. While the foundational principles of execution and liquidity provision remain rooted in the early models of the 1990s and 2000s, the field continues to expand, shaped by hardware frontiers, data availability, and new analytical methods. The next stage of development will likely come from integrating these elements—systematic modelling, high-performance infrastructure, and advanced AI—while maintaining the stringent reliability and control standards required in live markets.

## Types of Trading Algorithms

Trading algorithms can be grouped into a small number of broad categories according to their primary economic objective and their mode of interaction with financial markets. While real-world strategies often combine elements of more than one category, this classification provides a useful analytical framework for understanding the role algorithms play in modern trading systems. At a high level, trading algorithms can be divided into execution algorithms, market-making algorithms, and investment algorithms. Each category reflects a distinct function within the trading process, ranging from the efficient implementation of decisions, to the provision of liquidity, to the allocation of capital with the expectation of future returns.

### Execution Algorithms

The goal of executing algorithms is to buy or sell a financial instrument minimising the transaction costs. In this setting, the decision to trade is taken outside the algorithm, for example by a portfolio manager, risk manager, or also another trading algorithm. The algorithm’s role is to determine how to trade, taking into account market conditions, liquidity, and the structure of the trading venue.

These algorithms are particularly important when trading large volumes in markets organised around a limit order book. Liquidity at the best bid or offer is often insufficient to absorb a large order without significant price concessions. A naïve execution, such as submitting a single market order, would therefore result in substantial transaction costs, also called temporary market impact. The alternative of using limit orders does not guarantee execution and might signal other players the interest to transact. They might react modifying their orders in a way that adversely impact our cost of execution, for example by removing orders in the opposite side of the order book and placing them at less favourable prices. In both cases, the information conferred by these orders might produce a longer term effect on the other players, for instance affecting the likelihood of arrival of other investor's orders or the price at which they are willing to trade. This is called the permanent market impact. The following figure illustrates this trade-off at the level of primitive orders. 

```{figure} figures/limit_vs_market.png
:name: fig:limit_vs_market
:width: 8in
Illustration of the trade-off between executing an order in a limit order book (upper left) using market orders (upper right) or limit orders (lower left). Market orders guarantee immediacy of execution but incur in worse execution prices, since they consume the available liquidity. Limit orders can execute at more favourably prices, but their execution is not guaranteed.
```

This trade-off between market impact and execution probability is at the heart of the design of execution algorithms. Notice that execution probability translates into market or price risk if the algorithm must fill the full order, since prices might move adversely (but also, of course, favourably) if the order is not executed immediately. In general, execution algorithms seek to address this problem by intelligently deciding how to split the full order (also called the parent order) into smaller chunks (child orders) in order to reduce the market impact while keeping price risk under control. The algorithm not only decides the type and size of the child orders. It also can delay their submission to avoid leaking information to the market and expecting that the liquidity consumed will be replenished by new orders arriving to the market. 

For example, a simple execution strategy is the TWAP (Time Weighted Average Price), which splits the order in chunks of equal size that are executed over a given period of time (e.g. a trading session) during certain allocated time buckets (e.g. five minutes buckets). For example, an order of 300 shares to be executed during the next hour using a TWAP algorithm could be divided in twelve chunks of 25 shares to be executed every 5 minutes. Every chunk of 25 shares is then executed in the limit order book using primitive orders, e.g. a combination of limit orders and market orders. The following figure illustrates such strategy.

```{figure} figures/twap.png
:name: fig:twap
:width: 8in
Simple sketch of Time Weighted Average Price (TWAP) execution schedule, where an equal number of shares are allocated to equal time buckets over the proposed execution period. Within each bucket, the allocated order is executed using a combination of primitive orders. A TWAP strategy is a simple way to reduce market impact in execution without compromising the execution of the full order.
```

As we wil discuss in chapter {ref}`execution_fundamentals`, there is a large variety of standard execution algorithms that can be used depending on the objectives and profile of the party submitting the order. For instance, for orders that target the average price of the orders executed in the market during the execution window, there is the VWAP (Volume Weighted Average Price) algorithm. And the family of Implementation Shortfall execution algorithms allow to adjust the market impact vs price risk trade-off to the risk tolerance of the investor. 

### Market Making algorithms

Market-making algorithms are concerned with the continuous provision of liquidity to financial markets. These algorithms stand ready to buy and sell a financial instrument by continuously quoting bid and ask prices. The economic compensation for providing this immediacy is the bid–ask spread, which must cover both operating costs and the risks inherent in the activity.

Two main sources of risk characterise market making. The first is inventory risk, which arises because the market maker must hold positions in order to provide liquidity. If prices move unfavourably, the value of this inventory may decline. The second is information asymmetry, whereby counterparties may trade on superior information, leaving the market maker exposed to adverse selection. These risks explain why market makers typically quote prices away from a perceived fair value rather than at the mid-price. Additionally, the market-maker needs to strike a balance between the frequency of trading and the profitability per round-trip of buying and selling, determined by the spreads quoted. Since a high-frequency and low-profit strategy can be seen to have a lower volatility of overall profits & losses for the market-maker, this trade-off is also considered a form of risk, named transactional risk.

Algorithmic market making automates the process of quote generation and risk management. A full market-making algorithm typically needs to maintain good estimations of the fair price of the instrument quoted and determine appropriate bid and ask quotes around that price, taking into account current market conditions and internal risk constraints. Quotes may be adjusted asymmetrically to manage inventory, for example by quoting more aggressively on one side of the market to reduce accumulated exposure. In many implementations, inventory risk is further mitigated through automatic hedging using correlated instruments. The following figure sketches the components of a market-making algorithm for Interest Rate Swaps:

```{figure} figures/market-making.png
:name: fig:market_making
:width: 8in
A market-making algorithm for standard Interest Rate Swaps (IRS) quoted in interbank markets based on a limit order book. The main components of the algorithm are 1) fair price determination (mid-price in the order book), 2) spread determination, 3) hedging portfolio exposures, in this case using liquid futures on government bonds.
```

These algorithms are widely used by broker-dealers, particularly for smaller transactions, allowing human traders to focus on larger or more complex trades. They are also central to the business models of electronic liquidity providers and high-frequency trading firms. Market-making algorithms operate across different market structures, including order-driven, quote-driven, and hybrid markets, adapting their logic to the specific rules and microstructure of each venue.

### Investment algorithms

Investment can be widely defined as the allocation of scarce resources  with the expectation of future benefits. In particular, investment strategies in the financial markets allocate such resources to financial instruments, after a careful analysis of future profit opportunities. Investment trading algorithms simply execute these strategies autonomously using computers. Given the generality of this objective, it is not surprising that investment algorithms encompass a large variety of different strategies. And although it is possible to categorize broadly these strategies in families that share a common pattern for the source of profits, in practice investors that implement investment algorithms spend a fair amount of time trying to find new types of strategies or unexplored asset classes or markets where existing strategies can be applied. The reason is that as soon as certain investment strategies become popular, those trades become crowded and profit opportunities fade away quickly. 

Investment algorithms can operate over different time horizons, and the role of automation varies accordingly. A useful distinction can be made between intraday investment algorithms and investment algorithms operating over longer horizons.

Intraday investment algorithms focus on short-term opportunities that may persist for minutes, seconds, or even fractions of a second. These strategies aim to exploit transient patterns in prices, order flow, or relative valuations, such as short-term momentum, mean reversion, or arbitrage opportunities across instruments or venues. In this context, algorithms are often essential rather than optional: the speed at which signals emerge and decay makes manual trading impractical. As a result, intraday investment algorithms are typically implemented in a fully automated manner and are closely linked to market microstructure, execution quality, and latency.

By contrast, investment algorithms operating over longer time horizons —such as days, weeks, or months— often play a more varied role. In some cases, algorithms are used primarily as decision-support tools, systematically analysing data and generating signals that inform human investment decisions. Orders may then be executed manually or via standard execution algorithms. This hybrid approach is common in traditional asset management, where explainability, governance, and oversight considerations may limit full automation.

In other cases, particularly in systematic and robo-investment strategies, algorithms take on a more comprehensive role. They may determine asset allocation, rebalance portfolios periodically, and manage risk in a largely automated fashion. Execution itself may still be delegated to specialised execution algorithms, but the investment logic —how capital is allocated across assets and over time— is embedded directly in the algorithmic framework.

As the number of strategies, instruments, or portfolios managed by an institution increases, the economic rationale for automation becomes stronger. Managing a large and diverse set of investment strategies manually is costly and error-prone, even when trading frequencies are relatively low. In such environments, investment algorithms provide scalability, consistency, and the ability to manage complexity in a controlled and systematic way.

## Developing Trading Algorithms

Developing a trading algorithm is a structured and iterative process that begins with a clear definition of its objectives. The purpose of the algorithm dictates the approach, data requirements, and performance metrics. For execution algorithms, the primary objective is to minimize transaction costs and market impact when buying or selling large volumes of assets. This often involves breaking down orders into smaller trades and executing them over time or across multiple venues to avoid moving the market. For market-making algorithms, the goal is to provide liquidity by continuously quoting bid and ask prices, profiting from the spread while carefully managing inventory risk and adverse selection. Meanwhile, intraday investment algorithms aim to generate returns by exploiting short-term price inefficiencies, arbitrage opportunities, or momentum effects, where speed and precision are critical.

Once the objective is defined, the next step is to establish how the algorithm’s performance will be measured. The choice of benchmarks is crucial, as it determines how success is evaluated and how different strategies are compared. Performance metrics vary depending on the type of algorithm. For example, execution algorithms are often evaluated based on their ability to achieve a favorable average price relative to the market, while investment strategies focus on risk-adjusted returns and drawdowns. Market - making algorithms typically track the profit & loss of the portfolio, as well as specific liquidity provision measures like the percentage of time during the market hours that bid and ask quotes were posted (for LOB based market-making) or the percentage of request for quotes for which a price has been provided (for RfQ based market-making).

Data plays a central role in algorithmic trading. The type and quality of data required depend on the strategy: high-frequency trading demands ultra-low-latency, tick-level data, while longer-term strategies may rely on daily or hourly price series. Historical data is used for both backtesting and calibrating the algorithm’s parameters. However, it is essential to recognize the limitations of historical data, as markets evolve and past performance does not guarantee future results. Overfitting—where an algorithm is excessively tailored to historical patterns—can lead to poor performance in live trading. To address this, developers use techniques such as out-of-sample testing, cross-validation, and stress testing under different market conditions.

The design phase is where the algorithm is developed. There are several approaches to strategy creation:

- **Mathematical Optimization:** Techniques like Dynamic Programming or Mean - Variance optimization are used to design a strategy that achieves the selected goal. 
- **Machine Learning:** Algorithms can be trained to recognize patterns in market data, adapt to changing conditions, or predict short-term price movements. In addition, techniques like Reinforcement Learning can be used for developing adaptive trading strategies.
- **Heuristic Rules:** Some strategies are based on empirical observations or trader intuition, codified into rules that guide the algorithm’s actions. While these may lack the complexity of data-driven models, they can be effective in markets where human judgment is still valuable.
- **Hybrid Approaches:** Many algorithms combine elements of the above, leveraging machine learning for pattern recognition and mathematical optimization for efficient execution.

After the design phase, the algorithm is implemented in code, typically using languages such as Python, C++, or Java, depending on performance requirements. The algorithm is then tested in a controlled environment, first through historical backtesting and later in real-time simulations or paper trading. Backtesting helps assess how the algorithm would have performed in past market conditions, but it is important to account for transaction costs, slippage, and market impact, which are often overlooked in simplified tests. Stress testing under extreme scenarios—such as flash crashes or periods of low liquidity—helps identify potential vulnerabilities before deployment.

Deployment marks the beginning of a new phase: continuous monitoring and refinement. Markets are dynamic, and an algorithm that performs well in one regime may struggle in another. Real-time analytics are used to track performance and risk metrics, allowing for quick adjustments if needed. Successful algorithmic trading requires not only robust initial development but also ongoing adaptation to maintain effectiveness in changing market conditions.

## Benchmarks for Algorithmic Strategies

The choice of benchmarks depends on the type of algorithm and its objectives. Below are the most common benchmarks used in the industry, defined mathematically where applicable:

### Execution Strategies
For algorithms focused on executing trades with minimal market impact, the following benchmarks are typically used:

- **Close:** The mid-price of the asset at the time the strategy completes execution.
- **Market Order Close:** The cost of executing a market order at the end of the strategy’s time horizon, using the notional value of the strategy.
- **Open-High-Low-Close (OHLC) Average:** The average of the mid-prices at the open, high, low, and close during the execution period.
- **Time Weighted Average Price (TWAP):**
  The arithmetic mean of the asset’s price over the execution window, calculated as:
  $$
  \text{TWAP} = \frac{1}{N} \sum_{i=1}^{N} P_i
  $$
  where $P_i$ is the mid-price at time $i$ and $N$ is the number of time intervals.

- **Volume Weighted Average Price (VWAP):**
  The average price weighted by trading volume over the execution period, calculated as:
  $$
  \text{VWAP} = \frac{\sum_{i=1}^{N} (P_i \times V_i)}{\sum_{i=1}^{N} V_i}
  $$
  where $P_i$ is the price at time $i$ and \(V_i\) is the volume traded at that time.

- **Decision Open:** The mid-price of the asset at the time the strategy is initiated.
- **Market Order Decision Open:** The cost of executing a market order at the time the strategy is launched, using the notional value of the strategy.
- **Arrival Open:** The mid-price of the asset when the first order generated by the strategy reaches the market.
- **Market Order Arrival Open:** The cost of executing a market order at the time the first order reaches the market, using the notional value of the strategy.

### Market-Making and investment Strategies
For algorithms designed to generate returns or provide liquidity, such as market-making, momentum, mean-reversion, or arbitrage strategies, the following benchmarks are commonly used:

- **Profit and Loss (P&L):**
  The cumulative return of the strategy over a given period, starting from an initial position or inventory.

- **Sharpe Ratio:**
  Measures the excess return per unit of risk (volatility), defined as:
  $$
  S_a = \frac{E[R_a - R_b]}{\sigma_a}
  $$
  where $E[R_a - R_b]$ is the expected excess return of the strategy over a risk-free rate, and $\sigma_a$ is the standard deviation of the strategy’s returns.

- **Beta ($\beta$):**
  Indicates the sensitivity of the strategy’s returns to market movements. A beta greater than 1 suggests the strategy is more volatile than the market, while a beta less than 1 indicates lower volatility.

- **Maximum Drawdown:**
  The largest peak-to-trough decline in the strategy’s cumulative returns over a specified period. It is a measure of downside risk.

- **Sortino Ratio:**
  A variation of the Sharpe ratio that focuses on downside volatility, defined as:
  $$
  S = \frac{R - T}{DR}
  $$
  where $R$ is the average return, $T$ is the target return (often the risk-free rate), and $DR$ is the standard deviation of negative returns (downside deviation).

- **Omega Ratio ($\Omega$):**
  Compares the probability of achieving returns above a threshold to the probability of returns below that threshold, defined as:
  $$
  \Omega(r) = \frac{\int_{r}^{\infty} (1 - F(x)) \, dx}{\int_{-\infty}^{r} F(x) \, dx}
  $$
  where $F(x)$ is the cumulative distribution function of returns, and $r$ is the target return.

Market-making algorithms are also evaluated based on their ability to provide liquidity consistently and effectively. The following metrics are commonly used:

- **Percentage of Time Quoted (LOB-based market making)**:
The proportion of the trading session during which the algorithm maintains active bid and ask quotes in the limit order book (LOB). This reflects the algorithm’s presence and commitment to providing liquidity.

- **Percentage of Requests for Quote (RfQs) Quoted (RfQ-based market making)**:
The ratio of RfQs for which the algorithm returns a price to the client, calculated as:

$$\text{Quote Rate} = \frac{\text{Number of RfQs Quoted}}{\text{Total Number of RfQs Received}}$$

- **Hit Ratio (RfQ-based market making)**:
The ratio of RfQs that result in a trade (hit) to the total number of RfQs received, defined as:

$$\text{Hit Ratio} = \frac{\text{Number of Hits}}{\text{Total Number of RfQs Received}}$$

- **Hit & Miss Ratio (RfQ-based market making)**:
The ratio of RfQs that result in a trade (hit) to the total number of RfQs that are closed by any dealer (i.e., the client traded). This excludes *price discovery* RfQs where the client did not trade, and is calculated as:

$$\text{Hit \& Miss Ratio} = \frac{\text{Number of Hits}}{\text{Total Number of RfQs Closed by Any Dealer}}$$


## Algorithmic Trading Infrastructure

The effectiveness of an algorithmic trading strategy is not solely determined by the sophistication of the algorithm itself, but also by the robustness and efficiency of the infrastructure that supports it. A well-designed infrastructure ensures low latency, high capacity, and resilience—qualities that are indispensable in modern electronic markets. The infrastructure required for algorithmic trading is composed of several interconnected components, each playing a critical role in the execution, monitoring, and optimization of trading strategies.

### Core Requirements 

To support the demands of algorithmic trading, the infrastructure must meet several fundamental requirements:

*  **High speed and low latency**: delays in transmitting data or executing orders can significantly impact performance, particularly for high-frequency trading (HFT) strategies, where microsecond-level latency can make the difference between profit and loss. The necessary latency threshold depends on the type of algorithm and the markets in which it operates. For instance, HFT strategies often require microsecond-level precision, while execution algorithms may tolerate slightly higher delays.

* **Capacity**: algorithmic trading generates a vast number of messages due to the high frequency of orders, cancellations, and updates. The infrastructure must be capable of handling this volume without degradation in performance, ensuring that the system remains responsive even during periods of peak activity.

* **Resiliency**: the system must include mechanisms for monitoring performance in real-time and handling failures gracefully. This includes the ability to disconnect from the market quickly and orderly if necessary, as well as redundant systems to ensure continuity in the event of hardware or software failures. Resiliency also involves implementing pre-trade and post-trade controls to prevent errors and detect potential market abuse, ensuring that the trading process remains both efficient and compliant.

### Key Components of Algorithmic Trading Infrastructure

A robust algorithmic trading system relies on modular, interconnected components, each designed for a distinct role in the trading workflow. While real-world setups may consolidate some functions—especially in smaller or simpler systems—the architecture naturally evolves toward this specialized structure as complexity and scale increase. Below, we break down the key elements of this framework, as illustrated in the following figure.

```{figure} figures/algo_infrastructure.png
:name: fig:algo_infrastructure
:width: 8in
Architecture of an algorithmic trading system. The overall principle for the template is based on encapsulation and functional specialization of each component. 
```

#### Algorithmic Trading Server

The algorithmic trading server, often referred to as a "strategy container," is the core platform where trading algorithms are executed. It generates orders based on the algorithm’s logic and reacts to real-time market data. There are several approaches to building this component, each with its own advantages and trade-offs.

Firms may choose to use third-party servers that include a suite of pre-built algorithms. These platforms often provide tools for developing proprietary strategies, ranging from support for traditional programming languages to complex graphical interfaces. Examples of such providers are Algo Trader, Pragma360 and QuantConnect.

On the other hand, large brokers, dealers, and hedge funds often develop their own algorithmic trading servers in-house. This approach allows for greater customization and differentiation, as proprietary algorithms can be tailored to specific market conditions and trading objectives. The choice of programming language depends on performance requirements, with high-performance code typically written in languages like Java, C#, or C++, while Python and MATLAB are often used for prototyping and less latency-sensitive applications.

The server typically employs complex event processing (CEP) logic to handle real-time data streams and make rapid trading decisions. They are also sometimes built using reactive programming principles, which allow the system to respond dynamically to changes in market conditions, further enhancing the agility and responsiveness of the trading infrastructure.

#### Market Data Server (MDS)

The Market Data Server (MDS) serves as the central hub for both historical and real-time market data, which is essential for algorithm calibration, backtesting, and live trading (see later in the testing section for mor details). Historical data is stored in a "data store," "data lake," or "data repository" and is used for calibrating and backtesting strategies. KDB+ remains the industry standard for handling time-series data due to its in-memory performance and ability to process vast datasets at high speed. It is widely used in finance for algorithmic trading, risk management, and market surveillance, particularly in environments where latency and accuracy are paramount.

For real-time data, firms can obtain market data either directly from trading venues or through vendors like LSEG (acronym for London Stock Exchange Group, which bought Refinitiv, previously known as Thomson Reuters)  or Bloomberg. While vendors offer the advantage of a single point of access and standardized data formats, connecting directly to exchanges can reduce latency, which is critical for high-frequency and latency-sensitive strategies. For professional applications, it is recommended to have at least two alternative data sources to ensure redundancy and reliability.

#### Order Management System (OMS)

The Order Management System (OMS) is responsible for handling all orders sent to trading venues. It manages order entry, routing, and status monitoring, as well as trade booking and reconciliation. Key functionalities include order entry, which can be done manually or via algorithms, and order routing, which involves encoding orders according to a standardized protocol and transmitting them to trading venues.

The Financial Information eXchange (FIX) protocol remains the most widely used standard in electronic trading, providing a consistent and efficient means of communication between clients, brokers, and exchanges. OMS platforms such as Bloomberg AIM, Fidessa OMS, and FIS Valdi continue to be prominent in the industry, offering robust solutions for managing order flow across multiple asset classes and regions.

#### Execution Management System (EMS)

While OMS platforms focus on order management, Execution Management Systems (EMS) are specialized for order execution and algorithmic trading. EMS platforms often overlap with OMS in functionality but are more outward-facing, offering connectivity to multiple exchanges, brokers, and trading platforms. They provide tools for pre-trade and post-trade analysis, real-time monitoring, and Direct Market Access (DMA).

Bloomberg EMSX remains a leading EMS platform, offering global, broker-neutral equities and futures trading, as well as integration with Bloomberg’s buy-side OMS, AIM. EMSX supports a wide range of asset classes, including equities, futures, options, and index swaps, and provides access to nearly every listed market through its extensive network of broker destinations.

#### Market Making Trading Platforms

For firms engaged in market-making activities, specialized platforms are available that provide tools for managing Request for Quote (RfQ) and Request for Stream (RfS) workflows. These platforms typically include pricing and quoting engines, auto-quoting and auto-hedging capabilities, and integration with OMS and EMS.

Itiviti, now part of Broadridge, continues to offer a suite of market-making solutions, including Tbricks and Orc Trader, which are designed for listed derivatives and provide real-time risk control and customization. Numerix Oneview for Trading offers real-time pricing, market data management, and risk calculations for structured products and derivatives. ION Trading is a major player offering platforms for Fixed Income trading. 

#### Analytics and Backtesting Server

The analytics server is used for off-line analysis, including the calibration of algorithm parameters and performance evaluation. It relies on historical or synthetic data to simulate how strategies would have performed under different market conditions. Historical data reflects real market conditions but is limited to past scenarios, while synthetic data can be generated to simulate a wider range of market conditions, including extreme or unlikely scenarios.

Platforms like QuantConnect and Deltix provide comprehensive backtesting and analytics capabilities, allowing traders to test and refine their strategies before deployment.


#### Profit & Loss (P&L) and Risk Server

The P&L and risk server tracks the real-time performance of trading positions, providing metrics such as profit and loss, exposure, and risk indicators. These systems are often integrated with the firm’s broader risk management infrastructure but may include specialized features for algorithmic trading.

Murex MX.3 is a leading platform in this space, offering integrated solutions for trading, risk management, and processing across a wide range of asset classes. It provides real-time risk monitoring and analysis, enabling institutions to identify and mitigate potential risks promptly.

#### Infrastructure for Small Firms and Private Investors

Not all market participants require the same level of infrastructure. Small firms and private investors often rely on third-party solutions that bundle algorithmic trading servers, analytics, backtesting, and connectivity to brokers and exchanges.

Platforms like MetaTrader 5 (MT5), Interactive Brokers, and QuantConnect offer accessible and cost-effective alternatives, providing a range of tools for developing, testing, and deploying trading strategies. Crowdsourced hedge funds such as Numerai and Quantiacs continue to provide environments for developing and backtesting trading algorithms, with the best-performing strategies potentially being included in the fund’s portfolio.

For those with limited resources, open-source libraries like PyAlgoTrade, Zipline, and Backtrader provide cost-effective alternatives for backtesting and strategy development. Moreover, cloud providers like Amazon Web Services (AWS), Google Cloud, and Microsoft Azure further enhances accessibility, allowing traders to scale their operations without significant upfront investment.

## Testing trading algorithms

As it happens with any software, proper testing is central to algorithmic trading. Ensuring that a trading algorithm behaves as expected before releasing it into the market not only limits economical losses, it is also a regulatory requirement in many jurisdictions, given the potential for disruption that trading algorithms have in modern financial markets. 

The specific nature of trading algorithms as software development means they require a differential approach to their testing. Of course, as in any other software development, when developing trading algorithms it is advised to follow standard practices like implementing unitary and regression tests, as well as requiring peer code review before releasing to production. Specific to trading algorithms, although shared with other domains like data science and machine learning, are the following: 1) a functional testing based on analyzing the behaviour of the algorithm in past real trading scenarios (backtesting) or in 2) simulated markets, 3) real-time execution in testing environments, and 4) a gradual release to production in which the algorithm reaches its intended scope (volumes, markets, instruments) in gradual steps, so the developer can do a final controlled test in a real scenario. 

Let us analyze in detail each of these steps in the testing workflow of trading algorithms in detail.

### Backtesting

As mentioned, backtesting a trading algorithm typically involves simulating its execution on a market test environment that uses real historical data. Although it is almost guaranteed that in financial markets, the past does not repeats itself in the future, aggregated market characteristics are relatively stationary (at least form some periods of time), and using historical data ensures that we use data that has close enough characteristics to what we will potentially see once the trading algorithm is deployed in production. 

#### Historical market data

To perform backtesting, we need to retrieve and store sufficient historical market data. The amount of data needed depends on the type of trading algorithm, strategy, market and event instrument type. Trading algorithms intended to execute intraday will need higher resolution data but potentially less number of days. However, investment strategies that execute over days, weeks or months will need years of historical data to be properly tested, although with less resolution. 

Market data vendors typically offer market datasets with different granularity. When testing a trading algorithm, a good practice is to focus on the less granular data that is sufficient to test the behaviour of the algo, since the more granular the data is, the larger the adquisition cost, download times, storage and efficiency of the backtesting engine. Typical options are the following:

* **Tick by tick data**: as discussed in chapter {ref}`market_microstructure`, this is the most granular data available, since information is stored every time there is an update in an order in the market. For Limit Order Book based exchanges, there are typically two reports of tick data available: order book snapshots, that store volumes available at the different pice levels at a given time; and messages data, where each order update is recorded, both quotes and trades. Order book snapshots are sold with different granularity as well: 
  * *level I* data only records the best bid and ask
  * *level II* data includes more levels beyond the best bid and ask (4, 10, 20, depending on the provider)
  * finally, *level III* data provides information about the individual orders present at each of the price levels. 

  For RfQ based markets, tick by tick data typically records every update of composite prices as well as all the RfQ order status updates. 
  
  Tick by tick data can be obtained from major market data providers like Bloomberg, LSEG, ICE or Factset, or in many cases directly from the exchange providers. This data is typically not free, although some initiatives like Lobster make available samples for public research. Cryptocurrency data or prediction markets data (e.g. Polymarket) can be obtained (at the time of writing) also for free. 
  
  RfQ data is more difficult to obtain publicly, even for a free. Composites are published by platform providers like Bloomberg, Tradeweb and Market-Axess. RfQ data is typically proprietary for the dealers that participate in the RfQ process, and only trades are typically published (sometimes aggregated over time windows), particularly in instances where there is a regulatory obligation to do it, as it is the case in bonds for the Trace data  in the USA or the APAS in Europe.

* **OHLCV**: OHLCV stands for Open High Low Close Volume data. This data is typically provided at different frequencies (minutes, hours, days) and records the mid-price of a limit order book at the beginning of the interval (open), the end (close), as well as the highest (high) and lowest (low) mid-prices. It also typically (but not always) includes the total traded volume within the interval (volume). There are also versions of OHLC price data that records separately bid and ask prices, instead of the mid-prices. OHLCV data can be obtained as well from major market data providers like Bloomberg, LSEG and Factset, among others, for a fee. These providers generate this data typically from tick by tick data. 

* **EOD**: End of Day (EOD) is typically the easiest and cheapest to obtain, being provided for free for many instruments and exchanges. For instance, Yahoo and Google make this data available for major equity instruments and indexes. For fixed income instruments like bonds and swaps, as well as derivatives, sometimes it can be web-scrapped for free directly from the webpages of the exchanges where they trade. This is typically price data, although sometimes total traded volumes are also available. The reference used for the closing price depends on the market. For stocks, the price from the closing auction in the regulated market (e.g. NYSE, NASDAQ, LSE, etc) is used. In FX markets, that typically trade 24 hours, the reference is typically the one from official fixings, for example the ECB fix in Europe, based on a methodology from the European Central Bank that normally takes place around 14:10 CET. EOD data is typically very relevant since it is used to compute the value of positions in major financial institutions like banks, mutual, and pension funds, as well as to determine the settlement of financial contracts. 

#### Data pre-processing

Once data has been obtained, it needs to be carefully pre-processed before using it for backtesting. The following list covers some of the things that typically need to be accounted for when pre-processing market data for backtesting:

* **Missing data**: in the form of explicit $\text{NaN}$ (Not a Number), $\text{None}$, or implicitly, when there are gaps in an otherwise regular time series of market data. How to treat missing data is highly dependent on the use case. In some cases, skipping it is sufficient, e.g. simply removing $\text{NaN}$. In other cases, the algorithm performance might be affected by the absence of the data and we might resort to data imputation techniques, i.e. filling the gaps with some form of interpolation or extrapolation. There are multiple ways to do this, and we refer the reader to the excellent book {cite:p}`denev2020alternative` for more details. Naive strategies simply fill with the last data point, or make a linear interpolation between the closest data points to the gap. More advanced techniques estimate a generative probabilistic model from the available data, which is sampled to fill the gaps. The latter is a particular application of synthetic data that we will discuss more generally later in this section.

* **Outliers**: which are extreme data points that can come either from data corruption or because they were actually volatile market conditions. When the problem comes from data corruption, we can simply treat them as missing data, and use any of the strategies discussed in the previous point. However, in the second case, the approach depends on the nature of the backtesting we want to carry out. If our aim is to test the algorithm in *normal* trading conditions, we can potentially remove stressed periods that are predictable. For instance, the day after the Brexit referendum or the day after the first election of Donald Trump as US president. It is a typical practice to disconnect trading algorithms in those volatile days, or used versions specifically designed for such market conditions. It is a different situation when dealing with unpredictable market conditions, since in this case we probably want to assess how the algorithm will behave, since disconnecting it before hand will not be, by definition, possible. This is the case for instance of flash crashes or episodes of market manipulation, as the ones discussed later in this chapter. 

* **OTC Trades**: in Limit Order Book data, exchanges usually include OTC (Over The Counter) trades in the market data. OTC trades are block trades that happen out of the ordinary trading session. These OTC trades need to be removed since they were not actually present in the Order Book during the trading session, and including them will distort the behaviour of the trading algorithm. 

* **Price series adjustments**: synthetic transformations applied to historical price data to preserve continuity and economic interpretability. These adjustments introduce values that did not occur in actual trading sessions, but they remove mechanical discontinuities that are not economically meaningful and would otherwise distort statistical analysis or backtesting results.

  A common example arises from **corporate actions**, such as dividends and stock splits. These events generate mechanical jumps in the observed price series that do not correspond to genuine price movements. For instance, when a stock pays a dividend $D_t$, the ex-dividend price typically drops by approximately that amount. To avoid introducing a spurious negative return in the historical series, prices prior to the event are rescaled by an adjustment factor so that the series remains continuous. A common adjustment uses a multiplicative factor

  $$ A_t = \frac{P_{t-1}-D_t}{P_{t-1}}$$

  and historical prices are transformed as

  $$ P^{adj}_s = A_t P_s \quad \text{for } s < t$$

  The resulting adjusted prices are therefore synthetic, but they provide a representation of price dynamics that is more suitable for modeling and backtesting.

  Another important case arises when constructing **continuous futures price series**. Individual futures contracts have fixed expiries, and new contracts for a given maturity segment are issued periodically (often quarterly). Market participants typically migrate their positions to the most liquid contract, usually the most recently issued one. In order to obtain a long historical time series suitable for quantitative analysis, successive contracts must therefore be linked together. A common approach is to construct a *back-adjusted series*: when the roll occurs from contract $F^{(1)}$ to $F^{(2)}$ at time $t_r$, historical prices of the earlier contract are shifted so that the series does not exhibit a discontinuity at the roll date. For example, an additive adjustment defines

  $$ P^{adj}_t = P_t + \big(F^{(2)}_{t_r} - F^{(1)}_{t_r}\big), \quad t < t_r$$

  while multiplicative variants are also used. Another approach constructs a *perpetual series* by taking a weighted combination of the nearby and next contracts during a predefined roll window,

  $$P_t = w_t F^{(near)}_t + (1-w_t)F^{(next)}_t$$

  with weights $w_t$ gradually shifting as the roll date approaches. As in the case of corporate action adjustments, the resulting prices are not directly observed in the market, but they provide a continuous series that better reflects the underlying economic dynamics and can be used consistently in statistical analysis and algorithmic trading research.

#### Building the backtesting engine

At its core, running a backtest means trying to answer a *counterfactual question* (see chapter {ref}`intro_causal`): what would have our algorithm traded had it been executed in a past trading session? Our algorithm is sending order to the market that did not exist in the past, and we need to simulate the impact of these orders in the market. When working in **limit order book** based markets, we typically consider two different types of effects:

* **Instantaneous market impact**: which is the inmediate effect that our order has in the limit order book. For example, a limit order at a price where there is not an opposite matching order, will be added to the liquidity available in the order book. Alternatively, a market order will consume limit orders, removing the liquidity from the market. 

* **Permanent market impact**: which is the effect that our orders have on future orders arriving to the market. For instance, consuming liquidity from the limit order might trigger a cascade of orders in the same side, coming from algorithms making decisions based on the shape of the order book. Another possibility is that the price movement produced by this consumption of liquidity triggers stop orders. And so on.

The ideal backtest would simulate the market impact of our orders. However, this is not feasible if we intend to stick to the historical data: once our orders alter the market dynamics, historical orders are no longer compatible with it. This becomes the real of simulated markets, which we will discuss in the next section, which bring their own issues since the simulated dynamics might not necessarily be representative enough of real market dynamics, being model dependent. 

Therefore, in order to run backtests with historical data, we need to make some compromises when modelling the impact of our orders. The most simple one is completely ignore the effect of our orders in the market dynamics, i.e. neglecting both instantaneous and permanent market impact. In this *shadow* backtesting mode, we use historical data to trigger the orders from the trading algorithms, as well as to simulate their execution. For example:

* We can compute the price at which a market order is executed by reconstructing the limit order book at a given time and simulating an execution against the available liquidity. This liquidity is not, however, removed from the reconstructed order book, as we proceed forward with the simulation.

* Analogously, we could add our limit orders to the queue in a reconstructed order book at a certain price level, and simulate an execution against an incoming market order or agressive limit order that reaches the price level where the level sits (as well as having enough volume to reach our order a that price level). But again, the simulation continues on without considering the impact of our order. 

A second feasible option is to consider the instantaneous market impact, but not the permanent one. In this case, we rely completely on keeping a reconstruction of the order book over the simulation, which is updated with our own orders. For example, if we place an order at a tick above the best bid, an incoming market order of the same volume would consume our order but leave orders are the next price levels unaltered, which is something that would not have happened in the absence of our order. However, in our simulation, we continue using the history of incoming market and limit orders (or other order types), which we assume are not affected by the impact of our orders. 

As a side note, it is worth to point out that typical tick by tick datasets provide order information in the form of quotes and trades. This does not directly provide the information about the native orders that were submitted to the market. For instance, a trade could happen because of a market order or because of an aggressive limit order, to consider the most simple types of orders (see chapter {ref}`market_microstructure`). To reverse engineer the type of orders in order to consistently update our reconstruction of the limit order book, we need to make some hypotheses. A simple one maps quotes with limit orders and trades with market orders, the side of the latter being inferred comparing their price against the prevalent mid-price at the time of arrival of the order (the mid-price from the historical order books, not the reconstructed one, that might be already affected by our orders).

All this is to highlight that historical backtests are based on strong modelling assumptions and simplifications, and therefore their results need to be considered as much as optimistic bounds for the behaviour of the tested trading algorithm in real market conditions. 

To close this section, let us briefly discuss the case of backtesting in **RfQ based markets**. The most typical case in this setup is that of a dealer testing trading algorithms that generate prices to respond to the RfQs from the clients. As discussed above, historical data consists on past RfQs received. The same argument regarding market impact apply in this case.  If we want to stick to the history of RfQs, we have to assume that when testing alternative pricing policies as the ones that happen in the historical data will not affect future order flows, which is equivalent to the permanent market impact discussed above. Notice that this might be also a strong hypothesis in these markets since clients might, for instance, stop sending RfQs to a dealer that consistently quotes uncompetitive prices. A similar situation might occur when simulating indicative prices quoted by dealers in streaming to electronic platforms, which might influence the incoming flow of RfQs. 

The analogous to the instantaneous market impact in this setup is the actual outcome of the RfQ. From historical data the dealer knows if the client traded or not given the quoted price. There is also extra information that can be available pre and post-trade, as discussed in chapter {ref}`market_microstructure`. For instance, the client identity, instrument type, side, volume and number of competing dealers (in multi-dealer-to-client platforms) are available at the time of quoting. And afterwards, many platforms provide information about the second best price (cover) for dealers that won the RfQ, as well as information about the client trading with other dealer or simply walking away. As also discussed before, for some instruments there is information available about the prices and volume closed, typically due to regulatory requirements. This information can be used to simulate the outcome of the RfQ when using alternative pricing policies, by estimating models that predict the probability of trading given the RfQ context and the quoted price. These models will be discussed extensively in chapter {ref}`rfq_models`.


#### Backtesting runs and interpretation of results

The results of backtesting trading algorithms and trading strategies in general have to be considered optimistic: getting good results in backtesting does not guarantee good results in a real trading environment; however, if the results of the backtesting are bad, the trading algorithm should definitely be reviewed before releasing it into production. 

There are good practices and considerations, though, that help maximize the utility of a backtesting:

* When running a backtesting, we need to select a period of historical data and a universe of instruments that we intend to trade. For both selections, it is convenient to follow the general data science good practice of dividing data into three sub-sets: training, validation and testing. As its name suggests, the **training set** is used to train the strategy, which might involve from selecting the parameters that maximize the performance metrics of the strategy, to learning predictive models that are used for decision making. A **validation set** is typically used to choose across different candidate strategies and models, sometimes belonging to a parametric family of them. Therefore, it is typically said that the validation set is used to choose hyperparameters. Once a final candidate is chosen, we run a final backtesting using the **testing set**, that contains data that has not been used for training and validation. The results of the backtesting on the testing set are considered the closest to the real performance of the strategy

* The selection of these three datasets needs to be done carefully. A good practice is to select the training and validation sets from time periods before the testing set. This is to avoid a **look ahead bias**, in which we indirectly leak information from the future into the training and selection of the trading strategy. Given that markets show typically a strong autocorrelation, a good practice is to add some censored periods between training / validation and testing data, which are not used at all in the backtesting. This helps to reduce the effect of correlations between the different datasets.

* Markets usually show different **regimes**, typically in terms of trend and volatility. If our strategies are supposed to be used in a particular regime, it is convenient to select historical data from similar regimes. This selection has to be done using the same criteria that will be used in a real trading session to select if the regime is appropriate for the operation of the strategy.

* In terms of instrument selection, ideally if we intend to trade on a wide universe of instruments, it is convenient to leave entirely some instruments out of the training and validation set, unless we intend to finetune the strategy at the instrument level. In that case, we might want to train the strategy in all the instruments, but leave model and strategy selection for a subset of them. This and the previous good practices seek in the end to avoid the so-called **data snooping bias**, in which the choice of strategy is too influenced by patterns and correlations of the specific data in the testing and validation sets, which don't generalize well to other data and instruments in the tradable universe. A related problem is that of **overfitting**, that happens when we use overparametrized models and strategies, which makes it easier for the strategy to fit the training data in a way that does not generalize well to other datasets. 

* Finally, particularly when performing backtesting over long time periods like years, we have to be particularly careful about **survivorship bias**, i.e. selecting only the instruments that have performed well up to today but neglecting some that did not perform well. This can happen obviously in the case of firms that become bankrupt and their stock or bonds dissappear from the market, but also when using as the universe of tradable instruments those that are currently more liquid or that belong today to a relevant index like the S&P 500 or the Euro Stoxx 50. We have to use the same logic for universe selection in the past as the one we would use in the present, to ensure we also include potential *losers* in the backtesting.

For a deeper dive into the systematics of backtesting, the book by Marcos López de Prado is a good reference {cite:p}`dePrado2018`. 

### Testing in simulated markets

There are several reasons why backtesting with historical data might not provide enough safe guarantees when it comes to estimate the real performance in trading conditions. Let us summarize the main ones:

* **Lack of enough historical data**: there might be simply not enough data from previous trading sessions to do a comprehensive assessment, particularly for strategies that use end of day prices or even larger time intervals. The problem is compounded when we know that markets are continually changing so the older the data, the less representative might be of future trading conditions. 

* **Indirect data snooping bias**: given the scarcity of historical data, even if we are rigorous in avoiding the biases commented in the previous section for our particular design and testing of a trading strategy, the truth is that some of these datasets are the most crowded that exist. For example, end of day data from US and European stocks belonging to the main indexes. Thousands of articles and research reports have been devoted to testing trading strategies over this data, meaning that is rare that a professional or academic working in the financial sector has not been indirectly influenced by previous results working on these datasets. This means that when testing a new trading strategy on this data, we might be likely incurring at some degree on data snooping bias.

* **Insufficient market feedback**: as also discussed in the previous section, we can include some limited market feedback when working with historical data, particularly around instantaneous market impact when the orders of our trading strategy are relatively marginal with respect to those of the overall market. However, the reality is that real markets will adapt to our orders, and in order to incorporate this feedback effects we need to deviate from the historical time-series.

This motivates the use of market simulators that are able to generate an unlimited number of trading scenarios and provide a comprehensive feedback mechanism. These simulators might still rely on historical data for calibration or initialization, but the role of this data ends there. 

There are two major ways to build market simulations. The first one is based on estimating a generative probabilistic model for the orders in the market. The second one tries to model the behaviour of representative agents that operate in markets, which generate in turn the orders that arrive to the simulation. We will cover the simulation of dealer-to-client markets that operate with request for quotes in chapter {ref}`rfq_models`. Simulation of limit order book (LOB) markets is discussed in detail in {ref}`lob_models`.

## Effects and Risks of Algorithmic Trading

The expansion of algorithmic trading has had significant and measurable effects on market structure, both beneficial and potentially destabilising. Understanding these effects requires separating the structural consequences of widespread algorithmic participation from the specific pathologies that can arise when algorithms malfunction or are deliberately misused.

### Market Quality Effects

The most consistently documented positive effect of algorithmic trading—and of HFT market making in particular—is the compression of bid–ask spreads and the increase in quoted depth in electronic order books. By continuously quoting both sides of the market, algorithmic market makers increase the supply of immediately available liquidity, reducing transaction costs for end investors. Empirical studies across multiple asset classes confirm that the introduction of electronic and algorithmic trading has been associated with narrower spreads and lower price impact for standard-sized transactions {cite:p}`ESMAHFT2019`.

However, this liquidity is conditional and fragile. Unlike traditional broker-dealer market makers, who historically operated under contractual or reputational obligations to maintain quotes in stressed conditions, most algorithmic liquidity providers—particularly HFT firms—face no such obligations. Empirical evidence shows that HFT market makers tend to reduce or withdraw their quotes precisely during episodes of market stress, when spreads widen and volatility spikes. This behaviour, while individually rational, can amplify price dislocations when it occurs simultaneously across many participants, creating an asymmetry between normal and stressed market conditions {cite:p}`BIS2018HFTRisks`.

A related effect is the ambiguous net impact of algorithmic trading on volatility. In normal conditions, deeper liquidity tends to reduce volatility. Yet the episodic withdrawal of algorithmic liquidity during stress—and the herding dynamics described below—can amplify extreme events, making the overall effect of HFT on volatility difficult to sign empirically. The literature documents lower *routine* volatility alongside an elevated incidence of short-lived but severe dislocations.

Two further structural effects deserve mention. First, the widespread use of execution algorithms—which fragment large parent orders into sequences of smaller child orders spread across time and venues—has reduced the average trade size and increased the total number of trades and messages generated in modern markets. This trade fragmentation is a defining feature of post-2005 equity microstructure data across all major exchanges. Second, relative-value and arbitrage algorithms, by rapidly exploiting price discrepancies between related instruments or across venues, contribute to *price consistency*: persistent cross-market arbitrage opportunities that once lasted minutes or hours are now compressed to milliseconds in liquid markets {cite:p}`BIS2018HFTRisks`. In this sense, algorithmic activity promotes allocative efficiency by ensuring that prices reflect information more uniformly across venues and instruments.

### Systemic Risks

The same speed and interconnectedness that make algorithmic trading efficient in normal conditions become a source of systemic fragility under stress. A recurring concern is *algorithmic herding*: when many independently designed algorithms share similar data inputs, signals, or risk thresholds, they may react to market events in a highly correlated manner, amplifying price movements rather than dampening them. This self-reinforcing dynamic has been identified as a contributing factor in several episodes of sudden and severe market dislocation {cite:p}`ESMAHFT2019`.

The **Flash Crash of 6 May 2010** remains the most studied such episode. As shown in {numref}`fig:flash_crash_indices`, the DJIA, S&P 500 Index, and E-Mini S&P 500 futures all fell sharply together around 13:30 CT before recovering within approximately 20 minutes—a dislocation that was simultaneous across instruments and almost entirely reversed, two hallmarks of algorithmically driven rather than fundamentals-driven price moves. The joint CFTC–SEC investigation concluded that a large algorithmic sell order interacted with aggressive HFT strategies that withdrew their liquidity during the stress, producing a rapid cascade that temporarily disconnected prices from fundamentals {cite:p}`CFTC_SEC2010FlashCrash`. A subsequent investigation in 2015 identified that a London-based trader, Navinder Singh Sarao, had been deploying a *layering* strategy (described below) to artificially distort the order book for S&P 500 futures immediately before the crash, illustrating how deliberate manipulation can interact with automated systems to produce extreme outcomes.

```{figure} figures/flash_crash_equity_indices.png
:name: fig:flash_crash_indices
:width: 8in
U.S. equity indices on 6 May 2010. End-of-minute transaction prices of the Dow Jones Industrial Average (left axis) and the E-Mini S&P 500 futures contract and S&P 500 Index (right axis) from 8:30 to 15:15 CT. The simultaneous sharp drop and rapid recovery around 13:30–14:00 CT is visible across all three series. Source: {cite:t}`Kirilenko2017FlashCrash`, reproduced from the CFTC working paper version (U.S. government work, public domain).
```

The trader-level data analysed by {cite:t}`Kirilenko2017FlashCrash` reveals the mechanism in detail, as illustrated in {numref}`fig:flash_crash_traders`. During the down phase, Fundamental Sellers—representing the large algorithmic sell programme—increased their short positions substantially, while Opportunistic Traders (including HFT strategies) initially absorbed selling pressure but then rapidly reversed, amplifying the decline. Fundamental Buyers only stepped in meaningfully during the up phase. The figure makes visible how the withdrawal of algorithmic liquidity during the stress converted a large but not exceptional sell order into a self-reinforcing price dislocation.

```{figure} figures/flash_crash_trader_positions.png
:name: fig:flash_crash_traders
:width: 8in
Change in net positions of Fundamental and Opportunistic Traders in the E-Mini S&P 500 futures contract on 6 May 2010 (one-minute intervals, 13:19–14:09 CT), with transaction prices overlaid. The DOWN and UP phases of the crash are marked. Fundamental Sellers dominate the down phase; Opportunistic Traders (including HFTs) initially absorb but then amplify the move before reversing. Source: {cite:t}`Kirilenko2017FlashCrash`, reproduced from the CFTC working paper version (U.S. government work, public domain).
```

A structurally analogous episode occurred on **7 October 2016**, when sterling fell approximately six percent against the US dollar in a matter of minutes during a period of thin Asian-session liquidity before rapidly recovering. Investigations attributed the event to a combination of automated news-reading systems reacting to Brexit-related commentary, risk-management algorithms amplifying the initial move, and HFT liquidity withdrawal during the stress {cite:p}`BIS2017GBPFlash`. Notably, the episode was not attributed to a single algorithmic actor, but to the interaction of multiple independent systems operating under similar stress signals—an illustration of how systemic risk can emerge from individually rational behaviour.

Because many algorithmic strategies operate simultaneously across multiple instruments and venues—multi-leg arbitrage, index replication, delta hedging— a stress event in one market can propagate almost instantaneously to others. The 2010 Flash Crash demonstrated how stresses originating in equity index futures could transmit rapidly into individual equities, exchange-traded funds, and related derivative markets within seconds, a form of cross-market contagion that is qualitatively different from the slower contagion mechanisms observed in pre-algorithmic markets.

### Operational Risk

A distinct class of risk arises from algorithms that malfunction unintentionally due to implementation errors, infrastructure failures, or unanticipated market interactions. A canonical example is the **Knight Capital incident** of 1 August 2012. A production deployment error activated a legacy routing component that began submitting an uncontrolled stream of orders in more than one hundred NYSE-listed securities. Within 45 minutes, Knight Capital Group had accumulated large unintended positions and suffered losses of approximately $440 million—a sum representing a substantial fraction of the firm's equity capital—before the errant algorithm was halted. The positions were subsequently liquidated at a significant discount, contributing to the firm's eventual acquisition by a competitor {cite:p}`SEC_KnightCapital2013`. The incident demonstrated that the speed advantages of algorithmic trading translate equally into speed of loss when a system fails, and underscored the importance of pre-trade risk controls, kill-switch mechanisms, and disciplined production release procedures.

Operational risk in algorithmic trading is not limited to dramatic single-firm events. More routine failures—brief connectivity outages causing stale orders to linger, parameter miscalibrations causing algorithms to trade at unintended volumes, or race conditions in multi-venue routing logic—collectively represent a significant source of operational exposure for trading firms and, in aggregate, can affect market quality.

The increasing use of AI coding tools in software development poses, in this regard, a relevant risk. These tools tend to rewrite large chunks of code rather than the limited, targeted interventions that human developers typically make, enlarging the surface area of each change and making thorough review substantially harder. Without a corresponding increase in testing rigour—covering not just functional correctness but the domain-specific invariants of trading systems, such as order-size limits, position constraints, and connectivity fail-safes—AI-generated code introduces latent risk that may not surface until the algorithm is live. The Knight Capital incident is a cautionary parallel: a routine deployment change, inadequately reviewed, activated logic that should never have reached production. The speed with which AI tools generate and modify code, if not matched by proportionally stricter governance, risks increasing both the frequency and the magnitude of such episodes.

### Market Abuse

Beyond unintentional malfunctions, trading algorithms can be deployed deliberately to distort or manipulate markets. European regulation identifies specific forms of algorithmic market abuse under the Market Abuse Regulation (MAR, Regulation (EU) No 596/2014) {cite:p}`MAR596_2014`, and analogous prohibitions exist under U.S. securities and commodities law.

**Spoofing** involves placing a large limit order on one side of the order book—typically at or near the best bid or offer—with the intent to create a false impression of supply or demand, while simultaneously submitting a genuine order on the opposite side. Other market participants, particularly algorithms that use order-book imbalance as a short-term directional signal, may react to this order by trading at prices that benefit the spoofer. The distorting limit order is then cancelled before it can be filled -which, however, could happen in the interim, making this strategy also risky. A variant of the strategy waits for the best quote to reprice in response to the spoofed order, cancels the large limit order, and then consumes the repositioned liquidity with an aggressive market order.

**Layering** extends this logic by placing multiple distorting limit orders at several consecutive price levels on one side of the order book simultaneously, rather than a single large order. This creates a more convincing appearance of deep one-sided interest and is particularly effective in instruments where the natural depth at the best bid or offer is thin. The 2010 Flash Crash investigation identified layering in S&P 500 futures as a contributing trigger, and a series of enforcement actions across the U.S. and European jurisdictions has since established layering as a clearly prosecuted form of market abuse.

**Banging the close** refers to executing a large number of transactions near the end of a trading session with the intent of artificially influencing the settlement or closing price, which may be used to benefit positions in related derivatives or contracts that settle against that reference price.

**Front-running** involves trading on one's own account in advance of executing a known client order, exploiting privileged access to information about forthcoming order flow. The classical form is straightforward: for example, a broker who receives a large client buy order first purchases the same instrument for its own account, executes the client order —which moves the price— and then sells at a profit. This is unambiguously prohibited under securities law in all major jurisdictions.

A more contested variant, sometimes called *electronic front-running* or *latency arbitrage*, arises from the structure of fragmented electronic markets rather than from privileged bilateral information. When a large investor routes a block order across many venues simultaneously via a smart order router, the orders arrive at different exchanges at slightly different times due to varying transmission latencies. An HFT firm co-located at the nearest exchange can detect the first arriving slice, infer that further orders are headed to more distant venues, and race ahead to those venues to trade before the investor's orders arrive—effectively purchasing shares microseconds earlier and selling them to the investor at a marginally higher price. This mechanism is described in detail in Michael Lewis's *Flash Boys* {cite:p}`Lewis2014FlashBoys`, which documented how latency differences across the fragmented post-Reg NMS U.S. equity market created structural opportunities for such strategies.

The book further alleged that certain dark pools—off-exchange venues ostensibly designed to protect institutional order flow—had been configured in ways that allowed HFT firms to observe and trade against client orders; Lewis cites Goldman Sachs's dark pool Sigma X as a specific case where investors were found to be systematically disadvantaged. Whether such practices constitute front-running in the legal sense remains contested, as they do not rely on privileged bilateral information but on publicly observable order-arrival patterns and speed advantages. Regulators have nonetheless scrutinised them closely, and the episode prompted the founding of IEX, an exchange designed to neutralise latency arbitrage by imposing an equalised 350-microsecond delay on all incoming orders.

**Quote stuffing** consists of submitting a very large number of orders and cancellations in rapid succession, not to create false price signals but to saturate the message-processing capacity of competing systems. By flooding an exchange's data feed, the perpetrating algorithm degrades the ability of rival algorithms to maintain an accurate and timely view of the order book, effectively widening their operational latency window. Unlike spoofing, the mechanism is infrastructural rather than informational: the goal is to impair competitors rather than to attract their trades. Quote stuffing is explicitly addressed under MAR {cite:p}`MAR596_2014` and has been the subject of regulatory scrutiny in both European and U.S. markets.

**Momentum ignition** involves placing a series of orders designed to create the appearance of directional price momentum, with the intent of triggering other market participants—particularly momentum-following algorithms and automated stop-loss systems—to trade in the same direction. Once the induced price move is underway, the manipulator rapidly reverses position to profit from the artificially generated displacement. The strategy exploits the behavioural predictability of other algorithms rather than manipulating order-book depth directly, and is therefore distinct from spoofing even though it may involve order cancellations. Its effectiveness depends on the prevalence of signal-reactive algorithms in the market, making it a form of abuse that is structurally enabled by the algorithmic nature of modern market participants.

**Wash trading** refers to simultaneously buying and selling the same instrument—either through coordinated accounts or self-matching orders—to generate artificial trading volume without any genuine change in economic ownership. The resulting inflated volume creates a misleading impression of market activity and liquidity, which can attract other participants or satisfy volume thresholds required for certain index inclusions or fee tiers. Wash trading is prohibited under MAR and U.S. securities and commodities law. It has been particularly prevalent in cryptocurrency markets, where the absence of comprehensive regulation until recently, combined with low fees and fragmented venues, created conditions that made artificial volume generation both easy and economically attractive {cite:p}`Makarov2020CryptoHFT`.

Taken together, the effects and risks of algorithmic trading highlight a fundamental asymmetry: efficiency benefits are diffuse and continuous, while risks tend to be concentrated and episodic. Regulatory frameworks have responded by imposing obligations—pre-trade controls, real-time monitoring, kill switches, and mandatory record-keeping—aimed at ensuring that the speed and automation of algorithmic systems are matched by an equivalent level of oversight and accountability. These obligations are detailed in the following section.

## Algorithmic Trading Regulation

The regulatory framework governing algorithmic trading has evolved in response to the structural transformation of financial markets brought about by automation. The central challenge for regulators is to preserve the efficiency benefits of algorithmic trading while mitigating the systemic and conduct risks it introduces—a balance that has led to different regulatory approaches across jurisdictions.

### European Union: MiFID II and MiFIR

The most comprehensive regulatory framework for algorithmic trading was introduced in the European Union through MiFID II (Directive 2014/65/EU) {cite:p}`MiFIDII2014` and MiFIR (Regulation (EU) No 600/2014) {cite:p}`MiFIR600_2014`, both of which became applicable on 3 January 2018. The framework applies to investment firms engaged in algorithmic trading—including those operating high-frequency strategies—and is detailed in Regulatory Technical Standard 6 (RTS 6) {cite:p}`ESMA_RTS6_2016`, which specifies organisational requirements. The conduct obligations specific to algorithmic manipulation are governed by the Market Abuse Regulation {cite:p}`MAR596_2014`.

The MiFID II obligations for investment firms engaged in algorithmic trading are structured around four main areas:

**Governance.** Firms must maintain documented procedures covering the full lifecycle of algorithmic strategies, from development and testing to deployment and decommissioning. Each deployed algorithm must be assigned a unique identifier that is attached to every order it generates, creating an audit trail for supervisory purposes. Firms are required to maintain an inventory of all deployed algorithms, and staff involved in algorithmic trading must demonstrate the necessary technical competence.

**Testing.** MiFID II places significant emphasis on pre-deployment testing. Firms must establish dedicated test environments, physically and logically separated from production systems, in which conformance testing, adverse-scenario testing, and backtesting of all algorithms intended for production can be conducted. This requirement formalises the testing procedures described in the preceding section as a legal obligation, not merely a best practice.

**Resilience.** Firms must deploy real-time monitoring systems capable of detecting anomalous behaviour in deployed algorithms and acting upon it rapidly. A critical requirement is the implementation of *kill switch* mechanisms—controls that allow the immediate halting of an individual algorithm or of the firm's entire algorithmic order flow—a direct regulatory response to incidents such as Knight Capital. Pre-trade controls must be applied to all orders, whether generated manually or algorithmically, to prevent the submission of orders with parameters that could disrupt orderly trading—for example, orders whose size or price fall outside predefined limits. Post-trade controls must also be in place, covering order reconciliation, market and credit exposure monitoring, and surveillance for potential market abuse.

**Post-deployment and ongoing oversight.** Firms are required to conduct an annual self-assessment of their algorithmic trading activities, covering both standard and high-frequency operations, and to participate in annual stress tests conducted by trading platforms to assess system resilience under high-volume and high-message-rate conditions.

Firms whose activity falls under the MiFID II definition of high-frequency trading face additional obligations. Order timestamps must be recorded at microsecond precision, the offset from Coordinated Universal Time must not exceed 100 microseconds—a standard that effectively requires atomic or GPS-linked clock synchronisation—and all orders, including cancellations and rejections, must be stored for a minimum of five years to support post-event forensic analysis. Firms whose algorithmic activity qualifies as market making under MiFID II rules are additionally required to enter into formal market-making agreements with the trading venues at which they operate, committing to providing quotes within defined parameters and under defined conditions.

In Germany, a subset of these obligations was pre-empted by the High-Frequency Trading Act {cite:p}`BaFinHFTAct2013`, which introduced an explicit authorisation regime for HFT firms and added a speed-based criterion ensuring that firms not genuinely engaged in high-frequency activity are not subject to the most burdensome HFT-specific requirements.

### United Kingdom: Post-Brexit Framework

Following the end of the Brexit transition period on 31 December 2020, MiFID II no longer applies directly in the United Kingdom. The Financial Conduct Authority (FCA) has incorporated the substance of the MiFID II algorithmic and HFT provisions into UK domestic law through the retained EU law mechanism. In practice, the substantive requirements for governance, testing, resilience, and HFT obligations remain closely aligned with the EU framework, though divergence may increase as the FCA develops an independent UK regulatory agenda.

### United States

The United States does not have a single, comprehensive regulatory framework for algorithmic trading equivalent to MiFID II. Regulatory oversight is divided between two principal agencies according to the type of instrument traded.

The **Securities and Exchange Commission (SEC)** regulates securities markets. The principal regulation affecting algorithmic trading for SEC-supervised entities—including national securities exchanges, alternative trading systems, and broker-dealers—is Regulation Systems Compliance and Integrity (Reg SCI) {cite:p}`SEC_RegSCI2014`, which requires these entities to implement and maintain robust systems, establish business continuity plans, and report systems disruptions. Broker-dealers are additionally subject to oversight from the Financial Industry Regulatory Authority (FINRA), whose rules include requirements for pre-trade risk controls and supervision of algorithmic strategies.

The **Commodity Futures Trading Commission (CFTC)** regulates derivatives markets. Since 2015, the CFTC has been developing a comprehensive framework specifically targeting algorithmic trading—Regulation Automated Trading (Reg AT) {cite:p}`CFTC_RegAT2015`—which would impose requirements broadly similar in scope to MiFID II's RTS 6, covering pre-trade risk controls, development and testing standards, and mandatory registration for entities engaged in automated trading. As of the time of writing, Reg AT had not been finalised, reflecting both the technical complexity of the rulemaking and the political sensitivity of imposing prescriptive obligations on trading infrastructure.

### Overarching Principles

Across all three jurisdictions, the regulatory philosophy governing algorithmic trading rests on several shared principles. First, the speed and automation of algorithmic systems must be matched by equivalent speed and automation of risk controls: kill switches, pre-trade limits, and real-time monitoring are not discretionary but mandatory. Second, the accountability of the human principals behind algorithmic systems must be preserved: governance obligations, unique algorithm identifiers, and record-keeping requirements ensure that automation does not create gaps in supervisory oversight. Third, the potential for algorithmic systems to be used for market abuse must be addressed through both ex ante controls—surveillance systems, order flagging—and ex post enforcement, supported by the granular data generated by the record-keeping requirements.

For practitioners, these obligations translate into significant compliance costs and operational complexity. Testing environments, atomic clocks, five-year data archives, and annual self-assessments represent substantial investments. At the same time, they align closely with the operational best practices that responsible algorithmic trading firms would adopt in any case—because the cost of failing to detect a misbehaving algorithm, as the Knight Capital episode demonstrated, can far exceed the cost of prevention.


