(exercise_solutions)=

# Exercise Solutions

This appendix provides worked solutions to the exercises at the end of each chapter. For derivation exercises the key steps are shown; for computational exercises the numerical answer is given; for conceptual exercises the principal arguments are outlined. Solutions to exercises marked as requiring the accompanying notebooks assume access to the code provided there.

---

## Mechanics of Financial Instruments

**Exercise 1 — Bond pricing and yield.**

(a) Annual coupon $C = 0.03 \times 1000 = 30$. Price at $y=4\%$:

$$P = \frac{30}{1.04} + \frac{30}{1.04^2} + \frac{30}{1.04^3} + \frac{30}{1.04^4} + \frac{1030}{1.04^5} = 955.48$$

(b) At $y = 5\%$: $P' = 28.57 + 27.21 + 25.92 + 24.69 + 887.00 = 913.41$.

(c) Duration approximation (using $D_\text{mod} \approx 4.45$ from Exercise 2): $\Delta P \approx -4.45 \times 955.48 \times 0.01 = -42.52$. Actual change: $913.41 - 955.48 = -42.07$. The approximation captures about 99% of the move; the residual is convexity.

(d) A bond's cash flows are fixed. When yields rise, the present value of each cash flow falls, so the price falls. The longer the duration, the more sensitive the price.

---

**Exercise 2 — Duration and DV01.**

(a) Macaulay duration at $y = 4\%$:

$$D_\text{mac} = \frac{1}{955.48}\left(\frac{1\cdot30}{1.04} + \frac{2\cdot30}{1.04^2} + \frac{3\cdot30}{1.04^3} + \frac{4\cdot30}{1.04^4} + \frac{5\cdot1030}{1.04^5}\right) = \frac{4,252}{955.48} \approx 4.45 \text{ years}$$

(b) $D_\text{mod} = 4.45/1.04 = 4.28$.

(c) $\text{DV01} = D_\text{mod} \times P \times 0.0001 = 4.28 \times 955.48 \times 0.0001 = \$0.409$ per €1,000 face. Approximated price change for $+100$ bp: $-4.08 \times 10 \times 0.01 = -\$40.9$. Actual (Ex.1): $-\$42.1$. Close.

(d) Required offsetting DV01: $10{,}000 \times 0.409 \times 50 / 100 \approx \$2{,}045$ of DV01.

---

**Exercise 3 — Option payoffs and put-call parity.**

(a) $T = 0.25$. Put-call parity: $P = C - S_0 + Ke^{-rT} = 5.20 - 102 + 100 e^{-0.02 \times 0.25} = 5.20 - 102 + 99.50 = 2.70$.

(b) Quoted put $P' = 2.80 > 2.70$: the put is overpriced. Arbitrage: sell the put, sell the bond (borrow $Ke^{-rT}$), buy the call, and buy the stock short. More precisely — sell put, buy call, short stock, invest $Ke^{-rT}$ at the risk-free rate. At $T$: call-put spread replicates the forward and the invested cash repays $K$.

(c) At $S_T = 95$: call expires worthless ($C_T = 0$); put you sold pays out $100 - 95 = 5$; short stock gains $102 - 95 = 7$; bond investment returns $100$. Net: $-5.20 + 2.80 + (102 - 95) - (100 - 99.50) = -5.20 + 2.80 + 7.00 - 0.50 = \$4.10$ profit at time $0$ + riskless position at $T$. The actual arbitrage profit is the initial mis-pricing $2.80 - 2.70 = \$0.10$ per share, risklessly locked in at inception.

---

**Exercise 4 — Forward pricing.**

(a) No-arbitrage forward: $F = (S_0 - D e^{-r t_D}) e^{rT}$ with $t_D = 1/12$, $T = 6/12 = 0.5$.

(b) $F = (50 - 1 \cdot e^{-0.03/12}) e^{0.03 \times 0.5} = (50 - 0.9975) \times 1.01511 = 49.0025 \times 1.01511 = \$49.74$.

(c) $F' = 51 > 49.74$: the forward is overpriced. Cash-and-carry: borrow $S_0 - De^{-rt_D} = 49.00$ today, buy the stock, enter a short forward. At $T=0.5$: receive $F'=51$ from the forward, repay loan $49.00 \times e^{0.03 \times 0.5} = 49.74$. Riskless profit: $51 - 49.74 = \$1.26$ per share.

---

## Market Microstructure

**Exercise 1 — Roll estimator.**

Price changes: $\Delta P = [+0.02, -0.01, -0.03, +0.02]$. Product of consecutive pairs: $(+0.02)(-0.01) = -0.0002$, $(-0.01)(-0.03) = +0.0003$, $(-0.03)(+0.02) = -0.0006$. Mean: $(-0.0002 + 0.0003 - 0.0006)/3 = -0.000167$.

(b) $\hat{s} = 2\sqrt{0.000167} = 2 \times 0.01291 = 0.0258$ (2.58 bps half-spread or 5.2 bps full spread).

(c) The Roll estimator recovers the **transaction cost component** of the spread (the bid-ask bounce). It misses the **information component** (adverse selection cost), which does not generate mean reversion in prices. It fails when: the spread is asymmetric, there is autocorrelation in order flow, or prices trend persistently.

---

**Exercise 2 — Kyle's lambda.**

(a) $\lambda_K = \sigma_v / (2\sigma_u) = 0.5 / (2 \times 1.0) = 0.25$. Informed trader's optimal quantity: $\beta = \sigma_u / \sigma_v = 1.0/0.5 = 2$.

(b) Market maker sets price $P = \lambda_K \cdot q = 0.25 \times 2.0 = 0.50$ above the prior mean.

(c) A larger $\lambda_K$ means the market maker moves the price more aggressively per unit of order flow, reflecting a higher information ratio $\sigma_v/\sigma_u$. This corresponds to a less liquid market with more informed relative to noise trading.

---

**Exercise 3 — LOB impact.**

(a) A buy order of 400 shares fills: 200 at $P_a$, 150 at $P_a + \$0.01$, 50 at $P_a + \$0.02$.

(b) VWAP = $P_a + (0 \times 200 + 0.01 \times 150 + 0.02 \times 50)/400 = P_a + (1.50 + 1.00)/400 = P_a + \$0.00625$.

(c) Refilling within 5 seconds indicates high **resiliency**: the book quickly recovers its depth after a large order, implying competitive market-making and active liquidity provision.

(d) In an RfQ bond market of the same notional, there is no public order book to consume: the dealer quotes a two-way price directly. The transaction cost is the dealer's bid-ask spread, not the slippage through a book. Price impact is borne by the dealer's inventory, not immediately visible pre-trade.

---

**Exercise 4 — Market mechanism comparison.**

| | Electronic CLOB | RfQ (3 dealers) |
|---|---|---|
| Pre-trade transparency | Full book visible | No book; only price from responding dealers |
| Liquidity provider risk | Adverse selection from faster traders | Inventory + information asymmetry from client |
| Normal conditions | Tight spread, instant execution | Competitive quotes, 5–10 bps spread |
| Stressed conditions | Depth evaporates, large slippage | Dealers widen or decline; harder to execute |

The CLOB is preferred for standardised liquid instruments (on-the-run government bonds, equity futures) with many participants. The RfQ protocol is preferred for less liquid instruments (credit, off-the-run govvies) where dealers internalise risk and pre-trade transparency would disadvantage liquidity providers.

---

## Introduction to Bayesian Probability

**Exercise 1 — Beta-binomial conjugate update.**

(a) With prior $\text{Beta}(1,1)$ and $k=14$ heads from $n=20$: posterior is $\text{Beta}(1+14, 1+6) = \text{Beta}(15, 7)$.

(b) Posterior mean: $15/(15+7) = 15/22 \approx 0.682$. MLE: $14/20 = 0.70$. The posterior is shrunk toward 0.5 by the prior.

(c) The 95% credible interval is the 2.5th–97.5th percentile of $\text{Beta}(15,7)$: approximately $[0.46, 0.87]$ (via standard beta quantile).

(d) Starting from $\text{Beta}(15,7)$ and adding $m$ fair tosses, the posterior becomes $\text{Beta}(15 + m/2, 7 + m/2)$ in expectation, with mean $(15 + m/2)/(22 + m)$. Setting this equal to $0.5 + 0.01 = 0.51$ and solving: $(15 + m/2) = 0.51(22 + m)$, giving $15 + m/2 = 11.22 + 0.51m$, so $3.78 = 0.01m$, $m \approx 378$ additional tosses.

---

**Exercise 2 — BLR predictive distribution.**

(a) The posterior is $p(\mathbf{w} \mid \mathcal{D}) = \mathcal{N}(\mathbf{m}_N, \mathbf{S}_N)$ where $\mathbf{S}_N^{-1} = \alpha\mathbf{I} + \beta\boldsymbol{\Phi}^T\boldsymbol{\Phi}$ and $\mathbf{m}_N = \beta\mathbf{S}_N\boldsymbol{\Phi}^T\mathbf{y}$. The predictive mean is $\mu_* = \mathbf{m}_N^T\boldsymbol{\phi}_*$ (linearity of expectation over the Gaussian posterior). The predictive variance $\sigma_*^2 = \beta^{-1} + \boldsymbol{\phi}_*^T\mathbf{S}_N\boldsymbol{\phi}_*$ has two terms: aleatoric noise ($\beta^{-1}$) and epistemic uncertainty about $\mathbf{w}$.

(b) With $\boldsymbol{\Phi} = \begin{pmatrix}1&0.2\\1&0.5\\1&0.8\end{pmatrix}$, $\mathbf{y} = (1.1, 2.3, 2.9)^T$, $\alpha=1$, $\beta=10$:

$\mathbf{S}_N^{-1} = \begin{pmatrix}1&0\\0&1\end{pmatrix} + 10\begin{pmatrix}3&1.5\\1.5&0.93\end{pmatrix} = \begin{pmatrix}31&15\\15&10.3\end{pmatrix}$, so $\mathbf{S}_N \approx \begin{pmatrix}0.0837 & -0.1218\\-0.1218 & 0.2516\end{pmatrix}$.

$\mathbf{m}_N = 10\mathbf{S}_N\begin{pmatrix}6.3\\4.19\end{pmatrix} \approx \begin{pmatrix}0.176\\3.08\end{pmatrix}$.

At $x_* = 0.5$, $\boldsymbol{\phi}_* = (1, 0.5)^T$: $\mu_* = 0.176 + 3.08 \times 0.5 = 1.716$. $\sigma_*^2 = 0.1 + [0.0837 - 2(0.5)(0.1218) + 0.25(0.2516)] = 0.1 + 0.0215 = 0.1215$.

---

**Exercise 3 — d-separation.**

(a) Paths between $B$ and $C$: only one — $B \leftarrow A \rightarrow C$ (a fork at $A$) and $B \rightarrow D \leftarrow C$ (a collider at $D$).

(b) Given $\emptyset$: the fork $B \leftarrow A \rightarrow C$ is open (the common cause $A$ is not conditioned on), so $B$ and $C$ are **not** d-separated. Given $\{A\}$: the fork path $B \leftarrow A \rightarrow C$ is blocked; the collider path $B \rightarrow D \leftarrow C$ remains blocked (not conditioning on $D$). So $B \perp C \mid A$. Given $\{D\}$: the fork path $B \leftarrow A \rightarrow C$ is open; the collider path $B \rightarrow D \leftarrow C$ is now **opened** by conditioning on $D$. So $B$ and $C$ are **not** d-separated given $\{D\}$.

(c) Conditioning on a collider activates the path between its parents, inducing a spurious correlation — the "explaining away" effect. This is counter-intuitive: conditioning on more variables can create dependencies.

---

**Exercise 4 — EM convergence to k-means.**

(a) The responsibility $\gamma_{n,k} \propto \pi_k \exp(-\|\mathbf{x}_n - \boldsymbol{\mu}_k\|^2 / (2\epsilon))$. As $\epsilon \to 0$, the exponential is dominated by the nearest centroid: $\gamma_{n,k^*(n)} \to 1$, $\gamma_{n,k} \to 0$ for $k \neq k^*(n)$.

(b) The M-step centroid update $\boldsymbol{\mu}_k = \sum_n \gamma_{n,k}\mathbf{x}_n / \sum_n \gamma_{n,k}$ becomes, in the hard-assignment limit, $\boldsymbol{\mu}_k = \frac{1}{|C_k|}\sum_{n \in C_k}\mathbf{x}_n$ — exactly the k-means centroid update.

(c) Both k-means and EM for GMMs converge only to local minima of their respective objectives. The initialisation strongly affects the final solution; multiple random restarts are standard practice.

---

## Introduction to Causal Inference

**Exercise 1 — d-separation.**

(a) $A$ to $E$: paths go through $D$ (via $B$ or $C$). All paths from $A$ to $E$ pass through $D$. Conditioning on $D$ blocks the direct chain $A \to \cdots \to D \to E$, but opens the collider at $D$ ($B \to D \leftarrow C$), creating a new path $A \to B \to D \leftarrow C \leftarrow A$. However, this path already goes through $A$ itself. Net result: conditioning on $D$ blocks the $A \to \{B,C\} \to D$ paths since $D$ is a descendant. But $D$ is a collider on the path $B \to D \leftarrow C$. So: conditioning on $D$ opens $B$–$C$ but does not help $A$–$E$. The path $A \to B \to D \to E$ is blocked at $D$ (conditioned on). Similarly $A \to C \to D \to E$. So **yes, $A$ is d-separated from $E$ given $\{D\}$** — all paths from $A$ to $E$ pass through $D$ and are blocked.

(b) Path from $B$ to $C$: $B \leftarrow A \rightarrow C$ (fork at $A$). Conditioning on $A$ blocks this fork. No other path exists (the collider $B \to D \leftarrow C$ is not opened since we do not condition on $D$). **Yes, $B \perp C \mid A$.**

(c) Without conditioning: the fork $B \leftarrow A \rightarrow C$ is active. **$B$ and $C$ are not d-separated given $\emptyset$.**

---

**Exercise 2 — Back-door criterion.**

(a) Back-door paths from $\delta$ to $H$ (entering $\delta$ via a non-descendant): $\delta \leftarrow \sigma \rightarrow H$ and $\delta \leftarrow CF \rightarrow H$.

(b) $\{\sigma, RF, CF\}$ satisfies the back-door criterion: (i) no node in the set is a descendant of $\delta$; (ii) every back-door path ($\delta \leftarrow \sigma \rightarrow H$ and $\delta \leftarrow CF \rightarrow H$) is blocked by the set (both $\sigma$ and $CF$ are in it). $RF$ is included because it directly affects $H$ and controls for additional variation, though strictly only $\{\sigma, CF\}$ is a minimal adjustment set.

(c) $P(H=1 \mid \text{do}(\delta)) = \sum_{\sigma, rf, cf} P(H=1 \mid \delta, \sigma, rf, cf)\, P(\sigma)\, P(rf)\, P(cf)$.

---

**Exercise 3 — Interventional distribution via Rule 2.**

(a) Observational factorisation (Markov condition): $P(X,Y,Z) = P(Z)\,P(X \mid Z)\,P(Y \mid X,Z)$.

(b) Apply Rule 2 with $\mathcal{G}_{\overline{X}\,\underline{X}}$: removing arrows into $X$ gives a graph where $Z$ is d-separated from $Y$ given $X$ along the path through $X$ (since the edge $X \to Y$ remains and $Z \to X$ is removed but $Z \to Y$ remains). Formally, Rule 2 says $P(Y \mid \text{do}(X),Z) = P(Y \mid X,Z)$ when $(Y \perp Z \mid X)_{\mathcal{G}_{\overline{X}}}$ — here the graph with arrows into $X$ removed has $Z \to Y$ and $X \to Y$, and $Z$ is no longer a cause of $X$. Marginalising over $Z$: $P(Y \mid \text{do}(X=x)) = \sum_z P(Y \mid X=x, Z=z)\,P(Z=z)$.

(c) This is exactly the back-door formula with $Z$ as the adjustment set — the unique back-door path $X \leftarrow Z \rightarrow Y$ is blocked by conditioning on $Z$.

---

**Exercise 4 — Counterfactual reasoning.**

(a) $P(H=0 \mid \delta'=8) = P(\delta_\text{res} < 8) = 8/20 = 0.40$.

(b) Abduction: given $H=0$ and $\delta'=8$, we infer $\delta_\text{res} < 8$, i.e., $U < 8/20 = 0.4$. Posterior: $U \mid (H=0, \delta'=8) \sim \text{Uniform}[0, 0.4]$, so $\delta_\text{res} \mid \text{observed miss} \sim \text{Uniform}[0, 8]$.

(c) Action: set $\delta = 5$. Prediction: $P(H_{\delta=5}=1 \mid H=0, \delta'=8) = P(\delta_\text{res} \geq 5 \mid \delta_\text{res} \sim U[0,8]) = 3/8 = 0.375$.

(d) Interventional: $P(H=1 \mid \text{do}(\delta=5)) = P(\delta_\text{res} \geq 5) = 15/20 = 0.75$. The counterfactual (0.375) is lower because it conditions on the fact that this specific client's reservation spread was already revealed to be below 8 bps — a harder-to-win client than average. The interventional ignores this individual-level evidence.

---

## Introduction to Bayesian Probability and Stochastic Calculus

**Stochastic Calculus — Exercise 1 (Crank–Nicolson and inflation targeting).** *(Numerical — see notebook.)*

**Stochastic Calculus — Exercise 2 — Itô's lemma differentials.**

Apply $df = f'(W_t)\,dW_t + \frac{1}{2}f''(W_t)\,dt$ (since $dW_t^2 = dt$):

- $f = W_t^2$: $df = 2W_t\,dW_t + dt$.
- $f = tW_t$: by the product rule $d(tW_t) = t\,dW_t + W_t\,dt$.
- $f = e^{W_t}$: $df = e^{W_t}\,dW_t + \frac{1}{2}e^{W_t}\,dt$.

---

**Stochastic Calculus — Exercise 3 (Brownian motion via GP).** *(Numerical — see notebook.)*

---

**Stochastic Calculus — Exercise 4 — Poisson generating function.**

Multiply the equation $\partial_t P(N_t=n) = -\lambda P(N_t=n) + \lambda P(N_t=n-1)$ by $s^n$ and sum over $n \geq 0$:

$\partial_t G = -\lambda G + \lambda s G = \lambda(s-1)G$.

Solution with $G(0,s) = s^0 = 1$ (start at 0): $G(t,s) = e^{\lambda(s-1)t}$.

Expand: $G(t,s) = e^{-\lambda t}\sum_{n=0}^\infty \frac{(\lambda t s)^n}{n!} = \sum_{n=0}^\infty e^{-\lambda t}\frac{(\lambda t)^n}{n!}s^n$.

Matching coefficients: $P(N_t = n) = e^{-\lambda t}\frac{(\lambda t)^n}{n!}$ — the Poisson distribution.

---

## Stochastic Optimal Control

**Exercise 1 — LQSC for $N=3$, $\lambda=0$.**

Dynamics $x_{k+1} = x_k - u_k$, cost $\sum u_k^2$, terminal cost $A x_3^2$ with $A \to \infty$.

Riccati backward: $P_3 = A \to \infty$. Gain $K_2 = P_3/(1+P_3) \to 1$, $P_2 = P_3(1-K_2) = 0$ — wait: standard LQSC gain $K_k = B^T P_{k+1} B (R + B^T P_{k+1} B)^{-1}$ with $B=1$, $R=1$, $Q=0$:

$K_2 = P_3/(1+P_3) \to 1$; $P_2 = Q + A^T P_3 A - K_2 P_3 = P_3(1 - K_2) \to 0$.
$K_1 = P_2/(1+P_2) = 0$, so $u_1^* = 0$. Similarly $K_0 = 0$. The only non-trivial control is $u_2^* = x_2$ (liquidate everything in the last period), i.e., $u_k^* = x_k/3$ for each $k$ — the equal-slicing TWAP schedule, as required.

---

**Exercise 2 — Euler–Lagrange for general $f(t)$, $g(t)$.**

$\mathcal{L} = \dot{x}^2/f(t) + \lambda g(t) x^2$. Euler–Lagrange: $\frac{d}{dt}\frac{\partial\mathcal{L}}{\partial\dot{x}} - \frac{\partial\mathcal{L}}{\partial x} = 0$ gives $\frac{d}{dt}(2\dot{x}/f) - 2\lambda g x = 0$, or $\ddot{x}/f - \dot{x}\dot{f}/f^2 = \lambda g x$. For $f=\eta$, $g=\sigma^2$ constant: $\ddot{x}/\eta = \lambda\sigma^2 x$, i.e., $\ddot{x} = \kappa^2 x$ with $\kappa^2 = \lambda\sigma^2/\eta$ — the Almgren–Chriss equation.

---

**Exercise 3 — HJB with quadratic value function.**

Postulate $J(t,x) = a(t)x^2 + b(t)$. HJB: $-\partial_t J = \min_u\{u^2 + \partial_x J \cdot u + \frac{1}{2}\sigma^2\partial_{xx}J\}$. Minimise over $u$: $u^* = -\partial_x J/2 = -a(t)x$. Substituting: $-\dot{a}x^2 - \dot{b} = -a^2 x^2 + a\sigma^2$. Matching: $\dot{a} = a^2$, $\dot{b} = -a\sigma^2$, with terminal conditions $a(T) = \lambda$, $b(T)=0$. Solve: $a(t) = \lambda/(1-\lambda(T-t))$; $u^*(t,x) = -a(t)x = -\lambda x/(1-\lambda(T-t))$.

---

**Exercise 4 — Riccati recursion, $N=1$ and $N=2$.**

$A=B=1$, $Q=0$, $R=\eta$, $P_N = A_\text{term}$.

$N=1$: $K_0 = P_1/(P_1+\eta)$; $u_0^* = -K_0 x_0 = -\frac{A_\text{term}}{A_\text{term}+\eta}X$.

$N=2$: $P_1 = P_2 - P_2^2/(P_2+\eta) = \eta P_2/(P_2+\eta)$ where $P_2 = A_\text{term}$; $K_0 = P_1/(P_1+\eta) = A_\text{term}\eta/((A_\text{term}+\eta)(\eta + A_\text{term}\eta/(A_\text{term}+\eta)))$. As $A_\text{term}\to\infty$: $u_0^* = X/2$ (equal split over 2 periods — TWAP).

---

**Exercise 5 — Certainty equivalence.**

In LQSC the optimal gains $K_k$ depend on $P_k$ which satisfies the **deterministic** Riccati recursion — no $\sigma^2$ term enters because the noise $\sigma w_k$ has zero mean and does not affect the minimisation of the quadratic cost. The Bellman equation separates cleanly: $V_k(x) = x^T P_k x + c_k$ where $c_k$ accumulates the noise variance, but $P_k$ and hence $K_k$ are identical to the deterministic problem. This relies on: (i) linearity of dynamics (noise enters additively), (ii) quadratic cost (cross terms vanish under expectation), (iii) Gaussian noise (higher moments don't enter). For $|u_t|$ cost (not differentiable), the certainty equivalence fails because the optimal policy depends on the full distribution of the state.

---

**Exercise 6 — HJB for market making.** *(Conceptual — setup only.)*

State variables: $(t, q_t, S_t)$. Control: $\delta_t$. The HJB equation for $J(t, q, S) = \sup_\delta \mathbb{E}[\int_0^T \delta_t\lambda(\delta_t)dt - \phi q_T^2 \mid q_t=q, S_t=S]$ is:

$$\partial_t J + \frac{\sigma^2}{2}\partial_{SS}J + \sup_\delta\left\{\delta\lambda(\delta) + \lambda(\delta)\left[J(t,q+1,S) - J(t,q,S)\right] + \lambda(\delta)\left[J(t,q-1,S)-J(t,q,S)\right]\right\} = 0$$

with terminal condition $J(T,q,S) = -\phi q^2$. The state space is low-dimensional; standard treatments (Avellaneda-Stoikov) further reduce it by assuming $J(t,q,S) = S q + u(t,q)$ and show that the optimal depth $\delta^*$ depends only on $(t,q)$.

---

## LOB Models

**Exercise 1 — Hawkes stationarity.**

The stationary mean: $\bar{\lambda} = \mu + \phi\bar{\lambda}/\beta$ (since in stationarity $\mathbb{E}[\lambda(t)] = \mu + \phi\mathbb{E}[\int_{-\infty}^t e^{-\beta(t-s)}\lambda(s)ds] = \mu + (\phi/\beta)\bar{\lambda}$). Solving: $\bar{\lambda}(1 - \phi/\beta) = \mu$, giving $\bar{\lambda} = \mu\beta/(\beta-\phi)$. For convergence we need $1 - \phi/\beta > 0$, i.e., $\phi < \beta$.

For $(\mu,\phi,\beta) = (0.5, 1.5, 2.0)$: $\bar{\lambda} = 0.5 \times 2.0/(2.0-1.5) = 2.0$. *(Empirical verification: see notebook.)*

---

**Exercise 2 — Square-root impact.**

$MI = Y\sigma\sqrt{Q/\text{ADV}}$ with $Y=0.7$, $\sigma=1\%$, $\text{ADV}=10^6$:
- $Q=10^3$: $MI = 0.7\times0.01\times\sqrt{10^{-3}} = 0.7\times0.01\times0.0316 = 0.022\%$.
- $Q=10^4$: $MI = 0.7\times0.01\times0.1 = 0.07\%$.
- $Q=10^5$: $MI = 0.7\times0.01\times0.316 = 0.221\%$.

Doubling order size multiplies impact by $\sqrt{2} \approx 1.41$. Trading twice as fast with the same order means executing $Q/2$ twice; total impact is $2 \times Y\sigma\sqrt{Q/(2\text{ADV})} = \sqrt{2}$ times the single-trade impact — the same! The square-root model implies no benefit from splitting a given quantity over faster intervals at the same participation rate.

---

**Exercise 3 — Fill probability MLE.** *(Computational — see notebook.)*

Likelihood of censored exponential: $\ell(A,k) = \sum_{i:\text{filled}} \log(Ae^{-k\delta_i}) - Ae^{-k\delta_i}\tau_i + \sum_{i:\text{censored}} (-Ae^{-k\delta_i}\tau_{\max})$. Gradient ascent or `scipy.optimize` recovers $(A,k)$ close to $(2.0, 1.0)$.

---

**Exercise 4 — Order imbalance predictor.** *(Computational — see notebook.)*

**Exercise 5 — PIN estimation.** *(Computational — see notebook.)*

**Exercise 6 — Agent-based model calibration.** *(Computational — see notebook.)*

---

## RfQ Models

**Exercise 1 — Exchangeability of trade sequences.**

$P(a=1 \mid D=01100, p, \theta)$: the sequence $01100$ has 2 hits in 5 attempts. Writing the likelihood explicitly for each sequence using the informed/uninformed model, the number of buy signals, sell signals, and non-events determines the posterior — not their order. Since both $10100$ and $01100$ contain exactly 2 hits and 3 misses, the posterior $P(a=1 \mid \text{counts}, p, \theta)$ is identical. *(Formal proof: expand the Bayesian update summing over the order-insensitive sufficient statistics.)*

---

**Exercise 2 — Hit probability with causal adjustment.** *(Numerical integration.)*

$f(\delta) = \int_{0.5}^{2.0} \frac{1}{1+e^{-(2-0.3\delta-0.5\sigma)}} \frac{d\sigma}{1.5}$.

Numerical results: $f(1) \approx 0.65$, $f(3) \approx 0.53$, $f(5) \approx 0.39$, $f(8) \approx 0.22$.

Optimal spread: $\delta \cdot f(\delta)$ peaks near $\delta^* \approx 4$–$5$ bps.

Under higher volatility $\sigma \sim U[1.5,4.0]$, the term $-0.5\sigma$ shifts the logistic argument left, reducing $f(\delta)$ for all $\delta$, and the optimal spread widens slightly (higher vol reduces hit probability so the dealer compensates by extracting more per trade).

---

**Exercise 3 — Revenue potential.**

(a) $P(H=0 \mid \delta'=7) = P(\delta_\text{res} < 7) = 7/15 \approx 0.467$ (with $\delta_\text{res} \sim U[0,15]$).

(b) Posterior: $\delta_\text{res} \mid (H=0, \delta'=7) \sim U[0,7]$.

(c) Counterfactual at $\delta^\text{cf}=4$: $P(H_4=1 \mid H=0, \delta'=7) = P(\delta_\text{res} \geq 4 \mid \delta_\text{res} \sim U[0,7]) = 3/7 \approx 0.429$.

(d) Expected revenue of counterfactual: $4 \text{ bps} \times 500{,}000 \times 0.429 / 10{,}000 = \$857$ (where bps of notional = notional/10000). Revenue potential = $\$857$. This differs from the interventional $4 \times f(4) \times 500{,}000/10{,}000$ because the counterfactual conditions on this specific client being harder to win (reservation spread below 7 bps already established), giving a lower probability than the population average $f(4)$.

---

**Exercise 4 — Attrition risk.**

(a) Out of 500 RfQs where the dealer was best-priced: 800 — wait, 420 trades from 500. Of the 80 misses: 60 timed out, 20 traded away. Attrition rate $\hat{p}_\text{att} = 120/500 = 0.24$ (or $60/80 = 0.75$ of missed quotes were attrition). Conditional hit rate given no attrition: $420/(500 - 120) = 420/380 \approx 1.105$ — this is impossible, suggesting the 120 timed-out/cancelled should be excluded from the denominator: $\hat{p}_\text{hit} = 420/(500-120) = 420/380$. Re-reading: 800 hits from 1000 — the problem says 1000 RfQs, 800 hits, 120 timed-out, 80 cancelled. $\hat{p}_\text{att} = (120+80)/1000 = 0.20$. Conditional hit rate: $800/800 = 1.0$ — that can't be right either. The 800 hits + 120 timeout + 80 cancel = 1000. The naive win rate is $800/1000 = 80\%$. The attrition-corrected estimate excludes attrition: $800/(1000-200) = 800/800 = 100\%$. This is an extreme example; in practice attrition does not correlate perfectly with winning, so the attrition-corrected rate is $800/(800 + \text{trades missed to competitors})$, which the data doesn't separate. The key lesson is (b).

(b) A dealer that is consistently the best-priced but still sees misses due to attrition will count those misses in her denominator, underestimating her true competitive hit rate. If response latency is correlated with attrition probability, slow dealers have systematically downward-biased win rates that do not reflect their pricing quality.

(c) Attrition should enter the spread optimisation as a separate term: the effective hit probability is $f(\delta) \cdot (1 - p_\text{att}(\text{latency}))$. A dealer who can reduce latency increases effective $f(\delta)$ without changing the pricing model, enabling tighter competitive spreads.

---

**Exercise 5 — Axe matching.**

(a) Bond A (axe match = 1, buy order reduces short): $s_A = 2(1) - 0.5(3) = 2 - 1.5 = 0.5$. Bond B (axe match = 0, no inventory benefit): $s_B = 2(0) - 0.5(4) = -2$.

(b) Bond A has higher priority. The dealer should respond aggressively to Bond A — even tightening the spread slightly below the market to secure the axe trade, since reducing the short inventory has a risk benefit that offsets the smaller spread.

(c) Axe matching is equivalent to adjusting the reservation spread downward by $\alpha/\beta \times \delta_\text{quoted}$ for trades that reduce inventory risk, or equivalently, adding an inventory-reduction premium to the revenue from the trade. The scoring system makes this adjustment explicit and computable.

---

## Fair Price Estimation

**Exercise 1 — Optimal linear combination.**

For two predictors $\hat{s}_1, \hat{s}_2$ with variances $\sigma_1^2, \sigma_2^2$ and covariance $\sigma_{12}$, the combined predictor $\hat{s} = w\hat{s}_1 + (1-w)\hat{s}_2$ has variance $\text{Var}(\hat{s}) = w^2\sigma_1^2 + (1-w)^2\sigma_2^2 + 2w(1-w)\sigma_{12}$. Minimise over $w$:

$$w^* = \frac{\sigma_2^2 - \sigma_{12}}{\sigma_1^2 + \sigma_2^2 - 2\sigma_{12}}$$

For uncorrelated predictors: $w^* = \sigma_2^2/(\sigma_1^2+\sigma_2^2)$ — the inverse-variance weighting. The correlated case reduces to the same form after projecting out the shared component.

---

**Exercise 2 — BSM via option–option hedging.**

Hedging portfolio $\Pi_t = \Delta_t C_2 + \beta_t$. Self-financing: $d\Pi_t = \Delta_t\,dC_2 + r\beta_t\,dt$. Requiring $\Pi_T = C_1$: apply Itô to $C_1$ and $C_2$ under GBM $dS = rS\,dt + \sigma S\,dW$ and match the Brownian components to eliminate risk:

$\Delta_t = \frac{\partial C_1/\partial S}{\partial C_2/\partial S}$.

The remaining deterministic drift condition yields $r C_i = \frac{\partial C_i}{\partial t} + rS\frac{\partial C_i}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 C_i}{\partial S^2}$ for each $i=1,2$ — the BSM PDE. The connection to the market price of risk: both options have the same underlying, so they must have the same $\lambda_\text{mpr} = (\mu - r)/\sigma$ for the resulting PDE to be internally consistent.

---

**Exercise 3 — Roll estimator and Kalman.**

The autocovariance of first differences $\Delta p_t = p_t - p_{t-1}$ under the random walk with noise model: $p_t = s_t + \epsilon_t$ (mid $+$ noise), $s_t = s_{t-1} + \nu_t$. Then $\Delta p_t = \nu_t + \epsilon_t - \epsilon_{t-1}$, so $\text{Cov}(\Delta p_t, \Delta p_{t-1}) = -\sigma_\epsilon^2$ (only the overlap in $\epsilon_{t-1}$ contributes). Thus $\hat{\sigma}_\epsilon^2 = -\text{Cov}(\Delta p_t, \Delta p_{t-1})$ and the Roll spread $s = 2\hat{\sigma}_\epsilon$ gives $s^2/4 = -\text{Cov}(\Delta p_t, \Delta p_{t-1})$, matching the Roll formula. The Roll estimator assumes: (i) the mid-price is a random walk, (ii) trade direction is serially uncorrelated, (iii) no information asymmetry in the spread. It breaks down when trades are autocorrelated (momentum or mean reversion in order flow) or when informed trading causes the mid to drift persistently after a trade.

---

**Exercise 4 — Vasicek bond pricing.**

(a) Substitute $B(\tau) = (1-e^{-\kappa\tau})/\kappa$ and the corresponding $A(\tau)$ (standard form) into the Riccati ODE system $\dot{B} = 1 - \kappa B$, $\dot{A} = \frac{1}{2}\sigma^2 B^2 - (\kappa\theta - \lambda_0\sigma)B$. Both satisfy the ODEs by direct differentiation.

(b) As $\kappa \to 0$: $B(\tau) \to \tau$, and $A(\tau)/\tau \to -r_t\tau + \frac{\sigma^2\tau^2}{2} - \frac{\sigma^2\tau^3}{6}$. The bond price $P = e^{A-Br_t} \to \exp(-r_t\tau + \frac{\sigma^2\tau^3}{6})$ — matching the Ho-Lee model up to the cubic variance term.

---

**Exercise 5 — Utility indifference price limits.**

For small $\gamma$: the certainty equivalent $C_t$ satisfies $e^{-\gamma C_t} = E_t[e^{-\gamma\Pi_T}]$. As $\gamma\to 0$: expand $e^{-\gamma\Pi_T} \approx 1 - \gamma\Pi_T + O(\gamma^2)$, so $E_t[e^{-\gamma\Pi_T}] \approx 1 - \gamma E_t[\Pi_T]$, and $e^{-\gamma C_t} \approx 1 - \gamma C_t$. Thus $C_t \approx E_t[\Pi_T] = e^{-r(T-t)}E^Q[f(S_T)]$ (the BSM price, since the delta-hedged P&L under BSM is $\Pi_T = f(S_T)$ in expectation under the risk-neutral measure).

For large $\gamma$: $e^{-\gamma\Pi_T}$ is dominated by the worst-case path. $C_t = -\frac{1}{\gamma}\log E_t[e^{-\gamma\Pi_T}] \to e^{-r(T-t)}\inf_{\omega}f(S_T(\omega))$ (the worst-case payoff) by the Laplace principle for large $\gamma$.

---

**Exercise 6 — SDF and CAPM.**

(a) From $E[m R_f] = 1$: $R_f(a - b E[R_M]) = 1$. From $E[m R_M] = 1$: $a E[R_M] - b(E[R_M]^2 + \text{Var}(R_M)) = 1$. Solving the 2×2 system: $b = (E[R_M] - R_f)/(R_f\text{Var}(R_M))$; $a = (1 + bE[R_M])/R_f$.

(b) For asset $i$: $1 = E[mR_i] = aE[R_i] - b(E[R_M]E[R_i] + \text{Cov}(R_i,R_M))$. From $1 = E[mR_f] = aR_f$ and $1 = E[mR_M]$: $E[R_i] - R_f = b\text{Cov}(R_i,R_M)/a \cdot a = b\text{Cov}(R_i,R_M) \cdot R_f$... more cleanly: $E[R_i] - R_f = \frac{\text{Cov}(R_i,m)}{\text{Cov}(R_M,m)}(E[R_M]-R_f) = \beta_i(E[R_M]-R_f)$.

(c) For $m = a - bR_M$ to be a valid SDF it must be strictly positive: $a > bR_M$ for all realisations of $R_M$. Since $R_M$ can in principle be unbounded, this requires truncating the market return distribution or accepting approximate validity.

---

**Exercise 7 — Put-call parity from SDF.**

(a) $(S_T - K)^+ - (K-S_T)^+ = S_T - K$ identically (signed payoff of a forward). Taking SDF expectations:

$C_t - P_t = E_t[m_{t,T}(S_T-K)^+] - E_t[m_{t,T}(K-S_T)^+] = E_t[m_{t,T}(S_T-K)] = S_t - K\cdot E_t[m_{t,T}] = S_t - KP(t,T)$.

(b) The essential property is linearity of the pricing functional $E_t[m_{t,T}\cdot]$ — the SDF must price all assets consistently (law of one price).

(c) Put-call parity holds in any incomplete market as long as both the call and put can be priced by the same SDF. Even when markets are incomplete (multiple EMMs), put-call parity is a model-free no-arbitrage condition requiring only the existence of a replicating strategy for the forward — not the option itself.

---

**Exercise 8 — Kalman steady state.**

In steady state $K_t = K$ constant. The Kalman update: $\hat{s}_t = \hat{s}_{t-1|t-1} + K(p_t - \hat{s}_{t-1|t-1}) = (1-K)\hat{s}_{t-1} + Kp_t$ — an EWMA with smoothing constant $K$. The Kalman gain $K = \sigma_\nu^2/(\sigma_\nu^2 + \sigma_\epsilon^2)$. Equal weighting $K = 1/2$ requires $\sigma_\epsilon^2 = \sigma_\nu^2$.

---

## Liquidity Modelling

**Exercise 1 — Roll estimator on simulated data.** *(Computational — see notebook.)*

**Exercise 2 — Amihud ratio.** *(Computational — see notebook.)*

**Exercise 3 — Composite liquidity scores.** *(Computational — see notebook.)*

**Exercise 4 — Inventory rotation time.**

$\tau_{1/2}$ decreases with higher arrival rate $A$ (faster turnover), larger average size $\bar{x}$ (each trade reduces more inventory), and higher $p_0$ (proportion of two-way flow). It increases with higher volatility $\sigma$ (wider quotes needed) and lower $\alpha$ (steeper fill-probability curve, fewer fills per unit time). An on-the-run sovereign bond has high $A$, large $\bar{x}$, low $\sigma$ → short $\tau_{1/2}$. An off-the-run corporate has low $A$, small $\bar{x}$, high $\sigma$ → long $\tau_{1/2}$ and material inventory carrying cost.

**Exercise 5 — Intraday Amihud pattern.** *(Computational — see notebook.)*

---

## Execution Fundamentals

**Exercise 1 — Square-root impact and TWAP.**

Single market order: $MI = Y\sigma\sqrt{Q/\text{ADV}} = 1 \times 0.015\sqrt{500{,}000/2{,}000{,}000} = 0.015 \times 0.5 = 0.75\%$.

TWAP (12 slices of $Q/12$): impact per slice $= 0.015\sqrt{(500{,}000/12)/2{,}000{,}000} = 0.015/\sqrt{12} = 0.00433\%$. Total expected temporary impact: $12 \times 0.00433\% = 0.0520\%$. TWAP reduces expected impact by a factor of $1/\sqrt{N} = 1/\sqrt{12} \approx 0.29$ but introduces timing risk.

---

**Exercise 2 — IS and VWAP cost.**

Arrival mid: €50.00. VWAP\textsubscript{exec}: €50.15. VWAP\textsubscript{market}: €50.10. Fees: €500 on 100,000 shares = €0.005/share = 1 bp.

IS cost = (50.15 − 50.00)/50.00 × 10,000 bps + 1 bp = 30 bp + 1 bp = **31 bp**.
VWAP cost = (50.15 − 50.10)/50.10 × 10,000 = **9.98 bp** vs market VWAP.
IS P&L = −31 bp (cost to the buyer).

---

**Exercise 3 — Trader's dilemma.** *(Conceptual.)*

Reducing timing risk requires executing faster (higher participation rate), which increases market impact. Reducing market impact requires executing slower, which increases exposure to adverse price drift. The two objectives are in tension because they require opposite adjustments to the trading rate. The efficient frontier makes this tradeoff explicit: every point minimises risk for a given expected cost. The frontier degenerates to a single point only if the market impact function is linear and the timing risk is zero (no price uncertainty), which never holds in practice.

---

**Exercise 4 — Broker guaranteed VWAP.** *(Conceptual.)*

The broker prices the guarantee by modelling its own expected VWAP performance distribution. The "+5 bps" represents a margin above the broker's internal expected execution cost that covers: (i) the expected tracking error, (ii) a risk premium for adverse market moves, and (iii) the broker's profit margin. The broker bears **replication risk**: if market conditions deteriorate and it cannot achieve its internal VWAP estimate, it absorbs the loss.

---

**Exercise 5 — PoV strategy.**

In the first 5 minutes: $0.10 \times 50{,}000 = 5{,}000$ shares executed. For completion: need $500{,}000$ total shares. At $\rho = 10\%$ participation and total market volume $= 3{,}000{,}000$: algorithm executes $0.10 \times 3{,}000{,}000 = 300{,}000 < 500{,}000$ shares. The order is **not completed**: residual = 200,000 shares. Opportunity cost in IS: the unexecuted residual is valued at the final market price minus the arrival price, representing the cost of failing to trade.

---

**Exercise 6 — VWAP self-referential issue.** *(Conceptual.)*

When an algorithm is large relative to market volume, its own trades inflate the VWAP it is measured against. By trading more aggressively, it raises the benchmark, paradoxically improving its measured performance without reducing its true cost. This constitutes potential market manipulation (painting the tape or benchmark gaming) and is prohibited under MiFID II and equivalent frameworks.

---

## Optimal Execution

**Exercise 1 — IS derivation.**

Price model $dS_t = \sigma\,dW_t - \gamma v_t\,dt$, execution price $P_t = S_t - \eta v_t$. Cash proceeds from selling: $\int_0^T P_t v_t\,dt = \int_0^T (S_t - \eta v_t)v_t\,dt$. IS = $S_0 X - \int_0^T P_t v_t\,dt$. Substituting $S_t = S_0 - \gamma\int_0^t v_s\,ds + \sigma W_t$: $\mathbb{E}[IS] = \eta\int v_t^2\,dt + \gamma X\int_0^T v_t\int_0^t v_s\,ds\,dt$. The second term: integration by parts on $\int_0^T v_t\int_0^t v_s\,ds\,dt = \frac{1}{2}(\int_0^T v_t\,dt)^2 = X^2/2$. Hence $\mathbb{E}[IS] = \eta\int v_t^2\,dt + \frac{\gamma X^2}{2}$.

---

**Exercise 2 — IS variance.**

$\text{Var}[IS] = \sigma^2\text{Var}[\int_0^T v_t W_t\,dt] = \sigma^2\int_0^T\left(\int_t^T v_s\,ds\right)^2 dt = \sigma^2\int_0^T x_t^2\,dt$ where $x_t = \int_t^T v_s\,ds$ is the remaining inventory. The last equality uses Itô isometry after integration by parts: $\int_0^T v_t W_t\,dt = -\int_0^T x_t\,dW_t$.

---

**Exercise 3 — Almgren–Chriss trajectory.**

ODE $\ddot{x} = \kappa^2 x$ has general solution $x_t = Ae^{\kappa t} + Be^{-\kappa t}$. Boundary conditions $x_0 = X$, $x_T = 0$: $A + B = X$, $Ae^{\kappa T} + Be^{-\kappa T} = 0$. Solving: $x_t^* = X\sinh(\kappa(T-t))/\sinh(\kappa T)$. Verify: $x_0^* = X\sinh(\kappa T)/\sinh(\kappa T) = X$ ✓; $x_T^* = X\sinh(0)/\sinh(\kappa T) = 0$ ✓.

---

**Exercise 4 — Numerical AC computation.**

$\sigma=0.02$, $\eta=10^{-5}$, $\lambda=10^{-4}$, $T=1$ day, $X=10^6$.

$\kappa = \sqrt{\lambda\sigma^2/\eta} = \sqrt{10^{-4}\times4\times10^{-4}/10^{-5}} = \sqrt{4\times10^{-3}} = 0.0632$ day$^{-1}$.

$\kappa T = 0.0632$. Since $\kappa T$ is small, the trajectory is nearly linear (close to TWAP).

Initial rate $v_0 = \kappa X\cosh(\kappa T)/\sinh(\kappa T) = \kappa X/\tanh(\kappa T) \approx X/T \times (1 + (\kappa T)^2/3)$ — only ~0.13% faster than TWAP.

First quarter ($t = T/4$): $x_{T/4}^* = X\sinh(3\kappa T/4)/\sinh(\kappa T) \approx 75\%X$ — very close to the TWAP fraction.

---

**Exercise 5 — TWAP limit of IS.**

As $\kappa \to 0$: $\sinh(\kappa t)\approx\kappa t$, $v_t^* = \kappa X\cosh(\kappa(T-t))/\sinh(\kappa T) \to X/T$. Then $\eta\int_0^T v_t^2\,dt \to \eta X^2/T$ and $\sigma^2\int_0^T x_t^2\,dt \to \sigma^2 X^2 T/3$. Expected cost $\to \gamma X^2/2 + \eta X^2/T$: the permanent impact is constant (path-independent); the temporary impact falls as $T$ grows (slower execution is cheaper). Variance $\to \sigma^2 X^2 T/3$: grows with $T$ because more time means more exposure to random price drift.

---

**Exercise 6 — Dynamic VWAP reduces to static.**

With $V_n = 0$, $Q_n = 0$, $\mathbb{E}_n[\cdot] = \mathbb{E}_0[\cdot]$: $q_n^* = \Pi(0 + \mathbb{E}_0[v_n])/\mathbb{E}_0[V_M] - 0 = \Pi\mathbb{E}_0[v_n]/\mathbb{E}_0[V_M] = q_n^\text{static}$. ✓

---

**Exercise 7 — Two-asset portfolio eigenmodes.**

$K^2 = \lambda H^{-1}\Sigma$ with $H = \eta I$, $\Sigma = \sigma^2\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}$. $K^2 = (\lambda\sigma^2/\eta)\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}$. Eigenvalues: $\kappa_{\pm}^2 = (\lambda\sigma^2/\eta)(1\pm\rho)$. Eigenvectors: $(1,1)^T/\sqrt{2}$ (sum) and $(1,-1)^T/\sqrt{2}$ (difference). The sum mode has $\kappa_+^2 > \kappa_-^2$ (for $\rho > 0$), so it is **more aggressive**: correlated assets must be traded faster together to control correlated risk. The difference (spread) mode has lower risk and can be executed more slowly.

---

## Execution Tactics

**Exercise 1 — CARA HJB solution verification.**

Define $C_\gamma = \frac{A}{k+\gamma}\!\left(\frac{k}{k+\gamma}\right)^{k/\gamma}$. The reduced ODE for $q=1$ is $\partial_\tau H = C_\gamma e^{-kH}$ (since $\Delta H = H(\tau,1)$).

Substitute $H(\tau,1) = k^{-1}\ln(e^{-kb} + kC_\gamma\tau)$:

$\partial_\tau H = \frac{kC_\gamma}{k(e^{-kb}+kC_\gamma\tau)} = \frac{C_\gamma}{e^{-kb}+kC_\gamma\tau}$.

$C_\gamma e^{-kH} = C_\gamma\cdot(e^{-kb}+kC_\gamma\tau)^{-1}$. These match ✓.

Initial condition: $H(0,1) = k^{-1}\ln(e^{-kb}) = -b$ ✓.

**Risk-neutral limit.** As $\gamma\to 0$: $C_\gamma \to \frac{A}{k}\cdot e^{(k/\gamma)\ln(k/(k+\gamma))} = \frac{A}{k}\cdot e^{-1} = A/(ek)$ (using $\lim_{\gamma\to 0}\frac{k}{\gamma}\ln(1-\gamma/(k+\gamma)) = -1$). Substituting: $H\to k^{-1}\ln(e^{-kb}+A\tau/e)$, the risk-neutral solution ✓.

**Limits.** $\tau\to 0$: $H\to -b$, so $\delta^*(0,1) = \frac{1}{\gamma}\ln(1+\gamma/k) - b$. This is a market order when $b > \frac{1}{\gamma}\ln(1+\gamma/k)$; since the right-hand side is decreasing in $\gamma$, high risk aversion makes market orders more likely at deadline. $\tau\to\infty$: $H\to\infty$ and $\delta^*\to\infty$ — with unlimited time, even a risk-averse agent posts very passively.

---

**Exercise 2 — Urgency monotone in inventory.**

(a) $\delta^*(t,q) = \frac{1}{\gamma}\ln(1+\gamma/k) + \Delta H(t,q)$ with $\Delta H(t,q) = H(t,q)-H(t,q-1)$. Since $H(t,q)$ is concave in $q$ (the certainty equivalent is a decreasing, concave function of inventory), $\Delta H(t,q) \leq \Delta H(t,q-1)$, i.e., $\delta^*(t,q) \leq \delta^*(t,q-1)$. The risk-comfort depth $\frac{1}{\gamma}\ln(1+\gamma/k)$ is inventory-independent, so the monotonicity follows entirely from the monotonicity of $\Delta H$.

(b) As $t$ increases (time runs out, $\tau = T-t$ decreases), the urgency penalty intensifies: $H(t,q)$ becomes more negative and $\Delta H$ becomes more negative. Hence $\delta^*(t,q)$ decreases — the tactic posts shallower as deadline approaches. At the limit $\tau\to 0$: $\delta^*(0,q) = \frac{1}{\gamma}\ln(1+\gamma/k) - b < 0$ for $b$ large enough, triggering a market order.

---

**Exercise 3 — Two-venue SOR under CARA utility.**

(a) The CARA FOC for each venue gives $\delta_k^* = \frac{1}{\gamma}\ln(1+\gamma/k_k) + \Delta H$. With $A_1=2$, $k_1=0.5$, $A_2=0.5$, $k_2=2.0$, and risk aversion $\gamma$ fixed:

$\delta_1^* = \frac{1}{\gamma}\ln(1+2\gamma) + \Delta H$; $\quad\delta_2^* = \frac{1}{\gamma}\ln(1+\gamma/2) + \Delta H$.

The liquid venue (small $k_1=0.5$) attracts a deeper passive placement; the illiquid venue (large $k_2=2.0$) is approached more aggressively.

(b) For $\Delta H = -1$ and $\gamma = 2$: $\delta_1^* = \frac{1}{2}\ln(5) + (-1) = 0.805 - 1 = -0.195$ (market order); $\delta_2^* = \frac{1}{2}\ln(2) - 1 = 0.347 - 1 = -0.653$ (aggressive market order). Both venues attract market orders at this urgency level. Fill rates at $\delta_k^*=0$ (constrained): $\lambda_1(0) = 2$, $\lambda_2(0) = 0.5$; total $= 2.5$/min. On venue 1 alone: $\lambda_1(0) = 2$/min.

(c) The SOR uses the illiquid venue as a marginal fill source: even at the constrained depth, it contributes 0.5 fills/min additional. This exploits the separability of the CARA HJB — each venue's contribution is independent — and reduces the expected residual inventory at deadline, which is particularly valuable to a risk-averse agent.

---

**Exercise 4 — Pegged-to-mid order.**

Proceeds relative to mid at posting: $\mathbb{E}[\text{proceeds} - S_\text{mid,post}] = \mathbb{E}[\delta_t] = \delta$ where $\delta$ is the fixed peg offset. The fill occurs at $S_t + \delta$ regardless of where $S_t$ moved, so the expected spread captured is always $\delta$. Price volatility $\sigma$ does not affect expected proceeds because the limit price tracks the mid — the trader captures exactly the peg. This breaks down when: fills occur via trade-through (the mid jumps discontinuously past the limit), when there is significant adverse selection in who fills the order, or when the mid-price has a systematic drift that is correlated with the arrival of fill-generating orders.

---

**Exercise 5 — RL convergence and DQN.**

(a) Tabular Q-learning converges under: (i) all state-action pairs visited infinitely often, (ii) step sizes $\alpha_n \to 0$ with $\sum\alpha_n = \infty$, $\sum\alpha_n^2 < \infty$. These ensure the Robbins-Monro conditions are met and the contraction mapping of the Bellman operator drives $Q$ to $Q^*$.

(b) With function approximation, the Bellman target $r + \gamma\max_{a'}Q_\theta(s',a')$ depends on $\theta$ itself, making the update a semi-gradient rather than a true gradient of a fixed loss. This introduces a "moving target" that can cause divergence. Two stabilisation techniques: (i) **experience replay** breaks correlations between consecutive transitions by sampling from a buffer; (ii) **target network** uses a periodically updated copy $Q_{\theta^-}$ for the Bellman targets, making them locally stationary.

---

**Exercise 6 — Iceberg order trade-off.**

Visible limit: fill rate $\lambda = 0.5$ fills/min for 1000 shares. Expected fills in 30 min: $0.5 \times 30 = 15$ fills. Each fill = 1 unit (assume fills of 1 unit for comparability). If each fill is for 1000/N units this doesn't quite parse — assume each fill event fills 1 lot. Total expected lots: 15.

Iceberg (tip = 100 shares, $\lambda = 0.5$ fills/min per tip): each refill incurs 5/60 min = 0.0833 min delay. Expected fills per cycle = $\lambda \times (1/(1/\lambda + 0.0833)) \cdot \text{time}$. Effective rate: $1/(1/0.5 + 0.0833) = 1/2.0833 = 0.480$ fills/min. Expected fills in 30 min: $0.480 \times 30 = 14.4$ lots — slightly fewer than the visible order due to queue re-entry delays.

Optimal tip minimises total time = $Q/({\rm fill\_rate}(q_{\rm tip}))$ where ${\rm fill\_rate} = \lambda/(1 + \lambda \times {\rm delay/q_{\rm tip}})$. Taking derivative gives $q_{\rm tip}^* = \sqrt{Q \times {\rm delay} \times \lambda}$ as a rough estimate; for $Q=1000$, delay$=5/60$, $\lambda=0.5$: $q^*_{\rm tip} \approx \sqrt{1000 \times 0.0833 \times 0.5} \approx 6.5$ shares, suggesting very small tips maximise fill rate (fill more frequently, minimize delay penalty per unit).

---

## Market Making Fundamentals

**Exercise 1 — Grossman-Miller spread.**

$S_\text{GM} = \frac{\gamma\sigma^2 i}{n+1}$ where $n=4$ competing MMs, $i=100$ units, $\sigma=2\% = 0.02$, $\gamma=10$.

$S = 10 \times (0.02)^2 \times 100 / 5 = 10 \times 0.0004 \times 100/5 = 0.08$. If $n=3$: $S = 0.08 \times 5/4 = 0.10$ (spreads widen with fewer MMs). If $\sigma$ doubles to $4\%$: $S$ quadruples to $0.32$ (spreads increase with $\sigma^2$).

---

**Exercise 2 — Glosten-Milgrom spread.**

$V_H=102$, $V_L=98$, $p=0.5$, $\alpha=0.2$. Prior $\mu = 0.5\times102 + 0.5\times98 = 100$.

Ask: $a = \mu + \alpha(V_H - \mu) = 100 + 0.2\times2 = 100.4$.
Bid: $b = \mu - \alpha(\mu - V_L) = 100 - 0.2\times2 = 99.6$.
Spread: $a - b = 0.8 = \alpha(V_H - V_L) = 0.2 \times 4$.

With $\alpha=0.4$: spread $= 0.4 \times 4 = 1.6$. Adverse selection drives wider spreads.

---

**Exercise 3 — Inventory and skew.**

Executed 50 sells at ask (€100.2) and 30 buys at bid (€99.8). Net inventory: $-50 + 30 = -20$ (short 20 units). P&L from trading: $50 \times 0.2 + 30 \times 0.2 = \$16$ in spread income. If fair price moves to 99.9: unrealized P&L on short position = $+20 \times (100.0 - 99.9) = +\$2$ (price moved in favor of short). To reduce short inventory, skew bids upward (bid 99.9 instead of 99.8) to attract more sell orders from clients.

---

**Exercise 4 — Toxic flow diagnosis.** *(Conceptual.)*

Consistently negative flow value for one client indicates **adverse selection**: the client systematically trades against the market maker when the market subsequently moves in the client's direction. Possible cause: the client has superior information. Remediation: increase the spread for that client (client-specific pricing), apply a toxicity-driven skew that widens when pre-trade indicators (OI, recent price trend) align with the client's direction, or in extreme cases, decline to quote (quote withdrawal).

---

**Exercise 5 — Hedging vs skewing.** *(Conceptual.)*

**Hedging in the market**: the MM immediately trades in the interdealer market to offset the inventory position acquired from the client. Advantages: eliminates inventory risk immediately. Disadvantages: consumes bid-ask spread in the hedge market, may signal the client's direction and move prices adversely (information leakage). Better suited to: large positions, illiquid instruments with slow client flow, high-volatility environments.

**Skewing quotes**: the MM adjusts her bid-ask quotes to attract offsetting client flow. Advantages: monetises the inventory through the spread without incurring hedge market costs. Disadvantages: offsetting flow may take time, leaving residual risk; if the market moves before offset, losses exceed spread income. Better suited to: liquid instruments with active two-way client flow, tight hedge markets with visible adverse selection.

---

## Optimal Market Making

**Exercise 1 — GM full derivation.**

$p=0.5$, $n=3$, $\sigma_\text{intra} = 0.015$, $i=200$, $\gamma=5$.

Equilibrium bid: $b = \mu - \frac{\gamma\sigma_\text{intra}^2 i}{n+1} = \mu - \frac{5\times(0.015)^2\times200}{4} = \mu - \frac{5\times0.000225\times200}{4} = \mu - 0.05625$.

Spread: $S = 2\times0.05625 = 0.1125$.

$n=4$: $S = 2\times\frac{5\times0.000225\times200}{5} = 0.09$. Spread narrows with competition.

$n\to\infty$: $S\to0$ — perfectly competitive market.

---

**Exercise 2 — GL asymmetric case.**

$p=0.7$, $V_H=105$, $V_L=95$, $\alpha=0.3$. $\mu = 0.7\times105 + 0.3\times95 = 73.5 + 28.5 = 102$.

Zero-profit ask: informed buys at H with prob $\alpha p=0.21$; uninformed buys at rate $0.5(1-\alpha)=0.35$. Ask must satisfy: $\alpha p(V_H - a) + 0.5(1-\alpha)(\mu - a) = 0$, so $a(\alpha p + 0.5(1-\alpha)) = \alpha p V_H + 0.5(1-\alpha)\mu$. $a = (0.21\times105 + 0.35\times102)/(0.21+0.35) = (22.05 + 35.7)/0.56 = 57.75/0.56 = 103.13$.

Symmetrically: $b = (0.21\times95 + 0.35\times102)/0.56 = (19.95+35.7)/0.56 = 99.38$.

Spread: $103.13 - 99.38 = 3.75$. For $p=0.5$: spread $= \alpha(V_H-V_L) = 0.3\times10 = 3.0$. The asymmetric case widens the spread because $p>0.5$ increases the risk on the ask side.

---

**Exercise 3 — Multi-asset skew.**

Single-trade expected cost for the dealer holding inventory $\mathbf{q}_0 = (10,-5)^T$ before the trade, and quoting to buy $\bar{q}=8$ EUR bonds (becoming $q_\text{new}^1 = 18$):

$\delta^{1*} = \frac{\gamma}{2}\tau(\mathbf{q}_\text{new}^T\boldsymbol{\Gamma}\mathbf{q}_\text{new} - \mathbf{q}_0^T\boldsymbol{\Gamma}\mathbf{q}_0)/\bar{q} + \frac{1}{k} + \Delta\ell/\bar{q}$.

$\mathbf{q}_0^T\boldsymbol{\Gamma}\mathbf{q}_0 = 10^{-4}(4\times100 + 2\times2\times10\times(-5) + 3\times25) = 10^{-4}(400-200+75) = 0.0275$.

$\mathbf{q}_\text{new}^T\boldsymbol{\Gamma}\mathbf{q}_\text{new}= 10^{-4}(4\times324 + 2\times2\times18\times(-5)+3\times25) = 10^{-4}(1296-360+75) = 0.1011$.

$\delta^{1*} = \frac{10}{2}\times0.5\times(0.1011-0.0275)/8 + 1/20 + 0.002 = 5\times0.5\times0.0736/8 + 0.052 = 0.023 + 0.052 = 0.075$ (normalised units). The negative USD inventory reduces the incremental risk (negative cross-term helps the hedge), so $\delta^*$ is lower than the clean-book case.

---

**Exercise 4 — AS optimal spreads.**

(a) $\eta = \frac{1}{\gamma}\ln(1+\gamma/k) = \frac{1}{0.1}\ln(1+0.1/1.5) = 10\ln(1.0667) = 10\times0.0645 = 0.645$ (in spread units).

(b) GLF quadratic approximation: $\theta = \frac{1}{2}\gamma k\sigma^2(T-t) = \frac{1}{2}\times0.1\times1.5\times(0.01)^2\times1800 = 0.0135$.

For $q=5$: bid $\delta^b \approx \eta - \theta q = 0.645 - 0.0135\times5 = 0.645 - 0.0675 = 0.578$; ask $\delta^a \approx \eta + \theta q = 0.645 + 0.0675 = 0.713$. Skew: tighter bid (buy more urgently), wider ask — consistent with positive inventory.

---

**Exercise 5 — GLF sensitivities.**

(a) $\eta = \frac{1}{0.2}\ln(1 + 0.2/1.0) = 5\ln(1.2) = 0.912$. $\theta = \frac{1}{2}\times0.2\times1.0\times(0.012)^2\times T$. Without $T$ specified, $\theta \propto \sigma^2$.

(b) $\sigma\to 0.024$: $\eta$ unchanged (doesn't depend on $\sigma$). $\theta$ doubles ($\propto \sigma^2$) — skew becomes more aggressive.

(c) $A\to 3.0$: $\theta = \frac{\gamma\sigma^2}{2k}\frac{k}{A}$ (in the GLF formula $\theta$ decreases with $A$) — higher arrival rate means inventory turns over faster, reducing the incentive to skew. Economically: with more client flow, the MM can rebalance inventory through client trades rather than forcing an aggressive skew.

---

**Exercise 6 — Client segmentation.**

(a) $\gamma_A = 0.1 + 0.05\times3 = 0.25$; $\gamma_B = 0.1 + 0.4\times1 = 0.5$.

(b) $\eta_A = \frac{1}{\gamma_A}\ln(1+\gamma_A/k_A) = 4\ln(1 + 0.25/3) = 4\ln(1.0833) = 0.320$. $\eta_B = 2\ln(1 + 0.5/1) = 2\ln(1.5) = 0.811$.

(c) With a large long position: the MM skews bids downward and asks upward uniformly. Uninformed retail clients (class A) are more useful for inventory rebalancing because their trades are random and uncorrelated with the MM's inventory risk — the MM can offer them tighter prices to attract offsetting flow. Fund managers (class B) have high $\alpha_B$, so trading with them is expensive (high effective $\gamma_B$), and the MM will prefer to widen the spread or decline.

---

## Optimal Hedging

**Exercise 1 — Projection and basis risk.**

The minimum variance hedge $\mathbf{h}^* = q\boldsymbol{\Sigma}_{HH}^{-1}\boldsymbol{\sigma}_{XH}$ minimises $\text{Var}(\Delta X - \mathbf{h}^T\Delta\mathbf{H})$. In $L^2(\Omega)$ with inner product $\text{Cov}$: this is the orthogonal projection of $\Delta X$ onto the span of $\{\Delta H_1, \ldots, \Delta H_m\}$. The residual $\Delta X - (\mathbf{h}^*)^T\Delta\mathbf{H}$ is orthogonal to all $\Delta H_k$ (i.e., uncorrelated). Basis risk is the variance of this residual — the component of $\Delta X$ that cannot be explained by any linear combination of the hedge instruments.

---

**Exercise 2 — PCA hedge for 7-year bond.** *(Requires yield curve PCA data from notebook.)*

**Exercise 3 — Lasso hedge equivalence.**

Substitute $\tilde{\mathbf{h}} = \boldsymbol{\Sigma}_{HH}^{1/2}\mathbf{h}$ and $\tilde{\mathbf{y}} = q\boldsymbol{\Sigma}_{HH}^{-1/2}\boldsymbol{\sigma}_{XH}$:

$\min_{\mathbf{h}} \frac{1}{2}\mathbf{h}^T\boldsymbol{\Sigma}_{HH}\mathbf{h} - q\mathbf{h}^T\boldsymbol{\sigma}_{XH} + \lambda\|\mathbf{h}\|_1 = \min_{\tilde{\mathbf{h}}} \frac{1}{2}\|\tilde{\mathbf{h}} - \tilde{\mathbf{y}}\|^2 + \lambda\|\boldsymbol{\Sigma}_{HH}^{-1/2}\tilde{\mathbf{h}}\|_1$.

For diagonal $\boldsymbol{\Sigma}_{HH}$, this is a standard Lasso with design matrix $\boldsymbol{\Sigma}_{HH}^{1/2}$ and response $\tilde{\mathbf{y}}$. The regularisation path algorithm is LARS (Least Angle Regression).

---

**Exercise 4 — Delta hedging with transaction costs.**

(a) Daily hedging error: $\epsilon = \frac{1}{2}\Gamma\sigma^2 S^2\,dt = \frac{1}{2}\times0.05\times(0.20)^2\times(100)^2\times(1/252) \approx 3.97$.

(b) Whalley–Wilmott no-trade band width: $H_t = \left(\frac{3c\Gamma^2 S^2}{2\gamma}\right)^{1/3}$ where $c=0.001\times S=0.1$ per unit. $H_t = (3\times0.1\times(0.05)^2\times10000/(2\times0.01))^{1/3} = (3\times0.1\times0.0025\times10000/0.02)^{1/3} = (375)^{1/3} = 7.21$ shares.

(c) As expiry approaches, $\Gamma$ rises sharply for at-the-money options, narrowing $H_t \propto \Gamma^{-2/3}$ and forcing more frequent rehedging. Deep in or out of the money, $\Gamma\to0$ and the band widens to infinity (no rehedging needed).

---

**Exercise 5 — Deep hedging BSM optimality.**

Under GBM, the BSM delta $\pi^* = N(d_1)$ achieves perfect replication: $Z^{\boldsymbol{\delta}} = V_T - P_T = 0$ a.s. Thus the variance of the hedging P&L is zero, which is trivially the global minimum of the variance objective. No other strategy can do better than zero variance. In the deep hedging framework without transaction costs, the network recovers $N(d_1)$ in the GBM case by learning the exact replication strategy.

---

**Exercise 6 — Skew-versus-hedge band.**

From {cite:t}`barzykin2023skewhedge`, the threshold $q^*$ above which the dealer hedges (rather than skewing) scales as $q^* \propto c/\sigma^2$ for unit hedging cost $c$ and volatility $\sigma$. Increasing $c$ raises the threshold linearly: more expensive hedging leads the dealer to tolerate larger inventory positions before hedging. For arrival rate $A$: client flow is more likely to rebalance the book organically when $A$ is large, so $q^* \propto A^{-1/2}$ — the dealer can afford a larger skew band before the stochastic arrival of offsetting flow becomes too slow.

---

## Data-Driven Methods

**Exercise 1 — Bias–variance.** *(Conceptual + sketch.)*

As $M$ increases: bias decreases (the model is more flexible and can approximate $f^*$ better); variance increases (small changes in training data lead to very different fitted polynomials). At $M = N-1$, training error $\to 0$ (interpolating polynomial) but test error typically peaks due to overfitting. This is the classic bias-variance tradeoff.

---

**Exercise 2 — Ridge via SVD.**

OLS predictor: $\hat{f}(\mathbf{x}) = \sum_j (\mathbf{u}_j^T\mathbf{y})\mathbf{v}_j^T\boldsymbol{\phi}(\mathbf{x})$ (unweighted). Ridge adds penalty $\lambda\|\mathbf{w}\|^2$; the solution in the SVD basis shrinks each component by $s_j^2/(s_j^2+\lambda)$. Directions with small singular values (near-zero $s_j$) are shrunk toward zero — ridge regularisation stabilises the fit by discarding near-collinear directions.

---

**Exercise 3 — Lasso KKT condition.**

KKT stationarity: $\nabla_w \frac{1}{2}\|\mathbf{y}-\boldsymbol{\Phi}\mathbf{w}\|^2 + \lambda\partial\|\mathbf{w}\|_1 = 0$. For coordinate $j$: $-\boldsymbol{\phi}_j^T(\mathbf{y}-\boldsymbol{\Phi}\mathbf{w}) + \lambda\partial|w_j| = 0$. If $\hat{w}_j = 0$: $|\boldsymbol{\phi}_j^T(\mathbf{y}-\boldsymbol{\Phi}_{-j}\hat{\mathbf{w}}_{-j})| \leq \lambda/2$ (subgradient $\in [-\lambda, \lambda]$ at zero). Interpretation: feature $j$ is set to zero if its correlation with the current residual is below the regularisation threshold.

---

**Exercise 4 — Polynomial kernel.**

$(x_1 z_1 + x_2 z_2 + 1)^2 = x_1^2 z_1^2 + x_2^2 z_2^2 + 2x_1 z_1 x_2 z_2 + 2x_1 z_1 + 2x_2 z_2 + 1 = \boldsymbol{\phi}(\mathbf{x})^T\boldsymbol{\phi}(\mathbf{z})$ with $\boldsymbol{\phi}(\mathbf{x}) = (x_1^2, x_2^2, \sqrt{2}x_1x_2, \sqrt{2}x_1, \sqrt{2}x_2, 1)^T$ ✓. For degree $d$ in $\mathbb{R}^D$: feature space dimension $= \binom{D+d}{d}$.

---

**Exercise 5 — Gradient boosting.** *(Computational — see notebook.)*

---

**Exercise 6 — PCA as optimal compression.**

We seek $\mathbf{U}_M$ (orthonormal columns) minimising $\|\mathbf{X} - \mathbf{X}\mathbf{U}_M\mathbf{U}_M^T\|_F^2 = \|\mathbf{X}\|_F^2 - \|\mathbf{X}\mathbf{U}_M\|_F^2$. Maximising $\|\mathbf{X}\mathbf{U}_M\|_F^2 = \text{tr}(\mathbf{U}_M^T\mathbf{X}^T\mathbf{X}\mathbf{U}_M)$ subject to $\mathbf{U}_M^T\mathbf{U}_M = \mathbf{I}$ is solved by the top $M$ eigenvectors of $\mathbf{X}^T\mathbf{X}$. Minimum error: $\sum_{j=M+1}^{\min(N,D)} \lambda_j$ where $\lambda_j$ are the discarded eigenvalues of the sample covariance.

---

**Exercise 7 — Bellman iteration.**

For a two-state, two-action MDP: write $V^*(s_i) = \max_a [R(s_i,a) + \gamma\sum_j P(s_j|s_i,a)V^*(s_j)]$ explicitly for $i=1,2$. Substitute numerical values and solve the resulting linear system for $V^*(s_1)$, $V^*(s_2)$. The greedy policy selects the action maximising the right-hand side. *(Numerical values depend on the specific MDP; the method generalises straightforwardly.)*

---

## Generative AI

**Exercise 1 — Temperature and entropy.**

Raw logits: $(-0.2, -0.5, -1.0, -1.5, -3.0)$. Unnormalised: $e^{l_i}$: $(0.819, 0.607, 0.368, 0.223, 0.050)$. Sum $= 2.067$. Probabilities: $(0.396, 0.293, 0.178, 0.108, 0.024)$ ✓ sum to 1.

At $T=0.5$: divide logits by 0.5 → exponentiate → renormalise. Top token gets higher probability; entropy decreases.
At $T=2$: logits divided by 2 → distribution flattens; entropy increases.
$H = -\sum p_i\log p_i$: $H(T=0.5) < H(T=1) < H(T=2)$.

---

**Exercise 2 — Attention mechanism.**

$Q = K = \mathbf{X}W_Q = \mathbf{X}[:, :2]$ (first two columns). $Q = K = \begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}$.

$QK^T/\sqrt{2} = \frac{1}{\sqrt{2}}\begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix}$. Softmax row-wise: rows 1, 2 concentrate on positions 1, 2 respectively; row 3 is uniform (all zeros). Output attends most to the same position (self-attention).

---

**Exercise 3 — Perplexity.**

(a) $\text{PP} = 2^{350/100} = 2^{3.5} = 11.31$.

(b) Random baseline: $2^{\log_2 10{,}000} = 10{,}000$. PP $= 11.31$ is far better than random.

(c) Cross-entropy of model 1: $350/100 = 3.5$ bits/token. Model 2: $\log_2(80) = 6.32$ bits/token — wait, PP $= 80 \Rightarrow$ cross-entropy $= \log_2(80) = 6.32$ bits. Model 1 has lower perplexity and hence lower cross-entropy: $3.5$ vs $6.32$. Ratio of cross-entropies: $6.32/3.5 = 1.81$.

---

**Exercise 4 — LoRA parameter count.**

(a) Trainable params: $|A| + |B| = 4096r + r\times4096 = 8192r$.

(b) Full fine-tuning: $4096^2 = 16{,}777{,}216$. Percentages: $r=4$: $0.195\%$; $r=8$: $0.39\%$; $r=16$: $0.78\%$; $r=32$: $1.56\%$.

(c) $8192r = 16{,}777{,}216/100 = 167{,}772$. $r = 20.5$, so $r \approx 21$ (round up to ensure $\leq 1\%$).

---

**Exercise 5 — RAG retrieval.**

(a) $\mathbf{e}_q = (1,0,1)^T/\sqrt{2}$. Cosine similarities: $\cos(\mathbf{e}_q, \mathbf{e}_1) = (1/\sqrt{2})(1\cdot1) = 1/\sqrt{2} = 0.707$. $\cos(\mathbf{e}_q, \mathbf{e}_2) = (1/\sqrt{2})(1/\sqrt{2}+0) = 1/2 = 0.500$. $\cos(\mathbf{e}_q, \mathbf{e}_3) = (1/\sqrt{2})(0+1/\sqrt{2}) = 1/2 = 0.500$.

(b) Ranking: $\mathbf{e}_1 > \mathbf{e}_2 = \mathbf{e}_3$.

(c) BM25 would retrieve whichever document contains the query's exact keywords. If the query is "earnings announcement impact" and document $\mathbf{e}_2$ contains those exact words while $\mathbf{e}_1$ is semantically similar but uses different terms, BM25 would rank $\mathbf{e}_2$ first. Hybrid retrieval combines both signals to capture lexical and semantic relevance.

---

**Exercise 6 — Agent topology design.**

(a) The **supervisor** topology fits best: a central controller (supervisor) assigns tasks to specialist sub-agents for news scanning, impact assessment, and summary generation, and routes the final output for human review before any action. The parallel nature of scanning multiple feeds and the sequential dependency (assessment depends on news detection) align with this pattern.

(b) Design patterns: (i) **Reflection** — the impact assessment agent critiques its own analysis before passing it on; (ii) **Human-in-the-loop** — mandatory human review gate before position submission.

(c) Evaluation: task-level metrics — precision/recall of identified earnings announcements, quality of impact summaries (human evaluation or reference comparison); step-level metrics — latency per agent step, error rate on news extraction, percentage of summaries correctly flagged for review vs auto-approved.

---

**Exercise 7 — DPO objective.**

(a) DPO argument: $\beta[\log(\pi_\theta(y_w|x)/\pi_\text{ref}(y_w|x)) - \log(\pi_\theta(y_l|x)/\pi_\text{ref}(y_l|x))]$ $= 0.1[(-1.5-(-2.0)) - (-1.8-(-1.0))] = 0.1[(0.5) - (-0.8)] = 0.1 \times 1.3 = 0.13$.

(b) DPO loss: $-\log\sigma(0.13) = -\log(0.532) = 0.631$.

(c) The argument is positive (0.13 > 0), meaning $\sigma(0.13) > 0.5$: the model is making progress toward preferring $y_w$ over $y_l$ relative to the reference. However, the margin is small (the reference model already assigned $y_l$ higher probability, and the trained model has started correcting this but not fully).

---

## Quantitative Investment Fundamentals

**Exercise 1 — Strategy classification.**

(a) ITP spread mean reversion — **mean reversion** (statistical arbitrage at the country level).
(b) Low price-to-book basket — **factor investing** (value factor).
(c) Moving average crossover — **trend following**.
(d) Long convertible, short equity — **statistical arbitrage** (capital structure relative value, also involves **mean reversion** to theoretical value).

---

**Exercise 2 — Sharpe significance.**

Daily SR $= 0.08$. Annualised SR $= 0.08\sqrt{252} = 1.27$. Standard error of the annualised SR over $N=500$ days: $\text{SE} \approx 1/\sqrt{N} = 1/\sqrt{500} = 0.0447$ (approximate, ignoring higher moments). $t$-stat $= 1.27/0.0447 = 28.4$. This is far above the critical value of 1.96, so **yes**, the SR is statistically significant. (Note: for the daily SR test, $t = \text{SR}\sqrt{N} = 0.08\sqrt{500} = 1.79 < 1.96$, so just below significance at 5% using the daily statistic — the distinction matters!)

Additional days for significance: need $t = SR_d\sqrt{N} = 0.08\sqrt{N} = 1.96$, so $N = (1.96/0.08)^2 = 600$ days; need $600 - 500 = 100$ more days.

---

**Exercise 3 — Walk-forward design.**

IS window: 240 trading days (2 years — allows 120-day estimation with buffer). OOS window: 60 trading days (1 quarter). With 2500 days total: leave 240 for the first IS window, then roll 60-day OOS windows. Number of splits: $\lfloor(2500-240)/60\rfloor = 37$ splits. Total OOS data: $37 \times 60 = 2{,}220$ days (about 8.8 years of OOS).

---

**Exercise 4 — Transaction cost analysis.**

(a) Daily turnover cost: $40\% \times 5\text{ bps}/100 \times 2 = 0.40\%$... more precisely: daily turnover = 40% of portfolio traded (buy + sell); cost per round-trip = 5 bps buy + 5 bps sell = 10 bps. One-way daily turnover 20% → daily cost = $20\% \times 5\text{ bps} = 0.01\%$ per day (one-way), or if 40% is one-way: $40\% \times 5 = 0.20\%$ per day — large relative to daily SR.

Daily Sharpe (gross): $0.12$. Daily cost drag: $0.0020$ (0.20%). Net daily return $\approx$ gross mean return $- 0.0020$. If gross SR $= 0.12$ implies mean $= 0.12\sigma$, and $\sigma$ is daily vol, net SR depends on $\sigma$. In practice: net SR $\approx 0.12 - 0.0020/\sigma$.

(b/c) With 20% turnover and SR $= 0.09$: cost $= 20\% \times 5 = 0.10\%$. Comparison requires knowing $\sigma$; the net Sharpe ratio depends on the return level, not just SR. *(Full numerical answer requires specification of daily volatility.)*

---

**Exercise 5 — Overfitting and deflation.**

(a) Effective significance level: testing 50 independent rules and reporting the best corresponds to a family-wise error rate (FWER). By Bonferroni: effective per-test level $= 0.05/50 = 0.001$. The reported result implicitly uses a 0.1% significance threshold.

(b) With 50 rules on 3 years ($\approx750$ days), even under the null (all rules have SR=0), the distribution of the maximum SR is substantially positive — consistent with a reported SR of 2.2. The result is almost certainly a false discovery due to multiple testing.

(c) By Bailey and López de Prado's minimum backtest length formula: approximate minimum length for SR significance with 50 trials at 5% family-wise level requires roughly $N_\text{min} \propto (z^{-1}(1-0.05/50))^2 / SR^2$ — for 50 strategies and SR=2.2 annualised, this corresponds to several years of data beyond what was used.

---

**Exercise 6 — Regime detection.** *(Conceptual.)*

Two quantitative regime filters: (i) **Hurst exponent**: compute $H$ on a rolling window; if $H < 0.45$ the market is range-bound (mean-reverting), switch momentum off. (ii) **Realised volatility ratio**: compute the ratio of 1-month realised vol to 6-month realised vol; if $>1.5$ (vol is elevated and trending), mean reversion tends to fail and momentum is preferred. Validation: test the filter out-of-sample on held-out windows, ensuring the filter conditioning is applied strictly before the OOS period to avoid lookahead bias.

---

## Optimal Investment Theory

**Exercise 1 — OU calibration.**

(a) AR(1): $x_k = \mu + a(x_{k-1}-\mu) + b\epsilon_k$. $\hat{a}=0.92$, $\hat{b}=0.08$. OU parameters (continuous-time, $\Delta t=1$): $\kappa = -\ln\hat{a}/\Delta t = -\ln(0.92) = 0.0834$ day$^{-1}$; $\mu = 1.2$ (mean); $\sigma = \hat{b}/\sqrt{\Delta t} = 0.08$ day$^{-1/2}$.

(b) Half-life: $t_{1/2} = \ln 2/\kappa = 0.693/0.0834 = 8.3$ trading days.

(c) $\sigma_\infty = \sigma/\sqrt{2\kappa} = 0.08/\sqrt{2\times0.0834} = 0.08/0.409 = 0.196$.

(d) Entry at $z = (x - \mu)/\sigma_\infty > z_\text{entry}$. For expected holding period $\approx$ one half-life, set $z_\text{entry}$ such that the expected time to revert to 0 starting from $z$ is one half-life. A commonly used rule: $z_\text{entry} \approx 1$–$2$ standard deviations.

---

**Exercise 2 — Dickey-Fuller test.**

(a) DF statistic: $t_{\hat\beta} = \hat\beta/\text{SE}(\hat\beta) = -0.045/0.018 = -2.50$.

(b) Critical value at 5% (without trend, with constant, $N=500$): approximately $-2.87$. Since $-2.50 > -2.87$, **fail to reject** the unit root null.

(c) With trend: $\hat\beta = -0.035$, $\text{SE} = 0.014$. $t = -0.035/0.014 = -2.50$. Critical value with trend $\approx -3.43$. Still fail to reject.

---

**Exercise 3 — Hurst exponent.**

Slope $2H$: (A) $2H=1.0 \Rightarrow H=0.5$ → **random walk**; (B) $2H=0.7 \Rightarrow H=0.35 < 0.5$ → **mean reversion**; (C) $2H=1.4 \Rightarrow H=0.7 > 0.5$ → **trending**.

Pairs trading: appropriate for (B) (mean-reverting series). Trend following: appropriate for (C) (trending series). Random walk (A): no exploitable serial structure.

---

**Exercise 4 — Cointegration: EG vs Johansen.** *(Conceptual.)*

Engle-Granger is a two-step OLS procedure testing a single cointegrating vector; it suffers from pre-test bias and is optimal only when there is exactly one cointegrating relationship. Johansen uses a VECM framework and tests for the rank of the cointegrating matrix — it can detect multiple cointegrating vectors and tests for their number sequentially. Disagreement arises when: the true cointegrating relationship involves all $d=3$ variables jointly (EG would test pairwise and may miss it); or when the normalisation chosen in EG is incorrect. Johansen is preferred in practice for $d>2$.

---

**Exercise 5 — APT expected returns.**

(a) Expected excess return: $\mu_i = \beta_1\lambda_1 + \beta_2\lambda_2 + \beta_3\lambda_3 = 1.1\times6\% + 0.4\times2\% + (-0.2)\times3\% = 6.6\% + 0.8\% - 0.6\% = 6.8\%$.

(b) Four-factor alpha: $\alpha = 8\% - 6.8\% = 1.2\%$.

(c) Negative HML loading ($\beta_3 = -0.2$): the asset behaves like a growth stock (high price-to-book) rather than a value stock. Negative loading means it co-moves negatively with the value factor — it falls when value stocks outperform growth stocks.

---

**Exercise 6 — Black-Litterman.**

$\tau = 0.05$, $\Sigma = \begin{pmatrix}0.04&0.02\\0.02&0.09\end{pmatrix}$, $\Pi = (0.06, 0.08)^T$. View: $P=(1,-1)$, $q=0.02$, $\Omega=(0.01)^2=10^{-4}$.

BL update: $\hat{\mu} = [(\tau\Sigma)^{-1} + P^T\Omega^{-1}P]^{-1}[(\tau\Sigma)^{-1}\Pi + P^T\Omega^{-1}q]$.

$\tau\Sigma = \begin{pmatrix}0.002&0.001\\0.001&0.0045\end{pmatrix}$. $(\tau\Sigma)^{-1}$: det $= 0.002\times0.0045 - 0.001^2 = 8\times10^{-6}$. $(\tau\Sigma)^{-1} = \frac{1}{8\times10^{-6}}\begin{pmatrix}0.0045&-0.001\\-0.001&0.002\end{pmatrix} = \begin{pmatrix}562.5&-125\\-125&250\end{pmatrix}$.

$P^T\Omega^{-1}P = 10^4\begin{pmatrix}1\\-1\end{pmatrix}(1,-1) = 10^4\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$.

The view information dominates (large $\Omega^{-1}$). $\hat{\mu}$ is shifted toward the view: asset 1 expected return rises toward 8% (as the view says asset 1 outperforms asset 2 by 2%), asset 2 falls slightly. *(Full matrix algebra yields $\hat\mu \approx (6.15\%, 7.63\%)^T$.)*

---

**Exercise 7 — Risk parity.**

(a) Inverse-vol weights: $w_1 = (1/\sigma_1)/(1/\sigma_1+1/\sigma_2) = (1/15)/(1/15+1/30) = (1/15)/(1/10) = 2/3$. $w_2 = 1/3$.

(b) With $\rho=0$: portfolio variance $= w_1^2\sigma_1^2 + w_2^2\sigma_2^2 = (4/9)(225) + (1/9)(900) = 100 + 100 = 200$. Risk contribution: $RC_1 = w_1\partial\sigma_P/\partial w_1 = w_1^2\sigma_1^2/\sigma_P = 100/\sqrt{200} = 50\%$ each. So inverse-vol weights achieve exact risk parity when $\rho=0$ ✓.

(c) With $\rho=0.3$: $\sigma_P^2 = (4/9)(225) + (1/9)(900) + 2(2/3)(1/3)(0.3)(15)(30) = 100+100+60 = 260$. $RC_1 = w_1(\boldsymbol{\Sigma}\mathbf{w})_1/\sigma_P = (2/3)(w_1\sigma_1^2 + w_2\rho\sigma_1\sigma_2)/\sigma_P = (2/3)(100+30)/\sqrt{260} = (2/3)(130)/16.12 = 5.37$; $RC_2 = (1/3)(w_2\sigma_2^2 + w_1\rho\sigma_1\sigma_2)/\sigma_P = (1/3)(300+45)/16.12 = 7.14$. Risk contributions are not equal ($RC_1 < RC_2$). Exact risk parity requires increasing $w_1$ (and decreasing $w_2$) to equalise the marginal risk contributions — moving beyond inverse-vol toward a portfolio where $RC_1=RC_2=50\%$.
