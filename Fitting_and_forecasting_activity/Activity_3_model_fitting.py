import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the data
data = pd.read_csv('global-inequality-between-world-citizens-and-its-components.csv')

# grab what we need from the csv
X = data['Year'].values
y_total = data['Total inequality'].values
y_between = data['Inequality between country groups'].values
y_within = data['Inequality within country groups'].values

# pick which one you wanna analyse
y = y_total  # swap to y_between or y_within if you want

def fit_polynomial(x, y, degree):
    """fits a polynomial using numpy's polyfit"""
    coeffs = np.polyfit(x, y, degree)
    return coeffs

def predict_polynomial(x, coeffs):
    """make predictions with the polynomial coefficients"""
    return np.polyval(coeffs, x)

# gonna test polynomials from order 3 to 15
orders = range(3, 16)
results = []

for order in orders:
    # fit the model
    coeffs = fit_polynomial(X, y, order)
    
    # get predictions
    y_pred = predict_polynomial(X, coeffs)
    
    # now calculate all the metrics
    n = len(y)
    k = order + 1  # how many parameters we got
    
    # sum of squared residuals (how wrong we are)
    SSR = np.sum((y - y_pred)**2)
    
    # total sum of squares (baseline comparison)
    y_mean = np.mean(y)
    SST = np.sum((y - y_mean)**2)
    
    # r-squared (how much variance we explain)
    r2 = 1 - (SSR / SST)
    
    # degrees of freedom
    dof = n - k
    
    # chi-squared per degree of freedom (fit quality)
    chi2_per_dof = SSR / dof
    
    # bayesian information criterion (penalises complexity)
    bic = n * np.log(SSR / n) + k * np.log(n)
    
    # save everything
    results.append({
        'order': order,
        'chi2_per_dof': chi2_per_dof,
        'BIC': bic,
        'R2': r2,
        'SSR': SSR
    })

# turn it into a dataframe so we can work with it easier
results_df = pd.DataFrame(results)

# make the plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# first plot: chi-squared per degree of freedom
ax1.plot(results_df['order'], results_df['chi2_per_dof'], 
         'o-', color='#0088cc', linewidth=2, markersize=8)
ax1.set_xlabel('Polynomial order (n)', fontsize=12)
ax1.set_ylabel('Weighted χ² per degree of freedom', fontsize=12)
ax1.set_title('Model comparison by polynomial order (1820-1992)', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_xticks(results_df['order'])

# second plot bics
ax2.plot(results_df['order'], results_df['BIC'], 
         'o-', color='#ff8800', linewidth=2, markersize=8)
ax2.set_xlabel('Polynomial order (n)', fontsize=12)
ax2.set_ylabel('BIC', fontsize=12)
ax2.set_title('Bayesian Information Criterion vs Polynomial Order', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.set_xticks(results_df['order'])

plt.tight_layout()
plt.savefig('polynomial_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# print everything out
print("\nResults Summary:")
print(results_df.to_string(index=False))

# find which models did best
best_chi2 = results_df.loc[results_df['chi2_per_dof'].idxmin()]
best_bic = results_df.loc[results_df['BIC'].idxmin()]

print(f"\n\nBest model by χ²/ν: Order {int(best_chi2['order'])} (χ²/ν = {best_chi2['chi2_per_dof']:.4f})")
print(f"Best model by BIC: Order {int(best_bic['order'])} (BIC = {best_bic['BIC']:.2f})")