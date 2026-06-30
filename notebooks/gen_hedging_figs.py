"""Generate all figures for the optimal_hedging chapter and the new ML chapter sections."""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.linalg import cholesky
from scipy.optimize import minimize
from sklearn.linear_model import Lasso, LassoCV, Ridge
import torch
import torch.nn as nn
import torch.optim as optim
from scipy.stats import norm

FIGDIR = "../markdown/figures"
np.random.seed(42)
plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})

# ─────────────────────────────────────────────
# FIGURE 1: PCA yield curve factors & hedge
# ─────────────────────────────────────────────
print("Figure 1: PCA factors...")

T_obs = 1000       # trading days
D = 20             # maturities (6m, 1y, ..., 10y in 0.5y steps)
maturities = np.linspace(0.5, 10, D)

# True factor structure: level, slope, curvature
sigma_level   = 0.006   # 6bp per day
sigma_slope   = 0.003
sigma_curve   = 0.001
sigma_idio    = 0.0005

# Factor loadings
def pc_level(t):  return np.ones_like(t)
def pc_slope(t):  return (t - t.mean()) / (t.max() - t.min())
def pc_curve(t):
    slope = pc_slope(t)
    return slope**2 - (slope**2).mean()

U = np.column_stack([
    pc_level(maturities) / np.linalg.norm(pc_level(maturities)),
    pc_slope(maturities) / np.linalg.norm(pc_slope(maturities)),
    pc_curve(maturities) / np.linalg.norm(pc_curve(maturities)),
])

# Simulate yield changes
F = np.column_stack([
    np.random.randn(T_obs) * sigma_level,
    np.random.randn(T_obs) * sigma_slope,
    np.random.randn(T_obs) * sigma_curve,
])
E = np.random.randn(T_obs, D) * sigma_idio
dR = F @ U.T + E  # (T_obs, D) yield changes in levels (not bps)

# Estimate PCA from data
Sigma = np.cov(dR.T)
eigvals, eigvecs = np.linalg.eigh(Sigma)
idx = np.argsort(eigvals)[::-1]
eigvals, eigvecs = eigvals[idx], eigvecs[:, idx]

# DV01 vector for a 7-year bond: roughly proportional to maturity weighting
def dv01_bond(maturity, coupon=0.05, notional=1e6):
    """Approximate DV01 as the PV01 weighting across a simple bond."""
    cash_times = np.arange(0.5, maturity + 0.01, 0.5)
    r = 0.04
    pv01 = np.zeros(D)
    for t_cf in cash_times:
        # Cash flow
        cf = coupon * 0.5 * notional if t_cf < maturity else (coupon * 0.5 + 1) * notional
        pv = cf * np.exp(-r * t_cf)
        # Map t_cf to nearest maturity index
        idx_m = np.argmin(np.abs(maturities - t_cf))
        pv01[idx_m] += pv * t_cf          # DV01 (dollar per unit yield change)
    return pv01

d_7y  = dv01_bond(7.0)
d_2y  = dv01_bond(2.0)
d_5y  = dv01_bond(5.0)
d_10y = dv01_bond(10.0)

# PnL series
pnl_7y = dR @ d_7y
pnl_2y = dR @ d_2y
pnl_5y = dR @ d_5y
pnl_10y = dR @ d_10y

# DV01 hedge: neutralize total DV01 only (single instrument: 5y)
h_dv01 = np.sum(d_7y) / np.sum(d_5y)
pnl_dv01_hedged = pnl_7y - h_dv01 * pnl_5y

# 3-factor PCA hedge using 2y, 5y, 10y
hedge_pnls = np.column_stack([pnl_2y, pnl_5y, pnl_10y])
hedge_pvecs = np.column_stack([d_2y, d_5y, d_10y])

# Factor sensitivities
d7_factors = eigvecs[:, :3].T @ d_7y   # (3,)
hedge_factors = eigvecs[:, :3].T @ hedge_pvecs  # (3, 3) - factor sensitivities of hedges

h_pca = np.linalg.solve(hedge_factors, d7_factors)   # solve Ah=b
pnl_pca_hedged = pnl_7y - hedge_pnls @ h_pca

# Explained variance
cumvar = np.cumsum(eigvals) / np.sum(eigvals)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Top-left: sample yield curves
ax = axes[0, 0]
r_base = np.linspace(0.02, 0.05, D)
for i in range(0, T_obs, 100):
    curve = r_base + np.cumsum(dR[i]) * 5
    ax.plot(maturities, curve * 100, color='steelblue', alpha=0.2, linewidth=0.7)
ax.set_xlabel('Maturity (years)')
ax.set_ylabel('Yield (%)')
ax.set_title('Sample Yield Curves')

# Top-right: PCA eigenvectors
ax = axes[0, 1]
labels = ['Level (PC1)', 'Slope (PC2)', 'Curvature (PC3)']
colors = ['steelblue', 'darkorange', 'seagreen']
for k, (lbl, col) in enumerate(zip(labels, colors)):
    ax.plot(maturities, eigvecs[:, k] / np.abs(eigvecs[:, k]).max(),
            label=lbl, color=col, linewidth=2)
ax.axhline(0, color='grey', linewidth=0.5, linestyle='--')
ax.set_xlabel('Maturity (years)')
ax.set_ylabel('Loading (normalised)')
ax.set_title('PCA Eigenvectors')
ax.legend(fontsize=9)

# Bottom-left: P&L distributions
ax = axes[1, 0]
ax.hist(pnl_7y, bins=60, alpha=0.5, color='grey', label='No hedge', density=True)
ax.hist(pnl_dv01_hedged, bins=60, alpha=0.6, color='steelblue', label='DV01 hedge (5y)', density=True)
ax.hist(pnl_pca_hedged, bins=60, alpha=0.6, color='darkorange', label='3-factor PCA hedge', density=True)
ax.set_xlabel('Daily P&L (USD)')
ax.set_ylabel('Density')
ax.set_title('Hedge Performance (P&L Distribution)')
ax.legend(fontsize=9)
sd_nohedge = np.std(pnl_7y)
sd_dv01    = np.std(pnl_dv01_hedged)
sd_pca     = np.std(pnl_pca_hedged)
ax.text(0.98, 0.97,
        f'σ no hedge: ${sd_nohedge:,.0f}\nσ DV01: ${sd_dv01:,.0f}\nσ PCA:  ${sd_pca:,.0f}',
        transform=ax.transAxes, ha='right', va='top', fontsize=8, family='monospace',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Bottom-right: cumulative explained variance
ax = axes[1, 1]
ax.plot(np.arange(1, D+1), cumvar * 100, color='steelblue', linewidth=2, marker='o', markersize=4)
ax.axhline(95, color='grey', linestyle='--', linewidth=0.8, label='95% threshold')
ax.axvline(3, color='darkorange', linestyle='--', linewidth=0.8, label='3 factors')
ax.set_xlabel('Number of PC factors')
ax.set_ylabel('Cumulative explained variance (%)')
ax.set_title('PCA Explained Variance')
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig(f'{FIGDIR}/hedg_pca_factors.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"  σ: no hedge=${sd_nohedge:,.0f}, DV01=${sd_dv01:,.0f}, PCA=${sd_pca:,.0f}")

# ─────────────────────────────────────────────
# FIGURE 2: Lasso hedging
# ─────────────────────────────────────────────
print("Figure 2: Lasso hedging...")

# Use bonds of maturities 1y, 1.5y, ..., 6y, 8y, 9y, 10y as hedge instruments
# (12 instruments, all DV01 vectors consistent with pnl_7y)
hedge_maturities = list(np.arange(1.0, 6.5, 0.5)) + [8.0, 9.0, 10.0]
K_hedge = len(hedge_maturities)
hedge_pvecs_lasso = np.column_stack([dv01_bond(m) for m in hedge_maturities])
pnl_hedges = dR @ hedge_pvecs_lasso   # (T_obs, K_hedge), dollars consistent with pnl_7y

Sigma_HH = np.cov(pnl_hedges.T)
sigma_XH  = np.cov(pnl_7y, pnl_hedges.T)[0, 1:]   # (K_hedge,)

# Min-variance hedge (full OLS)
h_mv = np.linalg.solve(Sigma_HH, sigma_XH)
pnl_mv = pnl_7y - pnl_hedges @ h_mv

# Lasso path
lambdas = np.logspace(-2, 1, 80) * np.std(pnl_7y)
lasso_coefs = []
residual_vars = []
gross_notionals = []
for lam in lambdas:
    lasso = Lasso(alpha=lam, fit_intercept=False, max_iter=10000)
    lasso.fit(pnl_hedges, pnl_7y)
    lasso_coefs.append(lasso.coef_.copy())
    pnl_lasso = pnl_7y - pnl_hedges @ lasso.coef_
    residual_vars.append(np.var(pnl_lasso))
    gross_notionals.append(np.sum(np.abs(lasso.coef_)))

lasso_coefs = np.array(lasso_coefs)
var_nohedge = np.var(pnl_7y)
var_mv      = np.var(pnl_mv)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

# Lasso path
ax = axes[0]
colors_lasso = plt.cm.tab10(np.linspace(0, 1, K_hedge))
for j in range(K_hedge):
    ax.plot(lambdas / np.std(pnl_7y), lasso_coefs[:, j], color=colors_lasso[j], linewidth=1.5)
ax.set_xscale('log')
ax.set_xlabel('λ / σ_X')
ax.set_ylabel('Hedge coefficient')
ax.set_title('Lasso Hedge Path')
ax.axvline(1.0, color='grey', linestyle='--', linewidth=0.8)

# Residual variance vs lambda
ax = axes[1]
ax.plot(lambdas / np.std(pnl_7y), np.array(residual_vars) / var_nohedge * 100,
        color='steelblue', linewidth=2)
ax.axhline(var_mv / var_nohedge * 100, color='darkorange', linestyle='--',
           linewidth=1.5, label=f'Min-variance ({var_mv/var_nohedge*100:.0f}%)')
ax.axhline(100, color='grey', linestyle=':', linewidth=1, label='No hedge (100%)')
ax.set_xscale('log')
ax.set_xlabel('λ / σ_X')
ax.set_ylabel('Residual variance (% of unhedged)')
ax.set_title('Residual Variance vs Sparsity')
ax.legend(fontsize=9)

# Efficiency frontier: residual variance vs gross notional
ax = axes[2]
nz_counts = np.sum(np.abs(lasso_coefs) > 1e-6, axis=1)
sc = ax.scatter(gross_notionals, np.array(residual_vars) / var_nohedge * 100,
                c=nz_counts, cmap='plasma', s=25, zorder=3)
ax.axhline(var_mv / var_nohedge * 100, color='darkorange', linestyle='--',
           linewidth=1.2, label='Min-variance')
ax.set_xlabel('Gross notional of hedge')
ax.set_ylabel('Residual variance (%)')
ax.set_title('Efficiency Frontier')
plt.colorbar(sc, ax=ax, label='Active instruments')
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig(f'{FIGDIR}/hedg_lasso.png', dpi=150, bbox_inches='tight')
plt.close()

# ─────────────────────────────────────────────
# FIGURE 3: Pre-hedging
# ─────────────────────────────────────────────
print("Figure 3: Pre-hedging...")

def optimal_prehedge_fraction(p, cost_to_risk):
    """
    Analytical approximation to the optimal pre-hedge fraction phi*
    as a function of probability p and cost_to_risk ratio c/(gamma*sigma^2*T).
    Based on the Muhle-Karbe et al. wealth-transfer model:
    phi* = p / (1 + cost_to_risk)
    (simplified single-period version)
    """
    return p / (1 + cost_to_risk)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# phi* vs probability
ax = axes[0]
probs = np.linspace(0, 1, 200)
for ratio, lbl, col in [(0.1, 'c/risk = 0.1', 'steelblue'),
                          (0.5, 'c/risk = 0.5', 'darkorange'),
                          (1.0, 'c/risk = 1.0', 'seagreen'),
                          (2.0, 'c/risk = 2.0', 'firebrick')]:
    phi = optimal_prehedge_fraction(probs, ratio)
    ax.plot(probs, phi, label=lbl, color=col, linewidth=2)
ax.plot(probs, probs, color='grey', linestyle='--', linewidth=1, label='φ* = p (no cost)')
ax.set_xlabel('Probability of order materialising (p)')
ax.set_ylabel('Optimal pre-hedge fraction φ*')
ax.set_title('Pre-hedge Fraction vs Order Probability')
ax.legend(fontsize=9)
ax.set_xlim(0, 1); ax.set_ylim(0, 1)

# phi* vs cost-to-risk ratio
ax = axes[1]
cost_ratios = np.linspace(0, 3, 200)
for prob, lbl, col in [(1.0, 'p = 1.0', 'steelblue'),
                         (0.75, 'p = 0.75', 'darkorange'),
                         (0.5, 'p = 0.50', 'seagreen'),
                         (0.25, 'p = 0.25', 'firebrick')]:
    phi = optimal_prehedge_fraction(prob, cost_ratios)
    ax.plot(cost_ratios, phi, label=lbl, color=col, linewidth=2)
ax.set_xlabel('Cost-to-risk ratio $c / (\\gamma \\sigma^2 T)$')
ax.set_ylabel('Optimal pre-hedge fraction φ*')
ax.set_title('Pre-hedge Fraction vs Transaction Cost')
ax.legend(fontsize=9)
ax.set_xlim(0, 3); ax.set_ylim(0, 1)

plt.tight_layout()
plt.savefig(f'{FIGDIR}/hedg_prehedge.png', dpi=150, bbox_inches='tight')
plt.close()

# ─────────────────────────────────────────────
# FIGURE 4: Delta hedging
# ─────────────────────────────────────────────
print("Figure 4: Delta hedging...")

# BSM functions
def bsm_price(S, K, T, sigma, r=0.0, cp=1):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if cp == 1:
        return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    else:
        return K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

def bsm_delta(S, K, T, sigma, r=0.0, cp=1):
    if T <= 0:
        return float(cp == 1 and S > K)
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma * np.sqrt(T))
    return norm.cdf(d1) if cp == 1 else norm.cdf(d1) - 1

def bsm_gamma(S, K, T, sigma, r=0.0):
    if T <= 0:
        return 0.0
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma * np.sqrt(T))
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

# Simulate GBM paths
S0, K, T_opt, sigma, r = 100., 100., 1.0, 0.2, 0.0
dt = 1/252
n_steps = int(T_opt / dt)
n_paths = 5000
np.random.seed(42)

dW = np.random.randn(n_paths, n_steps) * np.sqrt(dt)
log_returns = (r - 0.5*sigma**2)*dt + sigma*dW
S_paths = S0 * np.exp(np.cumsum(log_returns, axis=1))
S_paths = np.column_stack([np.full(n_paths, S0), S_paths])  # (n_paths, n_steps+1)

option_price0 = bsm_price(S0, K, T_opt, sigma, r)

def simulate_delta_hedging(S_paths, K, T_opt, sigma, r, rebal_freq, tc=0.0):
    """Compute P&L of delta-hedging a short call at given rebalancing frequency."""
    n_paths, n_full = S_paths.shape
    n_steps_full = n_full - 1
    n_steps_rebal = n_steps_full // rebal_freq
    pnls = np.zeros(n_paths)

    for i in range(n_paths):
        S = S_paths[i]
        t_rebal = np.arange(0, n_steps_full + 1, rebal_freq)
        cash = option_price0  # received premium
        delta = 0.0
        for idx_t, step in enumerate(t_rebal[:-1]):
            t = step * dt
            T_rem = T_opt - t
            S_t = S[step]
            delta_new = bsm_delta(S_t, K, T_rem, sigma, r, cp=1)
            delta_change = delta_new - delta
            # Transaction cost
            cash -= tc * abs(delta_change) * S_t
            # Stock position cost
            cash -= delta_change * S_t
            cash *= np.exp(r * rebal_freq * dt)  # risk-free growth
            delta = delta_new
        # Unwind at expiry
        S_T = S[-1]
        cash += delta * S_T
        # Pay payoff
        payoff = max(S_T - K, 0)
        pnls[i] = cash - payoff
    return pnls

print("  Simulating delta hedging (daily)...")
pnl_daily    = simulate_delta_hedging(S_paths, K, T_opt, sigma, r, rebal_freq=1,  tc=0.0)
print("  Simulating delta hedging (weekly)...")
pnl_weekly   = simulate_delta_hedging(S_paths, K, T_opt, sigma, r, rebal_freq=5,  tc=0.0)
print("  Simulating delta hedging (monthly)...")
pnl_monthly  = simulate_delta_hedging(S_paths, K, T_opt, sigma, r, rebal_freq=21, tc=0.0)
print("  Simulating delta hedging (WW band, tc=0.1%)...")
pnl_ww       = simulate_delta_hedging(S_paths, K, T_opt, sigma, r, rebal_freq=1,  tc=0.001)

# Gamma-theta P&L along one path
path_idx = 42
S_path = S_paths[path_idx]
pnl_gt_series = []
for step in range(n_steps):
    t = step * dt
    T_rem = T_opt - t - dt
    if T_rem <= 0:
        break
    S_t = S_path[step]
    S_tp1 = S_path[step + 1]
    gamma_t = bsm_gamma(S_t, K, T_rem + dt, sigma, r)
    sigma_realized = abs(np.log(S_tp1/S_t)) / np.sqrt(dt)
    sigma_implied = sigma
    pnl_gt = 0.5 * gamma_t * S_t**2 * (sigma_realized**2 - sigma_implied**2) * dt
    pnl_gt_series.append(pnl_gt)
pnl_gt_series = np.array(pnl_gt_series)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# P&L distributions
ax = axes[0]
bins = np.linspace(-10, 10, 80)
ax.hist(pnl_daily,   bins=bins, alpha=0.5, density=True, color='steelblue',  label=f'Daily (σ={np.std(pnl_daily):.2f})')
ax.hist(pnl_weekly,  bins=bins, alpha=0.5, density=True, color='darkorange', label=f'Weekly (σ={np.std(pnl_weekly):.2f})')
ax.hist(pnl_monthly, bins=bins, alpha=0.5, density=True, color='seagreen',   label=f'Monthly (σ={np.std(pnl_monthly):.2f})')
ax.hist(pnl_ww,      bins=bins, alpha=0.5, density=True, color='firebrick',  label=f'WW band tc=0.1% (σ={np.std(pnl_ww):.2f})')
ax.set_xlabel('Hedging P&L ($)')
ax.set_ylabel('Density')
ax.set_title('Delta Hedging P&L Distributions')
ax.legend(fontsize=8)
ax.axvline(0, color='black', linewidth=0.5)

# Gamma-theta decomposition
ax = axes[1]
cumulative_pnl = np.cumsum(pnl_gt_series)
t_ax = np.arange(len(pnl_gt_series)) * dt
ax.bar(t_ax, pnl_gt_series, width=dt, color=np.where(pnl_gt_series > 0, 'steelblue', 'firebrick'),
       alpha=0.7, label='Gamma-theta P&L per step')
ax.plot(t_ax, cumulative_pnl, color='black', linewidth=1.5, label='Cumulative P&L')
ax.axhline(0, color='grey', linewidth=0.5)
ax.set_xlabel('Time (years)')
ax.set_ylabel('P&L ($)')
ax.set_title('Gamma–Theta P&L Decomposition (Single Path)')
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig(f'{FIGDIR}/hedg_delta_hedging.png', dpi=150, bbox_inches='tight')
plt.close()

# ─────────────────────────────────────────────
# FIGURE 5: Deep Hedging
# ─────────────────────────────────────────────
print("Figure 5: Deep hedging (PyTorch)...")

torch.manual_seed(42)
np.random.seed(42)

S0, K, T_opt, sigma_true, r = 100., 100., 1.0, 0.2, 0.0
n_steps_dh = 30  # monthly rebalancing
dt_dh = T_opt / n_steps_dh
tc_dh = 0.001   # 0.1% transaction cost
n_train = 4000
n_test  = 2000
gamma_ra = 0.1   # risk aversion for entropic measure

def simulate_gbm(n_paths, n_steps, S0, sigma, r, dt, seed=None):
    if seed is not None:
        torch.manual_seed(seed)
    dW = torch.randn(n_paths, n_steps) * np.sqrt(dt)
    log_S = (r - 0.5*sigma**2)*dt + sigma*dW
    S = S0 * torch.exp(torch.cumsum(log_S, dim=1))
    S = torch.cat([torch.full((n_paths, 1), S0), S], dim=1)
    return S  # (n_paths, n_steps+1)

class HedgingPolicy(nn.Module):
    def __init__(self, n_features=3, hidden=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_features, hidden),
            nn.Tanh(),
            nn.Linear(hidden, hidden),
            nn.Tanh(),
            nn.Linear(hidden, 1),
            nn.Sigmoid()   # delta in [0,1]
        )

    def forward(self, moneyness, time_rem, prev_delta):
        x = torch.stack([moneyness, time_rem, prev_delta], dim=1)
        return self.net(x).squeeze(-1)

def compute_pnl(S, policy, premium, n_steps, dt, tc):
    n_paths = S.shape[0]
    cash = torch.full((n_paths,), premium)
    delta = torch.zeros(n_paths)

    for t in range(n_steps):
        t_rem = torch.tensor((n_steps - t) / n_steps, dtype=torch.float32)
        moneyness = torch.log(S[:, t] / K)
        t_rem_tensor = t_rem.expand(n_paths)
        delta_new = policy(moneyness, t_rem_tensor, delta.detach())
        delta_change = delta_new - delta
        cash = cash - tc * torch.abs(delta_change) * S[:, t]
        cash = cash - delta_change * S[:, t]
        cash = cash * np.exp(r * dt)
        delta = delta_new

    # Final payoff
    payoff = torch.clamp(S[:, -1] - K, min=0)
    cash = cash + delta * S[:, -1]
    pnl = cash - payoff
    return pnl

# BSM-computed premium
premium_tensor = float(bsm_price(S0, K, T_opt, sigma_true, r))

# Generate training data
S_train = simulate_gbm(n_train, n_steps_dh, S0, sigma_true, r, dt_dh, seed=42)

# Train deep hedging policy
policy = HedgingPolicy(n_features=3, hidden=64)
optimizer = optim.Adam(policy.parameters(), lr=1e-3)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=100, gamma=0.8)

n_epochs = 300
batch_size = 512
losses = []

print("  Training deep hedging policy...")
for epoch in range(n_epochs):
    idx = torch.randperm(n_train)[:batch_size]
    S_batch = S_train[idx]
    pnl = compute_pnl(S_batch, policy, premium_tensor, n_steps_dh, dt_dh, tc_dh)
    # Variance risk measure
    loss = -pnl.mean() + gamma_ra * pnl.var()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    scheduler.step()
    if epoch % 30 == 0:
        losses.append(loss.item())
        print(f"    Epoch {epoch:3d}: loss={loss.item():.4f}")

# Evaluate on test set
S_test = simulate_gbm(n_test, n_steps_dh, S0, sigma_true, r, dt_dh, seed=99)

with torch.no_grad():
    pnl_dh_test = compute_pnl(S_test, policy, premium_tensor, n_steps_dh, dt_dh, tc_dh).numpy()

# BSM delta hedge on test set (using exact formula)
def bsm_delta_policy_pnl(S_paths_np, K, T, sigma, r, dt, tc, premium):
    n_paths, n_steps1 = S_paths_np.shape
    n_steps = n_steps1 - 1
    pnls = np.zeros(n_paths)
    for i in range(n_paths):
        cash = premium
        delta = 0.0
        for t in range(n_steps):
            T_rem = (n_steps - t) * dt
            S_t = S_paths_np[i, t]
            delta_new = bsm_delta(S_t, K, T_rem, sigma, r, cp=1)
            delta_change = delta_new - delta
            cash -= tc * abs(delta_change) * S_t
            cash -= delta_change * S_t
            cash *= np.exp(r * dt)
            delta = delta_new
        cash += delta * S_paths_np[i, -1]
        pnls[i] = cash - max(S_paths_np[i, -1] - K, 0)
    return pnls

print("  Computing BSM hedge P&L...")
S_test_np = S_test.numpy()
pnl_bsm_test = bsm_delta_policy_pnl(S_test_np, K, T_opt, sigma_true, r, dt_dh, tc_dh, premium_tensor)

# Learned delta vs BSM delta at t=0
moneyness_range = np.linspace(-0.5, 0.5, 100)
bsm_deltas = [bsm_delta(S0 * np.exp(m), K, T_opt/2, sigma_true, r) for m in moneyness_range]

with torch.no_grad():
    m_t = torch.tensor(moneyness_range, dtype=torch.float32)
    t_r = torch.full_like(m_t, 0.5)
    pd_t = torch.zeros_like(m_t)
    dh_deltas = policy(m_t, t_r, pd_t).numpy()

# CVaR at 95%
def cvar95(x):
    q = np.percentile(x, 5)
    return -np.mean(x[x <= q])

print(f"  Deep hedging: mean={pnl_dh_test.mean():.3f}, CVaR95={cvar95(pnl_dh_test):.3f}")
print(f"  BSM delta:    mean={pnl_bsm_test.mean():.3f}, CVaR95={cvar95(pnl_bsm_test):.3f}")

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

ax = axes[0]
bins = np.linspace(-15, 10, 70)
ax.hist(pnl_bsm_test, bins=bins, alpha=0.6, density=True, color='steelblue',
        label=f'BSM Δ (CVaR95={cvar95(pnl_bsm_test):.2f})')
ax.hist(pnl_dh_test,  bins=bins, alpha=0.6, density=True, color='darkorange',
        label=f'Deep Hedge (CVaR95={cvar95(pnl_dh_test):.2f})')
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel('Hedging P&L ($)')
ax.set_ylabel('Density')
ax.set_title('P&L Distribution (tc = 0.1%)')
ax.legend(fontsize=9)

ax = axes[1]
epoch_ax = np.arange(0, n_epochs, 30)
ax.plot(epoch_ax, losses, color='steelblue', linewidth=2, marker='o', markersize=4)
ax.set_xlabel('Training epoch')
ax.set_ylabel('Risk-adjusted loss')
ax.set_title('Deep Hedging Training Curve')

ax = axes[2]
ax.plot(moneyness_range, bsm_deltas, color='steelblue', linewidth=2, linestyle='--',
        label='BSM delta')
ax.plot(moneyness_range, dh_deltas, color='darkorange', linewidth=2,
        label='Learned policy (t = T/2)')
ax.set_xlabel('Log-moneyness ln(S/K)')
ax.set_ylabel('Delta')
ax.set_title('Hedge Ratio vs Moneyness')
ax.legend(fontsize=9)
ax.set_ylim(-0.05, 1.05)

plt.tight_layout()
plt.savefig(f'{FIGDIR}/hedg_deep_hedging.png', dpi=150, bbox_inches='tight')
plt.close()

# ─────────────────────────────────────────────
# FIGURE 6: Autoencoder (for data_driven_methods)
# ─────────────────────────────────────────────
print("Figure 6: Autoencoder...")
torch.manual_seed(0)
np.random.seed(0)

D_ae = 20
M_ae = 3
T_ae = 2000

# Simulate yield curves from a 3-factor model
sigma_ae = np.array([0.006, 0.003, 0.001])
U_ae = np.column_stack([
    pc_level(maturities) / np.linalg.norm(pc_level(maturities)),
    pc_slope(maturities) / np.linalg.norm(pc_slope(maturities)),
    pc_curve(maturities) / np.linalg.norm(pc_curve(maturities)),
])
F_ae = np.random.randn(T_ae, 3) * sigma_ae
E_ae = np.random.randn(T_ae, D_ae) * 0.0004
# Introduce slight nonlinearity
curves_ae = F_ae @ U_ae.T + E_ae + 0.5 * (F_ae[:, :1] @ F_ae[:, 1:2].T)[:T_ae, :T_ae].diagonal()[:, None] * 0.0001

X_ae = torch.tensor(curves_ae, dtype=torch.float32)
X_mean = X_ae.mean(0)
X_std  = X_ae.std(0)
X_norm = (X_ae - X_mean) / (X_std + 1e-8)

# Build autoencoder
class Autoencoder(nn.Module):
    def __init__(self, D, M, hidden=32):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(D, hidden), nn.Tanh(),
            nn.Linear(hidden, M)
        )
        self.decoder = nn.Sequential(
            nn.Linear(M, hidden), nn.Tanh(),
            nn.Linear(hidden, D)
        )
    def forward(self, x):
        z = self.encoder(x)
        return self.decoder(z), z

ae = Autoencoder(D_ae, M_ae, hidden=32)
opt_ae = optim.Adam(ae.parameters(), lr=1e-3)
for epoch in range(600):
    idx = torch.randperm(T_ae)[:256]
    xb = X_norm[idx]
    xhat, _ = ae(xb)
    loss_ae = ((xb - xhat)**2).mean()
    opt_ae.zero_grad()
    loss_ae.backward()
    opt_ae.step()

ae.eval()
with torch.no_grad():
    x_test = X_norm[1500:1510]
    xhat_test, z_test = ae(x_test)
    _, z_all = ae(X_norm)
    z_all_np = z_all.numpy()

x_test_np = (x_test.numpy() * (X_std.numpy() + 1e-8) + X_mean.numpy())
xhat_np   = (xhat_test.numpy() * (X_std.numpy() + 1e-8) + X_mean.numpy())

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

ax = axes[0]
for i in range(3):
    ax.plot(maturities, x_test_np[i] * 100, color='steelblue', linewidth=1.5,
            alpha=0.8, label='True' if i == 0 else None)
    ax.plot(maturities, xhat_np[i] * 100, color='darkorange', linewidth=1.5,
            linestyle='--', alpha=0.8, label='Reconstructed' if i == 0 else None)
ax.set_xlabel('Maturity (years)')
ax.set_ylabel('Yield change (bp equivalent)')
ax.set_title('Autoencoder Reconstruction (M=3 latent dims)')
ax.legend(fontsize=9)

ax = axes[1]
t_ax_ae = np.arange(T_ae) / 252
labels_ae = ['Latent z₁ (level)', 'Latent z₂ (slope)', 'Latent z₃ (curvature)']
colors_ae = ['steelblue', 'darkorange', 'seagreen']
for k, (lbl, col) in enumerate(zip(labels_ae, colors_ae)):
    ax.plot(t_ax_ae, z_all_np[:, k], color=col, linewidth=0.8, alpha=0.7, label=lbl)
ax.set_xlabel('Time (years)')
ax.set_ylabel('Latent code value')
ax.set_title('Latent Factor Time Series')
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig(f'{FIGDIR}/ddm_autoencoder.png', dpi=150, bbox_inches='tight')
plt.close()

# ─────────────────────────────────────────────
# FIGURE 7: Monotone neural network (for data_driven_methods)
# ─────────────────────────────────────────────
print("Figure 7: Monotone neural network...")
torch.manual_seed(3)
np.random.seed(3)

# Generate BSM call prices on a grid
S_vals = np.linspace(60, 140, 30)
T_vals = np.array([0.1, 0.25, 0.5, 1.0, 1.5, 2.0])
K_mn   = 100.0
sig_mn = 0.2
r_mn   = 0.0

rows = []
for S_v in S_vals:
    for T_v in T_vals:
        C = bsm_price(S_v, K_mn, T_v, sig_mn, r_mn)
        delta_true = bsm_delta(S_v, K_mn, T_v, sig_mn, r_mn)
        rows.append([S_v / K_mn, T_v, C / K_mn, delta_true])
rows = np.array(rows)

X_mn = torch.tensor(rows[:, :2], dtype=torch.float32)  # (S/K, T)
y_mn = torch.tensor(rows[:, 2], dtype=torch.float32)

# Standard MLP
class StandardMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 32), nn.Tanh(),
            nn.Linear(32, 32), nn.Tanh(),
            nn.Linear(32, 1), nn.ReLU()
        )
    def forward(self, x):
        return self.net(x).squeeze(-1)

# Monotone MLP: non-negative weights for input S/K (index 0), free for T (index 1)
class MonotoneMLP(nn.Module):
    def __init__(self, hidden=32):
        super().__init__()
        # Separate weight paths: constrained (for S/K) and unconstrained (for T and bias)
        self.W1_constrained = nn.Parameter(torch.randn(hidden, 1) * 0.3)   # for S/K
        self.W1_free = nn.Parameter(torch.randn(hidden, 1) * 0.3)           # for T
        self.b1 = nn.Parameter(torch.zeros(hidden))
        self.W2 = nn.Parameter(torch.randn(hidden, hidden) * 0.1)
        self.b2 = nn.Parameter(torch.zeros(hidden))
        self.W3 = nn.Parameter(torch.randn(1, hidden) * 0.1)
        self.b3 = nn.Parameter(torch.zeros(1))

    def forward(self, x):
        S = x[:, :1]   # moneyness
        T = x[:, 1:]   # time
        W1_pos = torch.exp(self.W1_constrained)  # always positive
        h = torch.tanh(S @ W1_pos.T + T @ self.W1_free.T + self.b1)
        W2_pos = torch.exp(self.W2)
        h = torch.tanh(h @ W2_pos.T + self.b2)
        out = torch.relu(h @ self.W3.T + self.b3).squeeze(-1)
        return out

mlp_std  = StandardMLP()
mlp_mono = MonotoneMLP(hidden=32)

for model, name in [(mlp_std, 'standard'), (mlp_mono, 'monotone')]:
    opt_m = optim.Adam(model.parameters(), lr=5e-3)
    for ep in range(2000):
        pred = model(X_mn)
        loss_m = ((pred - y_mn)**2).mean()
        opt_m.zero_grad()
        loss_m.backward()
        opt_m.step()
    print(f"  {name} MLP: train MSE = {loss_m.item():.6f}")

# Evaluate on dense grid
S_dense = np.linspace(50, 160, 200)
T_fixed = 0.5
X_dense = torch.tensor(np.column_stack([S_dense / K_mn, np.full(200, T_fixed)]),
                        dtype=torch.float32)
X_dense.requires_grad_(True)

with torch.no_grad():
    y_bsm_dense    = np.array([bsm_price(s, K_mn, T_fixed, sig_mn, r_mn) / K_mn for s in S_dense])
    delta_bsm_dense = np.array([bsm_delta(s, K_mn, T_fixed, sig_mn, r_mn) for s in S_dense])

# Gradients via autograd
def get_delta(model, X):
    X_g = X.clone().detach().requires_grad_(True)
    out = model(X_g)
    out.sum().backward()
    return X_g.grad[:, 0].detach().numpy() / (1 / K_mn)   # d(C/K)/d(S/K) = dC/dS

y_std_dense  = mlp_std(X_dense.detach()).detach().numpy()
y_mono_dense = mlp_mono(X_dense.detach()).detach().numpy()
delta_std    = get_delta(mlp_std,  X_dense)
delta_mono   = get_delta(mlp_mono, X_dense)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

ax = axes[0]
ax.plot(S_dense, y_bsm_dense * K_mn,    color='black',      linewidth=2,  label='BSM (ground truth)')
ax.plot(S_dense, y_std_dense * K_mn,    color='steelblue',  linewidth=1.5, linestyle='--', label='Standard MLP')
ax.plot(S_dense, y_mono_dense * K_mn,   color='darkorange', linewidth=1.5, linestyle=':',  label='Monotone MLP')
ax.set_xlabel('Spot price $S$')
ax.set_ylabel('Call price $C$ ($)')
ax.set_title('Call Price Approximation ($T=0.5$)')
ax.legend(fontsize=9)
ax.set_xlim(50, 160)

ax = axes[1]
ax.plot(S_dense, delta_bsm_dense, color='black',      linewidth=2,  label='BSM delta')
ax.plot(S_dense, delta_std,       color='steelblue',  linewidth=1.5, linestyle='--', label='Standard MLP delta')
ax.plot(S_dense, delta_mono,      color='darkorange', linewidth=1.5, linestyle=':',  label='Monotone MLP delta')
ax.axhline(0, color='grey', linewidth=0.5); ax.axhline(1, color='grey', linewidth=0.5)
ax.fill_between(S_dense, 0, 1, alpha=0.05, color='green', label='Valid range [0,1]')
ax.set_xlabel('Spot price $S$')
ax.set_ylabel('Delta $\\partial C / \\partial S$')
ax.set_title('Delta Comparison (Standard vs Monotone MLP)')
ax.legend(fontsize=9)
ax.set_xlim(50, 160)
ax.set_ylim(-0.2, 1.3)

plt.tight_layout()
plt.savefig(f'{FIGDIR}/ddm_monotone_nn.png', dpi=150, bbox_inches='tight')
plt.close()

print("\nAll figures saved successfully.")
