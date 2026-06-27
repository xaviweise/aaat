(preface)=

# Preface

Algorithmic trading sits at the intersection of several mathematical disciplines — probability theory, stochastic calculus, statistical inference, optimisation, and machine learning — applied to one of the most complex and dynamic systems human societies have built: financial markets. Each of these disciplines has an extensive literature of its own, and so does the practical craft of building trading systems. What is harder to find is a treatment that integrates them — that derives the Avellaneda–Stoikov market-making equations from first principles in the same breath as it explains how a Kalman filter tracks a fair mid-price, or that connects Bayesian decision theory to the design of a client quoting strategy.

This book is my attempt at that integration. It grew out of lecture notes developed across several teaching contexts: internal courses for my team at BBVA, where the focus was always on problems we faced in practice; a graduate course on algorithmic trading at the Universidad de Alcalá; and courses at the Instituto de Empresa. Each audience shaped the material differently — practitioners pushed for concrete models and implementable intuitions, while students pushed for accessible introductions to the core subjects — and the tension between those two demands is, I hope, visible in a positive way throughout these pages. The starting point for all of it was my own work at BBVA on algorithmic trading problems, from optimal execution in equity markets to market making in fixed income and FX. The result is a treatment that tries to be mathematically rigorous without sacrificing the practical intuition that makes models useful.

The book is, and will remain for some time, a work in progress. I release it in regular updates and welcome feedback from readers through the issue tracker on GitHub.

(prior-knowledge)=

## Prior Knowledge

The mathematical prerequisites are those of a strong undergraduate degree in mathematics, physics, engineering, or a quantitatively oriented economics or finance programme. Specifically, I assume familiarity with:

- **Calculus and linear algebra**: partial derivatives, the chain rule, integration, matrix operations, eigendecompositions, and the singular value decomposition. These are used throughout without review.
- **Probability and statistics**: probability spaces, random variables, expectations, conditional distributions, the Gaussian family, basic hypothesis testing, and the method of maximum likelihood. The {ref}`intro_bayesian` chapter introduces the Bayesian perspective from first principles, but a frequentist background is assumed.
- **Python**: the numerical examples and all figures are produced in Jupyter notebooks using standard scientific computing libraries (NumPy, SciPy, Matplotlib, pandas, scikit-learn). Readers comfortable with Python at an intermediate level should be able to run and modify the notebooks without difficulty.

Prior knowledge of finance or economics is helpful but not strictly required. The {ref}`intro_financial_markets` and {ref}`intro_financial_instruments` chapters introduce the institutional landscape, market structure, and the main asset classes from first principles. Readers with a finance background may skim these chapters and use them as a reference for notation.

(how-to-read-this-book)=

## How to Read This Book

The book is divided into five parts, which can be read sequentially or, for readers with relevant background, selectively.

**Part I — Financial Markets Fundamentals** ({ref}`intro_financial_markets`, {ref}`intro_financial_instruments`, {ref}`market_microstructure`, {ref}`algorithmic_trading`) establishes the institutional and microstructural context in which algorithmic trading operates. It covers market participants, order types and the central limit order book, the mechanics of price formation, and the regulatory framework. Readers who already work in financial markets can treat this part as a notation reference.

**Part II — Financial Modelling Fundamentals** ({ref}`intro_bayesian`, {ref}`intro_causal`, {ref}`stochastic_calculus`, {ref}`stochastic_optimal_control`, {ref}`data_driven_methods`, {ref}`generative_ai`) develops the mathematical toolkit used throughout the rest of the book. This is the most diverse part: it covers Bayesian probability and graphical models, causal inference, Itô calculus and stochastic differential equations, stochastic optimal control via the Hamilton–Jacobi–Bellman equation, the core of supervised and unsupervised machine learning, and the foundations of large language models and AI agents. These chapters can be read independently of each other, though {ref}`stochastic_calculus` is a prerequisite for {ref}`stochastic_optimal_control`, and {ref}`data_driven_methods` provides useful context for {ref}`generative_ai`.

**Part III — Execution Algorithms** ({ref}`execution_fundamentals`, {ref}`lob_models`, {ref}`optimal_execution`, {ref}`execution_tactics`) covers the problem of executing a pre-determined order in the market at minimum cost and risk. It begins with the taxonomy of execution benchmarks and cost models, develops models of the limit order book and order flow, derives the Almgren–Chriss optimal execution trajectory, and covers practical execution tactics including adaptive slicing and dark-pool routing.

**Part IV — Market Making Algorithms** ({ref}`market_making_fundamentals`, {ref}`fair_price_estimation`, {ref}`liquidity_modelling`, {ref}`rfq_models`, {ref}`optimal_market_making`, {ref}`optimal_hedging`) addresses the dealer's problem: continuously quoting bid and ask prices to clients while managing inventory and adverse selection risk. The chapters progress from the conceptual decomposition of the bid–ask spread through Kalman filter and Bayesian models for fair price estimation, liquidity measurement, and client behaviour modelling in request-for-quote markets, to the mathematical theory of optimal market making derived from stochastic optimal control, and the hedging of residual inventory risk.

**Part V — Investment Algorithms** ({ref}`quant_investment_fundamentals`, {ref}`optimal_investment_theory`) covers systematic investment strategies: the construction and evaluation of signals, the principles of backtesting and avoiding overfitting, and the mathematical foundations of the main strategy families — mean reversion, momentum, statistical arbitrage, factor models, and portfolio optimisation including Markowitz mean-variance optimisation, risk parity, and the Black–Litterman framework.

The natural reading order is Parts I through V sequentially. Readers primarily interested in execution can proceed from Part I directly to Part III, returning to Part II as individual chapters require it. Similarly, readers focused on market making will find that {ref}`intro_bayesian`, {ref}`stochastic_calculus`, and {ref}`stochastic_optimal_control` are the most directly relevant chapters from Part II, while investment-focused readers will draw most heavily on {ref}`data_driven_methods` and the portfolio theory sections of {ref}`intro_bayesian`.

Each chapter closes with a set of exercises. These range from short derivations intended to consolidate the mathematical content to longer computational problems whose solutions require the accompanying Jupyter notebooks. The notebooks are collected in the final section of the book and reproduce all figures in the main text.

(acknowledgments)=

## Acknowledgments

This book would not exist without the colleagues and collaborators who have shaped my thinking about algorithmic trading over many years. I am grateful to my team at BBVA for the daily conversations that have refined the ideas in these pages and for their patience in reading early drafts. Their questions are the origin of many of the derivations and examples in this book.

I also thank the many readers who have taken the time to file issues and suggestions through the GitHub repository. A living book improves through its readers, and their engagement has made this a better work.

Finally, I am indebted to my family for their continued support, which makes this project possible.
