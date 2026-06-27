(data_driven_methods)=
# Data-Driven Methods

Machine learning provides a collection of principled statistical methods for learning mappings from data, bypassing the need to specify a closed-form generative model for every phenomenon of interest. In algorithmic trading, the range of applications is broad: predicting short-term price displacements in {ref}`fair_price_estimation`, fitting win-probability curves in {ref}`rfq_models`, constructing composite liquidity indicators in {ref}`liquidity_modelling`, and generating investment signals in {ref}`quant_investment_fundamentals`. This chapter develops the mathematical foundations that underpin all of these applications, emphasising core theory rather than software libraries or data pipelines.

## Introduction

The chapter is organised as follows. We open with the **statistical learning framework** ({ref}`sec:ddm_framework`): the formalisation of learning as risk minimisation, the bias–variance decomposition, and the tools of regularisation and cross-validation. The bulk of the chapter is devoted to **supervised learning** ({ref}`sec:ddm_supervised`): linear regression and its probabilistic interpretation, ridge and lasso regularisation as MAP inference, logistic regression for classification, kernel methods and support vector machines, tree ensembles (random forests and gradient boosting), and the fundamentals of neural networks. We then cover **unsupervised learning** ({ref}`sec:ddm_unsupervised`): principal component analysis derived as a variance-maximising projection, and $k$-means clustering as a special case of the EM algorithm. The chapter closes with **reinforcement learning** ({ref}`sec:ddm_rl`): the Markov decision process, Bellman equations, $Q$-learning, and policy gradient methods, providing the theoretical scaffold for sequential decision-making in trading.

(sec:ddm_framework)=
## Statistical Learning Framework

### Risk minimisation

Let $(\mathbf{x}, y) \sim p(\mathbf{x}, y)$ be an input–output pair drawn from an unknown joint distribution, with $\mathbf{x} \in \mathbb{R}^D$ a feature vector and $y$ a target. A **model** is a function $f : \mathbb{R}^D \to \mathcal{Y}$ that predicts $y$ from $\mathbf{x}$. The quality of a prediction is measured by a **loss function** $\ell(y, f(\mathbf{x})) \geq 0$; common choices are the squared error $\ell(y, \hat{y}) = (y - \hat{y})^2$ for regression and the 0–1 loss $\ell(y, \hat{y}) = \mathbf{1}[y \neq \hat{y}]$ for classification. The **expected risk** (or generalisation error) of $f$ is

$$R[f] = \mathbb{E}_{(\mathbf{x},y) \sim p}[\,\ell(y, f(\mathbf{x}))\,]$$

The ideal model minimises $R[f]$ over all measurable functions. For squared-error loss, differentiating inside the expectation shows that the optimal predictor is the **regression function** $f^*(\mathbf{x}) = \mathbb{E}[y \mid \mathbf{x}]$ {cite:p}`murphy2013machine`. For the 0–1 loss, the optimal predictor is the **Bayes classifier** $f^*(\mathbf{x}) = \arg\max_k\, p(y = k \mid \mathbf{x})$.

Since $p(\mathbf{x},y)$ is unknown, $R[f]$ cannot be computed. Given a training dataset $\mathcal{D} = \{(\mathbf{x}_n, y_n)\}_{n=1}^N$ of i.i.d. samples, we substitute the **empirical risk**

$$\hat{R}[f] = \frac{1}{N}\sum_{n=1}^N \ell(y_n, f(\mathbf{x}_n))$$

**Empirical risk minimisation (ERM)** finds $\hat{f} = \arg\min_{f \in \mathcal{F}} \hat{R}[f]$ within a restricted function class $\mathcal{F}$. If $\mathcal{F}$ is too rich, $\hat{f}$ memorises the training data (**overfitting**); if too restricted, it cannot approximate $f^*$ (**underfitting**). The generalisation gap $R[\hat{f}] - \hat{R}[\hat{f}]$ depends on the **complexity** of $\mathcal{F}$, which is controlled through regularisation and cross-validation.

### Bias–variance decomposition

For squared-error loss and a model $\hat{f}$ learned from a training set $\mathcal{D}$ of size $N$, the expected test error at a point $\mathbf{x}$ decomposes as {cite:p}`bishop2006pattern`

$$\mathbb{E}_\mathcal{D}\bigl[(y - \hat{f}(\mathbf{x}))^2\bigr] = \underbrace{\bigl(\mathbb{E}_\mathcal{D}[\hat{f}(\mathbf{x})] - f^*(\mathbf{x})\bigr)^2}_{\mathrm{Bias}^2} + \underbrace{\mathbb{E}_\mathcal{D}\bigl[(\hat{f}(\mathbf{x}) - \mathbb{E}_\mathcal{D}[\hat{f}(\mathbf{x})])^2\bigr]}_{\mathrm{Variance}} + \underbrace{\sigma^2}_{\mathrm{Noise}}$$

where $\sigma^2 = \mathbb{E}[(y - f^*(\mathbf{x}))^2]$ is irreducible noise. The **bias** measures systematic error from model mis-specification; the **variance** measures sensitivity to the particular training set realised. More flexible models (higher-degree polynomials, deeper trees) reduce bias but increase variance, producing the characteristic U-shaped test error curve as a function of model complexity ({numref}`fig:ddm_bias_variance`). Regularisation and ensemble methods are the primary tools for managing this tradeoff.

```{figure} figures/ddm_bias_variance.png
:name: fig:ddm_bias_variance
:width: 8in
Test error (solid) and training error (dashed) as a function of polynomial degree on a sinusoidal regression problem with $N=15$ noisy observations, averaged over 50 datasets. The irreducible noise floor $\sigma^2$ is shown as a dotted line. Low degree yields high bias; high degree yields high variance. The optimal degree minimises test error.
```

### Regularisation

Regularisation incorporates a penalty on model complexity into the objective:

$$\hat{f}_\lambda = \arg\min_{f \in \mathcal{F}} \left[\hat{R}[f] + \lambda\,\Omega(f)\right]$$

where $\Omega(f) \geq 0$ measures complexity and $\lambda > 0$ is a hyperparameter. Increasing $\lambda$ shifts the bias–variance tradeoff towards higher bias and lower variance. From a Bayesian perspective ({ref}`intro_bayesian`), regularisation is MAP estimation under the prior $p(f) \propto e^{-\lambda\,\Omega(f)}$: the penalty encodes prior beliefs about the smoothness or sparsity of $f$.

### Cross-validation and model selection

The hyperparameter $\lambda$ — along with structural choices such as tree depth or network architecture — must be selected using data not in the training set. **$K$-fold cross-validation** divides $\mathcal{D}$ into $K$ equal folds, training on $K-1$ folds and evaluating on the remaining fold, then averaging over all $K$ splits:

$$\widehat{CV}(\lambda) = \frac{1}{K} \sum_{k=1}^K \hat{R}_{\mathcal{D}_k}\!\left[\hat{f}_\lambda^{(-k)}\right]$$

where $\hat{f}_\lambda^{(-k)}$ is the model trained on all folds except $k$ and $\hat{R}_{\mathcal{D}_k}$ is the empirical risk on fold $k$. Common choices are $K = 5$ or $K = 10$; the limit $K = N$ is **leave-one-out** cross-validation. A completely withheld **test set** is reserved for final evaluation and must never inform any modelling decision.

(sec:ddm_supervised)=
## Supervised Learning

Supervised learning covers problems where each training example pairs an input $\mathbf{x}_n$ with a target $y_n$. When $y \in \mathbb{R}$ the task is **regression**; when $y \in \{1, \ldots, K\}$ the task is **classification**. We treat the core model families in increasing order of flexibility.

(sec:ddm_regression)=
### Linear Regression

The simplest regression model is linear in a feature vector $\boldsymbol{\phi}(\mathbf{x}) \in \mathbb{R}^M$:

$$f(\mathbf{x}; \mathbf{w}) = \mathbf{w}^T \boldsymbol{\phi}(\mathbf{x})$$

The feature map $\boldsymbol{\phi}$ may include raw inputs, polynomial terms, or any fixed nonlinear transformation; the model remains **linear in the parameters** $\mathbf{w}$. Collecting all $N$ training points into the **design matrix** $\boldsymbol{\Phi} \in \mathbb{R}^{N \times M}$ with rows $\boldsymbol{\phi}(\mathbf{x}_n)^T$ and the target vector $\mathbf{y} \in \mathbb{R}^N$, ERM under squared-error loss gives the **ordinary least squares** (OLS) criterion

$$\hat{\mathbf{w}} = \arg\min_{\mathbf{w}} \|\mathbf{y} - \boldsymbol{\Phi}\mathbf{w}\|^2$$

Setting the gradient to zero yields the **normal equations** $\boldsymbol{\Phi}^T\boldsymbol{\Phi}\,\hat{\mathbf{w}} = \boldsymbol{\Phi}^T\mathbf{y}$, with closed-form solution

$$\hat{\mathbf{w}}_{\mathrm{OLS}} = (\boldsymbol{\Phi}^T\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^T\mathbf{y} = \boldsymbol{\Phi}^{\dagger}\mathbf{y}$$

where $\boldsymbol{\Phi}^{\dagger}$ is the Moore–Penrose pseudoinverse. Geometrically, $\hat{\mathbf{y}} = \boldsymbol{\Phi}\hat{\mathbf{w}}$ is the orthogonal projection of $\mathbf{y}$ onto the column space of $\boldsymbol{\Phi}$.

**Probabilistic interpretation.** Assuming $y_n = \mathbf{w}^T\boldsymbol{\phi}(\mathbf{x}_n) + \epsilon_n$ with $\epsilon_n \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)$, the log-likelihood is

$$\log p(\mathbf{y} \mid \boldsymbol{\Phi}, \mathbf{w}) = -\frac{N}{2}\log(2\pi\sigma^2) - \frac{1}{2\sigma^2}\|\mathbf{y} - \boldsymbol{\Phi}\mathbf{w}\|^2$$

Maximising over $\mathbf{w}$ recovers the OLS estimator: least squares is maximum likelihood under Gaussian noise. Placing a Gaussian prior on $\mathbf{w}$ and computing the posterior leads to **Bayesian linear regression** and the predictive distribution, developed in {ref}`intro_bayesian`.

**Gauss–Markov theorem.** Among all linear unbiased estimators, OLS achieves minimum variance — it is the Best Linear Unbiased Estimator (BLUE). This optimality can break down under high multicollinearity (when $\boldsymbol{\Phi}^T\boldsymbol{\Phi}$ is near-singular) or when some bias is acceptable in exchange for lower variance, motivating the regularised estimators of the next section.

(sec:ddm_regularization)=
### Regularisation

**Ridge regression** adds an $\ell_2$ penalty on the coefficients:

$$\hat{\mathbf{w}}_{\mathrm{ridge}} = \arg\min_{\mathbf{w}} \|\mathbf{y} - \boldsymbol{\Phi}\mathbf{w}\|^2 + \lambda\|\mathbf{w}\|^2$$

The unique closed-form solution is

$$\hat{\mathbf{w}}_{\mathrm{ridge}} = (\boldsymbol{\Phi}^T\boldsymbol{\Phi} + \lambda\mathbf{I})^{-1}\boldsymbol{\Phi}^T\mathbf{y}$$

Adding $\lambda\mathbf{I}$ conditions the Gram matrix and removes the singularity problem. Probabilistically, ridge regression is MAP estimation under a spherical Gaussian prior $p(\mathbf{w}) = \mathcal{N}(\mathbf{0},\, \sigma^2/\lambda \cdot \mathbf{I})$. Using the SVD $\boldsymbol{\Phi} = \mathbf{U}\mathbf{S}\mathbf{V}^T$, the prediction at a new input can be written as a sum over principal directions with **shrinkage factors** $s_j^2/(s_j^2 + \lambda)$: directions of small singular value $s_j$ (low signal-to-noise) are suppressed.

**Lasso regression** substitutes an $\ell_1$ penalty:

$$\hat{\mathbf{w}}_{\mathrm{lasso}} = \arg\min_{\mathbf{w}} \|\mathbf{y} - \boldsymbol{\Phi}\mathbf{w}\|^2 + \lambda\|\mathbf{w}\|_1$$

The $\ell_1$ penalty has a kink at the origin that forces many coefficients to be exactly zero for sufficiently large $\lambda$, performing **variable selection** simultaneously with shrinkage. Probabilistically, lasso is MAP under independent Laplace priors $p(w_j) \propto e^{-(\lambda/2)|w_j|}$. There is no closed-form solution; efficient algorithms use coordinate descent or the LARS algorithm {cite:p}`hastie2009elements`. ({numref}`fig:ddm_regularization`).

```{figure} figures/ddm_regularization.png
:name: fig:ddm_regularization
:width: 9in
Regularisation paths for ridge (left) and lasso (right) on a dataset with ten predictors, five informative (coloured lines). Each curve is one coefficient plotted against the log-penalty $\log_{10}\lambda$, moving from right (no penalty) to left (maximum penalty). Ridge shrinks all coefficients smoothly; lasso sets coefficients to zero sequentially, yielding a sparse model.
```

**Elastic net** combines both penalties: $\lambda_1\|\mathbf{w}\|_1 + \lambda_2\|\mathbf{w}\|^2$. It inherits lasso's sparsity while retaining the grouping property of ridge (correlated predictors are selected jointly), which is desirable when financial features are highly collinear. These regularised regression models are used in {ref}`liquidity_modelling` to combine liquidity metrics and identify their relative predictive contributions.

(sec:ddm_classification)=
### Classification and Logistic Regression

For a binary target $y \in \{0,1\}$, the **logistic regression** model places the posterior probability of the positive class as

$$p(y = 1 \mid \mathbf{x}; \mathbf{w}) = \sigma(\mathbf{w}^T\boldsymbol{\phi}(\mathbf{x})), \qquad \sigma(a) = \frac{1}{1 + e^{-a}}$$

The sigmoid $\sigma$ maps the linear score $a = \mathbf{w}^T\boldsymbol{\phi}$ to $(0,1)$. The log-odds ratio $\log[p/(1-p)] = \mathbf{w}^T\boldsymbol{\phi}$ is linear in $\mathbf{x}$, so the decision boundary $\{p = 1/2\} = \{\mathbf{w}^T\boldsymbol{\phi}(\mathbf{x}) = 0\}$ is a hyperplane in feature space. The negative log-likelihood under Bernoulli observations gives the **cross-entropy loss**

$$\mathcal{L}(\mathbf{w}) = -\sum_{n=1}^N \bigl[y_n \log \sigma_n + (1 - y_n)\log(1 - \sigma_n)\bigr]$$

where $\sigma_n = \sigma(\mathbf{w}^T\boldsymbol{\phi}(\mathbf{x}_n))$. This is convex in $\mathbf{w}$ but has no closed-form minimiser; iterative methods such as gradient descent or Newton–Raphson (IRLS) are used. The gradient has the clean form $\nabla_\mathbf{w}\mathcal{L} = \boldsymbol{\Phi}^T(\boldsymbol{\sigma} - \mathbf{y})$: it is the residual of predicted probabilities against targets, projected by the design matrix.

For $K > 2$ classes, logistic regression extends to the **softmax** model:

$$p(y = k \mid \mathbf{x}; \mathbf{W}) = \frac{e^{\mathbf{w}_k^T\boldsymbol{\phi}(\mathbf{x})}}{\sum_{j=1}^K e^{\mathbf{w}_j^T\boldsymbol{\phi}(\mathbf{x})}}$$

with a corresponding multinomial cross-entropy loss. Logistic regression is used in {ref}`rfq_models` to estimate the probability that a client's reservation price exceeds the dealer's quoted spread, and to identify whether a client is engaging in price discovery.

```{figure} figures/ddm_decision_boundary.png
:name: fig:ddm_decision_boundary
:width: 9in
Decision boundaries on a two-dimensional binary classification dataset for logistic regression (linear boundary), SVM with RBF kernel (smooth nonlinear boundary), and a two-hidden-layer MLP (complex nonlinear boundary). All three achieve similar training accuracy; the nonlinear models adapt to the data geometry at the cost of higher variance.
```

(sec:ddm_kernels)=
### Kernel Methods and Support Vector Machines

Many problems require nonlinear decision boundaries. Rather than engineering nonlinear features explicitly, the **kernel trick** exploits the fact that many learning algorithms depend on the data only through inner products $\boldsymbol{\phi}(\mathbf{x})^T\boldsymbol{\phi}(\mathbf{x}')$. If one defines a **kernel function** $k(\mathbf{x}, \mathbf{x}') = \boldsymbol{\phi}(\mathbf{x})^T\boldsymbol{\phi}(\mathbf{x}')$, these inner products can be evaluated directly in input space without ever computing $\boldsymbol{\phi}$. By Mercer's theorem, any symmetric positive semi-definite function is a valid kernel {cite:p}`bishop2006pattern`. The Gaussian (RBF) kernel $k(\mathbf{x},\mathbf{x}') = \exp(-\|\mathbf{x}-\mathbf{x}'\|^2/2\ell^2)$ corresponds to an infinite-dimensional feature space.

**Kernel ridge regression.** By the representer theorem, the optimal weight vector of any regularised learning algorithm lies in the span of the training feature vectors: $\hat{\mathbf{w}} = \sum_n \alpha_n\boldsymbol{\phi}(\mathbf{x}_n)$. Substituting into the ridge objective and writing $\mathbf{K}_{nm} = k(\mathbf{x}_n, \mathbf{x}_m)$ for the $N \times N$ Gram matrix yields the dual formulation

$$\hat{\boldsymbol{\alpha}} = (\mathbf{K} + \lambda\mathbf{I})^{-1}\mathbf{y}, \qquad \hat{f}(\mathbf{x}) = \mathbf{k}(\mathbf{x})^T\hat{\boldsymbol{\alpha}}$$

where $\mathbf{k}(\mathbf{x})_n = k(\mathbf{x}, \mathbf{x}_n)$. This is equivalent to Gaussian process regression ({ref}`intro_bayesian`) with kernel $k$ as the covariance function.

**Support vector machines.** The **SVM** {cite:p}`vapnik1995nature` seeks the maximum-margin linear separator in feature space. For linearly separable data, the primal problem is

$$\min_{\mathbf{w}, b} \frac{1}{2}\|\mathbf{w}\|^2 \quad \text{subject to} \quad y_n(\mathbf{w}^T\boldsymbol{\phi}(\mathbf{x}_n) + b) \geq 1, \quad n = 1,\ldots,N$$

The margin between the two supporting hyperplanes is $2/\|\mathbf{w}\|$, so minimising $\|\mathbf{w}\|^2$ maximises the margin. The Lagrangian dual depends only on the inner products $\boldsymbol{\phi}(\mathbf{x}_n)^T\boldsymbol{\phi}(\mathbf{x}_m)$, which are replaced by $k(\mathbf{x}_n,\mathbf{x}_m)$ to give the **kernel SVM**. Only training points that lie on the margin boundary have non-zero dual variables and are called **support vectors**; the decision boundary depends only on these. For non-separable data, slack variables $\xi_n \geq 0$ relax the constraints at cost $C\sum_n\xi_n$, with $C = 1/\lambda$ acting as inverse regularisation strength.

(sec:ddm_trees)=
### Tree Ensembles

A **decision tree** partitions the input space into rectangular regions by recursively splitting on one feature at a time. At each node, the best split on feature $j$ at threshold $t$ maximises the gain in purity

$$\Delta = I(\mathcal{R}) - \frac{|\mathcal{R}_L|}{|\mathcal{R}|}I(\mathcal{R}_L) - \frac{|\mathcal{R}_R|}{|\mathcal{R}|}I(\mathcal{R}_R)$$

where $I(\mathcal{R})$ is within-region variance for regression or Gini impurity $\sum_k p_k(1-p_k)$ for classification. A single deep tree is a high-variance, low-bias estimator: small changes in the training data can alter the entire partition. Ensemble methods reduce variance by aggregating many trees.

**Random forests** {cite:p}`breiman2001random` build $B$ trees in parallel, each trained on a bootstrap sample $\mathcal{D}_b$. At each split, only $m \ll D$ features are considered (typically $m \approx \sqrt{D}$ for classification, $m \approx D/3$ for regression), de-correlating the trees. The prediction is the average (regression) or majority vote (classification):

$$\hat{f}_{\mathrm{RF}}(\mathbf{x}) = \frac{1}{B}\sum_{b=1}^B \hat{f}_b(\mathbf{x})$$

By the bias-variance decomposition, the ensemble variance is $\rho\sigma^2 + (1-\rho)\sigma^2/B$, where $\rho$ is the average pairwise correlation between tree predictions. Feature randomisation reduces $\rho$ below what bagging alone achieves, and as $B \to \infty$ the variance converges to $\rho\sigma^2$, without further decrease; adding trees only reduces sampling noise.

**Gradient boosted trees** {cite:p}`friedman2001greedy` build trees sequentially. Each new tree $h_m$ fits the negative gradient of the loss with respect to the current ensemble prediction $F_{m-1}$:

$$F_m(\mathbf{x}) = F_{m-1}(\mathbf{x}) + \eta\,h_m(\mathbf{x})$$

For squared-error loss the negative gradient is the residual $r_{mn} = y_n - F_{m-1}(\mathbf{x}_n)$, so each tree fits the current residuals. For a general differentiable loss $\ell$, the pseudo-residuals

$$r_{mn} = -\frac{\partial\,\ell(y_n, F(\mathbf{x}_n))}{\partial F(\mathbf{x}_n)}\bigg|_{F = F_{m-1}}$$

define the gradient direction in function space. This **functional gradient descent** perspective makes gradient boosting highly flexible: the loss can be cross-entropy for classification, quantile loss for prediction intervals, or any domain-specific objective. Modern implementations (XGBoost, LightGBM) add second-order Newton steps and column/row subsampling for regularisation. Gradient-boosted trees achieve state-of-the-art performance on tabular financial data and are widely used in {ref}`rfq_models` for win-probability estimation ({numref}`fig:ddm_trees`).

```{figure} figures/ddm_trees.png
:name: fig:ddm_trees
:width: 9in
Left: test RMSE as a function of the number of trees for a random forest and gradient-boosted ensemble, against the single-tree baseline (dashed). The random forest converges quickly; gradient boosting improves monotonically. Right: feature importances (mean decrease in impurity) from the random forest, with the five truly informative features highlighted.
```

(sec:ddm_neural)=
### Neural Networks

A **multilayer perceptron** (MLP) is a function formed by composing affine transformations and pointwise nonlinearities. With $L$ hidden layers of widths $H_1, \ldots, H_L$, the forward pass is

$$\begin{aligned}
\mathbf{h}^{(0)} &= \mathbf{x} \\
\mathbf{h}^{(\ell)} &= g\!\left(\mathbf{W}^{(\ell)}\mathbf{h}^{(\ell-1)} + \mathbf{b}^{(\ell)}\right), \quad \ell = 1,\ldots,L \\
f(\mathbf{x}) &= \mathbf{W}^{(L+1)}\mathbf{h}^{(L)} + \mathbf{b}^{(L+1)}
\end{aligned}$$

where $g$ is an activation function applied element-wise. Popular choices include the ReLU $g(a) = \max(0,a)$ (avoids vanishing gradients, induces sparsity in activations), the hyperbolic tangent $g(a) = \tanh(a)$, and for the output layer the sigmoid $\sigma$ or softmax for classification.

**Universal approximation.** The MLP is a universal function approximator: for any continuous $f^*: [0,1]^D \to \mathbb{R}$ and $\varepsilon > 0$, there exists an MLP with a single hidden layer and sufficiently many units such that $\sup_{\mathbf{x}}|f(\mathbf{x}) - f^*(\mathbf{x})| < \varepsilon$ {cite:p}`cybenko1989approximation`. Depth provides efficiency: deeper networks can represent the same functions with exponentially fewer parameters, motivating the deep architectures used in practice {cite:p}`goodfellow2016deep`.

**Backpropagation.** Training minimises the empirical risk $\hat{R}(\boldsymbol{\theta}) = \frac{1}{N}\sum_n \ell(y_n, f(\mathbf{x}_n;\boldsymbol{\theta}))$ over all parameters $\boldsymbol{\theta} = \{\mathbf{W}^{(\ell)}, \mathbf{b}^{(\ell)}\}$ using gradient descent. The gradient is computed by **backpropagation** {cite:p}`rumelhart1986learning`, which applies the chain rule backward through the network. Defining the error signal at layer $\ell$ as $\boldsymbol{\delta}^{(\ell)} = \partial\hat{R}/\partial\mathbf{a}^{(\ell)}$ (where $\mathbf{a}^{(\ell)} = \mathbf{W}^{(\ell)}\mathbf{h}^{(\ell-1)} + \mathbf{b}^{(\ell)}$ is the pre-activation), the backward recurrence is

$$\boldsymbol{\delta}^{(L+1)} = \nabla_{\mathbf{h}^{(L+1)}}\ell, \qquad \boldsymbol{\delta}^{(\ell)} = \bigl(\mathbf{W}^{(\ell+1)}\bigr)^T\boldsymbol{\delta}^{(\ell+1)} \odot g'(\mathbf{a}^{(\ell)})$$

The gradient with respect to the weight matrix is $\nabla_{\mathbf{W}^{(\ell)}}\hat{R} = \boldsymbol{\delta}^{(\ell)}(\mathbf{h}^{(\ell-1)})^T$. The total computational cost is $O(N \cdot |\boldsymbol{\theta}|)$, the same order as a single forward pass. In practice, **mini-batch SGD** replaces the full-data gradient with a noisy estimate over a small batch $\mathcal{B} \subset \mathcal{D}$:

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta_t \cdot \frac{1}{|\mathcal{B}|}\sum_{n \in \mathcal{B}} \nabla_{\boldsymbol{\theta}}\,\ell(y_n, f(\mathbf{x}_n;\boldsymbol{\theta}_t))$$

Adaptive optimisers — Adam, RMSProp — maintain per-parameter step sizes and converge faster in practice. Regularisation of neural networks uses **weight decay** ($\ell_2$ penalty on $\boldsymbol{\theta}$), **dropout** (randomly zeroing activations during training, equivalent to an ensemble of thinned networks), and early stopping based on validation loss ({numref}`fig:ddm_nn_training`).

```{figure} figures/ddm_nn_training.png
:name: fig:ddm_nn_training
:width: 9in
Training and validation MSE for an MLP on a simulated regression task, without regularisation (left) and with $\ell_2$ weight decay (right). Without regularisation the model overfits: training loss falls while validation loss rises after an early minimum. Weight decay maintains a small gap between the two curves.
```

Deep neural networks — including recurrent networks for sequential data and the Transformer architecture — build on these foundations and are covered in {ref}`generative_ai` in the context of language modelling and generative AI.

(sec:ddm_unsupervised)=
## Unsupervised Learning

Unsupervised learning addresses settings where no target label $y$ is available and the objective is to discover structure in the marginal distribution $p(\mathbf{x})$. The two main themes are **dimensionality reduction** — finding a low-dimensional representation that preserves information — and **clustering** — identifying groups or modes in $p(\mathbf{x})$.

(sec:ddm_pca)=
### Principal Component Analysis

Let $\mathbf{X} \in \mathbb{R}^{N \times D}$ be a centred data matrix (columns mean-zero). **Principal component analysis** (PCA) finds the orthogonal directions $\mathbf{u}_1, \ldots, \mathbf{u}_M$ that maximise the projected variance. The first principal component solves

$$\mathbf{u}_1 = \arg\max_{\|\mathbf{u}\|=1} \mathbf{u}^T\mathbf{S}\mathbf{u}$$

where $\mathbf{S} = \frac{1}{N}\mathbf{X}^T\mathbf{X}$ is the sample covariance matrix. By Lagrange multipliers, $\mathbf{S}\mathbf{u}_1 = \lambda_1\mathbf{u}_1$: the first PC is the eigenvector of $\mathbf{S}$ with the largest eigenvalue $\lambda_1$, which equals the projected variance. Successive PCs are the remaining eigenvectors in decreasing eigenvalue order, subject to orthogonality.

Equivalently, PCA minimises reconstruction error: with the score matrix $\mathbf{Z} = \mathbf{X}\mathbf{U}_M \in \mathbb{R}^{N \times M}$ (columns $\mathbf{u}_1, \ldots, \mathbf{u}_M$), the reconstruction $\hat{\mathbf{X}} = \mathbf{Z}\mathbf{U}_M^T$ minimises $\|\mathbf{X} - \hat{\mathbf{X}}\|_F^2$ over all rank-$M$ approximations. By the **Eckart–Young theorem**, the minimum is achieved by the truncated SVD $\mathbf{X} \approx \mathbf{U}_M\mathbf{S}_M\mathbf{V}_M^T$, and the minimum reconstruction error equals $\sum_{j=M+1}^D s_j^2$. The fraction of variance explained by $M$ components is $\sum_{j=1}^M\lambda_j / \sum_{j=1}^D\lambda_j$ ({numref}`fig:ddm_pca`).

PCA has many financial applications: extracting common risk factors from a returns covariance matrix, constructing composite indicators from correlated liquidity metrics ({ref}`liquidity_modelling`), and identifying the idiosyncratic residuals of stock returns relative to market factors in statistical arbitrage ({ref}`optimal_investment_theory`).

```{figure} figures/ddm_pca.png
:name: fig:ddm_pca
:width: 9in
Left: a two-dimensional correlated dataset with the two principal component directions overlaid; arrow length is proportional to the square root of the corresponding eigenvalue. Right: cumulative explained variance ratio as a function of the number of components for a ten-dimensional dataset; the elbow marks the intrinsic dimensionality of the data.
```

(sec:ddm_clustering)=
### Clustering and the EM Algorithm

**$K$-means** partitions $N$ points into $K$ clusters $\{C_k\}_{k=1}^K$ by minimising the total within-cluster variance

$$J = \sum_{k=1}^K \sum_{n \in C_k} \|\mathbf{x}_n - \boldsymbol{\mu}_k\|^2$$

The standard algorithm alternates between two steps:

- **Assignment:** $z_n = \arg\min_k\|\mathbf{x}_n - \boldsymbol{\mu}_k\|^2$ — assign each point to the nearest centroid.
- **Update:** $\boldsymbol{\mu}_k = \frac{1}{|C_k|}\sum_{n \in C_k}\mathbf{x}_n$ — recompute centroids as cluster means.

Each step decreases $J$, guaranteeing convergence to a local minimum. $K$-means is a special case of the **EM algorithm** applied to a Gaussian mixture model (GMM) with equal, isotropic covariances and equal mixing weights: the E-step is a hard assignment of each point to the nearest component, and the M-step re-estimates the means. The soft-assignment GMM ({ref}`intro_bayesian`) replaces hard assignments with responsibilities $r_{nk} = p(z=k\mid\mathbf{x}_n)$ and also learns the covariance structure of each component, yielding a proper density model.

Selecting the number of clusters $K$ requires a model selection criterion. The **Bayesian Information Criterion** $\mathrm{BIC} = \log p(\mathbf{X}\mid\hat{\boldsymbol{\theta}}) - \frac{d}{2}\log N$ penalises the log-likelihood by the number of free parameters $d$ and the log-sample-size, providing a principled tradeoff between fit and complexity {cite:p}`murphy2013machine`.

(sec:ddm_rl)=
## Reinforcement Learning

Reinforcement learning (RL) addresses sequential decision-making problems in which an **agent** interacts with an **environment** over discrete time steps, taking actions and receiving scalar rewards {cite:p}`sutton2018reinforcement`. Unlike supervised learning, there is no labelled dataset: the agent must discover which actions are beneficial by exploration. The formal framework is the **Markov decision process** (MDP).

### Markov Decision Processes

An MDP is specified by the tuple $(\mathcal{S}, \mathcal{A}, P, R, \gamma)$:

- $\mathcal{S}$: state space (observations available to the agent),
- $\mathcal{A}$: action space,
- $P(s' \mid s, a)$: transition kernel (environment dynamics),
- $R(s, a) \in \mathbb{R}$: expected immediate reward for taking action $a$ in state $s$,
- $\gamma \in [0,1)$: discount factor that down-weights future rewards.

The agent follows a **policy** $\pi(a \mid s)$, a conditional distribution over actions given the state. The goal is to find the policy that maximises the **expected discounted return** $G_t = \sum_{k=0}^\infty \gamma^k R_{t+k}$.

### Value Functions and Bellman Equations

The **state-value function** of policy $\pi$ is the expected return from state $s$:

$$V^\pi(s) = \mathbb{E}_\pi\!\left[\sum_{k=0}^\infty \gamma^k R_{t+k} \;\middle|\; S_t = s\right]$$

The **action-value function** $Q^\pi(s,a) = \mathbb{E}_\pi[G_t \mid S_t = s, A_t = a]$ captures the expected return of taking action $a$ in state $s$ and thereafter following $\pi$. Both satisfy **Bellman equations** expressing the value of a state recursively in terms of successor states:

$$V^\pi(s) = \sum_a \pi(a\mid s)\sum_{s'} P(s'\mid s,a)\bigl[R(s,a) + \gamma V^\pi(s')\bigr]$$

$$Q^\pi(s,a) = \sum_{s'} P(s'\mid s,a)\bigl[R(s,a) + \gamma\sum_{a'}\pi(a'\mid s')Q^\pi(s',a')\bigr]$$

The **optimal value function** $V^*(s) = \max_\pi V^\pi(s)$ satisfies the **Bellman optimality equations**, a system of nonlinear fixed-point equations whose solution defines the **optimal policy** $\pi^*(a\mid s) = \arg\max_a Q^*(s,a)$.

### $Q$-Learning and Policy Gradient

When the transition kernel $P$ is unknown, **model-free** methods learn $Q^*$ directly from experience. **$Q$-learning** applies the update

$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha\bigl[r_t + \gamma\max_{a'}Q(s_{t+1}, a') - Q(s_t, a_t)\bigr]$$

The bracketed term is the **temporal-difference (TD) error** between the current estimate and the one-step bootstrapped target. When $Q$ is represented by a neural network — the **deep Q-network** (DQN) — this approach scales to high-dimensional state spaces such as order book snapshots.

**Policy gradient** methods directly parameterise the policy $\pi_\theta$ and maximise $J(\theta) = \mathbb{E}_{\pi_\theta}[G_0]$ by gradient ascent. The **policy gradient theorem** provides an unbiased gradient estimator:

$$\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta}\!\left[\nabla_\theta\log\pi_\theta(a\mid s)\cdot Q^{\pi_\theta}(s,a)\right]$$

which can be estimated from sampled trajectories without knowledge of $P$. **Actor-critic** methods combine a parameterised policy (the actor) with a learned value function (the critic) to reduce the variance of the policy gradient estimator, using the advantage $A^\pi(s,a) = Q^\pi(s,a) - V^\pi(s)$ instead of $Q^\pi$ as the learning signal. RL provides the theoretical basis for applications in market making and optimal execution, where a trading agent must take sequential decisions under uncertainty about the order flow and market impact.

## Exercises

1. **Bias–variance decomposition.** Consider estimating $f^*(x) = \sin(2\pi x)$ from $N=15$ noisy observations using polynomial regression of degree $M$ with OLS. (a) Sketch qualitatively how squared bias and variance change with $M$ and explain why. (b) Show that as $M \to N-1$, training error approaches zero. What happens to test error and why?

2. **Ridge shrinkage via SVD.** Using the SVD $\boldsymbol{\Phi} = \mathbf{U}\mathbf{S}\mathbf{V}^T$, show that the ridge predictor at a test point can be written as $\hat{f}_{\mathrm{ridge}}(\mathbf{x}) = \sum_j \frac{s_j^2}{s_j^2+\lambda}(\mathbf{u}_j^T\mathbf{y})\,\mathbf{v}_j^T\boldsymbol{\phi}(\mathbf{x})$ and compare the shrinkage factors to OLS. What happens to directions of very small singular value?

3. **Lasso sparsity via subgradients.** Using the KKT conditions for the lasso, show that the $j$-th coefficient satisfies $\hat{w}_j = 0$ if and only if $|\boldsymbol{\phi}_j^T(\mathbf{y} - \boldsymbol{\Phi}_{-j}\hat{\mathbf{w}}_{-j})| \leq \lambda/2$, where $\boldsymbol{\phi}_j$ is the $j$-th column of $\boldsymbol{\Phi}$ and $\hat{\mathbf{w}}_{-j}$ denotes all other coefficients. Interpret the condition in terms of the correlation between feature $j$ and the residuals.

4. **Kernel computation.** Verify that the polynomial kernel $k(\mathbf{x}, \mathbf{z}) = (\mathbf{x}^T\mathbf{z} + 1)^2$ for $\mathbf{x}, \mathbf{z} \in \mathbb{R}^2$ corresponds to the explicit feature map $\boldsymbol{\phi}(\mathbf{x}) = (x_1^2, x_2^2, \sqrt{2}x_1x_2, \sqrt{2}x_1, \sqrt{2}x_2, 1)^T$. What is the dimension of the feature space for a degree-$d$ polynomial kernel in $\mathbb{R}^D$?

5. **Gradient boosting.** Implement gradient boosting for a regression problem from scratch using $B = 100$ depth-1 trees (stumps) and squared-error loss. Plot ensemble predictions after 1, 10, 50, and 100 rounds and plot training and test error vs. boosting iteration. How does the learning rate $\eta$ affect convergence and overfitting behaviour?

6. **PCA as optimal compression.** Show that the rank-$M$ linear reconstruction $\hat{\mathbf{X}} = \mathbf{X}\mathbf{U}_M\mathbf{U}_M^T$ minimises $\|\mathbf{X} - \hat{\mathbf{X}}\|_F^2$ over all choices of $M$ orthonormal columns in $\mathbf{U}_M$. Express the minimum error in terms of the discarded eigenvalues of the sample covariance matrix.

7. **Bellman iteration.** For a two-state, two-action MDP with known $P$ and $R$, write the Bellman optimality equations explicitly and solve for $V^*(s_1), V^*(s_2)$. Verify that the greedy policy $\pi^*(a\mid s) = \arg\max_a Q^*(s,a)$ recovers the optimal policy found by exhaustive enumeration.
