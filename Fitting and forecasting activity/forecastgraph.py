import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1 - load and prepare data
try:
    # load the dataset
    data = pd.read_csv('global-inequality-between-world-citizens-and-its-components.csv')
    
    df = data[data['Entity'] == 'World'][['Year', 'Total inequality']].copy()

    df.rename(columns={'Total inequality': 'Inequality'}, inplace=True)
    
    # 2 - this bit subsamples data
 
    fit_limit_year = 1980
    
    df_fit = df[df['Year'] <= fit_limit_year]
   
    df_reality = df[df['Year'] > fit_limit_year]
    
    x_fit, y_fit = df_fit['Year'], df_fit['Inequality']
    x_reality, y_reality = df_reality['Year'], df_reality['Inequality']
    
    # 3 - this model testing bit calculates chi squared
    
    polynomial_orders = range(1, 10) # test polynomials from order 1 to 9
    chi_squared_results = []
    
   
    uncertainty = 1.0 
    
    for order in polynomial_orders:
        coeffs = np.polyfit(x_fit, y_fit, order)
        
        # calculate the expected values (e_i) from our model
        y_expected = np.polyval(coeffs, x_fit)
        
        # calculate the chi squared statistic
        chi_squared = np.sum(((y_fit - y_expected) / uncertainty) ** 2)
        
        # calculate number of degrees of freedom
        num_observations = len(df_fit)
        num_parameters = order + 1
        degrees_of_freedom = num_observations - num_parameters
        
        
        if degrees_of_freedom > 0:
            reduced_chi_squared = chi_squared / degrees_of_freedom
            chi_squared_results.append({'order': order, 'chi_sq_nu': reduced_chi_squared})

    results_df = pd.DataFrame(chi_squared_results)
    
    # find the best model for the minimum reduced chi squared
    best_model_order = results_df.loc[results_df['chi_sq_nu'].idxmin()]['order']
    print(f"The best performing model is a polynomial of order: {best_model_order}")

    # 4 - this bit generates plots

    x_full_range = np.linspace(df['Year'].min(), df['Year'].max(), 200)

    plt.figure(figsize=(12, 7))
    
    # plot the observed data
    plt.scatter(x_fit, y_fit, label='Fitting Data (<=1980)')
    plt.scatter(x_reality, y_reality, color='gray', label='Reality Data (>1980)')
    
    # plot the best fit polynomial
    best_coeffs = np.polyfit(x_fit, y_fit, best_model_order)
    plt.plot(x_full_range, np.polyval(best_coeffs, x_full_range), 'r-', 
             label=f'Best-fit polynomial (order {best_model_order})')
             
    # plot an under fit polynomial order 1 for comparison
    underfit_coeffs = np.polyfit(x_fit, y_fit, 1)
    plt.plot(x_full_range, np.polyval(underfit_coeffs, x_full_range), 'g:', 
             label='Polynomial order 1 (underfit)')
             
    # plot an over fit polinomial order 7 for comparison
    overfit_coeffs = np.polyfit(x_fit, y_fit, 7)
    plt.plot(x_full_range, np.polyval(overfit_coeffs, x_full_range), 'm--', 
             label='Polynomial order 7 (overfit)')

    # add the fit limit lines
    plt.axvline(x=fit_limit_year, color='black', linestyle='--', label=f'Fit limit ({fit_limit_year})')

    plt.title('Global Income Inequality: Polynomial Fits Comparison')
    plt.xlabel('Year')
    plt.ylabel('Total Inequality (Gini Index)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # plot 2 model selection plot
    plt.figure(figsize=(10, 6))
    plt.plot(results_df['order'], results_df['chi_sq_nu'], 'bo-')
    plt.title(f'Model Comparison by Polynomial Order (Fit up to {fit_limit_year})')
    plt.xlabel('Polynomial Order (n)')
    plt.ylabel('Reduced Chi-Squared (Goodness of Fit)')
    plt.xticks(results_df['order'])
    plt.grid(True)
    plt.show()

except FileNotFoundError:
    print("Error: The file 'global-inequality-between-world-citizens-and-its-components.csv' was not found.")
    print("Please make sure the CSV file is in the same directory as this script.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")