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

The chapter is organised as follows. We begin with **cash instruments** ({ref}`sec:ifi_cash`), covering equities ({ref}`sec:ifi_equities`), money market instruments ({ref}`sec:ifi_money_market`), fixed income ({ref}`sec:ifi_fixed_income`), and foreign exchange ({ref}`sec:ifi_fx`). For each family we discuss economic function, valuation principles, and the market risk factors that drive price dynamics. We then turn to **derivative instruments** ({ref}`sec:ifi_derivatives`): forwards and futures ({ref}`sec:ifi_forwards`), swaps ({ref}`sec:ifi_swaps`), and options ({ref}`sec:ifi_options`), developing the no-arbitrage pricing intuition and introducing key concepts such as the cost-of-carry model, the term structure of forward rates, and option Greeks. The chapter closes with **hybrid and structured products** ({ref}`sec:ifi_structured`), which combine features of cash and derivatives to create tailored payoff profiles.

(sec:ifi_cash)=
## Cash instruments and the main market risk factors

Cash instruments represent direct claims on an asset, income stream, or borrower. They are the foundation of capital markets, facilitating investment, funding, and liquidity management. Their valuation depends primarily on the expected cash flows, credit risk, and time value of money.

As mentioned above, from a risk perspective, cash instruments can be used to define market risk factors, which are latent factors that can be used to largely explain their observable co-movements in prices. In equities, while individual stocks exhibit significant idiosyncratic risk, the dominant systematic risk factor is captured at the portfolio level through broad market indexes, which represent aggregate exposure to economic growth, risk appetite, and discount-rate dynamics. Fixed-income instruments are primarily driven by the dynamics of interest-rate and credit spreads curves; money-market instruments by short-term funding rates and liquidity conditions; and foreign exchange instruments by relative interest rates, macroeconomic fundamentals, and cross-border capital flows.

(sec:ifi_equities)=
### Equities

Equities are financial instruments through which investors provide capital to a company in exchange for participation in its economic performance and governance. Unlike debt, equities do not promise predefined cash flows. Instead, the payoff to equity holders is directly linked to the evolution of the firm's assets, profitability, and long-term prospects. This feature makes equity the primary risk-bearing instrument in a company's capital structure and the main channel through which investors gain exposure to corporate growth.

From a balance sheet perspective, equity represents shareholders' capital and is defined residually through the fundamental accounting identity

$$\text{Assets} = \text{Liabilities} + \text{Equity}$$

This identity must always hold. Consequently, any change in the value of a firm's assets or liabilities is mechanically reflected in equity. In practice, the nominal value of debt is largely fixed by contract, so short-term fluctuations in firm value are absorbed almost entirely by equity. When asset values decline, equity is reduced first; only after equity is exhausted do losses begin to impair debt holders. This asymmetric position explains both the higher volatility of equity prices and the shareholders' claim on the firm's upside.

Companies raise equity by issuing shares, either privately or through public offerings in organized markets. In a public issuance, investors purchase shares in a competitive process, providing cash capital to the firm. A defining feature of equity markets is the existence of a liquid secondary market, where shares can be freely traded among investors. Although trading in the secondary market does not directly affect the firm's cash position, it plays a crucial economic role: liquidity increases investors' willingness to supply capital in the primary market and generates a continuously updated market valuation of the firm.

An equity share typically grants three fundamental rights. First, shareholders participate in the firm's profits through dividends, when and if these are distributed. Second, they hold a residual claim on the firm's assets in the event of liquidation, after all creditors have been paid. Third, equity often confers control rights, usually exercised through voting on corporate governance matters. Importantly, equity imposes no obligation on the firm to repay the invested capital or to make regular payments, sharply distinguishing it from debt financing.

This absence of contractual repayment makes equity a flexible and, from the firm's perspective, often cheaper source of financing. Dividends are paid only when profits allow, whereas debt requires fixed interest payments regardless of business conditions. As a result, adverse shocks to firm value tend to be reflected first and most strongly in equity prices, while debt valuations remain relatively stable until default risk becomes material.

#### Valuation of Equity

Equity valuation can be approached using several complementary frameworks, each emphasizing a different economic dimension of the equity claim.

##### Accounting (book value) approach #####
 
From the balance sheet, total equity is defined as the difference between assets and liabilities. On a per-share basis, book value is given by

$$\text{Book Value per Share} = \frac{\text{Assets} - \text{Liabilities}}{\text{Number of Shares Outstanding}}$$

Book value provides an accounting anchor for equity valuation, but it often differs substantially from market prices. This divergence reflects conservative accounting rules, historical cost conventions, and the limited recognition of economically important assets on the balance sheet. Intangible assets such as intellectual property, proprietary technology, data, organizational capital, and workforce skills are typically expensed rather than capitalized, despite being central to value creation in many modern firms. As a result, market prices necessarily incorporate expectations about future assets and liabilities that are only imperfectly captured by accounting statements.

##### Market valuation #####

In traded markets, equity is valued through its share price. The market value of equity, or market capitalization, is defined as

$$\text{Market Capitalization} = P \times N $$

where $P$ denotes the share price and $N$ the number of outstanding shares. Market prices aggregate investors' expectations about future profitability, risk, growth, and the evolution of both tangible and intangible assets, making equity valuation inherently forward-looking and partially speculative. Persistent deviations between market value and book value are therefore not anomalies per se, but reflections of beliefs about future economic outcomes.

##### Discounted dividend approach ##### 

Conceptually, a share can be viewed as a claim on an uncertain stream of future dividends. Under this perspective, and using the ideas of fair value that will be thoroughly discussed in chapter {ref}`fair_price_estimation`, a fundamental model for the price of a stock satisfies

$$P_t = \mathbb{E}_t\left[ \sum_{k=1}^{\infty} \frac{d_{t+k}}{(1+r)^k} \right]$$

where $d_{t+k}$ denotes dividends paid in the future, which are brought into present value using discount factors at a rate $r$. This rate cannot, in general, be identified with the risk-free rate if the price is to reflect the risk borne by investors. Instead, $r$ should be interpreted as a risk-adjusted discount rate that compensates investors for both the time value of money and the uncertainty associated with future dividends.

The discounted dividend framework has been subject to important critiques, though. Shiller's volatility argument {cite:p}`Shiller1981` considers the implication of the present-value relation under rational expectations. Let

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

(sec:ifi_money_market)=
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

More broadly, conditions in money markets influence the transmission of monetary policy to the rest of the financial system. Disruptions in short-term funding can impair banks' ability to extend credit, weaken the pass-through of policy rate changes, and force central banks to intervene as lenders of last resort. For this reason, the stability and smooth functioning of money markets are not only a technical concern, but a core objective of modern central banking.

#### Reference Rates 

Modern financial markets rely on reference interest rates—benchmarks used to determine floating-rate payments in loans, bonds, and derivatives. These rates serve as the foundation for trillions of dollars of financial contracts, ensuring a consistent and transparent mechanism for pricing and settlement. Monetary markets play a key role for the determination of reference rates, typically linked to instruments issued in these markets. 

Probably the most famous reference rate is the London Interbank Offered Rate (LIBOR), which became the dominant global benchmark during the 1980s, although its roots date back to the late 1960s. The first recorded use of a LIBOR-like rate appeared in 1969, when a group of London-based banks agreed to price a syndicated loan to the Shah of Iran at a margin over the rate at which they could borrow short-term funds in the interbank market. This convention proved practical for cross-border lending, allowing banks to align loan pricing with their own funding costs. As syndicated lending expanded in the 1970s and derivatives markets emerged in the 1980s, LIBOR was formalized by the British Bankers' Association (BBA) as a standard daily benchmark, calculated as the average rate at which major banks believed they could borrow from one another on an unsecured basis.

However, the credibility of LIBOR was deeply undermined during the LIBOR manipulation scandal uncovered between 2011 and 2012. Investigations revealed that several panel banks had deliberately altered their submissions, either to profit from derivative positions or to disguise funding stress during the global financial crisis. The scandal exposed structural weaknesses: submissions were often based on expert judgment rather than actual transactions, making the benchmark vulnerable to manipulation. Regulatory responses included substantial fines, criminal prosecutions, and the establishment of new oversight frameworks for benchmark administration. Yet, the damage to trust was profound and accelerated global efforts to reform reference rate frameworks.

In the aftermath, regulators and market participants collaborated to design risk-free rates (RFRs) rooted in observable market transactions. These new benchmarks aim to eliminate reliance on subjective quotes and to reflect nearly risk-free overnight funding costs. Examples include:
* the Secured Overnight Financing Rate (SOFR) in the United States
* the Euro Short-Term Rate (€STR) in the euro area
* SONIA in the United Kingdom. 

Unlike LIBOR, which was unsecured and term-based, these rates are overnight and transaction-based, typically derived from repo or wholesale funding markets. Over time, derivatives markets have developed conventions for compounded-in-arrears calculations to build synthetic term structures compatible with existing financial products.

The transition from LIBOR to alternative rates has relevant contractual implications. Because LIBOR was embedded in an enormous range of financial instruments—from corporate loans to floating-rate notes and interest-rate swaps—its cessation required robust fallback provisions. Industry bodies such as ISDA introduced standardized fallback methodologies and spread adjustments to account for the credit and term premia embedded in LIBOR. Market participants had to amend legacy contracts, update systems, and reprice instruments to maintain consistency and avoid legal uncertainty.

#### Main monetary market instruments 

##### Treasury Bills

Treasury bills (T-bills) are short-term debt obligations issued by sovereign governments, typically with maturities of one, three, six, or twelve months. They are the most liquid and creditworthy money market instruments, carrying the full faith and credit of the issuing government. As such, their yields serve as the practical benchmark for the risk-free rate at short maturities.

T-bills are issued at a discount to face value and redeemed at par; the investor's return is the difference between the purchase price and the face value. Pricing follows the discount convention:

$$P = N \left(1 - d \cdot \frac{T}{360}\right)$$

where $N$ is face value, $d$ is the discount rate, and $T$ is the number of days to maturity. The equivalent money-market yield, which makes T-bill returns comparable to interest-bearing instruments, is

$$y = \frac{N - P}{P} \cdot \frac{360}{T}$$

T-bill auctions are conducted regularly by treasury departments and are a primary mechanism for government cash management. In secondary markets, T-bills trade at extremely tight bid-ask spreads and serve as near-perfect substitutes for cash, making them the instrument of choice for collateral, reserve management, and short-term investment. The overnight and one-month T-bill yields are closely followed as indicators of monetary policy expectations and funding conditions.

##### Commercial Paper

Commercial paper (CP) is short-term, unsecured promissory notes issued by corporations, bank holding companies, and financial institutions to meet immediate funding needs. Maturities typically range from overnight to 270 days — the 270-day threshold is significant in the United States, as it exempts issuers from full SEC registration requirements, reducing issuance costs. In practice, the bulk of commercial paper outstanding has maturities of thirty days or less.

Like T-bills, CP is typically issued at a discount and redeemed at par. Pricing and yield conventions mirror those of T-bills, using the discount rate and a 360-day year. However, unlike T-bills, CP carries credit risk. Only issuers with strong credit ratings can access the CP market at competitive spreads; lower-rated issuers either pay a substantial premium or are effectively excluded. Credit ratings from agencies such as Moody's, S&P, and Fitch are therefore central to CP market access.

Commercial paper markets distinguish between directly-placed paper, where large financial institutions distribute their own notes to investors without an intermediary, and dealer-placed paper, where investment banks intermediate the issuance. The CP market plays an important role in the funding structure of financial intermediaries: money market funds are among the largest investors, which created systemic vulnerabilities exposed during the 2008 crisis, when the failure of Lehman Brothers triggered a run on money market funds and a near-freeze of the CP market.

##### Certificates of Deposit

Certificates of deposit (CDs) are time deposits issued by banks that pay a fixed interest rate over a specified term. Unlike ordinary savings deposits, large-denomination negotiable CDs — typically with a minimum face value of $\$100,000$ — can be freely sold in secondary markets before maturity, making them proper money market instruments. Non-negotiable CDs are personal saving products and are not traded.

Negotiable CDs are issued at face value and pay interest at maturity, making their valuation straightforward:

$$\text{Proceeds at maturity} = N \left(1 + r \cdot \frac{T}{360}\right)$$

where $r$ is the agreed deposit rate and $T$ is the term in days. The yield on negotiable CDs trades at a spread above comparable T-bill yields, reflecting the credit risk of the issuing bank and the lower liquidity of secondary markets relative to government paper. During periods of banking stress, CD spreads widen sharply, providing a real-time signal of perceived bank credit risk. Euro-dollar CDs — dollar-denominated CDs issued by banks outside the United States — form an important segment of the global money market, particularly the London market, and historically provided the basis for LIBOR fixings.

##### Repurchase Agreements (Repos)

Repurchase agreements, or repos, are among the most important instruments in modern money markets. A repo is a short-term secured loan: one party sells a security—typically a government bond—with the commitment to repurchase it at a later date and a slightly higher price. The difference between the sale and repurchase price reflects the repo rate, analogous to an interest rate on a collateralized borrowing. From the counterparty's point of view, the transaction is a reverse repo, meaning it lends cash against the security as collateral.

Repos are fundamental to liquidity management and collateral circulation. They enable financial institutions to fund positions efficiently, manage short-term liquidity, and facilitate price discovery in fixed income markets. Central banks also rely on repos as a primary instrument of monetary policy, using them to inject or withdraw liquidity and to influence short-term interest rates. The global repo market is vast: outstanding balances are estimated in the tens of trillions of dollars, with the U.S. segment alone exceeding $5 trillion in daily transactions {cite:p}`OFR2023repo`.

Mechanically, two key parameters define the economics of a repo: the repo rate and the haircut—the percentage discount applied to the market value of the collateral. A higher haircut protects the lender against a fall in collateral value but increases the borrower's funding cost. Haircuts vary with the perceived credit quality and liquidity of the collateral: Treasury securities typically carry haircuts close to zero, while corporate bonds or structured products may require 5–20%. In stressed conditions, haircuts often rise sharply, forcing deleveraging and amplifying market instability, as seen during the 2008 financial crisis.

For example, consider a repo in which a bank borrows $\$98$ million in cash for one week and pledges $\$100$ million in Treasury bonds as collateral. The haircut is therefore 2%. If the agreed repo rate is 3% per annum, the repurchase price after seven days will be:

$$98{,}000{,}000 \times \left(1 + 0.03 \times \frac{7}{360}\right) \approx 98{,}057{,}166\,\$$$

At maturity, the bank repays $\$98.06$ million and receives back its $\$100$ million in bonds. For the cash lender, the repo rate represents the secured yield on the transaction, while for the borrower, it represents the funding cost of holding the securities.

Repos are also integral to the market-making business. Suppose a dealer sells a bond to an asset manager such as Amundi, but does not hold the bond in inventory. The dealer can borrow the bond in the repo market, for instance from another asset manager like BlackRock, who lends it against cash collateral. The dealer delivers the bond to the client and must then either wait for another client to take the opposite position, renew the repo agreement upon maturity, or buy the bond in the interbank market to close the position. This continuous use of repos allows dealers to provide liquidity and make markets without holding large inventories of bonds.

Repos also underpin short selling, as they provide the mechanism by which short sellers borrow securities to sell them in anticipation of price declines. However, short positions carry significant risk if prices rise. Public data on open short positions—such as the short‐interest reports published by FINRA, NYSE, and Nasdaq—allow regulators and market participants to monitor short activity and its potential influence on price pressure and funding conditions. For example, the GameStop short squeeze in early 2021 {cite:p}`SEC2021gamestop` demonstrated how short sellers can face extreme pressure when prices move unexpectedly, forcing them to cover positions at large losses. Earlier examples, such as those portrayed in The Big Short {cite:p}`Lewis2010bigshort`, show that even when short sellers are correct in their analysis, they can face severe liquidity and timing risks.

(sec:ifi_fixed_income)=
### Fixed Income 

Fixed income instruments are debt securities that promise a predefined set of cash flows over time, either in fixed or variable form. By purchasing a fixed income instrument, investors lend capital to an issuer in exchange for contractual payments and the repayment of principal at maturity. Unlike equity, which represents a residual claim on a firm's assets, fixed income securities confer senior, legally binding claims. 

Issuers of fixed income instruments span the full spectrum of the economy. **Sovereign issuers** finance fiscal activity and provide benchmark risk-free curves. **Corporate issuers** use bonds to fund investment and manage leverage. **Municipal issuers** finance regional and local infrastructure, while **supranational institutions** issue debt to support international development and policy objectives. 

Across all cases, the dominant fixed income instrument is the **bond**, characterized by periodic coupon payments and a final repayment of principal at a specified maturity. The presence of a maturity date anchors valuation in a way that sharply contrasts with equities, whose cash flows are discretionary and potentially infinite.

#### Valuation of fixed income instruments

As we will discuss in chapter {ref}`fair_price_estimation`, the theoretical foundation of fixed income valuation is the **time value of money**.

This logic extends naturally to bonds, which deliver multiple future cash flows. For a bond with maturity $T$, coupon payments $C_t$, and face value $N$, the price $P$ is given by the sum of discounted promised payments:

$$P = \sum_{t=1}^{T} \frac{C_t}{(1+r_t)^t} + \frac{N}{(1+r_T)^T}$$

In practice, bonds traded in the market have observable prices that do not necessarily match with these theoretical prices, since there are additional risks and liquidity constraints for which investors typically demand an extra *yield* in order to invest in these instruments as alternatives to risk-free deposits. We define the **yield to maturity** as the constant rate $y$ that equates the discounted value of promised cash flows to the observed market price:

$$P = \sum_{t=1}^{T} \frac{C_t}{(1+y)^t} + \frac{N}{(1+y)^T}$$

The yield is therefore an implied quantity rather than a fundamental primitive: it is the discount rate that reconciles price and cash flows and allows bonds with different coupons and maturities to be compared on a common basis. If we compute yields for a set of bonds from the same issuer with different maturities, the sorted collection of yields is called the *yield curve*.

#### Fixed income risk factors

Risk in fixed income markets is commonly organized around two broad dimensions. The first is **interest rate risk**, driven by movements in the level and shape of the yield curve for relatively risk-free issuers, typically sovereign bonds issued by governments with solid finances like the USA, Germany or Japan, or supranational entities like the European Union. Alternatively, interest rate risk factors can also be inferred from short-term monetary instruments and interest rate derivatives like standard interest rate swaps (IRS). The collection of inferred rates across maturities constitutes the **term structure of interest rates**. Changes in this term structure are typically highly correlated and can be mostly described in term of latent risk factors driving co-movements like parallel shifts, steepening, or flattening of the interest rate curve. Such risk factors are then linked to movements in prices government bond portfolios and other rates products. Notice that short-term rates movements are typically tied to monetary policy decisions, while longer-term rates embed expectations about future policy paths, inflation, and macroeconomic conditions.

The second major risk dimension is **credit risk**. Bonds issued by corporations, institutions or governments that are exposed to default risk trade at yields above those of comparable risk-free sovereign benchmarks. The difference between the yield on a risky bond and the yield on a benchmark bond of the same maturity is the **credit spread** $s$:

$$s = y_{\text{risky}} - y_{\text{risk-free}}$$

Credit spreads compensate investors for expected default losses, recovery uncertainty, liquidity risk, and risk premia. In sovereign markets, this differential is often referred to as a risk premium relative to a benchmark issuer; in corporate markets, it is the central pricing variable for credit as an asset class.

This distinction between rates risk and credit risk provides the organizing principle for fixed income markets. It also motivates the common separation between rates products and credit products in trading, portfolio management, and risk analysis. For a deeper introduction to this topic, a classical reading is {cite:p}`Fabozzi2007Handbook`.

#### Main fixed income instrument types

**Coupon types.** Bonds are classified by the structure of their coupon payments. A **fixed-coupon bond** pays a constant coupon $C = c \cdot N$ at each period, where $c$ is the coupon rate and $N$ is the face value. A **floating-rate note** (FRN) pays a coupon that resets periodically, typically equal to a reference rate (SOFR, €STR, or a legacy LIBOR rate) plus a fixed spread: $C_t = (r_t^{\text{ref}} + s) \cdot N$. Because the coupon resets to market rates, FRNs have low duration and trade close to par under normal conditions, making them a common choice for issuers and investors who wish to minimise interest rate risk. A **zero-coupon bond** pays no intermediate coupons; the investor receives only the face value $N$ at maturity $T$, and the price is simply $P = N / (1+y)^T$. Zero-coupon bonds have the highest duration for a given maturity and are widely used in liability-driven investment and as building blocks for stripping coupon bonds into their constituent cash flows.

**Price conventions.** Bond prices are quoted in two ways. The **dirty price** (or full price) is the actual cash consideration paid by the buyer and equals the present value of all remaining cash flows. The **clean price** (or flat price) is the dirty price minus the **accrued interest** — the portion of the next coupon payment that has accrued since the last coupon date:

$$\text{Accrued Interest} = C \cdot \frac{\text{days since last coupon}}{\text{days in coupon period}}$$

In most markets, bonds are quoted on a clean price basis, even though settlement occurs at the dirty price. This convention stabilizes the quoted price around par between coupon dates, making it easier to compare bonds with different coupon frequencies. At each coupon payment date, the clean and dirty prices coincide.

**Interest rate sensitivity: duration and convexity.** The sensitivity of a bond's price to changes in yield is captured by two measures. **Modified duration** $\mathcal{D}$ is the percentage change in price for a unit increase in yield:

$$\mathcal{D} = -\frac{1}{P}\frac{\partial P}{\partial y}$$

For a fixed-coupon bond, modified duration is approximately equal to the weighted average time to receipt of cash flows (Macaulay duration) divided by $(1+y)$. A bond with duration of 5 years loses approximately 5% in price for a 100 basis point rise in yield. For portfolios, the aggregate DV01 (dollar value of a basis point) — the dollar change in portfolio value for a one-basis-point move in yields — is the standard risk measure in fixed income trading.

Duration provides a first-order approximation. The second-order correction, **convexity**, captures the curvature of the price-yield relationship:

$$\Delta P \approx -\mathcal{D} \cdot P \cdot \Delta y + \frac{1}{2} \cdot \text{Convexity} \cdot P \cdot (\Delta y)^2$$

Positive convexity means that a bond gains more than duration predicts when yields fall, and loses less than duration predicts when yields rise — a desirable property. Standard fixed-coupon bonds have positive convexity; mortgage-backed securities and callable bonds can exhibit negative convexity in certain rate environments because of their embedded optionality.

**Credit bond valuation.** For bonds subject to default risk, the promised yield $y$ exceeds the risk-free rate $r_f$ by the credit spread $s$. A simple structural model sets the spread as compensation for expected default losses: if the issuer defaults with annual probability $\lambda$ and bondholders recover a fraction $R$ of face value, the fair spread satisfies approximately $s \approx \lambda(1-R)$. In practice, credit spreads also embed liquidity premia and risk premia for the uncertainty of default timing. A well-known episode illustrating the materiality of recovery assumptions was the bankruptcy of the FTX cryptocurrency exchange in 2022, where the ultimate recovery for creditors was subject to extreme uncertainty, and even senior claims traded at deep discounts reflecting the legal and operational complexity of the estate.

(sec:ifi_fx)=
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

$$F_{A/B} = S_{A/B} \times \frac{(1 + i_A T)}{(1 + i_B T)}$$

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
  Strong performance in a country's stock market can attract foreign investment, as investors seek higher returns. To purchase local equities, they must first acquire the domestic currency, boosting its demand and potentially appreciating its spot value.

- **Trade Balance (Exports vs. Imports):**  
  The balance of trade between countries also impacts currency valuation. If a country exports more than it imports, foreign buyers must convert their currency into the exporter's currency to pay for goods. Over time, sustained trade surpluses can increase demand for the exporter's currency, appreciating its value. Conversely, persistent deficits may weaken it.

(sec:ifi_derivatives)=
## Derivative Instruments

Derivatives are contracts whose value depends on the price or level of an underlying asset, rate, or index. They allow market participants to transfer, hedge, or create specific risk exposures without exchanging the underlying asset itself. Their valuation rests on no-arbitrage principles, linking them to the prices of cash instruments and to the dynamics of the underlying via stochastic models developed in {ref}`stochastic_calculus` and {ref}`fair_price_estimation`.

(sec:ifi_forwards)=
### Forwards and Futures

A **forward contract** is a bilateral agreement to buy or sell an asset at a future date $T$ at a price $F$ agreed today. No cash changes hands at inception. At maturity, the buyer receives the asset (or its cash equivalent) and pays $F$; the seller delivers and receives $F$. The payoff to the long position is $S_T - F$, where $S_T$ is the spot price at maturity.

**Cost-of-carry pricing.** The no-arbitrage forward price is determined by the cost of carrying the underlying asset from today to maturity. For a non-dividend-paying asset with spot price $S$ and continuous risk-free rate $r$:

$$F = S \cdot e^{rT}$$

The argument is simple: buying the asset today and financing it at $r$ for $T$ years must be equivalent to locking in the forward purchase. If $F > Se^{rT}$, one can buy the asset, sell the forward, and earn a riskless profit; if $F < Se^{rT}$, the reverse arbitrage applies. For assets that pay a continuous income yield $q$ (dividends for equities, foreign interest rate for FX), the forward price adjusts to $F = S \cdot e^{(r-q)T}$. For bonds, the net cost of carry subtracts the present value $I$ of coupon payments received during the holding period: $F = (S - I) \cdot e^{rT}$.

**Futures contracts** are economically equivalent to forwards but are exchange-traded and standardized. Key institutional differences include:

- **Daily mark-to-market and margining**: futures gains and losses are settled daily in a margin account. If the margin falls below the maintenance level, the holder receives a margin call. This eliminates counterparty credit risk but introduces funding liquidity risk.
- **Standardization**: contract size, delivery date, and underlying specifications are fixed by the exchange, enabling liquid secondary markets.
- **Central clearing**: futures are cleared through a central counterparty (CCP), which further reduces bilateral credit risk.

Major futures markets include equity index futures (S&P 500, Euro Stoxx 50), government bond futures (where delivery involves a cheapest-to-deliver bond selected from a basket, with a conversion factor adjusting for coupon and maturity differences), and commodity futures. Forward contracts dominate in FX and OTC fixed income, where customization is more important than secondary market liquidity.

(sec:ifi_swaps)=
### Swaps

A swap is a bilateral contract to exchange a series of cash flows over time, according to a pre-agreed schedule and formula. Swaps are the most widely used derivatives by notional outstanding and are fundamental instruments for transforming interest rate, currency, and credit exposures.

**Interest rate swaps (IRS).** In a plain vanilla IRS, one party pays a fixed rate $K$ (the swap rate) on a notional $N$ and receives a floating rate (typically SOFR or €STR for new contracts) on the same notional, for a sequence of payment dates $t_1 < t_2 < \ldots < t_n = T$. The fixed leg pays $K \cdot \delta_i \cdot N$ at each date $t_i$, where $\delta_i$ is the day-count fraction for the period; the floating leg pays the reference rate observed at the start of each period, accrued over $\delta_i$. Only net cash flows are exchanged — there is no exchange of notional. The **par swap rate** $K$ is the fixed rate that makes the initial value of the swap equal to zero:

$$K = \frac{\sum_{i=1}^{n} \delta_i \cdot P(0, t_i) \cdot f(0; t_{i-1}, t_i)}{\sum_{i=1}^{n} \delta_i \cdot P(0, t_i)}$$

where $P(0,t_i)$ is today's discount factor for maturity $t_i$ and $f(0; t_{i-1}, t_i)$ is the forward rate for the period $[t_{i-1}, t_i]$. Once traded, an IRS gains or loses value as interest rates move: a receiver of fixed (payer of floating) gains when rates fall and loses when rates rise, with a duration profile similar to a fixed-coupon bond of the same maturity.

**Cross-currency swaps** exchange cash flows in two different currencies, including the notional at inception and maturity. They are used to transform funding from one currency to another and to manage the currency exposure of foreign-currency assets or liabilities. The pricing builds on covered interest parity but also incorporates a **cross-currency basis** — an additional spread that reflects supply and demand for funding in different currencies and which widened dramatically during the 2008 and 2020 crises.

**Credit default swaps (CDS).** A CDS is a contract that provides insurance against the default of a reference entity. The **protection buyer** pays a periodic spread $s$ (the CDS spread, quoted in basis points per annum on notional $N$) and receives a payment from the **protection seller** if a credit event occurs. The payment on default is typically $(1-R) \cdot N$, where $R$ is the recovery rate. The CDS spread therefore reflects the market's implied default probability and recovery assumptions. In the absence of arbitrage, a CDS on a bond issuer should be priced consistently with the credit spread on the issuer's bonds, though basis between cash and CDS markets arises from funding costs, supply-demand imbalances, and technical factors. CDS are governed by ISDA documentation, which specifies the list of credit events (bankruptcy, failure to pay, restructuring) and settlement mechanisms (physical or cash).

(sec:ifi_options)=
### Options

Options are derivatives contracts that grant the holder the option (hence the name) to buy or sell (depending on the option) a given financial instrument (the underlying) at a price contingent to the clauses of the contract. The most simple option, the European option, pre-specifies a given time $T$, the expiry, and price $K$, the strike, to exercise this option. But there are many other variations in the market. An option to buy a financial instrument is referred to as a call option, and an option to sell is a put option. 

Let us consider European options on stocks. If the market price of the stock at expiry is $S_T$, a call option will be exercised by a rational investor only if the price is higher than the strike $K$, making a profit of $S_T - K$, which in some cases is directly paid in cash, in others the actual stock is received, but of course it could be directly sold in the market at a favourable price. Therefore, the payoff of a call option can be written as:

$$C_T = (S_T - K)^+$$

where $(.)^+$ denotes the positive part of the argument. On the contrary, a put option will only be exercised if the market price is below the strike, hence the payoff is:

$$P_T = (K - S_T)^+$$

Options can be traded in regulated markets or be quoted by bank dealers. Since the investor that holds the option cannot lose money from it, such option does not come for free, and the question is how much such an option is worth, which is called the premium of the option. At expiry, the price is naturally the payoff function. But at time $t < T$ there is still uncertainty about the price $S_T$ which will determine the final profit (if any), so the premium will be different. The theory of option pricing is developed in detail in {ref}`fair_price_estimation` using the tools of stochastic calculus and no-arbitrage arguments.

#### Basic strategies

Options can be combined into a wide variety of payoff structures. The most fundamental is the **put-call parity** relationship, which links the prices of European calls and puts with the same strike and expiry under no-arbitrage:

$$C - P = S - K e^{-rT}$$

This identity — a call minus a put equals the forward — holds regardless of the model and can be verified by a simple portfolio argument: a portfolio long a call and short a put replicates the payoff of a forward contract.

Common single-option strategies include the **protective put** (long underlying + long put), which caps downside losses while preserving upside exposure, and the **covered call** (long underlying + short call), which generates income from the option premium at the cost of capped upside. Multi-leg strategies combine options to express views on direction and volatility: a **straddle** (long call + long put at the same strike) profits from large moves in either direction, while a **strangle** uses out-of-the-money options to achieve a similar payoff at lower premium cost. **Spread strategies** (call spreads, put spreads) combine a long and a short option at different strikes to cap both the maximum gain and the maximum cost.

#### Valuation: time value, volatility, and Greeks

At any time $t < T$, the option premium decomposes into **intrinsic value** — the payoff if exercised immediately, $\max(S_t - K, 0)$ for a call — and **time value**, the additional premium reflecting the possibility of favourable moves before expiry. Time value is always non-negative for a standard European option and declines to zero as $t \to T$.

The sensitivity of an option's price to its inputs is captured by the **Greeks**:

- **Delta** $\Delta = \partial C / \partial S$: the change in option price per unit change in the underlying. A call has $\Delta \in (0,1)$; a put has $\Delta \in (-1,0)$. Delta-neutral hedging — holding $-\Delta$ units of the underlying per option — eliminates first-order directional exposure.
- **Gamma** $\Gamma = \partial^2 C / \partial S^2$: the rate of change of delta with respect to the underlying. Long option positions have positive gamma, meaning the hedge ratio must be adjusted as the underlying moves. Positive gamma also means that the P&L from gamma exceeds the cost of hedging when the underlying moves significantly, connecting option pricing to realized volatility.
- **Theta** $\Theta = \partial C / \partial t$: the change in option price with the passage of time. Theta is typically negative for long options (time decay), reflecting the loss of time value as expiry approaches. Long gamma and short theta are the two sides of the same trade: buyers of options pay time decay and profit from large moves.
- **Vega** $\mathcal{V} = \partial C / \partial \sigma$: the sensitivity to changes in volatility. Options are long vega — their value increases when volatility rises. Vega is largest for at-the-money options with long expiry.
- **Rho** $\rho = \partial C / \partial r$: the sensitivity to the risk-free rate. Rho is typically small for short-dated options but more relevant for long-dated equity options or interest rate options.

The fundamental result of Black-Scholes-Merton theory ({ref}`fair_price_estimation`) is that, under log-normal dynamics for the underlying, a delta-hedged option position earns or loses money at a rate proportional to $\frac{1}{2}\Gamma S^2(\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)$ — the difference between realized and implied variance. This connection makes options the natural instrument for trading views on volatility.

#### Implied volatility and volatility surface

The Black-Scholes formula provides a bijective mapping between option prices and a single volatility parameter $\sigma$. **Implied volatility** $\sigma_{\text{impl}}(K, T)$ is defined as the value of $\sigma$ that makes the Black-Scholes formula reproduce the observed market price for the option with strike $K$ and expiry $T$.

In practice, implied volatility varies across strikes and expiries, forming the **volatility surface**. Two main features are observed:

- **Volatility smile / skew**: for equity options, implied volatility is typically higher for low strikes (out-of-the-money puts) than for high strikes (out-of-the-money calls). This **skew** reflects the asymmetric demand for downside protection and the empirical finding that large negative equity moves are more likely than Black-Scholes predicts. For FX options, the pattern is more symmetric (a smile), reflecting two-sided tail risk.
- **Term structure**: implied volatility varies with expiry, typically rising during periods of uncertainty and falling as conditions stabilize. The term structure encodes the market's expectation of future realized volatility at different horizons.

The volatility surface is not a model-free object — its shape and dynamics are specific to each underlying and market. Advanced models (local volatility, stochastic volatility, jump-diffusion) attempt to reproduce the observed surface while remaining internally consistent with no-arbitrage.

#### Market conventions

In exchange-traded options markets (CME, Eurex, CBOE), options are standardized with fixed expiries and strikes, and cleared through a CCP with daily margining. In OTC markets — which dominate for FX, interest rate, and credit options — contracts are customized and documentation follows ISDA or similar frameworks.

For FX options, a distinctive quoting convention expresses prices in terms of delta rather than strike, since the delta is more informative about the position's directional exposure. Risk reversals (the premium of a call over a put at the same delta, e.g., 25-delta) and strangles (the average of call and put at the same delta) are the standard building blocks of the FX volatility market and encode the skew and smile separately.

### Other Derivative Types

Beyond the core derivative families, markets have developed a range of specialized instruments. **Commodity derivatives** — futures and options on oil, natural gas, metals, and agricultural products — are among the oldest derivative markets and share the same pricing logic as financial derivatives, with the cost-of-carry adjusted for storage costs and convenience yield. **Volatility derivatives**, notably variance swaps and the VIX futures market, allow participants to trade the realized or implied volatility of an index directly, without taking directional exposure to the level of the index. **Exotic options** extend the European framework with path-dependent or state-dependent payoffs: barrier options activate or extinguish if the underlying crosses a level; Asian options pay based on an average of the underlying over the life of the contract; digital (binary) options pay a fixed amount if the underlying is above or below a strike at expiry.

(sec:ifi_structured)=
## Hybrid and Structured Products

Hybrid and structured products combine features of multiple instruments to create customized payoff profiles. They often embed derivative components within a funding or investment vehicle, enabling issuers and investors to fine-tune exposure to market variables, credit risk, or volatility.

### Structured Notes and Deposits

A structured note is a debt instrument issued by a financial institution that embeds one or more derivative payoffs within a bond-like wrapper. The issuer borrows at a spread to the risk-free rate and uses part of that spread — or accepts a below-market coupon — to purchase an embedded option, the payoff of which is passed on to the investor.

The two archetypal designs are **principal-protected notes** and **principal-at-risk notes**. A principal-protected note guarantees the return of face value at maturity (via a zero-coupon bond) while allocating the remaining budget to a call option on an underlying index, giving investors full upside participation with no downside risk to capital. A reverse convertible is a principal-at-risk structure: the investor receives an enhanced coupon, but if the underlying falls below a barrier, the principal is repaid in shares (or at a loss), effectively because the investor has sold a put option to the issuer.

Common variations include **range accruals** (coupons accrue only while an index stays within a range), **auto-callables** (the note redeems early at a premium if the underlying is above a trigger level on specific observation dates), and **capital-protected participation notes** with digital payoffs. Valuation of structured notes requires decomposing the product into its bond and derivative components, pricing each separately, and adding the issuer's credit spread. Investors must also account for the liquidity premium embedded in the OTC wrapper: structured products often trade at wide bid-ask spreads or have no secondary market.

### Credit-Linked Instruments

Credit-linked notes (CLNs) are funded versions of credit default swaps: the investor buys a note whose coupon is enhanced by a CDS premium, and the principal is at risk if a specified credit event occurs on a reference entity. From the issuer's perspective, a CLN is an alternative to buying CDS protection: it provides funded protection — the cash is received upfront and returned only if there is no default. CLNs are commonly issued by banks as a way to transfer concentrated credit exposures to a broader investor base.

Asset-backed securities (ABS) and mortgage-backed securities (MBS) securitize pools of cash-flow generating assets — residential mortgages, auto loans, credit card receivables — into tradable securities. The cash flows from the underlying pool are allocated across **tranches** in a defined priority order (the **waterfall**): senior tranches absorb losses last and receive the lowest yield; mezzanine tranches absorb intermediate losses; the equity tranche absorbs the first losses and earns the highest return. Tranching allows different investors to access the risk-return profile that matches their mandate, and enables the originating institution to transfer credit risk off its balance sheet. Collateralized debt obligations (CDOs) extend this logic to pools of bonds or CDS, creating additional layers of tranching. The mispricing of CDO tranches — particularly the correlation assumptions embedded in their valuation — was a central mechanism in the buildup and amplification of the 2008 financial crisis.

### Securitization and Structured Finance

Securitization is the process of pooling illiquid financial assets and issuing tradable securities backed by the cash flows of that pool. The economic rationale is twofold: it frees balance sheet capacity for originators (banks can lend more by transferring credit risk), and it creates investment instruments with cash-flow profiles that are difficult to replicate with standard bonds.

The legal structure involves a **special purpose vehicle** (SPV): a bankruptcy-remote entity to which the originator sells the underlying assets (a **true sale**), isolating them from the originator's own credit risk. The SPV then issues securities to investors, backed solely by the asset pool. The **waterfall** determines how interest and principal receipts are distributed across the tranches at each payment date, typically prioritizing senior tranches in both interest and principal repayment.

Securitization is regulated following the lessons of 2008, when poor underwriting standards and opaque structures led to massive losses in MBS and CDO markets. Post-crisis regulation — including risk retention rules (the originator must retain at least 5% of the economic exposure in the EU and US), increased disclosure requirements, and stricter capital treatment for securitization exposures held by banks — has substantially reshaped the market structure.

### Hybrid Securities

Hybrid securities occupy the boundary between debt and equity in the capital structure, combining features of both to achieve specific regulatory, accounting, or funding objectives.

**Convertible bonds** are corporate bonds with an embedded equity call option: the holder has the right to convert the bond into a fixed number of shares at a predetermined conversion price. If the share price rises above the conversion price, conversion becomes attractive and the bond behaves like equity; below that level, the bond floor provides downside protection. Convertibles are therefore long-gamma instruments and are actively traded by hedge funds who exploit the optionality through delta-hedging. From the issuer's perspective, convertibles allow borrowing at a below-market coupon in exchange for the potential dilution of existing shareholders.

**Contingent convertible bonds** (CoCos) are hybrid capital instruments issued by banks that convert into equity or are written down if the issuing bank's capital ratio falls below a trigger level. They are designed to absorb losses in stress scenarios and to strengthen the bank's capital position precisely when it is most needed. The conversion trigger and loss-absorption mechanism introduce path-dependency and model risk into their valuation; investors must therefore assess not only the credit risk of the issuer but also the regulatory and accounting treatment of the capital trigger.

**Preferred shares** rank between senior debt and common equity in the capital structure. They typically carry fixed cumulative dividends that must be paid before any dividend is paid on common shares, but they rank behind all creditors in the event of liquidation. Preferred shares are used extensively in bank capital structures (as Additional Tier 1 or AT1 capital under Basel III) and in private equity structures, where their seniority in distributions and liquidation preferences are negotiated contractually.

## Exercises

1. **Bond pricing and yield.** A 5-year government bond has face value €1,000, annual coupon rate 3%, and yield to maturity (YTM) 4%. (a) Compute the bond price $P = \sum_{t=1}^{5} \frac{C}{(1+y)^t} + \frac{F}{(1+y)^5}$. (b) Recompute the price if the YTM rises to 5%. (c) What percentage of the price change is accounted for by the duration approximation $\Delta P \approx -D_{\text{mod}} \cdot P \cdot \Delta y$? (d) Explain intuitively why the bond price falls when yields rise.

2. **Duration and DV01.** For the bond in Exercise 1 priced at YTM $= 4\%$: (a) Compute the Macaulay duration $D_{\text{mac}} = \frac{1}{P}\sum_{t=1}^{5} t \cdot \frac{C_t}{(1+y)^t}$. (b) Compute the modified duration $D_{\text{mod}} = D_{\text{mac}}/(1+y)$. (c) Compute the DV01 (dollar value of a basis point) and verify it approximates the price change from Exercise 1(b). (d) A portfolio manager holds €10 million face value of this bond and wants to hedge against a 50bp parallel shift in yields. How much DV01 of an offsetting instrument is required?

3. **Option payoffs and put-call parity.** A European call and put on the same non-dividend-paying stock have strike $K = 100$ and 3-month expiry. The current stock price is $S_0 = 102$, the 3-month continuously compounded risk-free rate is $r = 2\%$ p.a., and the call trades at $C = 5.20$. (a) Using put-call parity $C - P = S_0 - Ke^{-rT}$, compute the fair put price $P$. (b) If the put is quoted at $P' = 2.80$, describe a cash-and-carry arbitrage: what positions are entered today and what are the payoffs at expiry? (c) Compute the arbitrage profit if $S_T = 95$ at expiry.

4. **Forward pricing and cash-and-carry.** A stock trades at $S_0 = 50$ and pays a known dividend $D = 1$ at $t = 1$ month. The continuously compounded risk-free rate is $r = 3\%$ p.a. Delivery is at $T = 6$ months. (a) Derive the no-arbitrage forward price $F = (S_0 - De^{-r t_D})e^{rT}$ where $t_D$ is the dividend date. (b) Compute $F$ numerically. (c) If the forward is quoted at $F' = 51$, describe the arbitrage (cash-and-carry or reverse cash-and-carry) and compute the riskless profit per share.
