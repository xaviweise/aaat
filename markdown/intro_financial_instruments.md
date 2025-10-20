(intro_financial_instruments)=
# Mechanics of Financial Instruments

## Introduction

As discussed in the previous chapter, a financial instrument is an exchangeable contract that specifies the conditions for the transfer of funds between two parties — including the amounts exchanged, the timing, and any clauses or rights involved. Given the diversity of objectives among issuers and investors, it is not surprising that financial instruments have become a major field of innovation, constantly adapting to new funding, investment, and risk management needs.

Classical financial instruments such as stocks and bonds form the foundation of modern markets. They articulate the basic economic functions of financing corporations and governments — the former in exchange for ownership and a share of profits (whether retained or paid as dividends), and the latter through fixed periodic payments and the promise of capital repayment at maturity. These are often referred to as cash instruments, since they involve direct investment or lending relationships and represent claims on real assets or income streams.

Beyond equities and bonds, the cash universe includes money market instruments — such as repos, treasury bills, and commercial paper — which facilitate short-term financing and liquidity management. Closely related are foreign exchange (FX) instruments, which enable the exchange of funds across currencies. FX spot transactions are also cash instruments, involving the immediate delivery of one currency against another, while FX forwards and swaps allow participants to manage funding or hedging needs across different currencies and maturities. Together, these cash markets provide the foundation for pricing, liquidity, and risk transfer across the global financial system.

Financial innovation has, however, gone far beyond these classical instruments. Derivative markets extend the set of available contracts by allowing exposures to be tailored — separating, transferring, or amplifying specific sources of risk. Instruments such as futures, swaps, and options are now central to global markets, used both for risk management and speculation. Their design allows participants to trade not the assets themselves, but the conditions under which value changes — such as interest rates, credit spreads, or exchange rates.

Finally, a broad range of hybrid and structured products combine features of both cash and derivative instruments to meet more specialized investment or funding objectives. Products such as structured notes, credit-linked instruments, and securitizations illustrate how financial engineering can reshape risk and return profiles to suit diverse investor preferences.

In what follows, we organize financial instruments into three broad families:

* Cash instruments, encompassing equities, bonds, money-market, and foreign exchange products;

* Derivative instruments, including forwards, swaps, and options; and

* Hybrid and structured products, which combine multiple exposures and payoff structures.

This structure reflects both the economic function of instruments and the way modern markets are organized in practice.

## Cash Instruments

Cash instruments represent direct claims on an asset, income stream, or borrower. They are the foundation of capital markets, facilitating investment, funding, and liquidity management. Their valuation depends primarily on the expected cash flows, credit risk, and time value of money.

### Equities

* Definition and economic role: Ownership claims on a company’s assets and profits.

* Common vs. preferred stock.

* Dividends and reinvestment.

* Corporate actions (splits, rights issues, buybacks).

* Market conventions: indices, tick sizes, settlement.

* Valuation basics: dividend discount model, price–earnings ratio.

* Equity-linked products: ETFs, ADRs, convertibles (bridge to hybrids).

### Money Market Instruments

* Purpose: short-term funding and liquidity management.

* Key instruments:

    * Treasury bills

    * Commercial paper

    * Certificates of deposit

    * Repurchase agreements (repos and reverse repos)

* Repo mechanics: collateral, haircut, repo rate, rehypothecation.

* Role in monetary policy implementation.

* Yield conventions (discount rate, money market yield).

### Fixed Income 

* Definition: Debt instruments promising fixed or variable payments.

* Issuers: sovereign, corporate, municipal, supranational.

* Coupon types: fixed, floating, zero-coupon.

* Yields and pricing: present value, yield-to-maturity, clean/dirty price.

* Interest rate sensitivity: duration, convexity.

* Credit risk and ratings.

* Benchmark yield curves.

* Secondary market trading and repo link.


### Foreign Exchange (FX) Instruments

The foreign exchange (FX) market enables the transfer of funds and the management of exposures between currencies. It is the mechanism through which international trade, investment, and financing are denominated, settled, and hedged. Participants include corporations managing cross-border payments, investors reallocating portfolios internationally, banks optimizing liquidity, and central banks implementing monetary policy or intervention.

FX instruments therefore serve two fundamental purposes:

1. **Transaction and funding needs:** facilitating payments and transfers between currencies.  
2. **Risk management:** hedging the exposure that arises when assets, liabilities, or revenues are denominated in foreign currencies.

The FX market operates continuously, 24 hours a day, across major financial centers, and is the largest and most liquid market in the world.

#### FX Spot Transactions

An FX spot transaction is the most basic form of foreign exchange. It represents an agreement to exchange two currencies for near-immediate delivery — conventionally T+2 business days after the trade date (T+1 for certain pairs like USD/CAD).

Spot prices are quoted as base/quote currency pairs, for example:

> EUR/USD = 1.0750

which means that one euro (the base currency) costs 1.0750 U.S. dollars (the quote currency).

Prices are typically quoted with *bid–ask spreads*, reflecting market liquidity and transaction costs:

> EUR/USD 1.0749–1.0751

indicating the dealer is willing to buy euros at 1.0749 (bid) and sell them at 1.0751 (ask).

Spot FX serves as the reference price for a wide range of currency-linked instruments. While we will briefly describe forwards and swaps in this section, their mechanics and broader applications will be examined in more detail in the following chapter on derivatives. Spot FX also underpins cross-border settlement systems like CLS (Continuous Linked Settlement), which reduce counterparty risk by ensuring the simultaneous settlement of both legs of the transaction.

#### FX Forward Contracts

An FX forward is a contract to exchange two currencies at a future date and a predetermined rate. The forward rate is determined by *covered interest parity (CIP)*, which ensures the absence of arbitrage between spot and forward markets.

Formally, for currencies $A$ and $B$:

$$
F_{A/B} = S_{A/B} \times \frac{(1 + i_A T)}{(1 + i_B T)}
$$

where $S_{A/B}$ is the spot rate (price of one unit of A in units of B), $i_A$ and $i_B$ are the interest rates in each currency, and $T$ is the maturity in years.

Intuitively, the forward rate reflects the interest rate differential between the two currencies: the currency with the higher interest rate will typically trade at a forward discount, and the one with the lower rate at a forward premium.

FX forwards are extensively used by corporations and investors to hedge currency exposures associated with foreign-denominated assets, liabilities, or anticipated cash flows.

#### FX Swaps

An FX swap combines two FX transactions — a spot exchange of currencies and a simultaneous forward transaction that reverses the exchange at a later date.

It allows participants to borrow or lend one currency while using another as collateral, without taking directional exposure to the exchange rate. In practice, FX swaps function as short-term funding instruments and are widely used by banks, asset managers, and central banks for liquidity management across currencies.

The swap points (difference between forward and spot rates) are determined by the same interest rate differential that drives forward pricing.

#### Determinants of Spot FX Rates

While short-term FX movements can be driven by order flow, risk sentiment, or central bank interventions, medium- and long-term exchange rate trends are influenced by macroeconomic fundamentals. Some of the most relevant drivers include:

- **Real Interest Rate Differentials:**  
  Real interest rates (nominal rates adjusted for inflation) between two economies can significantly influence currency valuation. When one economy offers higher real yields, global investors may shift capital to take advantage of the better return, increasing demand for that currency and driving its spot FX price higher.

- **Local Stock Market Performance:**  
  Strong performance in a country’s stock market can attract foreign investment, as investors seek higher returns. To purchase local equities, they must first acquire the domestic currency, boosting its demand and potentially appreciating its spot value.

- **Trade Balance (Exports vs. Imports):**  
  The balance of trade between countries also impacts currency valuation. If a country exports more than it imports, foreign buyers must convert their currency into the exporter’s currency to pay for goods. Over time, sustained trade surpluses can increase demand for the exporter’s currency, appreciating its value. Conversely, persistent deficits may weaken it.


## Derivative Instruments

Derivatives are contracts whose value depends on the price or level of an underlying asset, rate, or index. They allow market participants to transfer, hedge, or create specific risk exposures. Their valuation rests on no-arbitrage principles, linking them to the prices of cash instruments.

### Forwards and Futures

Definition: agreements to buy/sell an asset at a future date and price.

Pricing intuition: cost-of-carry model; relationship to spot price.

Margining and daily settlement (for futures).

Examples: FX forwards, bond futures, equity index futures.

Uses: hedging, speculation, arbitrage.

### Swaps

Interest rate swaps (IRS): fixed-for-floating exchange, notionals, netting.

Pricing and valuation: discounting, forward rates, and par swap rates.

Cross-currency swaps: exchanging cash flows in different currencies.

Credit default swaps (CDS): protection leg, premium leg, credit events.

Applications: managing funding costs, transforming exposures.

Market conventions: day count, accrual, ISDA documentation.

### Options

Options are derivatives contracts that grant the holder the  the option (hence the name) to buy or sell (depending on the option) a given financial instrument (the underlying) at a price at time contingent to the clauses of the contract. The most simple option, the European option, pre-specifies a given time $T$, the expire, and price $K$, to exercise this option. But there are many other variations in the market. An option to buy a financial instrument is referred as a call option, and an option to sell is a put option. 

Let us consider european options of stocks. If the market price of the stock at the expiry is $S_T$, a call option will be exercised by a rational investor only if the price is higher than the strike $K$, making a profit of $S_T-K$, which in some cases is directly paid in cash, in others the actual stock is received, but of course it could be directly sold in the market at a favorable price. Therefore, the payoff of a call option can be written as:

$$C_T = (S_T-K)^+$$

where $(.)^+$ denotes the positive part of the argument. On the contrary, a put option will only be exercised if the market price is below the strike, hence the payoff is:

$$P_T = (K-S_T)^+$$

Options can be traded in regulated markets or be quoted by bank dealers. Since the investor that holds the option cannot lose money from it, such option does not come for free, and the question is how much is worth such option, which is called the premium of the option. At expiry, the price is naturally the payoff function. What at at time $t < T$ there is still  uncertainty about the price $S_T$ which will determine the final profit (if any), so the premium will be different. But how much? That is the subject of the theory of option pricing.


#### Basic strategies: long/short positions, spreads, combinations.

#### Valuation intuition: time value, volatility, and Greeks.

#### Implied volatility and surface.

#### Market conventions: OTC vs. exchange-traded, delta quoting.

### Other Derivative Types (optional)

* CDO tranches (intro).

* Commodity and volatility derivatives.

* Exotic options: barriers, Asians, digitals (brief mention).


## Hybrid and Structured Products

Hybrid and structured products combine features of multiple instruments to create customized payoff profiles. They often embed derivative components within a funding or investment vehicle, enabling issuers and investors to fine-tune exposure to market variables, credit risk, or volatility.

### Structured Notes and Deposits

Concept: debt instrument plus embedded option.

Examples: equity-linked notes, reverse convertibles, range accruals.

Payoff design: principal protection, participation rates, caps/floors.

Valuation and risks: credit of issuer, liquidity, complexity.

### Credit-Linked Instruments

Credit-linked notes (CLN).

Securitized credit exposures (ABS, MBS).

Tranching and credit enhancement mechanisms.

Relation to CDS markets.

### Securitization and Structured Finance

Economic rationale: transferring credit risk and freeing balance sheet capacity.

Structure: SPV, collateral pool, tranches, waterfalls.

Market evolution and crises context (e.g., 2008).

### Hybrid Securities

Convertible and exchangeable bonds.

Perpetual bonds and contingent convertibles (CoCos).

Preferred shares and hybrids between debt and equity.
