import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = r"/workspaces/program/CloudWatch_Traffic_Web_Attack.csv"
df = pd.read_csv(file_path)

# Display basic info
print("Dataset Info:")
print(df.info())
print(df.head())

# Clean data: convert datetime fields
df['creation_time'] = pd.to_datetime(df['creation_time'], errors='coerce')
df['end_time'] = pd.to_datetime(df['end_time'], errors='coerce')
df['time'] = pd.to_datetime(df['time'], errors='coerce')

# Drop rows with null critical timestamps
df.dropna(subset=['creation_time', 'end_time'], inplace=True)

# Feature Engineering: Session duration
df['session_duration'] = (df['end_time'] - df['creation_time']).dt.total_seconds()

# Handle any remaining missing values
df['bytes_in'].fillna(df['bytes_in'].median(), inplace=True)
df['bytes_out'].fillna(df['bytes_out'].median(), inplace=True)
df.dropna(subset=['src_ip', 'dst_ip'], inplace=True)

# Create a new feature: average packet size
df['avg_packet_size'] = (df['bytes_in'] + df['bytes_out']) / df['session_duration'].replace(0, np.nan)
df['avg_packet_size'].fillna(0, inplace=True)

# Exploratory Data Analysis
plt.figure(figsize=(12, 6))
sns.histplot(df['bytes_in'], bins=50, color='blue', kde=True, label='Bytes In')
sns.histplot(df['bytes_out'], bins=50, color='red', kde=True, label='Bytes Out')
plt.legend()
plt.title('Distribution of Bytes In and Bytes Out')
plt.show()

# Anomaly Detection
features = df[['bytes_in', 'bytes_out', 'session_duration', 'avg_packet_size']]
model = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = model.fit_predict(features)
df['anomaly'] = df['anomaly'].map({1: 'Normal', -1: 'Suspicious'})

# Anomaly scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bytes_in', y='bytes_out', hue='anomaly', data=df,
                palette={'Normal': 'green', 'Suspicious': 'red'})
plt.title('Anomalies in Web Traffic')
plt.show()

# Summary
print("Anomaly Counts:\n", df['anomaly'].value_counts())
print("\nSuspicious Examples:\n", df[df['anomaly'] == 'Suspicious'].head())
