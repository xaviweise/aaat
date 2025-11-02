# Algorithmic Trading

## Introduction

Algorithmic trading refers to the use of computer programs to automate the process of making trading decisions and executing orders in financial markets. Although the term is widely used, its precise meaning can vary depending on the context and the regulatory framework. Two influential definitions are the following:

* Bank for International Settlements (BIS, 2011):
*Trading technology in which order and trade decisions are made electronically and autonomously.*

* MiFID II (Directive 2014/65/EU, Article 4, Definition 39):
 *Trading in financial instruments where a computer algorithm automatically determines individual parameters of orders such as whether to initiate the order, the timing, price or quantity of the order or how to manage the order after its submission, with limited or no human intervention.*

Notice that we use the terms algorithmic trading and automated trading as synonyms. In some references, algorithmic trading is used more narrowly to denote algorithmic execution, a specific form of automated trading focused on the optimal execution of predefined orders.

Algorithmic trading can be viewed as a subset of *systematic trading*, which refers to any trading strategy defined in a rule-based, methodical manner. It is also a subset of *quantitative trading*, where trading decisions follow the principles of the scientific method. In this framework, we first construct a scientific model of the trading environment—for example, a stochastic process such as a random walk—to represent market dynamics. This model is then used to derive inferences about quantities of interest, such as the likely range or direction of future prices. These inferences serve as inputs to mathematical optimization procedures, which determine the optimal trading actions—such as when and at what levels to trade—under given objectives and constraints.

The MiFID II definition is intentionally broad. It encompasses both complex, fully automated trading strategies and simpler automated rules, such as dynamic stop-loss orders or auto-negotiation mechanisms.
In our following discussion, we will adopt the first, more restrictive definition, focusing on sophisticated algorithmic strategies where automation plays a central role in decision-making and execution.
 
 
 ## Exercises
