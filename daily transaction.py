import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style='whitegrid')

# Load dataset from your local path
file_path = r"/workspaces/program/Daily Household Transactions.csv"
df = pd.read_csv(file_path)

# Initial Overview
print("Data Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

# Handle missing values
df['Subcategory'].fillna('Unknown', inplace=True)
df['Note'].fillna('No Description', inplace=True)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset=['Date'], inplace=True)

# Basic info
print("\nCleaned Data Info:\n")
print(df.info())

# Transaction Mode Plot
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Mode', order=df['Mode'].value_counts().index)
plt.title('Transaction Mode Distribution')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Category Count Plot
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Category', order=df['Category'].value_counts().head(10).index)
plt.title('Top 10 Transaction Categories')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Subcategory Plot
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Subcategory', order=df['Subcategory'].value_counts().head(10).index)
plt.title('Top 10 Transaction Subcategories')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Income vs Expense
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Income/Expense')
plt.title('Income vs Expense Distribution')
plt.show()

# Amount Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Amount'], bins=50, kde=True)
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.show()

# Boxplot by Category
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='Amount', y='Category', order=df['Category'].value_counts().head(5).index)
plt.title('Transaction Amount by Top Categories')
plt.show()

# Time Series Monthly Trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_trend = df.groupby('Month')['Amount'].sum()

plt.figure(figsize=(14, 6))
monthly_trend.plot(marker='o')
plt.title('Monthly Transaction Amount Trend')
plt.xlabel('Month')
plt.ylabel('Total Amount')
plt.grid(True)
plt.show()

# Correlation Heatmap
pivot_table = df.pivot_table(index='Date', columns='Category', values='Amount', aggfunc='sum', fill_value=0)
correlation_matrix = pivot_table.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Between Transaction Categories')
plt.show()
