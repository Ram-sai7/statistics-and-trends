"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
#from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='age', y='ptb', data=df)
    plt.title("Scatter Plot: Age vs PTB Status")
    plt.xlabel("Age")
    plt.ylabel("PTB Status (0=Negative, 1=Positive)")
    plt.savefig('relational_plot.png')
    plt.show()

# Categorical Plot
def plot_categorical_plot(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(x="gender", hue="ptb", data=df)
    plt.title("Bar Plot: PTB Cases by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.legend(title="PTB Status")
    plt.savefig('categorical_plot.png')
    plt.show()

# Statistical Plot
def plot_statistical_plot(df):
    plt.figure(figsize=(8, 6))
    
    # Select only numeric columns for correlation calculation
    numeric_df = df.select_dtypes(include=['number'])
    
    # Check if there are any numeric columns left
    if numeric_df.empty:
        print("No numeric data available for correlation heatmap.")
        return
    
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.savefig('statistical_plot.png')
    plt.show()


def statistical_analysis(df, col: str):
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col].dropna())
    excess_kurtosis = ss.kurtosis(df[col].dropna())
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    # Handle missing values
    df.fillna(df.median(numeric_only=True), inplace=True)
    
    # Convert categorical data to lowercase and strip spaces
    if 'gender' in df.columns:
        df['gender'] = df['gender'].astype(str).str.lower().str.strip()

    if 'ptb' in df.columns:
        df['ptb'] = df['ptb'].astype(str).str.strip()

    # Convert 'age' column to numeric (if applicable)
    if 'age' in df.columns:
        df['age'] = df['age'].astype(str).str.extract('(\d+)')  # Extract numeric part
        df['age'] = pd.to_numeric(df['age'], errors='coerce')  # Convert to float

    # Remove any non-numeric columns from correlation analysis
    numeric_df = df.select_dtypes(include=['number'])

    # Print summary and correlation for numeric data
    print("Data Summary:\n", numeric_df.describe())
    print("Data Correlation:\n", numeric_df.corr())


def writing(moments, col):
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    
    skewness = "right-skewed" if moments[2] > 0 else "left-skewed" if moments[2] < 0 else "not skewed"
    kurtosis_type = "leptokurtic" if moments[3] > 0 else "platykurtic" if moments[3] < 0 else "mesokurtic"

    print(f'The data is {skewness} and {kurtosis_type}.')
    return


def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = 'age'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
