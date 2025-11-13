Global Inequality Forecasting & Model Fitting


An analysis of polynomial model fitting using historical data on global income inequality.

I took Gini index data up to 1980, fitted it with polynomial models of varying complexity, and used a reduced chi-squared analysis to find the optimal fit. The goal was to see how well these models could predict post-1980 trends and to visualize the concepts of underfitting and overfitting.

Content:

forecastgraph.py: The main script. It loads the data, performs the polynomial fits, calculates the goodness-of-fit for each model order, and generates the comparison plots.
global-inequality-between-world-citizens-and-its-components.csv: The historical data on global inequality.

Global Income Inequality...png: The first plot, showing the underfit, best-fit, and overfit models against the historical data.

Model Comparison...png: The second plot, which visualizes the reduced chi-squared values to identify the best-performing model order.
To run:

You will need pandas, numpy, and matplotlib installed.

Run the script from your terminal:
python forecastgraph.py

The script will display the two analysis plots.