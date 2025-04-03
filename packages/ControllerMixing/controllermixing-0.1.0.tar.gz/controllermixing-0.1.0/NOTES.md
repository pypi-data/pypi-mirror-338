# Package Notes

## Overview

Best practice is to follow the example in the notebook:  
`controllers/Notebooks/Example_NoSlack.ipynb`

The goal of this package is to:

- Fit continuous controllers of a **proportional-integral** nature.
- Estimate the **mixing coefficient** that determines how each controller contributes to the actor's control at each moment \( t \).

---

## Required Input Format

### 1. Input Trials

`Xdsgn` should be a list of trials with the following **pre-computed columns**:

```
'prey1Xaccel', 'prey1Xpos', 'prey1Xvel',
'prey1Yaccel', 'prey1Ypos', 'prey1Yvel',
'prey2Xaccel', 'prey2Xpos', 'prey2Xvel',
'prey2Yaccel', 'prey2Ypos', 'prey2Yvel',
'selfXpos', 'selfXvel', 'selfYaccel',
'selfYpos', 'selfYvel'
```

### 2. Preprocessing Step

Before computing derivatives, **rescale positions** to avoid gradient explosions:

```python
rescale = 0.001
selfpos['selfXpos'] *= rescale
selfpos['selfYpos'] *= rescale
```

_Do the same for prey positions._

---

## Optimizer & Regularization Settings

Defined in `cfgparams`. The loss is implemented in `JaxMod.create_loss_function_inner_bayes`.

### Loss Function (JAX)

```python
# Negative log-likelihood
residuals = u_out - u_obs
log_likelihood = -0.5 * jnp.log(2 * jnp.pi) - 0.5 * jnp.sum(residuals ** 2)

# Regularization term using GMF prior
if use_gmf_prior:
    S_x = generate_smoothing_penalty(num_rbfs)
    gmf_prior = -0.5 * (weights @ S_x @ weights.T)
else:
    gmf_prior = 0.0

# Gaussian priors
prior_weights = -0.5 * jnp.sum((weights / prior_std['weights']) ** 2) * 0.0  # size penalty, not smoothing
prior_widths = -0.5 * jnp.sum((widths / prior_std['widths']) ** 2)
prior_gains = -0.5 * (jnp.sum((L1 / prior_std['gains']) ** 2) + jnp.sum((L2 / prior_std['gains']) ** 2))

# Total loss
loss = -log_likelihood - lambda_reg * gmf_prior - 0 * prior_weights - prior_widths - prior_gains
```

---

## Example `cfgparams`

```python
cfgparams = {
    'session': 1,                          # Session number
    'trials': 10,                          # Number of trials
    'models': ['p', 'pv', 'pf', 'pvi', 'pif', 'pvf'],  # Models to fit
    'ngains': [1, 2, 2, 3, 3, 3],          # Number of gains per model
    'rbfs': [30],                          # Number of RBF basis functions
    'restarts': 1,                         # Number of random restarts
    'slack': False,                        # No slack model used
    'subject': 'H',                        # Subject ID (used for loading data)
    'lambda_reg': 3,                       # GMF Laplacian RBF regularization
    'uncertain_tiebreak': False,          # Choose best model (no random tie break)
    'prior_std': {
        'weights': 10,
        'widths': 6,
        'gains': 5
    },
    'elbo_samples': 40,                   # Monte Carlo samples for ELBO
    'gpscaler': [1, 5],                   # Simulation only — GP-based W(t) complexity
    'only_p': True,                       # Simulation only — restricts to position model
    'optimizer': 'lbfgs'                  # Optimizer ('lbfgs' or 'trust')
}
```

---

## Notes on `cfgparams`

- `prior_std`: Sets Gaussian prior scale per parameter group.  
  Default: `{ 'weights': 10, 'widths': 6, 'gains': 5 }`

- `lambda_reg`: Controls smoothing prior (GMF/Laplacian).  
  A value of `3` works well as default.

- `elbo_samples`: Number of posterior samples for estimating ELBO.  
  `40` is typically sufficient for simple models.

---

## Model Comparison and Averaging

To compare models using ELBOs:
```python
    JaxMod.compute_model_probabilities(elbos)
```

To average across models (Bayesian Model Averaging — BMA):  
_Fit all models first_, then use the probabilities output above.

---

