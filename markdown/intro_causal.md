(intro_causal)=
# Causal inference

## Introduction

The tools introduced in the {ref}`intro_bayesian` chapter give us a powerful framework for reasoning under uncertainty: given observations, we can update our beliefs about latent variables and model parameters, make predictions, and take decisions that minimize expected loss. Yet there is a class of questions that standard probabilistic inference cannot answer, no matter how much data we collect.

Consider a dealer quoting a bond instrument. The dealer observes that, historically, tighter spreads correlate with higher hit rates. Should she tighten her spread? The correlation is real, but it does not tell us what will happen if she *intervenes* and changes her spread — because the historical spread was itself set by a policy that depended on bond characteristics, client type, and market conditions. The clients who received tight spreads were not a random sample: they may have been clients with better credit ratings, larger notional requests, or bonds in high demand. A purely statistical model trained on this data will confound the effect of the spread with the effect of all these background variables.

This is the domain of **causal inference**: the study of what happens when we *do* something, rather than merely observe it. The distinction is fundamental. A probabilistic model can answer *observational* questions of the form "given that I see spread $\delta$, what is the probability of a hit?" but not *interventional* questions of the form "if I set spread $\delta$, what would the probability of a hit be?" The difference between these two quantities is the confounding effect of the variables that determined the historical spread.

Causal inference, formalized by Judea Pearl {cite:p}`pearl2016causal`, provides a principled framework to answer interventional and counterfactual questions using a combination of graphical models and a symbolic calculus. The framework rests on three key components: (1) a **causal graph** (a directed acyclic graph, or DAG) that encodes qualitative assumptions about which variables causally influence which others; (2) the **do-operator**, which formally distinguishes interventions from observations; and (3) **identification theorems** (notably the back-door criterion) that tell us when, and how, interventional quantities can be estimated from observational data.

This chapter introduces these ideas in a self-contained way. Readers familiar with Bayesian Networks from the {ref}`intro_bayesian` chapter will recognize the graphical language; the new content is the causal semantics layered on top. The chapter is organized as follows. We begin with Pearl's *ladder of causation*, which hierarchically orders the types of questions that probabilistic and causal models can answer. We then develop the formalism of structural causal models and the do-operator, including the back-door criterion and the adjustment formula. We close with counterfactual reasoning, which occupies the highest rung of the ladder and enables reasoning about hypothetical scenarios.

The ideas developed here are applied directly in the {ref}`rfq_models` chapter, where the RfQ pricing problem is formulated as a causal intervention and the back-door criterion is used to identify a valid conditioning set for the hit probability model.

## The three ladders of causation

Pearl's central organizing principle is the **ladder of causation** {cite:p}`pearl2016causal`, a three-rung hierarchy that classifies queries by the type of information they require:

| Rung | Activity | Query form | Example |
|------|----------|------------|---------|
| 1 | Seeing (Association) | $P(Y \mid X = x)$ | What is the hit rate when spread is $\delta$? |
| 2 | Doing (Intervention) | $P(Y \mid \text{do}(X = x))$ | What hit rate would result if we set spread to $\delta$? |
| 3 | Imagining (Counterfactual) | $P(Y_x \mid X = x')$ | Would this RfQ have been a hit if we had quoted $\delta$ instead of $\delta'$? |

**Rung 1 — Association.** Standard probability and statistics live on this rung. Given a dataset, we can estimate conditional probabilities $P(Y \mid X = x)$ by grouping observations and fitting a model. The key limitation is that this quantity reflects the *distribution of the population that happened to have $X = x$*, not the distribution that would result from forcing $X$ to equal $x$. In the bond market, the population of RfQs where the dealer quoted a tight spread is not representative of all RfQs: it was selected by the dealer's pricing policy, which in turn depended on bond and client characteristics.

**Rung 2 — Intervention.** The second rung asks what would happen if we surgically set $X = x$ for every unit in the population, overriding whatever value $X$ would naturally have taken. This is written $P(Y \mid \text{do}(X = x))$. In a randomized controlled experiment, we directly observe this quantity by randomly assigning $X$ regardless of background variables. Without randomization, answering second-rung queries requires a causal model — a representation of the data-generating mechanism that lets us reason about hypothetical interventions.

**Rung 3 — Counterfactuals.** The third rung goes further: it asks what would have happened to a *specific* individual unit had a different value been assigned to $X$, given that we know what actually happened to that unit. This is written $P(Y_x \mid X = x')$, the probability that $Y$ would take a given value if $X$ had been $x$, for a unit that actually had $X = x'$. Counterfactuals are fundamental to attribution and responsibility: "would this client have hit if we had quoted 5 bps tighter?" They require the full machinery of structural causal models.

A crucial insight is that Rung 2 queries cannot in general be answered from Rung 1 data without additional assumptions, and Rung 3 queries cannot in general be answered from Rung 1 or 2 data alone. The ladder is strict: each rung requires strictly more information than the one below it.

## Interventions and the Do-calculus

### Structural Causal Models and DAGs

The formal language of causal inference is the **Structural Causal Model (SCM)**. An SCM consists of:

1. A set of endogenous (modelled) variables $V = \{V_1, \ldots, V_n\}$.
2. A set of exogenous (background) variables $U = \{U_1, \ldots, U_n\}$, assumed mutually independent.
3. A set of **structural equations** $V_i = f_i(\text{Pa}(V_i), U_i)$ for each $i$, where $\text{Pa}(V_i)$ are the *parents* of $V_i$: the variables that directly causally determine $V_i$.

Each SCM induces a **directed acyclic graph (DAG)** $\mathcal{G}$, where each variable $V_i$ is a node and a directed edge $V_j \to V_i$ exists whenever $V_j \in \text{Pa}(V_i)$. The acyclicity condition rules out causal loops; the graph encodes the qualitative causal structure of the model.

The probabilistic Bayesian Network framework introduced in {ref}`intro_bayesian` uses the same DAG language and the same conditional independence reading via d-separation. The critical addition in the SCM framework is *causal* semantics: arrows represent mechanisms, not mere conditional dependences. This distinction only becomes visible when we intervene.

**Example.** Consider three variables: bond volatility $\sigma$, the dealer's spread $\delta$, and the RfQ outcome (hit/miss) $H$. In the observational distribution, $\sigma$ and $\delta$ are correlated because the dealer uses $\sigma$ to set $\delta$: high-volatility bonds attract wider spreads. If we simply condition on $\delta$ in a regression of $H$ on $\delta$, we confound the true effect of $\delta$ on $H$ with the selection effect induced by $\sigma$. The DAG $\sigma \to \delta$, $\sigma \to H$, $\delta \to H$ makes this confounding explicit: $\sigma$ is a common cause of both $\delta$ and $H$, opening a spurious back-door path $\delta \leftarrow \sigma \to H$.

### The Do-Operator

An **intervention** $\text{do}(X = x)$ on an SCM is implemented by replacing the structural equation for $X$ with a constant: $X \leftarrow x$, removing all arrows *into* $X$ in the DAG. All other structural equations remain unchanged. The resulting modified SCM defines the **interventional distribution** $P(V \mid \text{do}(X = x))$.

This *mutilation* of the graph is the formal counterpart of a randomized experiment: by setting $X$ externally, we sever the causal link from $X$'s natural parents to $X$, eliminating confounding through those parents. The do-operator thus replaces an observational quantity with a causal one.

In the bond RfQ example, $P(H \mid \text{do}(\delta))$ is the probability of a hit if the dealer were to set spread $\delta$ by a policy that ignores $\sigma$, client features, and all other variables that would normally influence $\delta$. This is the interventional quantity of interest for optimal pricing.

### Identifying Causal Effects: the Back-Door Criterion

The central identification problem is: when can we compute $P(Y \mid \text{do}(X))$ from purely observational data, and how? The **adjustment formula** gives the answer when a valid conditioning set $Z$ can be found:

$$P(Y \mid \text{do}(X = x)) = \sum_z P(Y \mid X = x, Z = z) \, P(Z = z)$$

where the sum (or integral) is over all values of the conditioning set $Z$. The left-hand side is a causal quantity; the right-hand side involves only standard conditional probabilities, which can be estimated from data. The key is finding a $Z$ that makes this identity valid.

**Definition (Back-door criterion).** A set of variables $Z$ satisfies the back-door criterion relative to an ordered pair $(X, Y)$ in DAG $\mathcal{G}$ if:
1. No variable in $Z$ is a descendant of $X$.
2. $Z$ blocks every path between $X$ and $Y$ that contains an arrow *into* $X$ (a *back-door path*).

A *back-door path* is any path from $X$ to $Y$ that begins with an arrow pointing into $X$: such paths represent confounding by common causes of $X$ and $Y$. Condition 2 requires all such paths to be blocked by $Z$, where "blocked" is defined by the d-separation rules from {ref}`intro_bayesian`: a path is blocked by $Z$ if it contains a chain $A \to M \to B$ or a fork $A \leftarrow M \to B$ with $M \in Z$, or a collider $A \to C \leftarrow B$ with $C \notin Z$ (and no descendant of $C$ in $Z$).

When $Z$ satisfies the back-door criterion, the adjustment formula holds and we can estimate the causal effect from observational data by:
1. Conditioning on $Z$ when fitting the outcome model $P(Y \mid X, Z)$.
2. Marginalizing over the distribution of $Z$ in the population.

In practice, we prefer the *smallest* valid $Z$ to minimize variance. Among valid sets, the analyst should prefer variables that are more easily measured and least collinear with $X$.

**Example (RfQ pricing, continued).** In the causal DAG for the RfQ process (see {ref}`rfq_models`), the back-door paths from dealer spread $\delta$ to hit probability $H$ run through bond features $BF$, client features $CF$, RfQ features $RF$, and volatility $\sigma$ — all of which influence both $\delta$ (through the dealer's pricing policy) and $H$ (through client reservation price and competitor spreads). The minimal valid conditioning set is $\mathcal{Z}_t^{\min} = \{\sigma, RF, BF, CF\}$, giving:

$$P(H \mid \text{do}(\delta), \text{RfQ}) = P(H \mid \delta, \text{RfQ}, \sigma, RF, BF, CF)$$

The do-operator on the left is replaced by a standard conditional probability on the right, which can be estimated by any supervised learning method trained on the correct feature set.

### Do-Calculus

Pearl's **do-calculus** is a complete set of three symbolic inference rules for transforming expressions involving the do-operator into estimable observational quantities. Each rule applies under specific d-separation conditions in modified versions of the graph $\mathcal{G}$:

- $\mathcal{G}_{\overline{X}}$: graph with all arrows *into* $X$ removed.
- $\mathcal{G}_{\underline{X}}$: graph with all arrows *out of* $X$ removed.

**Rule 1 (Insertion/deletion of observations):**
$$P(y \mid \text{do}(x), z, w) = P(y \mid \text{do}(x), w) \quad \text{if } (Y \perp\!\!\!\perp Z \mid X, W)_{\mathcal{G}_{\overline{X}}}$$

**Rule 2 (Action/observation exchange):**
$$P(y \mid \text{do}(x), \text{do}(z), w) = P(y \mid \text{do}(x), z, w) \quad \text{if } (Y \perp\!\!\!\perp Z \mid X, W)_{\mathcal{G}_{\overline{X}\,\underline{Z}}}$$

**Rule 3 (Insertion/deletion of actions):**
$$P(y \mid \text{do}(x), \text{do}(z), w) = P(y \mid \text{do}(x), w) \quad \text{if } (Y \perp\!\!\!\perp Z \mid X, W)_{\mathcal{G}_{\overline{X}\,\overline{Z(W)}}}$$

where $Z(W)$ denotes the set of $Z$-nodes that are not ancestors of any $W$-node in $\mathcal{G}_{\overline{X}}$. These rules are complete: any causal quantity that is expressible in observational data can be derived by a finite sequence of these rules applied to the observational distribution. The back-door adjustment formula is a direct consequence of Rule 2.

## Counterfactuals

Counterfactuals occupy the top rung of the ladder of causation. A counterfactual statement has the form: "Given that unit $u$ was observed to have $X = x'$ and $Y = y'$, what would $Y$ have been if $X$ had been $x$ instead?" This is written $Y_x(u)$ for a specific unit $u$, or $P(Y_x = y \mid X = x', Y = y')$ in the population version.

To evaluate counterfactuals, the SCM framework uses a three-step **abduction-action-prediction** procedure:

1. **Abduction**: Use the observed evidence on unit $u$ to infer the exogenous variables $U$ that are consistent with what was observed. This updates the prior $P(U)$ to the posterior $P(U \mid \text{evidence})$.

2. **Action**: Modify the structural equations by performing the hypothetical intervention: replace the equation for $X$ with $X \leftarrow x$.

3. **Prediction**: Use the modified SCM with the updated exogenous variables to compute the counterfactual outcome $Y_x(u)$.

Counterfactuals are logically stronger than interventional quantities because they condition on individual-level data. An interventional query $P(Y \mid \text{do}(X=x))$ asks "what would happen to a randomly drawn unit if we set $X=x$?", whereas a counterfactual $P(Y_x \mid X=x', Y=y')$ asks "what would have happened to *this specific* unit?" — one for which we already know both the treatment $x'$ and the outcome $y'$. The posterior over $U$ obtained in the abduction step is what allows this individual-level reasoning.

**Example.** A dealer quotes $\delta' = 10$ bps on an RfQ and misses. The counterfactual question is: "Would the client have hit if the dealer had quoted $\delta = 7$ bps?" The abduction step infers the client's reservation spread $\delta_{\text{res}}$ from the observed miss: since the client did not hit at $\delta' = 10$, either $\delta_{\text{res}} < 10$ bps or a competitor quoted more aggressively. This posterior on $\delta_{\text{res}}$ is sharper than the unconditional prior. The action step sets $\delta = 7$ in the structural equation for $RS$. The prediction step computes the probability that $\delta = 7 \leq \delta_{\text{res}}$ and $\delta \leq \delta_{\text{dealer}}$ given the updated posterior on $\delta_{\text{res}}$.

This type of reasoning is central to post-trade attribution and revenue potential analysis in RfQ markets. In practice, counterfactuals are often approximated by simpler interventional quantities; the full counterfactual calculation requires a fully specified SCM including the exogenous noise structure.
