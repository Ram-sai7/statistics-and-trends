"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns

def plot_relational_plot(df):
    """Creates relational plot"""
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='age', y='ptb', hue='gender')
    plt.title('Age vs PTB Status')
    plt.savefig('relational_plot.png')
    plt.close()

def plot_categorical_plot(df):
    """Creates categorical plot"""
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='gender', hue='ptb')
    plt.title('PTB Cases by Gender')
    plt.savefig('categorical_plot.png')
    plt.close()

def plot_statistical_plot(df):
    """Creates histogram"""
    plt.figure(figsize=(8, 6))
    sns.histplot(df['age'], bins=20, kde=True)
    plt.title('Age Distribution')
    plt.savefig('statistical_plot.png')
    plt.close()

def statistical_analysis(df, col: str):
    """Computesstatistical moments"""
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col], nan_policy='omit')
    excess_kurtosis = ss.kurtosis(df[col], nan_policy='omit')
    return mean, stddev, skew, excess_kurtosis

def preprocessing(df):
    """Preprocesses the dataset"""
    df = df.dropna()
    df = df.copy()
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

    df = df.dropna()
    return df

def writing(moments, col):
    """ statistical analysis"""
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    if moments[2] > 2 or moments[2] < -2:
        skewness = "highly skewed"
    else:
        skewness = "approximately symmetric"
    
    if moments[3] > 2:
        kurtosis = "leptokurtic (peaked)"
    elif moments[3] < -2:
        kurtosis = "platykurtic (flat)"
    else:
        kurtosis = "mesokurtic (normal)"
    
    print(f'The data is {skewness} and {kurtosis}.')
    return

def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, 'age')
    writing(moments, 'age')
    return

if __name__ == '__main__':
    main()
