# Market microstructure

## Introduction

Market microstructure is the study of the processes and mechanisms through which financial instruments are traded in financial markets. It focuses on how different participants —such as investors, intermediaries, and liquidity providers—interact, and how their actions affect the price formation, liquidity, and efficiency of markets. Whereas many financial models often assume that prices reflect all available information, market microstructure digs deeper into the realities of trading: the role of transaction costs, bid-ask spreads, order types, and how information asymmetry influences trading strategies and outcomes.

At the core of market microstructure is the understanding that prices are not simply the result of supply and demand but are shaped by specific choices in the architecture of the market. These include:
* Trading mechanisms: how in practice investors interact with each other to trade (buy or sell) instruments
* Trading times and frequency: when and how often can a financial instrument be traded
* Order types: how investors communicate their intention of trading
* Trading protocols: what are the technical rules of the market
* Transparency: which information can be given to investors to
ensure they can trade fairly

By studying these elements, market microstructure helps explain phenomena like price discovery, short-term price fluctuations, and the impact of large trades.

## Types of trading mechanisms

The way financial markets are structured has a profound effect on how trades are executed, how prices are formed, and how liquidity is provided. At the heart of this structure lies the mechanism that governs how buyers and sellers interact. Broadly speaking, we can categorize trading mechanisms into three types: quote-driven, order-driven, and hybrid. Each has its unique characteristics and implications for market participants.

**Quote-Driven Markets**

In a quote-driven market, transactions revolve around a specialized intermediary known as a dealer or market maker. The dealer plays a central role by continuously quoting prices at which they are willing to buy and sell a given financial instrument. These quotes typically consist of two parts: the bid price, which is the price the dealer is willing to pay to buy the instrument, and the ask price, which is the price at which they are willing to sell it. The dealer profits from the spread, the difference between the bid and ask prices, and adjusts these quotes dynamically based on supply, demand, and market conditions.

In this system, investors cannot trade directly with each other. Instead, they must transact exclusively through the dealer, who provides liquidity by maintaining an inventory of the instruments and adjusting quotes to reflect market activity. This structure is particularly common in over-the-counter (OTC) markets, such as foreign exchange or bond markets, where liquidity might not be as readily available as in centralized exchanges.

An important feature of quote-driven markets is that prices are often indicative—they provide an approximation of the market but may not be immediately executable, especially for larger quantities or illiquid instruments. In many cases, a negotiation process is necessary for larger trades. Investors and dealers engage in a dialogue to finalize the trade, allowing the dealer to reassess risk and adjust prices accordingly.

**Order-Driven Markets**

Order-driven markets operate very differently from their quote-driven counterparts. Instead of relying on dealers to provide prices and liquidity, these markets use a central order book where buyers and sellers submit their orders. Investors place orders that specify the price at which they are willing to buy or sell a security, and the market matches these orders according to a predefined set of rules.

In an order-driven system, participants interact directly with each other through their orders. There is no negotiation process; instead, a matching engine automatically pairs buy and sell orders based on their price and the time they were entered into the system. This ensures a fair and transparent market, where prices are determined by the collective actions of all market participants.

The most common types of orders are limit orders and market orders. A limit order specifies a price at which the trader is willing to buy or sell, while a market order is an instruction to execute the trade immediately at the best available price. The order book is public, meaning that participants can see all current bids and asks, providing a high level of transparency in terms of available liquidity and market sentiment.

Order-driven markets are typical of centralized exchanges, such as stock exchanges like the New York Stock Exchange (NYSE) or futures markets. These markets tend to have high volumes of orders, allowing for continuous matching and a high degree of liquidity, particularly in actively traded instruments.

**Hybrid Markets**

Many modern markets blend the features of both quote-driven and order-driven systems to offer the best of both worlds. These hybrid markets are designed to provide liquidity through dealers while maintaining the transparency and fairness of an order-driven system.

One version of a hybrid market includes quote-driven mechanisms where dealers post executable prices. Unlike indicative quotes, these prices are firm and represent actual tradeable prices for specified quantities. This arrangement provides certainty for investors, especially when trading in large quantities or illiquid instruments, where the guarantee of liquidity from a dealer can be critical.

In another version of a hybrid market, dealers are obligated to participate in an order-driven system. They act as liquidity providers, continually placing passive two-way orders (both buy and sell orders) on the public order book. These dealers, often referred to as market makers, must post prices even when the market is quiet, ensuring that there is always liquidity available. This contractual obligation to provide liquidity helps maintain market stability and reduces the risk of sudden price jumps due to a lack of counter-party interest.

Hybrid markets strike a balance between dealer-driven liquidity provision and the transparency and efficiency of an order book system. They are commonly used in highly liquid markets, such as foreign exchange platforms and some modern equity exchanges, where large institutional players need the certainty of liquidity alongside the openness of an order-driven market.

**The rationale for each trading mechanism**

Each of these trading mechanisms serves different types of markets and participants. Quote-driven markets are particularly useful for illiquid or over-the-counter products, where large trades and custom negotiations are common. Order-driven markets thrive in environments with high trading volumes and transparency, offering fast execution and price discovery through collective action. Hybrid markets bring together the strengths of both systems, ensuring liquidity and fairness even in challenging trading conditions. Understanding these mechanisms is crucial for anyone looking to navigate today’s financial markets.

## Trading Times and Frequencies

The timing of trades and the frequency with which they occur are essential aspects of market design, significantly impacting how liquidity, price discovery, and volatility are managed. Different trading mechanisms operate under varying time structures, and these structures influence the behavior of market participants, the efficiency of order execution, and the stability of markets. Broadly, trading times and frequencies can be categorized into continuous trading, periodic auctions, and request-driven trading. Each of these methods plays a role in shaping market dynamics, especially under different market conditions such as periods of high volatility or when liquidity is scarce.

**Continuous Trading**

Continuous trading is the most common method used in modern financial markets, where trading happens continuously within a defined window of time. During this window, market participants can submit and execute orders at any moment, allowing for a constant flow of trades and real-time price updates. This method is particularly effective in markets with high trading volumes, where liquidity is readily available throughout the trading day.

- **Order-Driven Continuous Trading**: In order-driven markets, continuous trading typically takes place using a **continuous double auction** mechanism. In this system, all buy and sell orders are collected in a **limit order book**, where they are matched based on price and time priority. The order book allows for ongoing price discovery as orders are continuously executed whenever a matching counterparty is found. Traders have full visibility of the order book, seeing both the available bids and asks at various price levels, which ensures transparency and competitive pricing.

- **Quote-Driven Continuous Trading**: In quote-driven markets, dealers play a pivotal role in continuous trading by constantly updating their **bid** and **offer prices** for the instruments they manage. In **purely quote-driven markets**, these prices are often indicative, meaning they serve as guidelines and may require negotiation before a trade can be executed. However, in **hybrid markets**, dealers may quote **firm prices**, which are executable immediately for specific quantities. This ensures that liquidity is available continuously, even when direct order matching between investors is not feasible.

Continuous trading is particularly advantageous for markets with high liquidity, as it enables fast execution and efficient price formation. However, in periods of high volatility, continuous trading can exacerbate price fluctuations, as large orders or sudden imbalances between supply and demand can cause significant price swings.

**Continuous Trading with Scheduled Call Auctions**

To address the challenges of volatility in continuous markets, some systems introduce scheduled **call auctions** at key points during the trading day. A call auction is a method where all orders are temporarily pooled and then executed simultaneously at a single price, which balances supply and demand. 

In a **continuous trading with call auctions** model, the market operates continuously but pauses at predetermined times, such as the market **open** or **close**, or during periods of heightened volatility, to conduct a call auction. These auctions help stabilize prices by concentrating liquidity into a single moment, allowing for a more orderly transition between trading sessions or a more controlled response to volatility spikes.

At the open, for example, call auctions help manage the influx of orders that accumulate overnight, ensuring that the market starts trading at a fair price that reflects the balance of supply and demand. Similarly, at the close, call auctions help establish a final price for the trading session, which is often used as a reference for pricing derivatives and other financial products.

**Scheduled Call Auctions**

In markets that rely on **scheduled call auctions**, trades only happen at specific times, rather than continuously. Investors submit their buy and sell orders in advance, and these orders are aggregated until a scheduled auction takes place. At the auction time, the market clears at a single price that maximizes the volume of trades, ensuring that the highest number of buy and sell orders are matched.

Scheduled call auctions are often used in less liquid markets, where continuous trading might lead to significant price instability due to the low number of orders. By pooling orders into a single event, scheduled auctions create concentrated liquidity and help prevent large price jumps between trades.

This method is commonly employed in initial public offerings (IPOs), where the initial price discovery process can be difficult due to uncertainty about demand. Scheduled call auctions provide a more controlled environment for determining the opening price of the security.

**Request-Driven Trading**

In some markets, trading does not happen on a continuous or scheduled basis but instead occurs **at the discretion of the client**. This model, known as **request-driven trading**, is often used in over-the-counter (OTC) markets for instruments that are not frequently traded or have specialized liquidity needs.

In request-driven trading, a client requests a quote or a trade from a dealer at a specific time, and the dealer responds with a price. The trade is executed based on this interaction, often involving some negotiation over the size or price of the transaction. This model is common in markets for customized or illiquid products, such as large blocks of bonds or structured financial instruments, where finding a counter-party may not be straightforward.

Request-driven trading provides flexibility for both clients and dealers, allowing them to negotiate trades that meet specific needs. However, it lacks the transparency and immediacy of continuous or auction-based systems, as each trade is typically a private transaction between the client and the dealer.

**The rationale behind these choices**

The choice of trading frequency and timing mechanism reflects the unique characteristics of each market and the needs of its participants. Continuous trading offers fast execution and real-time price discovery, while scheduled auctions and request-driven trading provide alternatives that manage liquidity and volatility more effectively under specific conditions. Understanding these mechanisms is crucial for market participants seeking to navigate the intricacies of different trading environments.

### Order-Driven Markets and the Central Limit Order Book (CLOB)

Order-driven markets are a fundamental type of financial market structure where prices and liquidity are determined directly by the orders placed by market participants, without the need for intermediaries such as dealers. In these markets, investors interact through a **central limit order book (CLOB)**, a system that aggregates and displays buy and sell orders in real time. The CLOB organizes these orders based on price, ensuring that the best available prices are always visible to participants, making the system transparent and efficient.

CLOBs don't allow orders at arbitrary prices, instead enforcing minimum price increments known as **tick sizes**, which define the smallest allowable difference between order prices. The tick size choice traditionally falls to the market owner, who aims to balance liquidity by setting smaller tick sizes, encouraging tighter spreads and more precise pricing. However, overly small tick sizes can also penalize liquidity providers who maintain constant bid and ask orders in the CLOB, as they may face more frequent price competition and increased order cancellations.

In recent years, regulatory bodies in some markets have implemented restrictions on tick sizes to stabilize order book structures and reduce excessive market noise. For instance, in the European Union, MiFID II introduced a tick size regime based on price levels and average daily number of trades for specific instruments, limiting the ability of markets to set overly fine increments. Similarly, in the U.S., tick size pilot programs have explored tick adjustments for smaller-cap stocks to assess impacts on liquidity and execution quality. Such regulatory measures aim to ensure fairer conditions for both liquidity providers and market participants, while supporting orderly and efficient markets.

Additionally to tick sizes, markets typically impose restrictions on the the quantities that can be traded, known as **lot sizes**.

#### The Structure of the Central Limit Order Book (CLOB)

At any given moment, the CLOB provides a snapshot of the market by showing all active buy and sell orders. These orders are aggregated anonymously and displayed in two columns: one for **buy orders** (bids) and another for **sell orders** (asks or offers). Each column is ordered by price, with the best bid (the highest price a buyer is willing to pay) and the best ask (the lowest price a seller is willing to accept) at the top.

- **Best Bid/Ask**: The best bid and ask, $P^b_{best}$ and $P^a_{best}$, represent the highest and lowest prices, respectively, that are currently available in the market. The difference between them is the **bid-ask spread**, which can serve as a measure of liquidity. A narrow spread generally indicates higher liquidity.

- **Market Depth**: The CLOB also shows the **market depth**, which refers to the number of orders available at various price levels. Market depth gives traders insight into the potential for price movements based on the volume of buy and sell interest at different prices.

- **Mid-Price**: The **mid-price** is calculated as the average of the best bid and best ask prices. It serves as an estimate of the fair market price at a given moment:

$$ P_{mid} = \frac{1}{2}(P^b_{best} + P^a_{best}) $$

- **Spread**: The difference between the best bid and ask prices. It is a metric of liquidity in the order book, since the larger it is the less likely is that investors can trade at prices close to the mid-price:

$$ S = P^a_{best} + P^b_{best} $$

- **Volume Imbalance**: it refers to the difference in the volume of buy orders, typically at the best bid and ask prices, although a larger number of levels might be taken for a more robust estimation. A significant imbalance can indicate potential price movement; for example, if the volume at the best bid is substantially higher than the volume at the best ask, it may suggest upward pressure on the price. This feature helps traders gauge short-term supply and demand dynamics and assess potential price changes. It is typically reported as a percentage over total volume in the best bid and ask: 

$$ I = \frac{V^b_{best} - V^a_{best}}{V^b_{best} + V^a_{best}} $$

The following picture shows a visualization of the order book called market depth, since it shows the current orders sitting in the book ordered by price. Each level might have orders from different participants, but we show them aggregated which is how real markets report them in their feeds. 

```{figure} figures/market_depth_clob.png
:name: fig:market_depth_clob
:width: 8in
Market Depth visualization of a Central Limit Order Book, with orders sorted by price. Volume is aggregated for the different orders in the same price level. In this example, the tick size is 1, the mid price is $P_{mid} = 100$, the spread is $S = 4$ and the imbalance $I = 0.53$
```

#### Types of Orders

Market participants in order-driven markets can use a variety of order types, each serving different trading objectives:

1. **Market Orders**: These orders instruct the system to buy or sell immediately at the best available price, consuming always the liquidity available at best prices (**price priority**). Market orders are executed quickly, but they carry the risk of paying a higher price or receiving a lower price than expected if there is insufficient liquidity at the best bid or ask. In this case, the order may "walk the book," executing across multiple price levels and resulting in a higher average price (for buys) or lower average price (for sells). The execution price of an order that consumes liquidity across various levels is computed using the **volume weighted average price (VWAP)**:

$$ P_{exec} = \frac{\sum_i v_i P_i}{\sum_i v_i} $$

   **Example**: Taking the previous CLOB example, suppose an investor wants to buy Suppose an investor wants to buy 500 shares with a market order. As shown in the figure below, the order consumes liquidity up to three levels. The resulting execution price is 103.51. After the market order, the mid-price is recalculated given the new liquidity, to $P_{mid} = 101$, and the spread broadens to $S = 6$ 

```{figure} figures/market_order.png
:name: fig:market_order
:width: 8in
Effect of a buy market order of size 500 in the Central Limit Order Book. 
```


2. **Limit Orders**: These specify a price at which the trader is willing to buy or sell. If the limit price is not immediately available to trade, the order remains in the order book until a matching counter-party arrives or the order is canceled. Limit orders allow traders to control the price at which they execute but come with the risk that the order may not be executed if the market price moves away from the limit.

When an order is added to a level with existing liquidity, there is the question of which order has the priority when a matching order arrives at the CLOB. Most markets use a **time priority** or first in first out (FIFO) rule, in which orders that arrived earlier are consumed first. It is not the only rule, though. For instance some markets use a **pro-rata rule**, in which all existing orders are consumed proportionally to their size. 

   **Example 1**: Using again the previous order book, suppose and investor wants to buy the 500 shares but instead of sending a market order, it uses a limit order at price 98. Since there are order existing at that price level, the order sits at the bottom of the level. If this is a market with a time priority rule, this means this order will be the last to be consumed at the level. After placing the order, the mid-price and the spread does not change, but the imbalance is affected, see figure below.

   ```{figure} figures/limit_order_passive.png
   :name: fig:limit_order_passive
   :width: 8in
   Effect of a buy limit order of size 500 and price 98 in the Central Limit Order Book. 
   ```

   **Example 2**: If the investor instead places the order at price 102, there is partial matching liquidity at this level. A partial execution of the limit order happens at price 102, with the remaining order sitting now at this price level. The new mid-price is $P_mid = 102.5$ and the spread $S = 1$.

   ```{figure} figures/limit_order_aggressive.png
   :name: fig:limit_order_aggressive
   :width: 8in
   Effect of a buy limit order of size 500 and price 102 in the Central Limit Order Book. A hatch pattern is used to show the consumed liquidity by the limit order. 
   ```

3. **Hidden Orders**: Hidden orders are limit orders that are not visible to other market participants. They allow traders to conceal their trading intentions, which can be advantageous in avoiding market impact or revealing their strategy to others. However, hidden orders generally have **lower priority** compared to visible orders at the same price level, meaning they will only be executed after all visible orders at that price have been matched.

   **Prevalence**: Estimates suggest that hidden orders can account for approximately 10% to 20% of total liquidity on major exchanges like the NASDAQ or NYSE. The prevalence of hidden orders tends to increase during periods of high volatility or when large institutional players are active.

4. **Other Order Types**:

   - **Market-to-Limit**: Begins as a market order but converts into a limit order if only part of the order is filled.
   - **Immediate-Or-Cancel**: Any unexecuted portion of the order is canceled immediately after partial execution.
   - **Fill-Or-Kill**: The order is either executed in full immediately or not at all.
   - **All-Or-None**: Similar to Fill-Or-Kill, but the order may remain active if it cannot be immediately executed.
   - **Stop Orders**: Triggered when a specified price is reached, turning into a market or limit order based on conditions.

### Trading Fees

Trading fees are an important consideration in order-driven markets, as they can impact the overall cost of executing trades. Exchanges generally apply fees based on the type of order and the participant's role in providing or taking liquidity. The common fee structures include:

* Maker-Taker Model: This model differentiates between liquidity providers (makers) and liquidity takers. Makers, who place limit orders that add liquidity to the order book, are typically rewarded with a rebate, while takers, who execute against existing orders and remove liquidity, are charged a fee. This model incentivizes the addition of liquidity to the market.

* Inverted Maker-Taker Model: In some cases, the exchange may use an inverted model, where takers receive a rebate, and makers are charged a fee. This is used to attract more aggressive trading and increase market activity.

* Flat Fee Model: Some exchanges charge a flat fee per transaction, regardless of whether the participant is adding or removing liquidity. This approach provides simplicity and is often used in less active markets.

The specific fee structure and the level of fees depend on various factors, including the type of asset being traded, the exchange, and the participant's trading volume. In some markets, high-frequency traders may receive favorable fee arrangements due to the large volumes they generate, which contribute significantly to market liquidity.

#### Types of Order Book Data

Order-driven markets often provide different levels of data to market participants, depending on their needs:

- **Level I**: This basic level shows only the best bid and ask prices, giving traders a minimal snapshot of the market.

- **Level II**: More advanced, this level displays multiple bid and ask levels beyond the best prices, giving insight into the market depth.

- **Level III**: The most detailed level of data, showing individual orders, their sizes, prices, and time stamps. This information is typically used by algorithmic traders and market makers to track the behavior of specific market participants.

**Tick Data**

Historical data from order books is called **tick data**, and captures every change that occurs in the order book. It is  provided by the exchanges or via financial data companies like LSEG (ex Refinitiv) and Bloomberg, which aggregate and normalize this data.  There are also free resources with samples of data like Lobster. 

Tick data generally comes in two forms:

* **Order Book Snapshots**: also known as market-depth data, this form of tick data provides detailed information about the order book at specific time intervals, showing the number of buy and sell orders at various price levels. Order book snapshots allow traders to assess liquidity and understand the potential for price movements based on supply and demand. For example, a trader using order book snapshots can identify a large concentration of sell orders at a specific price level, indicating potential resistance.

* **Message Data**: this data records all order book events, such as order submissions, cancellations, and executions, with timestamps. Message data allows traders to reconstruct the order book and analyze the flow of activity in real time. For instance, a trader reviewing message data might notice a series of large buy orders submitted successively, indicating strong buying interest and potentially signaling an upward trend.

#### Advantages and Challenges of Order-Driven Markets

The CLOB system provides significant **pre-trade transparency**, as market participants can view the full order book and adjust their strategies based on available prices and liquidity. This transparency promotes price discovery, helping ensure that prices reflect the collective expectations of all market participants.

However, the system is not without challenges. In less liquid markets, **price volatility** can be higher due to the lack of continuous buy and sell interest. Large market orders can "sweep" through multiple price levels, causing significant short-term price fluctuations. Moreover, the transparency of the system can also lead to **front-running**, where certain traders take advantage of visible large orders by placing their own orders ahead of them.

To mitigate these issues, many markets incorporate mechanisms like **circuit breakers** and **trading halts** during periods of extreme volatility, as well as **opening and closing auctions** to establish stable prices at the beginning and end of trading sessions.

## Quote-driven markets: the Request for Quote protocol

## Exercises
