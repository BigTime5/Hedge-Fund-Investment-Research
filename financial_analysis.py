import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json

# Load datasets
balance_df = pd.read_excel('data/Balance_Sheet.xlsx')
income_df = pd.read_excel('data/Income_Statement.xlsx')

# Rename columns for consistency
balance_df.columns = balance_df.columns.str.strip()
income_df.columns = income_df.columns.str.strip()

# Merge datasets
df = pd.merge(balance_df, income_df, on=['company', 'comp_type', 'Year'], how='inner')
df.columns = df.columns.str.strip()

# Clean company names
df['company'] = df['company'].str.strip()

# Calculate Financial Ratios
# Profitability Ratios
df['Gross_Margin'] = (df['Gross Profit'] / df['Total Revenue']) * 100
df['Operating_Margin'] = (df['Operating Income'] / df['Total Revenue']) * 100

# For ROE, we need Net Income. Since we don't have it directly, we'll use Operating Income as proxy
# In real analysis, you'd use Net Income. Using Operating Income for this analysis.
df['ROE_Operating'] = (df['Operating Income'] / df['Total Stockholder Equity']) * 100

# Leverage Ratios
df['Debt_to_Equity'] = df['Total Liab'] / df['Total Stockholder Equity']
df['Debt_to_Assets'] = df['Total Liab'] / df['Total Assets']
df['Financial_Leverage'] = df['Total Assets'] / df['Total Stockholder Equity']
df['Equity_Multiplier'] = df['Total Assets'] / df['Total Stockholder Equity']

# Current Ratio (Liquidity)
df['Current_Ratio'] = df['Total Current Assets'] / df['Total Current Liabilities']

# Replace infinities and NaN with appropriate values
df = df.replace([np.inf, -np.inf], np.nan)

# Industry mapping
industry_names = {
    'tech': 'Technology',
    'fmcg': 'Fast-Moving Consumer Goods',
    'real_est': 'Real Estate'
}
df['Industry'] = df['comp_type'].map(industry_names)

# Save processed data
df.to_csv('processed_financial_data.csv', index=False)

# Summary statistics by industry
industry_summary = df.groupby('Industry').agg({
    'Gross_Margin': 'mean',
    'Operating_Margin': 'mean',
    'ROE_Operating': 'mean',
    'Debt_to_Equity': 'mean',
    'Debt_to_Assets': 'mean',
    'Financial_Leverage': 'mean',
    'Total Revenue': 'sum',
    'Total Assets': 'sum',
    'Total Liab': 'sum',
    'Total Stockholder Equity': 'sum'
}).round(2)

industry_summary.to_csv('industry_summary.csv')

# Real Estate specific analysis
real_est_df = df[df['comp_type'] == 'real_est']
real_est_company_summary = real_est_df.groupby('company').agg({
    'Gross_Margin': 'mean',
    'Operating_Margin': 'mean',
    'ROE_Operating': 'mean',
    'Debt_to_Equity': 'mean',
    'Debt_to_Assets': 'mean',
    'Financial_Leverage': 'mean',
    'Total Revenue': 'mean',
    'Total Assets': 'mean',
    'Total Liab': 'mean',
    'Total Stockholder Equity': 'mean'
}).round(2)

real_est_company_summary.to_csv('real_est_company_summary.csv')

# Calculate correlation between leverage and profitability for real estate
real_est_clean = real_est_df.dropna(subset=['Debt_to_Equity', 'Operating_Margin'])
if len(real_est_clean) > 2:
    leverage_profitability_corr = real_est_clean['Debt_to_Equity'].corr(real_est_clean['Operating_Margin'])
else:
    leverage_profitability_corr = np.nan

# Year-over-year trends for real estate
real_est_trend = real_est_df.groupby('Year').agg({
    'Operating_Margin': 'mean',
    'Debt_to_Equity': 'mean',
    'ROE_Operating': 'mean'
}).round(2)

real_est_trend.to_csv('real_est_trend.csv')

# All industries trend comparison
industry_trend = df.groupby(['Year', 'Industry']).agg({
    'Operating_Margin': 'mean',
    'Debt_to_Equity': 'mean',
    'ROE_Operating': 'mean'
}).round(2).reset_index()

industry_trend.to_csv('industry_trend.csv', index=False)

# Prepare data for visualization
chart_data = df.to_dict('records')
with open('chart_data.json', 'w') as f:
    json.dump(chart_data, f)

# Prepare summary data for HTML
summary_stats = {
    'total_companies': df['company'].nunique(),
    'total_observations': len(df),
    'industries': list(industry_names.values()),
    'year_range': f"{df['Year'].min()}-{df['Year'].max()}",
    'real_est_companies': df[df['comp_type'] == 'real_est']['company'].nunique()
}

with open('summary_stats.json', 'w') as f:
    json.dump(summary_stats, f)

print("Analysis complete!")
print(f"Total companies: {summary_stats['total_companies']}")
print(f"Total observations: {summary_stats['total_observations']}")
print(f"Real Estate correlation (Debt-to-Equity vs Operating Margin): {leverage_profitability_corr:.4f}")
