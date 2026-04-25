# ============================================================
#   UNEMPLOYMENT ANALYSIS WITH PYTHON
#   BTech Internship Project | Simple & Beginner Friendly
# ============================================================

# STEP 1: Import all required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# STEP 2: Load the two CSV datasets
# ============================================================

# Dataset 1: Monthly unemployment data
df1 = pd.read_csv("Unemployment in India.csv")

# Dataset 2: Region-wise unemployment data (up to Nov 2020)
df2 = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# ============================================================
# STEP 3: Explore and clean the data
# ============================================================

print("=" * 50)
print("DATASET 1 - First 5 rows:")
print(df1.head())
print("\nColumn Names:", df1.columns.tolist())
print("Shape:", df1.shape)

print("\n" + "=" * 50)
print("DATASET 2 - First 5 rows:")
print(df2.head())
print("\nColumn Names:", df2.columns.tolist())
print("Shape:", df2.shape)

# Strip extra spaces from column names (common issue with these CSVs)
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# Rename columns to simple names for easy use
df1.rename(columns={
    'Region': 'State',
    'Date': 'Date',
    'Frequency': 'Frequency',
    'Estimated Unemployment Rate (%)': 'Unemployment_Rate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Labour_Participation'
}, inplace=True)

df2.rename(columns={
    'Region': 'State',
    'Date': 'Date',
    'Frequency': 'Frequency',
    'Estimated Unemployment Rate (%)': 'Unemployment_Rate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Labour_Participation',
    'Area': 'Area'
}, inplace=True)

# Convert Date column to datetime format
df1['Date'] = pd.to_datetime(df1['Date'], dayfirst=True)
df2['Date'] = pd.to_datetime(df2['Date'], dayfirst=True)

# Check for missing values
print("\nMissing values in Dataset 1:\n", df1.isnull().sum())
print("\nMissing values in Dataset 2:\n", df2.isnull().sum())

# Drop rows with missing values
df1.dropna(inplace=True)
df2.dropna(inplace=True)

# ============================================================
# STEP 4: Basic Statistics
# ============================================================

print("\n" + "=" * 50)
print("BASIC STATISTICS - Dataset 1")
print(df1[['Unemployment_Rate', 'Employed', 'Labour_Participation']].describe())

print("\nBASIC STATISTICS - Dataset 2")
print(df2[['Unemployment_Rate', 'Employed', 'Labour_Participation']].describe())

# ============================================================
# STEP 5: VISUALIZATION
# ============================================================

# Set a clean style for all plots
sns.set(style="darkgrid")
plt.rcParams['figure.figsize'] = (12, 6)

# -------------------------------------------------------
# PLOT 1: Unemployment Rate Over Time (from Dataset 1)
# -------------------------------------------------------
plt.figure()
# Group by date and take average unemployment rate
monthly_avg = df1.groupby('Date')['Unemployment_Rate'].mean().reset_index()

plt.plot(monthly_avg['Date'], monthly_avg['Unemployment_Rate'],
         color='orange', linewidth=2, marker='o', markersize=4)
plt.title('Average Unemployment Rate in India Over Time', fontsize=15)
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plot1_unemployment_over_time.png')
plt.show()
print("Plot 1 saved!")

# -------------------------------------------------------
# PLOT 2: State-wise Average Unemployment Rate (Bar Chart)
# -------------------------------------------------------
plt.figure(figsize=(14, 7))
state_avg = df1.groupby('State')['Unemployment_Rate'].mean().sort_values(ascending=False)

sns.barplot(x=state_avg.values, y=state_avg.index, palette='YlOrRd')
plt.title('Average Unemployment Rate by State', fontsize=15)
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('State')
plt.tight_layout()
plt.savefig('plot2_statewise_unemployment.png')
plt.show()
print("Plot 2 saved!")

# -------------------------------------------------------
# PLOT 3: Impact of COVID-19 (Before vs After April 2020)
# -------------------------------------------------------
plt.figure()
# April 2020 = COVID lockdown spike
df1['Period'] = df1['Date'].apply(
    lambda x: 'After COVID (Apr 2020+)' if x >= pd.Timestamp('2020-04-01') else 'Before COVID'
)

covid_comparison = df1.groupby('Period')['Unemployment_Rate'].mean()
colors = ['steelblue', 'tomato']

covid_comparison.plot(kind='bar', color=colors, edgecolor='black')
plt.title('Unemployment Rate: Before vs After COVID-19', fontsize=15)
plt.ylabel('Average Unemployment Rate (%)')
plt.xlabel('')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('plot3_covid_impact.png')
plt.show()
print("Plot 3 saved!")

# -------------------------------------------------------
# PLOT 4: Urban vs Rural Unemployment (from Dataset 2)
# -------------------------------------------------------
if 'Area' in df2.columns:
    plt.figure()
    area_avg = df2.groupby('Area')['Unemployment_Rate'].mean()
    colors2 = ['#FF8C00', '#2C3E50']

    area_avg.plot(kind='bar', color=colors2, edgecolor='black')
    plt.title('Urban vs Rural Unemployment Rate', fontsize=15)
    plt.ylabel('Average Unemployment Rate (%)')
    plt.xlabel('Area Type')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('plot4_urban_vs_rural.png')
    plt.show()
    print("Plot 4 saved!")

# -------------------------------------------------------
# PLOT 5: Heatmap - State vs Month (from Dataset 1)
# -------------------------------------------------------
plt.figure(figsize=(16, 10))

df1['Month'] = df1['Date'].dt.strftime('%b %Y')  # e.g., "Jan 2020"
heatmap_data = df1.pivot_table(
    values='Unemployment_Rate',
    index='State',
    columns='Month',
    aggfunc='mean'
)

sns.heatmap(heatmap_data, cmap='YlOrRd', linewidths=0.5, annot=False)
plt.title('Unemployment Rate Heatmap: State vs Month', fontsize=15)
plt.xlabel('Month')
plt.ylabel('State')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('plot5_heatmap.png')
plt.show()
print("Plot 5 saved!")

# ============================================================
# STEP 6: Key Insights
# ============================================================
print("\n" + "=" * 50)
print("KEY INSIGHTS FROM THE ANALYSIS")
print("=" * 50)

highest_state = state_avg.idxmax()
lowest_state = state_avg.idxmin()
overall_avg = df1['Unemployment_Rate'].mean()
max_rate = df1['Unemployment_Rate'].max()
max_date = df1.loc[df1['Unemployment_Rate'].idxmax(), 'Date']

print(f"Overall Average Unemployment Rate : {overall_avg:.2f}%")
print(f"Highest Unemployment Rate Recorded: {max_rate:.2f}% on {max_date.strftime('%B %Y')}")
print(f"State with HIGHEST avg unemployment: {highest_state}")
print(f"State with LOWEST  avg unemployment: {lowest_state}")

before = df1[df1['Period'] == 'Before COVID']['Unemployment_Rate'].mean()
after  = df1[df1['Period'] == 'After COVID (Apr 2020+)']['Unemployment_Rate'].mean()
print(f"Avg Unemployment BEFORE COVID : {before:.2f}%")
print(f"Avg Unemployment AFTER  COVID : {after:.2f}%")
print(f"Increase due to COVID         : {after - before:.2f}%")

print("\nAll plots saved as PNG files in the same folder.")
print("Analysis Complete!")
