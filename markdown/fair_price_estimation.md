# Introduction

# Pricing of flow products

## The Kalman Filter model for pricing

### Two correlated instruments

$$\begin{aligned}
K_t = \frac{1}{(\sigma_{v,1}^2 + (\sigma_{1,t}^{t-1})^2)(\sigma_{v,2}^2 + (\sigma_{2,t}^{t-1})^2) -  (\rho_t^{t-1}\sigma_{1,t}^{t-1}\sigma_{2,t}^{t-1})^2} \nonumber \\
\begin{pmatrix} 
(\sigma_{1,t}^{t-1})^2 \sigma_{v,2}^2 + (\sigma_{1,t}^{t-1})^2(\sigma_{2,t}^{t-1})^2(1- (\rho_t^{t-1})^2) &  \rho_t^{t-1} \sigma_{1,t}^{t-1}\sigma_{2,t}^{t-1}\sigma_{v,1}^2 \\ 
  \rho_t^{t-1} \sigma_{1,t}^{t-1}\sigma_{2,t}^{t-1}\sigma_{v,1}^2 & (\sigma_{2,t}^{t-1})^2\sigma_{v,1}^2 + (\sigma_{1,t}^{t-1})^2 (\sigma_{2,t}^{t-1})^2)(1-(\rho_t^{t-1})^2)
  \nonumber \\
\end{pmatrix}
\end{aligned}$$

For the case in which $\sigma_{v,2} = 0$ let us see the effect of the
observation of the second instrument on the first one: $$\begin{aligned}
\hat{P}^{t}_{1,t} = \hat{P}^{t-1}_{1,t} + \frac{1}{1-(\rho_t^{t-1})^2 + (\frac{\sigma_{v,1}}{\sigma_{1,t}^{t-1}})^2}\left((1-(\rho_t^{t-1})^2)(O_{1,t} - \hat{P}^{t}_{1,t}) + \rho_t^{t-1} \frac{\sigma_{v,1}^2}{\sigma_{1,t}^{t-1} \sigma_{2,t}^{t-1}}(O_{2,t} - \hat{P}^{t}_{2,t})  \right)  \nonumber \\
\end{aligned}$$

## Pricing sources and models

### Composites

### RfQs

### Trades

### LOBs

### HitMiss

### Correlated instruments

# Derivatives pricing

## The Black Scholes model

# Appendix: The Feynman - Kac Theorem

# Exercises
