(intro_financial_instruments)=
# Mechanics of Financial Instruments

## Introduction

As discussed in the previous chapter, a financial instrument is an exchangeable contract that specifies the conditions for the transfer of funds between two parties — including the amounts exchanged, the timing, and any clauses or rights involved. Given the diversity of objectives among issuers and investors, it is not surprising that financial instruments have become a major field of innovation, constantly adapting to new funding, investment, and risk management needs.

Classical financial instruments such as stocks and bonds form the foundation of modern markets. They articulate the basic economic functions of financing corporations and governments — the former in exchange for ownership and a share of profits (whether retained or paid as dividends), and the latter through fixed periodic payments and the promise of capital repayment at maturity. These are often referred to as cash instruments, since they involve direct investment or lending relationships and represent claims on real assets or income streams.

Beyond equities and bonds, the cash universe includes money market instruments — such as repos, treasury bills, and commercial paper — which facilitate short-term financing and liquidity management. Closely related are foreign exchange (FX) instruments, which enable the exchange of funds across currencies. FX spot transactions are also cash instruments, involving the immediate delivery of one currency against another, while FX forwards and swaps allow participants to manage funding or hedging needs across different currencies and maturities. Together, these cash markets provide the foundation for pricing, liquidity, and risk transfer across the global financial system.

Financial innovation has, however, gone far beyond these classical instruments. Derivative markets extend the set of available contracts by allowing exposures to be tailored — separating, transferring, or amplifying specific sources of risk. Instruments such as futures, swaps, and options are now central to global markets, used both for risk management and speculation. Their design allows participants to trade not the assets themselves, but the conditions under which value changes — such as interest rates, credit spreads, or exchange rates.

Finally, a broad range of hybrid and structured products combine features of both cash and derivative instruments to meet more specialized investment or funding objectives. Products such as structured notes, credit-linked instruments, and securitizations illustrate how financial engineering can reshape risk and return profiles to suit diverse investor preferences.

In what follows, we organize financial instruments into three broad families:

* Cash instruments, encompassing equities, bonds, money-market, and foreign exchange products. These instruments have typically liquid prices and conform the main so-called *market risk factor*, i.e. the fundamental sources of systematic risk arising from movements in observable market variables such as equity prices, interest rates, yield curves, credit spreads, and exchange rates.

* Derivative instruments, including forwards, swaps, and options. These instruments derive their value from underlying cash instruments or market variables and are primarily used to transfer, hedge, or leverage market risk factors, often introducing nonlinear and path-dependent payoffs

* Hybrid and structured products, which combine multiple risk exposures and payoff structures. These instruments embed derivatives within cash products to tailor risk–return profiles, resulting in complex sensitivities to several market risk factors and, in many cases, reduced transparency and liquidity

This structure reflects both the economic function of instruments and the way modern markets are organized in practice.

## Cash instruments and the main market risk factors

Cash instruments represent direct claims on an asset, income stream, or borrower. They are the foundation of capital markets, facilitating investment, funding, and liquidity management. Their valuation depends primarily on the expected cash flows, credit risk, and time value of money.

As mentioned above, from a risk perspective, cash instruments can be used to define market risk factors, which are latent factors that can be used to largely explain their observable co-movements in prices. In equities, while individual stocks exhibit significant idiosyncratic risk, the dominant systematic risk factor is captured at the portfolio level through broad market indexes, which represent aggregate exposure to economic growth, risk appetite, and discount-rate dynamics. Fixed-income instruments are primarily driven by the dynamics of interest-rate and credit spreads curves; money-market instruments by short-term funding rates and liquidity conditions; and foreign exchange instruments by relative interest rates, macroeconomic fundamentals, and cross-border capital flows.

### Equities

Equities are financial instruments through which investors provide capital to a company in exchange for participation in its economic performance and governance. Unlike debt, equities do not promise predefined cash flows. Instead, the payoff to equity holders is directly linked to the evolution of the firm’s assets, profitability, and long-term prospects. This feature makes equity the primary risk-bearing instrument in a company’s capital structure and the main channel through which investors gain exposure to corporate growth.

From a balance sheet perspective, equity represents shareholders’ capital and is defined residually through the fundamental accounting identity

$$\text{Assets} = \text{Liabilities} + \text{Equity}$$

This identity must always hold. Consequently, any change in the value of a firm’s assets or liabilities is mechanically reflected in equity. In practice, the nominal value of debt is largely fixed by contract, so short-term fluctuations in firm value are absorbed almost entirely by equity. When asset values decline, equity is reduced first; only after equity is exhausted do losses begin to impair debt holders. This asymmetric position explains both the higher volatility of equity prices and the shareholders’ claim on the firm’s upside.

Companies raise equity by issuing shares, either privately or through public offerings in organized markets. In a public issuance, investors purchase shares in a competitive process, providing cash capital to the firm. A defining feature of equity markets is the existence of a liquid secondary market, where shares can be freely traded among investors. Although trading in the secondary market does not directly affect the firm’s cash position, it plays a crucial economic role: liquidity increases investors’ willingness to supply capital in the primary market and generates a continuously updated market valuation of the firm.

An equity share typically grants three fundamental rights. First, shareholders participate in the firm’s profits through dividends, when and if these are distributed. Second, they hold a residual claim on the firm’s assets in the event of liquidation, after all creditors have been paid. Third, equity often confers control rights, usually exercised through voting on corporate governance matters. Importantly, equity imposes no obligation on the firm to repay the invested capital or to make regular payments, sharply distinguishing it from debt financing.

This absence of contractual repayment makes equity a flexible and, from the firm’s perspective, often cheaper source of financing. Dividends are paid only when profits allow, whereas debt requires fixed interest payments regardless of business conditions. As a result, adverse shocks to firm value tend to be reflected first and most strongly in equity prices, while debt valuations remain relatively stable until default risk becomes material.

#### Valuation of Equity

Equity valuation can be approached using several complementary frameworks, each emphasizing a different economic dimension of the equity claim.

##### Accounting (book value) approach #####
 
From the balance sheet, total equity is defined as the difference between assets and liabilities. On a per-share basis, book value is given by

$$\text{Book Value per Share} = \frac{\text{Assets} - \text{Liabilities}}{\text{Number of Shares Outstanding}}$$

Book value provides an accounting anchor for equity valuation, but it often differs substantially from market prices. This divergence reflects conservative accounting rules, historical cost conventions, and the limited recognition of economically important assets on the balance sheet. Intangible assets such as intellectual property, proprietary technology, data, organizational capital, and workforce skills are typically expensed rather than capitalized, despite being central to value creation in many modern firms. As a result, market prices necessarily incorporate expectations about future assets and liabilities that are only imperfectly captured by accounting statements.

##### Market valuation #####

In traded markets, equity is valued through its share price. The market value of equity, or market capitalization, is defined as

$$\text{Market Capitalization} = P \times N $$

where $P$ denotes the share price and $N$ the number of outstanding shares. Market prices aggregate investors’ expectations about future profitability, risk, growth, and the evolution of both tangible and intangible assets, making equity valuation inherently forward-looking and partially speculative. Persistent deviations between market value and book value are therefore not anomalies per se, but reflections of beliefs about future economic outcomes.

##### Discounted dividend approach ##### 

Conceptually, a share can be viewed as a claim on an uncertain stream of future dividends. Under this perspective, and using the ideas of fair value that will be thoroughly discussed in chapter {ref}`fair_price_estimation`, a fundamental model for the price of a stock satisfies

$$P_t = \mathbb{E}_t\left[ \sum_{k=1}^{\infty} \frac{d_{t+k}}{(1+r)^k} \right]$$

where $d_{t+k}$ denotes dividends paid in the future, which are brought into present value using discount factors at a rate $r$. This rate cannot, in general, be identified with the risk-free rate if the price is to reflect the risk borne by investors. Instead, $r$ should be interpreted as a risk-adjusted discount rate that compensates investors for both the time value of money and the uncertainty associated with future dividends.

The discounted dividend framework has been subject to important critiques, though. Shiller’s volatility argument {cite:p}`Shiller1981` considers the implication of the present-value relation under rational expectations. Let

$$P_t^* = \sum_{k=1}^{\infty} \frac{d_{t+k}}{(1+r)^k}$$

denote the ex post realized present value of future dividends. Under rational expectations, the observed price satisfies $P_t = \mathbb{E}_t[P_t^*]$. A basic variance inequality then implies

$$\operatorname{Var}(P_t) \leq \operatorname{Var}(P_t^*).$$

Empirically, however, stock prices exhibit substantially greater volatility than the realized discounted value of dividends, violating this inequality. This excess volatility indicates that a literal, constant-discount-rate rational expectations dividend discount model cannot fully account for observed equity price dynamics. Possible resolutions include time-varying discount rates, changing risk premia, or deviations from fully rational expectations.

#### Risk Factors and Expected Returns

While valuation frameworks describe what equity prices represent, asset pricing models focus on why equities earn the returns they do. At the portfolio level, expected equity returns are primarily compensation for exposure to systematic risk factors rather than idiosyncratic firm-level uncertainty. The idea underlying this theoretical framework is that idiosyncratic risk can be removed by providing sufficient diversification to a portfolio, but systematic risks can not. 

The Capital Asset Pricing Model (CAPM) expresses the expected excess return on an asset as proportional to its covariance with the market portfolio:

$$\mathbb{E}[R_i] - R_f = \beta_i\,\big(\mathbb{E}[R_m] - R_f\big), \quad \beta_i = \frac{\operatorname{Cov}(R_i, R_m)}{\operatorname{Var}(R_m)}$$

where $R_f$ is the risk-free rate and $R_m$ the market return. In this framework, equity risk is summarized by market beta, and only market-wide risk is priced.

Empirical evidence suggests that additional systematic factors help explain cross-sectional differences in equity returns. The Fama–French three-factor model extends CAPM by including size and value factors:

$$R_i - R_f = \alpha_i + \beta_{m,i}(R_m - R_f) + \beta_{s,i}\,\text{SMB} + \beta_{v,i}\,\text{HML} + \varepsilon_i$$

where SMB (small minus big) captures size-related risk and HML (high minus low) captures capitalization-related risk. The Carhart four-factor model further augments this specification with a momentum factor (MOM):

$$R_i - R_f = \alpha_i + \beta_{m,i}(R_m - R_f) + \beta_{s,i}\,\text{SMB} + \beta_{v,i}\,\text{HML} + \beta_{mom,i}\,\text{MOM} + \varepsilon_i$$

In these models, expected equity returns arise from exposure to multiple sources of systematic risk, each associated with a risk premium. Equity pricing thus reflects not only expectations about future cash flows, but also how those cash flows co-vary with broader economic conditions, completing the link between valuation, risk, and returns.

### Money Market Instruments

Money market instruments are short-term financial instruments used to manage liquidity, fund short-term obligations, and transmit monetary policy through the financial system. They are characterized by short maturities, typically ranging from overnight to one year, high credit quality, and low price volatility under normal market conditions. Unlike equities, money market instruments are not designed to provide exposure to long-term growth, but to preserve capital, provide liquidity, and facilitate the efficient functioning of payment and funding markets.

From a balance sheet perspective, money market instruments primarily arise from the short-term financing needs of governments, banks, and corporations. For issuers, they represent short-term liabilities used to bridge timing mismatches between cash inflows and outflows. For investors, they appear as near-cash assets—claims with well-defined nominal values and short horizons. Because maturities are short and contractual cash flows are fixed or highly predictable, valuation uncertainty is typically limited relative to longer-dated fixed income or equity instruments.

Money market instruments play a central role in the architecture of modern financial systems. They underpin interbank lending, collateralized funding, treasury cash management, and the settlement of securities transactions. Instruments such as Treasury bills, commercial paper, certificates of deposit, and repurchase agreements form an interconnected ecosystem in which liquidity is continuously redistributed among market participants. Disruptions in these markets therefore tend to have immediate and systemic consequences, as illustrated by repeated episodes of stress in interbank and repo markets.

#### Risk Characteristics

Although money market instruments are often perceived as low-risk, they are not risk-free. Their short maturity significantly reduces interest rate risk, but other sources of risk remain relevant. Credit risk arises from the possibility that the issuer may fail to repay at maturity, even over short horizons. Liquidity risk reflects the potential inability to sell or roll over positions without price concessions, particularly during periods of market stress. In collateralized instruments, such as repos, valuation and haircut risk play an additional role, as changes in collateral values can amplify funding pressures.

From a portfolio perspective, money market instruments are typically viewed as low-volatility assets with minimal exposure to long-term systematic risk factors. However, they are highly sensitive to funding conditions and confidence effects. What appears as idiosyncratic credit or liquidity risk at the instrument level can rapidly become systemic when many institutions attempt to secure short-term funding simultaneously.

#### Link to Monetary Policy

Money market instruments are the primary channel through which central banks implement and transmit monetary policy. Policy rates are operationally targeted in overnight or very short-term money markets, and central bank actions directly affect the pricing and availability of short-term funding. Open market operations, standing facilities, and asset purchase programs operate by injecting or absorbing reserves, thereby influencing money market rates and spreads.

Because of their short maturity, yields on money market instruments closely track policy rates and expectations of near-term monetary policy. Changes in central bank target rates, corridor systems, or liquidity provision frameworks are rapidly reflected in money market prices. As a result, money markets provide a real-time signal of monetary conditions and play a crucial role in anchoring the short end of the yield curve.

More broadly, conditions in money markets influence the transmission of monetary policy to the rest of the financial system. Disruptions in short-term funding can impair banks’ ability to extend credit, weaken the pass-through of policy rate changes, and force central banks to intervene as lenders of last resort. For this reason, the stability and smooth functioning of money markets are not only a technical concern, but a core objective of modern central banking.

#### Reference Rates 

Modern financial markets rely on reference interest rates—benchmarks used to determine floating-rate payments in loans, bonds, and derivatives. These rates serve as the foundation for trillions of dollars of financial contracts, ensuring a consistent and transparent mechanism for pricing and settlement. Monetary markets play a key role for the determination of reference rates, typically linked to instruments issued in these markets. 

Probably the most famous reference rate is the London Interbank Offered Rate (LIBOR), which became the dominant global benchmark during the 1980s, although its roots date back to the late 1960s. The first recorded use of a LIBOR-like rate appeared in 1969, when a group of London-based banks agreed to price a syndicated loan to the Shah of Iran at a margin over the rate at which they could borrow short-term funds in the interbank market. This convention proved practical for cross-border lending, allowing banks to align loan pricing with their own funding costs. As syndicated lending expanded in the 1970s and derivatives markets emerged in the 1980s, LIBOR was formalized by the British Bankers’ Association (BBA) as a standard daily benchmark, calculated as the average rate at which major banks believed they could borrow from one another on an unsecured basis.

However, the credibility of LIBOR was deeply undermined during the LIBOR manipulation scandal uncovered between 2011 and 2012. Investigations revealed that several panel banks had deliberately altered their submissions, either to profit from derivative positions or to disguise funding stress during the global financial crisis. The scandal exposed structural weaknesses: submissions were often based on expert judgment rather than actual transactions, making the benchmark vulnerable to manipulation. Regulatory responses included substantial fines, criminal prosecutions, and the establishment of new oversight frameworks for benchmark administration. Yet, the damage to trust was profound and accelerated global efforts to reform reference rate frameworks.

In the aftermath, regulators and market participants collaborated to design risk-free rates (RFRs) rooted in observable market transactions. These new benchmarks aim to eliminate reliance on subjective quotes and to reflect nearly risk-free overnight funding costs. Examples include:
* the Secured Overnight Financing Rate (SOFR) in the United States
* the Euro Short-Term Rate (€STR) in the euro area
* SONIA in the United Kingdom. 

Unlike LIBOR, which was unsecured and term-based, these rates are overnight and transaction-based, typically derived from repo or wholesale funding markets. Over time, derivatives markets have developed conventions for compounded-in-arrears calculations to build synthetic term structures compatible with existing financial products.

The transition from LIBOR to alternative rates has relevant contractual implications. Because LIBOR was embedded in an enormous range of financial instruments—from corporate loans to floating-rate notes and interest-rate swaps—its cessation required robust fallback provisions. Industry bodies such as ISDA introduced standardized fallback methodologies and spread adjustments to account for the credit and term premia embedded in LIBOR. Market participants had to amend legacy contracts, update systems, and reprice instruments to maintain consistency and avoid legal uncertainty.

#### Main monetary market instruments 


##### Treasury Bills


##### Commercial Paper


##### Certificates of Deposit


##### Repurchase Agreements (Repos)

Repurchase agreements, or repos, are among the most important instruments in modern money markets. A repo is a short-term secured loan: one party sells a security—typically a government bond—with the commitment to repurchase it at a later date and a slightly higher price. The difference between the sale and repurchase price reflects the repo rate, analogous to an interest rate on a collateralized borrowing. From the counterparty’s point of view, the transaction is a reverse repo, meaning it lends cash against the security as collateral.

Repos are fundamental to liquidity management and collateral circulation. They enable financial institutions to fund positions efficiently, manage short-term liquidity, and facilitate price discovery in fixed income markets. Central banks also rely on repos as a primary instrument of monetary policy, using them to inject or withdraw liquidity and to influence short-term interest rates. The global repo market is vast: outstanding balances are estimated in the tens of trillions of dollars, with the U.S. segment alone exceeding $5 trillion in daily transactions {cite:p}`OFR2023repo`.

Mechanically, two key parameters define the economics of a repo: the repo rate and the haircut—the percentage discount applied to the market value of the collateral. A higher haircut protects the lender against a fall in collateral value but increases the borrower’s funding cost. Haircuts vary with the perceived credit quality and liquidity of the collateral: Treasury securities typically carry haircuts close to zero, while corporate bonds or structured products may require 5–20%. In stressed conditions, haircuts often rise sharply, forcing deleveraging and amplifying market instability, as seen during the 2008 financial crisis.

For example, consider a repo in which a bank borrows $\$98$ million in cash for one week and pledges $\$100$ million in Treasury bonds as collateral. The haircut is therefore 2%. If the agreed repo rate is 3% per annum, the repurchase price after seven days will be:

$$98,000,000×(1+0.03×\frac{7}{360})≈98,057,166\$ $$

At maturity, the bank repays $\$98.06$ million and receives back its $\$100$ million in bonds. For the cash lender, the repo rate represents the secured yield on the transaction, while for the borrower, it represents the funding cost of holding the securities.

Repos are also integral to the market-making business. Suppose a dealer sells a bond to an asset manager such as Amundi, but does not hold the bond in inventory. The dealer can borrow the bond in the repo market, for instance from another asset manager like BlackRock, who lends it against cash collateral. The dealer delivers the bond to the client and must then either wait for another client to take the opposite position, renew the repo agreement upon maturity, or buy the bond in the interbank market to close the position. This continuous use of repos allows dealers to provide liquidity and make markets without holding large inventories of bonds.

Repos also underpin short selling, as they provide the mechanism by which short sellers borrow securities to sell them in anticipation of price declines. However, short positions carry significant risk if prices rise. Public data on open short positions—such as the short‐interest reports published by FINRA, NYSE, and Nasdaq—allow regulators and market participants to monitor short activity and its potential influence on price pressure and funding conditions. For example, the GameStop short squeeze in early 2021 {cite:p}`SEC2021gamestop` demonstrated how short sellers can face extreme pressure when prices move unexpectedly, forcing them to cover positions at large losses. Earlier examples, such as those portrayed in The Big Short {cite:p}`Lewis2010bigshort`, show that even when short sellers are correct in their analysis, they can face severe liquidity and timing risks.

### Fixed Income 

Fixed income instruments are debt securities that promise a predefined set of cash flows over time, either in fixed or variable form. By purchasing a fixed income instrument, investors lend capital to an issuer in exchange for contractual payments and the repayment of principal at maturity. Unlike equity, which represents a residual claim on a firm’s assets, fixed income securities confer senior, legally binding claims. 

Issuers of fixed income instruments span the full spectrum of the economy. **Sovereign issuers** finance fiscal activity and provide benchmark risk-free curves. **Corporate issuers** use bonds to fund investment and manage leverage. **Municipal issuers** finance regional and local infrastructure, while **supranational institutions** issue debt to support international development and policy objectives. 

Across all cases, the dominant fixed income instrument is the **bond**, characterized by periodic coupon payments and a final repayment of principal at a specified maturity. The presence of a maturity date anchors valuation in a way that sharply contrasts with equities, whose cash flows are discretionary and potentially infinite.

#### Valuation of fixed income instruments

As we will discuss in chapter {ref}`fair_price_estimation`,  The theoretical foundation of fixed income valuation is the **time value of money**.

This logic extends naturally to bonds, which deliver multiple future cash flows. For a bond with maturity $T$, coupon payments $C_t$, and face value $N$, the price $P$ is given by the sum of discounted promised payments:

$$P = \sum_{t=1}^{T} \frac{C_t}{(1+r_t)^t} + \frac{N}{(1+r_T)^T}$$

In practice, bonds traded in the market have observable prices that do not necessarily match with these theoretical prices, since there are additional risks and liquidity constraints for which investors typically demand an extra *yield* in order to invest in these instruments as alternatives to risk-free deposits. We define the **yield to maturity**  as the constant rate $y$ that equates the discounted value of promised cash flows to the observed market price:

$$P = \sum_{t=1}^{T} \frac{C_t}{(1+y)^t} + \frac{N}{(1+y)^T}$$

The yield is therefore an implied quantity rather than a fundamental primitive: it is the discount rate that reconciles price and cash flows and allows bonds with different coupons and maturities to be compared on a common basis. If we compute yields for a set of bonds from the same issuer with different maturities, the sorted collection of yields is called the *yield curve*.

#### Fixed income risk factors

Risk in fixed income markets is commonly organized around two broad dimensions. The first is **interest rate risk**, driven by movements in the level and shape of the yield curve for relatively risk-free issuers, typically sovereign bonds issued by governments with solid finances like the USA, Germany or Japan, or supranational entities like the European Union. Alternatively, interest rate risk factors can also be inferred from short-term monetary instruments and interest rate derivatives like standard interest rate swaps (IRS).  The collection of inferred rates across maturities constitutes the **term structure of interest rates**. Changes in this term structure are typically highly correlated and can be mostly described in term of latent risk factors driving co-movements like parallel shifts, steepening, or flattening of the interest rate curve. Such risk factors are then linked to movements in prices government bond portfolios and other rates products. Notice that short-term rates movements are typically tied to monetary policy decisions, while longer-term rates embed expectations about future policy paths, inflation, and macroeconomic conditions.

The second major risk dimension is **credit risk**. Bonds issued by corporations, institutions or governments that are exposed to default risk trade at yields above those of comparable risk-free sovereign benchmarks. The difference between the yield on a risky bond and the yield on a benchmark bond of the same maturity is the **credit spread** $s$:

$$s = y_{\text{risky}} - y_{\text{risk-free}}$$

Credit spreads compensate investors for expected default losses, recovery uncertainty, liquidity risk, and risk premia. In sovereign markets, this differential is often referred to as a risk premium relative to a benchmark issuer; in corporate markets, it is the central pricing variable for credit as an asset class.

This distinction between rates risk and credit risk provides the organizing principle for fixed income markets. It also motivates the common separation between rates products and credit products in trading, portfolio management, and risk analysis. For a deeper introduction to this topic, a classical reading is {cite:p}`Fabozzi2007Handbook`.

#### Main fixed income instrument types


* Bonds with different coupon types: fixed, floating, zero-coupon.

* Price conventions: clean/dirty price.

* Risk factors from the term structured: pca, factor models

* Interest rate sensitivity: duration, convexity.

* Credit bond valuation: recovery rates, default risk. Anecdote recovery FTX


### Foreign Exchange (FX) 

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
