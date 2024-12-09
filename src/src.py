# Step 1: Import the necessary libraries
import pandas as pd  # This will help us load and analyze the data
import matplotlib.pyplot as plt  # This will help us create charts

# Step 2: Load the dataset
# Replace the file path with the path to your dataset
file_path = r'C:\Users\Gaming 15\Downloads\week0\data.csv'

# Load the dataset into a pandas DataFrame
df = pd.read_csv(file_path)  # This reads the dataset from the CSV file

# Step 3: Show the first few rows of the dataset
print("Dataset Overview:")
print(df.head())  # This prints the first 5 rows of the data so we can see what it looks like

# Step 4: Get basic information about the dataset
print("\nData Summary:")
print(df.info())  # This shows details like column names, data types, and missing values

# Step 5: Identify numerical columns (columns that contain numbers)
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
print("\nNumerical Columns:")
print(numerical_cols)  # This prints the columns that contain numbers (e.g., age, salary)

# Step 6: Identify categorical columns (columns that contain text or categories)
categorical_cols = df.select_dtypes(include=['object']).columns
print("\nCategorical Columns:")
print(categorical_cols)  # This prints the columns that contain text or categories (e.g., name, city)

# Step 7: Check for missing values in the dataset
print("\nMissing Values:")
print(df.isnull().sum())  # This shows how many missing values (NaN) are in each column

# Step 8: Get basic statistics for numerical columns (like mean, min, max)
print("\nStatistical Summary:")
print(df.describe())  # This shows summary statistics for numerical columns (mean, min, max)

# Step 9: Visualize the distribution of numerical data using histograms
for col in numerical_cols:  # For each numerical column
    plt.hist(df[col].dropna(), bins=30, alpha=0.7, label=col)  # Create a histogram for that column
plt.xlabel('Value')  # Label for the x-axis (horizontal axis)
plt.ylabel('Frequency')  # Label for the y-axis (vertical axis)
plt.title('Distribution of Numerical Columns')  # Title for the chart
plt.legend()  # Show a legend for the columns
plt.show()  # Display the histogram

# Step 10: Check the correlation (relationship) between numerical columns
correlation = df.corr()  # This finds the correlation between numerical columns
print("\nCorrelation Matrix:")
print(correlation)  # This shows how the numerical columns are related to each other

# Step 11: Visualize the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))  # Make the figure bigger
plt.imshow(correlation, cmap='coolwarm', interpolation='none')  # Show the correlation as a heatmap
plt.colorbar()  # Add a color bar to show the scale of correlation
plt.title('Correlation Heatmap')  # Title for the heatmap
plt.show()  # Display the heatmap
