(intro_financial_markets)=
# Financial Markets

## Introduction

Financial markets address a fundamental challenge faced by societies: the efficient allocation of savings toward productive uses. Individuals and institutions with excess funds aim to achieve the highest returns from them (investment) while keeping them as readily available as possible (i.e. with maximum *liquidity*, a central concept in modern finance that will be discussed formally in {ref}`liquidity_modelling`). Consequently, they often prefer to lend money on a short-term basis. Conversely, those requiring capital (for example, to launch new ventures, expand existing businesses, acquire assets such as homes through mortgages, or finance social programs) seek to secure funds at minimal cost and for extended periods. Without a mechanism to reconcile these opposing objectives, surplus funds may remain idle, hindering their potential to contribute to economic productivity.

Modern economies solve this problem in two complementary ways, which form the backbone of the financial system: the banking system and financial markets {cite:p}`Mehrling2011NewLombardStreet`. This chapter first explains how each of these two mechanisms resolves the tension between liquidity and funding, with a strong focus on financial markets, that will be the focus of the rest of the book. It then introduces the main asset classes traded in these markets, before turning to how markets are structured — the venues, participants, and protocols through which trading actually happens — and how that structure is regulated. Later chapters build directly on this material: {ref}`intro_financial_instruments` develops the mechanics and valuation of the instruments introduced here, and {ref}`market_microstructure` develops the trading mechanisms introduced in this chapter's discussion of market structure.

## The Banking System

In the banking system, the center is the bank: an institution that offers short-term deposits with high availability to those with excess funds, and long-term loans to those who need funds. A capital cushion, held partly in cash and partly in short-term loans, is maintained to meet potential withdrawals. Mehrling's *money view* of banking frames this as banks acting as dealers in liquidity — market-making between depositors who want to lend short and borrowers who want to borrow long {cite:p}`Mehrling2011NewLombardStreet`. This activity is not exempt from risk:

-   **liquidity risk**, which can happen if the demand to withdraw deposits exceeds the capital cushion, and depositors cannot be satisfied (a so-called *bank run*)

-   **credit risk**, which happens when borrowers of funds default on their obligations and don't give back those funds

Banks compensate those risks by charging a spread between the interest paid on loans and the interest paid on deposits, on top of a margin to cover their own operations. The banking system has traditionally been the core of the financial system in Europe.

## How Financial Markets Work

In financial markets, those who need funds issue financial instruments: legally binding contracts that articulate the terms under which those funds will be returned to the investor, as well as the compensation for the service. So far that is not so different from a traditional banking loan. What sets financial instruments apart is the possibility of transferring ownership of the contract, i.e. the right to receive those future cash flows. This gives the lender a way to recover funds before the contract ends, solving the liquidity problem even when the underlying contract has a long-term horizon.

Of course, doing so requires the lender to find a counterpart willing to purchase the instrument, and to agree on a price. Pricing financial instruments is not a simple task, since their value depends on assumptions about the certainty of those future cash flows (for instance, what if the borrower cannot commit to paying back in the future?). There are also opportunity costs to consider, since a potential investor will compare the return on the instrument with other productive uses of their money. Financial markets developed precisely to solve these two problems: finding counterparts, and setting a price.

Financial markets are the place where interested parties meet and negotiate prices. In *primary markets*, financial instruments are issued by borrowers and acquired initially by investors, sometimes via intermediaries like banks. In *secondary markets*, already-issued instruments are traded between investors, with the original borrower no longer playing any part in the process. Most trading today occurs in secondary markets.

Financial markets therefore serve two functions at once: they give investors a mechanism to obtain liquidity from their investments, and they serve as a mechanism for price discovery. In the end, as in any market, the price of a financial instrument is whatever two willing parties agree to transact at, independent of the subjective value each of them places on it. By bringing many investors together in the same venue to negotiate, financial markets aggregate their diverse expectations about the value of an instrument into a single price. That price then guides other investors' future decisions — a theme {ref}`market_microstructure` returns to in more formal terms when discussing price discovery in specific trading mechanisms.

## Who Participates in Financial Markets?

Financial markets primarily involve legal entities, although natural persons (individuals) may also participate, typically through intermediaries such as banks or brokers. The core participants issuing financial instruments are varied: corporations issue securities to fund their business activities, while governments at all levels — local, regional, national, and supranational — issue bonds to finance social programs or public investments. Banks also design and issue customized products aimed at meeting the investment needs of institutional and individual investors.

On the demand side, institutional investors such as hedge funds, mutual funds, pension funds, and insurance companies acquire financial instruments either to generate returns for their clients or to manage specific risks. Corporations also buy financial instruments, both to make their excess cash productive and to hedge against business risks. Banks acquire these instruments as part of their liquidity management, to generate returns on customer deposits, and to mitigate financial risks. Central banks are participants as well, using financial instruments to execute monetary policy and influence money supply and interest rates.

In terms of intermediation, banks and brokers facilitate market transactions. Banks, particularly in their role as market-makers, are key *liquidity providers*: they stand ready to buy or sell financial instruments, profiting from the spread — the difference between the buying and selling price — which compensates them for holding the instrument until an opposing counterparty emerges. Brokers, by contrast, connect buyers and sellers through their networks or proprietary platforms, charging a fee for matchmaking without holding the instruments themselves.

A more recent addition to this landscape are the *new liquidity providers*: technology-driven, non-bank firms, many of which originated in high-frequency trading, that now use automated algorithms to provide liquidity in electronic markets. They compete directly with traditional bank market-makers on speed and pricing, and we will return to their role repeatedly throughout this chapter — as systematic internalizers, as counterparties in retail order flow, and as participants in each individual asset class.

## Types of Financial Instruments and Asset Classes

Financial instruments are the building blocks of financial markets: the contracts or securities through which money flows. They are typically grouped into distinct *asset classes* based on their characteristics, the type of return they provide, and the markets they trade in. This section introduces each asset class only at the level needed to understand market structure and regulation; {ref}`intro_financial_instruments` covers their economic function, valuation, and risk factors in depth.

The major asset classes are equity, fixed income, money markets, derivatives, foreign exchange (FX), commodities, and cryptocurrencies.

### Equity and Fixed Income

The most well-known financial instruments are stocks and bonds, which form the foundation of two major asset classes: equity and fixed income.

- **Stocks** represent ownership in a corporation and give investors a claim on a portion of the company's assets and earnings. Stocks are part of the equity asset class, providing potential for capital appreciation and dividends. However, they also expose investors to market volatility and business risk, making them a relatively high-risk, high-reward investment.
  
- **Bonds**, on the other hand, are debt securities issued by governments, corporations, or other entities to raise capital. Investors in bonds lend money to the issuer in exchange for periodic interest payments and the return of the bond's face value at maturity. Bonds belong to the fixed income asset class, which generally offers more stable and predictable returns than equity, although they are still subject to risks such as interest rate fluctuations and credit default. Within fixed income, we typically distinguish between rates and credit instruments:
    * **Rates instruments**, whose value is primarily driven by changes in interest rates (e.g. government bond yields, central bank policy rates). Government bonds fall into this category.
    * **Credit instruments**, primarily driven by the creditworthiness of the issuer — corporate bonds being the main example. As we discuss in {ref}`intro_financial_instruments`, corporate bond value is also influenced by interest rates, though the effect is generally more marginal than the credit-spread component.

Both stocks and bonds are often referred to as *cash instruments*, meaning their value derives directly from the underlying market dynamics, without the need for an intermediary asset.

### Money Markets

Within the fixed income category, the money market is a sub-sector of short-term debt securities that typically mature in less than a year, such as Treasury bills, commercial paper, and certificates of deposit. MiFID II lists money-market instruments as their own category, distinct from transferable securities such as bonds {cite:p}`MiFIDII2014`; in practice, this book treats them as part of the broader fixed income family, since they share the same rates-driven valuation logic, just at very short maturities. Money market instruments are highly liquid and relatively low-risk, making them attractive both for institutions managing short-term liquidity needs and for investors seeking a safe place to park cash temporarily.

### Derivatives

Derivatives are financial contracts whose value is derived from the performance of an underlying asset, index, or rate. They can be based on a wide range of underlying assets, including stocks, bonds, commodities, currencies, and interest rates. This is why some categorize derivatives within the asset class of the underlying instrument, though they are often considered an asset class of their own due to their unique characteristics.

Derivatives are versatile and serve several purposes, such as hedging risks, speculating on price movements, or leveraging positions. Common types of derivatives include futures, options, swaps, and forwards, each offering different structures and risk profiles. For example, a company might use derivatives to hedge against fluctuations in interest rates or commodity prices, while a trader might use options to speculate on the price of a stock.

### Foreign Exchange (FX)

The foreign exchange (FX) market is where participants trade currencies. Transactions in the FX market are generally categorized as either **spot** or **derivative** transactions.

- **Spot transactions** involve the immediate exchange of currencies, typically settling within two business days. They are essential for international trade and finance, but are not classified as financial instruments under MiFID II, since they do not involve contractual obligations extending beyond the settlement period {cite:p}`MiFIDII2014`.

- **FX derivatives**, such as forwards, options, and swaps, are used to hedge currency risk or speculate on currency movements. Unlike spot transactions, these contracts involve specific obligations between parties and are therefore considered financial instruments.

FX markets are used by a wide range of participants, including central banks (to manage currency reserves), corporations (to hedge currency risk in international operations), and investors looking to profit from currency fluctuations.

### Commodities

Commodities are physical goods such as oil, gold, and agricultural products, traded primarily in spot markets. These goods themselves are not considered financial instruments, as they represent tangible assets rather than financial claims. However, the derivatives based on commodities, such as futures and options on commodities, are classified as financial instruments. These contracts enable investors to gain exposure to commodity price movements without needing to take physical delivery of the underlying goods, providing opportunities for hedging and speculation.

### Cryptocurrencies

Cryptocurrencies, such as Bitcoin and Ethereum, are a relatively new and rapidly evolving asset class. Unlike traditional financial instruments, cryptocurrencies do not represent contractual obligations or financial claims. Instead, they function as digital assets, leveraging blockchain technology to provide decentralized and transparent transactions. Their value is driven by supply and demand dynamics, making them highly volatile compared to other asset classes.

Cryptocurrencies themselves are not classified as financial instruments under MiFID II; in the European Union, they instead fall under the dedicated Markets in Crypto-Assets Regulation (MiCA) {cite:p}`MiCA2023`, discussed further in this chapter's section on regulation. Derivatives on cryptocurrencies (such as Bitcoin futures), by contrast, are considered financial contracts and allow market participants to speculate on or hedge against cryptocurrency price movements, much as they would with any other asset class.

## Financial Market Structures

Market structures shape how participants interact and how trades are executed. Traditionally, markets were organized around the needs of intermediaries — dealers who facilitate trading by providing liquidity — but technology, competition, and regulation have reshaped this considerably. Financial markets can broadly be organized into three structures, based on who is allowed to interact with whom:

**Inter-Dealer Markets**: venues where intermediaries, typically dealers or market makers, trade exclusively with each other in order to manage their own inventories before serving clients in dealer-to-client markets. The main types are exchanges and inter-dealer broker networks, both discussed below. While traditionally restricted to dealers, some inter-dealer markets now grant institutional investors direct membership or connectivity — an arrangement known as **Direct Market Access (DMA)**.

**Dealer-to-Client Markets**: the most common venues, where dealers interact with institutional and retail clients. These markets are typically either quote-driven, where dealers set the price, or order-driven, where buyers and sellers are matched directly; {ref}`market_microstructure` develops this distinction and the trading mechanisms behind it in more formal detail. Electronic platforms have increasingly displaced voice-based trading in both.

**Alternative ("all-to-all") Markets**: structures that eliminate the segmentation between dealers and clients, letting any participant — dealer or client — trade under the same conditions. These have gained ground as technology lowered the cost of running an order book, and as regulation pushed toward broader competition, most notably Reg NMS in the United States {cite:p}`SEC2005RegNMS` and MiFID II in Europe {cite:p}`MiFIDII2014`.

Markets have historically moved through these three structures in roughly this order: single-dealer platforms, where a client could only trade with one intermediary, common in the early stages of a market or for niche, complex products; multi-dealer platforms, where competition among dealers improved price transparency for clients; a dealer-to-dealer layer, letting dealers manage inventory in bulk once trading between them was itself well established; and finally all-to-all markets, removing the dealer/client distinction altogether. No asset class has completed this progression uniformly — as the per-asset-class discussion later in this chapter shows, equities and standardized derivatives are largely all-to-all today, while much of fixed income remains dealer-centric.

Three trends have driven this evolution across asset classes: **accessibility**, as all-to-all markets let participants reach liquidity directly, bypassing intermediaries; **transparency**, as post-crisis regulation increasingly requires disclosure of pricing and trade data; and **fragmentation**, as more venues competing for the same order flow split liquidity that used to sit on a single exchange.

### Market Structure Terminology by Jurisdiction

Regulators on each side of the Atlantic use different terms for broadly the same structures. In the **United States**, regulation distinguishes Exchanges from Alternative Trading Systems (ATS) — the latter grouping all non-exchange venues such as ECNs, inter-dealer broker networks, and dark pools — while Dodd-Frank introduces Swap Execution Facilities (SEFs) as the venue type for standardized derivatives, particularly swaps {cite:p}`DoddFrank2010`.

In **Europe**, MiFID II defines four categories {cite:p}`MiFIDII2014`:
* **Regulated Markets (RMs)**: broadly equivalent to exchanges.
* **Multilateral Trading Facilities (MTFs)**: broadly equivalent to ATS, covering ECNs and dark pools. A related category, **Organized Trading Facilities (OTFs)**, is restricted to non-equity instruments and carries somewhat lighter requirements, but is structurally similar to an MTF.
* **Systematic Internalizers (SIs)**: not a market structure in the same sense as the others — an SI is a broker or dealer executing client orders on its own account, outside RMs, MTFs, or OTFs.

## The Building Blocks of Financial Market Structure

### Exchanges

Exchanges are among the oldest institutions in financial markets: centralized venues where buyers and sellers meet to trade. Historically, they were physical floors where traders negotiated prices through open outcry; today they operate almost entirely as electronic **Central Limit Order Books (CLOBs)**, which match buy and sell orders by price and time priority.

An exchange's primary role is price discovery: by aggregating the supply and demand of many participants and publicly disseminating orders and executed trades, it produces a transparent benchmark price and reduces information asymmetry among participants. Its second role is concentrating liquidity — bringing enough buyers and sellers into one venue that participants can trade without a lengthy search for a counterparty.

Access to exchanges has traditionally been restricted to members such as brokers and dealers, trading on behalf of clients or for their own account. Direct Market Access (DMA), introduced above, now lets institutional investors connect directly through broker-provided infrastructure, reducing reliance on intermediaries.

Prominent examples include the New York Stock Exchange (NYSE) and NASDAQ for US equities, the London Stock Exchange (LSE) and Deutsche Börse in Europe, and the Chicago Mercantile Exchange (CME) and Eurex for standardized derivatives; many have since diversified into newer instruments such as exchange-traded funds (ETFs). Exchanges increasingly compete with the alternative trading systems discussed next — dark pools and ECNs — a competition that both MiFID II in Europe and Reg NMS in the United States have actively encouraged by lowering the barriers to running a rival venue {cite:p}`MiFIDII2014` {cite:p}`SEC2005RegNMS`.

### Inter-Dealer Broker Networks (IDBs)

Inter-dealer broker (IDB) networks act as intermediaries between dealers, particularly in over-the-counter (OTC) markets where trading is less centralized and instruments are often bespoke. Unlike exchanges, IDBs operate exclusively among dealers — banks and other institutions acting as market makers — helping them manage inventory imbalances, hedge positions, and execute large trades without disrupting the broader market.

IDBs historically relied on voice brokers connecting dealers by phone, well suited to illiquid or bespoke instruments that require negotiation. Electronic platforms have since taken over for more liquid instruments: BrokerTec and MTS Cash for government and corporate bonds, ICAP and CME SwapStream for swaps, and EBS for FX. A defining feature of IDBs is anonymity — brokers act as neutral intermediaries so that a dealer's trading strategy or inventory position is not revealed to competitors, which matters most where large trades can move prices.

MiFID II and Dodd-Frank have both pushed IDBs toward greater transparency and reporting {cite:p}`MiFIDII2014` {cite:p}`DoddFrank2010`, and some IDBs now offer institutional investors limited DMA-style access, blurring the line with dealer-to-client markets.

### Electronic Communication Networks (ECNs)

Electronic Communication Networks (ECNs) connect buyers and sellers directly through fully transparent, "lit" order books, much like an exchange. As trading has become almost entirely electronic, the practical differences between ECNs and exchanges have narrowed to two: exchanges retain a dominant role for intermediaries such as market-makers, and exchange prices remain the official reference used for end-of-day valuation and contract settlement.

ECNs matter most where no traditional exchange exists. In FX, platforms such as FXAll, Hotspot FX, and 360T fill that role; in crypto, exchanges such as Binance and Coinbase Pro function as order-driven venues much like ECNs adapted to digital assets. ECNs have also expanded into asset classes that already have exchanges, competing on fees and functionality — Turquoise in pan-European equities, CBOE (formerly BATS) in US equities, and BrokerTec and MarketAxess in fixed income, the latter combining ECN-style order books with Request-for-Quote (RfQ) protocols.

ECNs are subject to the same transparency requirements under MiFID II and Reg NMS as exchanges {cite:p}`MiFIDII2014` {cite:p}`SEC2005RegNMS`, and the proliferation of competing ECNs is itself a driver of the liquidity fragmentation discussed above.

### Dark Pools

Dark pools are private venues where buy and sell orders are matched without being publicly displayed before execution. Institutional investors use them to execute large orders without signaling their intentions to the broader lit market, which would otherwise move the price against them.

Dark pools use one of three matching mechanisms: **dark order books**, matching hidden limit orders by price and time priority; **midpoint matching**, using the bid-ask midpoint from a lit market as the reference price; and **pass-through mechanisms**, routing unmatched orders to lit venues. Prominent examples include Liquidnet in equities and Hotspot QT in FX.

Because dark trading removes volume from public order books, regulators worry it degrades price discovery in lit markets; MiFID II responded with volume caps on dark pool trading, alongside exemptions for large-in-scale orders {cite:p}`MiFIDII2014`.

### Systematic Internalizers

A Systematic Internalizer (SI) is an investment firm that executes client orders against its own capital rather than routing them to an exchange, MTF, or OTF. Unlike the venues above, an SI has no central order book open to multiple participants — it quotes bilaterally to its own clients.

SIs traditionally handled smaller or less liquid trades, where a dealer's own capital could offer tighter pricing than an external venue. Over the last decade, the *new liquidity providers* introduced earlier in this chapter — non-bank, technology-driven firms such as Citadel Securities and Virtu Financial, most with roots in high-frequency trading — have become the dominant SIs in equities. Their main business as an SI is internalizing the retail order flow routed by brokers such as Robinhood: retail orders are relatively uninformed, so they can be matched internally at a saving in fees and spread that is partly passed back to the broker. This arrangement, known as **payment for order flow (PFOF)**, lets brokers offer commission-free trading to retail clients, at the cost of routing that order flow away from lit venues — a structure that has drawn regulatory scrutiny over potential conflicts of interest, which we return to at the end of this chapter.

## Market Structure by Asset Class

The three structures and five venue types described above combine differently across asset classes, largely as a function of how standardized the instruments are and how each market's history shaped the balance between dealers and exchanges. The table below summarizes the main pattern; the discussion that follows highlights only what is specific to each asset class, since the regulatory drivers — Reg NMS, MiFID II, Dodd-Frank, EMIR — already introduced apply across all of them.

| Asset class | Dominant venue type | OTC vs. exchange-traded | Non-bank liquidity providers |
|---|---|---|---|
| Equity | Exchange / CLOB, with heavy retail internalization via SIs | Predominantly exchange-traded | Citadel Securities, Virtu Financial |
| Fixed income | Inter-dealer CLOB for government bonds; dealer-to-client RfQ for corporate bonds | Predominantly OTC | Active mainly in the most liquid government bonds |
| FX | Single- and multi-dealer platforms, ECNs | Entirely OTC | Citadel Securities, XTX Markets |
| Derivatives | Exchange/CLOB for standardized futures and options; OTC for swaps | Split by standardization | Citadel Securities, Virtu Financial |
| Crypto | Centralized exchanges (CEXs); decentralized exchanges (DEXs) | No regulated-exchange equivalent | Native crypto market makers |

**Equity** markets are the closest of any asset class to a fully all-to-all structure: the exchanges described above compete with ECNs (Instinet, and BATS/CBOE) and dark pools (Liquidnet), all operating under Reg NMS best-execution rules in the US and MiFID II's transparency and dark-pool volume caps in Europe {cite:p}`SEC2005RegNMS` {cite:p}`MiFIDII2014`. What most distinguishes equities today is the scale of retail internalization: platforms like Robinhood route most retail orders to SIs such as Citadel Securities under the PFOF arrangement introduced above, rather than to a lit exchange — a structure that has driven much of the recent regulatory debate over execution quality, which we return to at the end of this chapter.

**Fixed income** remains the most dealer-centric of the major asset classes, since a dealer's own balance sheet is often needed to take the other side of a trade in a less liquid bond {cite:p}`Fabozzi2007Handbook`. Government bonds trade mostly on inter-dealer CLOBs (BrokerTec, MTS, Eurex Repo); corporate bonds trade mostly dealer-to-client via RfQ on platforms like Tradeweb and MarketAxess. According to a Bank for International Settlements study, electronic trading captured roughly 60-70% of government bond activity but only 30-40% of corporate bond activity by the mid-2010s {cite:p}`BIS2016ElectronicTradingFixedIncome` — a gap that reflects exactly this liquidity difference. MarketAxess's *Open Trading* model, which lets any participant act as a liquidity provider rather than only traditional dealers, is a notable move toward the all-to-all end of the spectrum.

**FX** is the largest and most liquid market in the world, and the only major asset class with no central exchange anywhere: trading is entirely OTC, across single-dealer platforms (Citi Velocity, Deutsche Bank Autobahn), multi-dealer platforms (Refinitiv FXall, 360T), and ECNs (EBS, CBOE FX). BIS studies of FX market structure document a steady rise of algorithmic and electronic trading in this OTC setting, alongside the growing presence of non-bank liquidity providers such as Citadel Securities and XTX Markets {cite:p}`BIS2011`. This structure enables 24-hour trading across time zones, but also means FX liquidity is less uniform than in equities: retail traders face wider spreads, and the practice of *last look* — where a liquidity provider can reject a trade even after quoting a price — remains a live source of regulatory concern about execution quality.

**Derivatives** split cleanly along the standardization of the contract. Futures and options trade on exchanges (CME, Eurex, formerly LIFFE) using the same CLOB mechanism as equities. Swaps and other bespoke contracts trade OTC — platforms like Tradeweb and CME SwapStream have added electronic trading and central clearing to what was historically a voice-negotiated market — increasingly through Swap Execution Facilities mandated by Dodd-Frank, with instruments such as credit default swaps (CDS) increasingly cleared through central counterparties like ICE Clear Credit {cite:p}`DoddFrank2010`. This split is itself a direct consequence of post-2008 regulation, which pushed standardizable OTC contracts toward exchange-like execution and central clearing specifically to reduce the counterparty risk that materialized in that crisis.

**Crypto** does not map cleanly onto the exchange/IDB/ECN/dark-pool/SI taxonomy above, since it grew up outside traditional financial regulation. Centralized exchanges (Binance, Coinbase, Kraken) function much like equity exchanges — order books, custody of client assets — but without the regulatory oversight, clearing infrastructure, or capital requirements a bank-run exchange would carry. Decentralized exchanges (Uniswap, SushiSwap) remove the intermediary altogether: smart contracts and automated market-making (AMM) pools set prices algorithmically from the ratio of assets deposited by liquidity providers, at the cost of lower liquidity and higher fees during network congestion. Beyond spot trading, DeFi protocols built on the same infrastructure extend to lending, borrowing, and yield farming, while OTC desks (Genesis Trading, Cumberland DRW) serve large institutional trades much as fixed-income dealer desks do. The entry of institutions such as BlackRock and Fidelity into custody and regulated trading venues is steadily narrowing the gap with traditional market structure — a gap that matters: the absence of the compliance infrastructure taken for granted elsewhere in this chapter is what let the FTX exchange misappropriate customer funds to prop up its affiliated trading firm, Alameda Research, before its 2022 collapse {cite:p}`SEC2022FTXCharges`. The EU's MiCA regulation, discussed next, is the first comprehensive attempt at closing that gap {cite:p}`MiCA2023`.

## Regulation of Financial Markets

Financial market regulation governs the activities of trading venues, intermediaries, and participants, shaping how capital flows and risks are managed. It maps directly onto the risks introduced earlier in this chapter — liquidity risk, credit risk, and, at market scale, systemic risk — and evolves constantly in response to technological change, market innovation, and crises that expose vulnerabilities in the system. Its main objectives are:

* **Market integrity**: preventing fraud, manipulation, and insider trading.
* **Investor protection**: rules on disclosure, risk assessment, and the fiduciary duties of intermediaries.
* **Transparency**: pre- and post-trade reporting requirements — the mechanism behind most of the venue-level rules discussed above.
* **Systemic risk mitigation**: capital adequacy, margin requirements, and stress testing.
* **Competition**: enabling new entrants and alternative venues while curbing anti-competitive behavior.

### Key Regulatory Frameworks

In the **United States**, two frameworks dominate. **Regulation NMS (Reg NMS)**, introduced in 2005, governs equities and requires best execution and fair access across venues — the direct regulatory source of the market fragmentation discussed throughout this chapter {cite:p}`SEC2005RegNMS`. The **Dodd-Frank Wall Street Reform and Consumer Protection Act**, enacted after the 2008 financial crisis, targets derivatives markets: it introduced Swap Execution Facilities and mandatory central clearing, and imposed stricter oversight on complex financial products {cite:p}`DoddFrank2010`.

In **Europe**, **MiFID II** provides the comprehensive cross-asset framework referenced throughout this chapter — pre- and post-trade transparency, the RM/MTF/OTF/SI taxonomy, and dark pool volume caps {cite:p}`MiFIDII2014`. The **European Market Infrastructure Regulation (EMIR)** complements it specifically for derivatives, mandating central clearing for standardized contracts and enhanced reporting {cite:p}`EMIR2012`.

At a **global** level, the **Basel III** framework sets international banking capital, leverage, and liquidity standards {cite:p}`BCBS2010BaselIII`, and the **International Organization of Securities Commissions (IOSCO)** sets non-binding global benchmarks for securities regulation to support cross-border coordination {cite:p}`IOSCO2017Objectives`.

### Challenges and Recent Developments

Regulating financial markets is a moving target: technological change — most visibly high-frequency trading and cryptocurrencies — tends to outpace the frameworks meant to govern it, and cross-border trading creates room for regulatory arbitrage between jurisdictions with different rules.

Three developments stand out as active areas of regulatory attention:

* **Algorithmic trading**. Electronic and algorithmic trading were among the first technological shifts to prompt dedicated regulation. MiFID II addresses it directly through RTS 6, which imposes organizational and risk-control requirements on firms trading via algorithms, with specific provisions for high-frequency trading {cite:p}`MiFIDII2014`; {ref}`algorithmic_trading` develops this regulatory framework in full, alongside the technology it governs. Cryptocurrencies and decentralized finance have prompted a parallel, more recent regulatory effort, most developed in the EU's MiCA {cite:p}`MiCA2023`, with the United States still building a comprehensive framework. The use of large language models and agentic frameworks in trading is likely to be the next area regulators turn to.
* **ESG disclosure**. As sustainable investing has grown, regulators have moved to mandate ESG disclosures and curb greenwashing, led in Europe by the Sustainable Finance Disclosure Regulation (SFDR) {cite:p}`SFDR2019`.
* **Data and cybersecurity**. Reliance on digital platforms and cloud infrastructure has pulled financial regulation into the same orbit as data protection law, including the EU's General Data Protection Regulation (GDPR) {cite:p}`GDPR2016`.

Retail investor protection cuts across all three: the growth of retail trading on platforms like Robinhood has prompted new rules on execution quality and on practices such as PFOF, introduced earlier in this chapter.

## Summary

This chapter opened with a simple problem: savers want liquidity, borrowers want long-term funding, and someone has to reconcile the two. Banks solve it by holding both sides of the mismatch on their own balance sheet, at the cost of bearing liquidity and credit risk themselves. Financial markets solve it differently, by making the claim on those future cash flows tradable — which turns the problem from bearing risk into finding a counterparty and agreeing on a price.

Everything else in this chapter follows from that shift. The asset classes are the different forms that tradable claim can take. The venues — exchanges, inter-dealer broker networks, ECNs, dark pools, systematic internalizers — are the mechanisms that solve the counterparty-finding and pricing problem in practice, combined differently depending on how standardized each asset class is. And regulation exists to keep that price-discovery process fair and the system stable as trading has moved from dealer floors to algorithms.

The next two chapters build directly on this foundation. {ref}`intro_financial_instruments` works out the mechanics and valuation of each instrument type introduced here, and {ref}`market_microstructure` returns to the trading mechanisms — quote-driven, order-driven, and hybrid — that underlie the venues described in this chapter's discussion of market structure.


