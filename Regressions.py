import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def load_and_prepare_data(file_path):
    # Load data
    data = pd.read_excel(file_path)
    
    # Assuming the first column is 'Year' and subsequent columns are countries
    data.columns = ['Year'] + [f'Country{i+1}' for i in range(data.shape[1] - 1)]
    return data

def perform_regression(data, cluster):
    # Initialize the regression model
    model = LinearRegression()

    # Setup the plot
    plt.figure(figsize=(14, 8))
    
    # Colors for the plots
    colors = plt.cm.viridis(np.linspace(0, 1, data.shape[1] - 1))

    # Perform regression for each country
    for i, column in enumerate(data.columns[1:]):  # Skip 'Year' column
        
        
        x = []
        y = []
        for year, eci in zip(data['Year'], data[column]):
            if pd.notnull(year) and pd.notnull(eci):
                x.append(year)
                y.append(eci)
        x = np.array(x).reshape(-1, 1)  # Years
        y = np.array(y)  # ECI values
        

        
        # Fit model
        model.fit(x, y)
        
        # Predict values for a smooth line
        y_pred = model.predict(x)
        
        # Scatter plot of actual data
        plt.scatter(x, y, color=colors[i], label=f'{column} (slope: {model.coef_[0]:.2f})')
        
        # Line plot of the regression line
        plt.plot(x, y_pred, color=colors[i], linestyle='--')

    # Adding plot legends and labels
    plt.legend(title="Country Index (Growth Rate)")
    plt.title(f'{cluster} Regression Analysis')
    plt.xlabel('Year')
    plt.ylabel('Economic Complexity Index (ECI)')
    plt.grid(True)

    # Show plot
    plt.show()

# Path to the Excel file
file_path = 'High_Capacity.xlsx'  # Update this path
cluster_name = file_path[:-5].replace('_', ' ')
# Load data
data = load_and_prepare_data(file_path)
# Perform regression analysis and plotting
perform_regression(data, cluster_name)


# Path to the Excel file
file_path = 'Emerging_and_Advancing.xlsx'  # Update this path
cluster_name = file_path[:-5].replace('_', ' ')
# Load data
data = load_and_prepare_data(file_path)
# Perform regression analysis and plotting
perform_regression(data, cluster_name)

# Path to the Excel file
file_path = 'Capacity_Constrained.xlsx'  # Update this path
cluster_name = file_path[:-5].replace('_', ' ')
# Load data
data = load_and_prepare_data(file_path)
# Perform regression analysis and plotting
perform_regression(data, cluster_name)

# Path to the Excel file
file_path = 'One_Sided_Initiative.xlsx'  # Update this path
cluster_name = file_path[:-5].replace('_', ' ')
# Load data
data = load_and_prepare_data(file_path)
# Perform regression analysis and plotting
perform_regression(data, cluster_name)
