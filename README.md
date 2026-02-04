# 📊 Hedge Fund Investment Research: Real Estate Leverage & Profitability Analysis

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-green)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Report](https://img.shields.io/badge/Report-Live-red)](https://bigtime5.github.io/Hedge-Fund-Investment-Research/)

## 🎯 Executive Summary

A comprehensive financial analysis framework designed to evaluate the relationship between leverage and profitability in real estate companies, providing actionable investment insights for hedge fund decision-making.

**🔍 Key Finding:** Statistical analysis reveals a **positive correlation (r=0.62, p<0.01)** between leverage and profitability in real estate companies, with highly leveraged firms showing 2.2x higher operating margins on average.

**📈 View Interactive Report:** [https://bigtime5.github.io/Hedge-Fund-Investment-Research/](https://bigtime5.github.io/Hedge-Fund-Investment-Research/)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Data Architecture](#-data-architecture)
- [Analysis Methodology](#-analysis-methodology)
- [Key Findings](#-key-findings)
- [Project Structure](#-project-structure)
- [Technical Stack](#-technical-stack)
- [Results & Outputs](#-results--outputs)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## 🌟 Project Overview

### Business Context
As a quantitative analyst at a hedge fund, this project addresses a critical investment question: **"Are highly leveraged real estate companies more profitable?"** The analysis spans 15 companies across three industries (Technology, FMCG, Real Estate) over a 5-year period (2018-2022).

### Objectives
1. **Quantify** the leverage-profitability relationship in real estate
2. **Compare** real estate performance against other sectors
3. **Identify** optimal investment targets using risk-adjusted metrics
4. **Provide** data-driven portfolio allocation recommendations

### Deliverables
- 🌐 **Interactive Web Dashboard** - Public-facing HTML report
- 📊 **Jupyter Notebook** - Detailed analysis with visualizations
- 📈 **Processed Datasets** - Clean, analysis-ready CSV files
- 📋 **Statistical Models** - Correlation and regression analysis

---

## ✨ Key Features

### 1. **Automated Financial Analysis Pipeline**
- ETL process for balance sheet and income statement data
- 15+ financial ratios calculated automatically
- Outlier detection and data quality checks

### 2. **Advanced Statistical Analysis**
- Pearson & Spearman correlation coefficients
- Linear regression modeling
- Quartile analysis for performance segmentation
- Risk-adjusted return metrics (Sharpe-like ratios)

### 3. **Interactive Visualizations**
- Plotly-powered interactive charts
- Multi-dimensional scatter plots with company annotations
- Time series analysis with trend lines
- Industry comparison heatmaps

### 4. **Investment Intelligence**
- Company ranking by risk-adjusted performance
- DuPont analysis for ROE decomposition
- Coefficient of variation for consistency metrics
- Sector-relative performance benchmarking

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/bigtime5/Hedge-Fund-Investment-Research.git
cd Hedge-Fund-Investment-Research
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Required Packages:
```
pandas>=1.3.0
numpy>=1.21.0
plotly>=5.3.0
scipy>=1.7.0
openpyxl>=3.0.7
jupyter>=1.0.0
```

---

## 💡 Quick Start

### Option 1: Run Complete Analysis
```bash
python run_analysis.py
```

### Option 2: Interactive Jupyter Notebook
```bash
jupyter notebook financial_analysis_notebook.ipynb
```

### Option 3: View Results Only
Open `index.html` in your browser or visit the [live report](https://bigtime5.github.io/Hedge-Fund-Investment-Research/)

---

## 📊 Data Architecture

### Input Data Structure
```
data/
├── Balance_Sheet.xlsx       # 60 observations, 15 companies
│   ├── Company (ticker)
│   ├── comp_type (industry)
│   ├── Year (2018-2022)
│   └── Financial metrics (Assets, Liabilities, Equity)
│
└── Income_Statement.xlsx    # 60 observations, 15 companies
    ├── Company (ticker)
    ├── comp_type (industry)
    ├── Year (2018-2022)
    └── Financial metrics (Revenue, EBITDA, Operating Income)
```

### Calculated Metrics
| Category | Metrics |
|----------|---------|
| **Profitability** | Gross Margin, Operating Margin, EBITDA Margin |
| **Leverage** | Debt-to-Equity, Debt-to-Assets, Financial Leverage |
| **Efficiency** | ROE (Operating), ROA, Asset Turnover |
| **Liquidity** | Current Ratio, Working Capital |
| **Risk-Adjusted** | Coefficient of Variation, Risk-Adjusted Score |

---

## 🔬 Analysis Methodology

### 1. Data Processing Pipeline
```python
Raw Data → Data Cleaning → Ratio Calculation → Statistical Analysis → Visualization → Insights
```

### 2. Statistical Framework
- **Correlation Analysis**: Pearson (r=0.616, p=0.004) and Spearman correlations
- **Regression Modeling**: Operating Margin = 17.54 + 2.19 × Debt-to-Equity
- **Quartile Analysis**: Performance segmentation by leverage levels
- **Time Series**: Year-over-year trend analysis

### 3. Risk-Return Framework
```
Risk-Adjusted Score = Operating Margin / (1 + Coefficient of Variation)
```

---

## 📈 Key Findings

### 1. **Primary Hypothesis: CONFIRMED**
> Highly leveraged real estate companies demonstrate **significantly higher profitability**

| Leverage Quartile | Avg Operating Margin | Avg ROE |
|-------------------|---------------------|---------|
| Low (D/E < 2)     | 20.0%              | 15.6%   |
| High (D/E > 8)    | 43.4%              | 79.9%   |

### 2. **Top Investment Targets**
| Rank | Company | Operating Margin | Leverage | Risk-Adj Score |
|------|---------|-----------------|----------|----------------|
| 1    | SPG     | 47.9%           | 9.7x     | 44.35         |
| 2    | AMT     | 38.0%           | 8.6x     | 36.90         |
| 3    | CCI     | 28.4%           | 2.8x     | 26.32         |

### 3. **Industry Comparison**
- Real Estate leads in operating margin (30.0%) vs Tech (27.4%) and FMCG (20.7%)
- Real Estate shows highest leverage (5.7x) but maintains competitive ROE (43.9%)

---

## 📁 Project Structure

```
Hedge-Fund-Investment-Research/
│
├── 📊 data/                          # Input data files
│   ├── Balance_Sheet.xlsx
│   └── Income_Statement.xlsx
│
├── 📓 financial_analysis_notebook.ipynb  # Main analysis notebook
├── 🐍 financial_analysis.py              # Core analysis functions
├── 🚀 run_analysis.py                    # Automation script
├── 🌐 index.html                         # Interactive report
│
├── 📈 Output Files
│   ├── processed_financial_data.csv     # Clean dataset
│   ├── industry_summary.csv             # Industry aggregates
│   ├── real_est_company_summary.csv     # Company-level metrics
│   ├── real_est_trend.csv               # Time series data
│   ├── industry_trend.csv               # Industry trends
│   ├── summary_stats.json               # Statistical summary
│   └── chart_data.json                  # Visualization data
│
├── 📋 Documentation
│   ├── README.md                        # This file
│   ├── QUICKSTART.txt                   # Quick reference
│   └── requirements.txt                 # Dependencies
```

---

## 💻 Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Data Processing** | Pandas, NumPy | ETL, calculations |
| **Statistical Analysis** | SciPy | Correlation, regression |
| **Visualization** | Plotly | Interactive charts |
| **Reporting** | HTML, JavaScript | Web dashboard |
| **Development** | Jupyter | Interactive analysis |
| **Version Control** | Git/GitHub | Code management |

---

## 📊 Results & Outputs

### 1. **Interactive Dashboard**
- Live at: [https://bigtime5.github.io/Hedge-Fund-Investment-Research/](https://bigtime5.github.io/Hedge-Fund-Investment-Research/)
- Features: Responsive charts, drill-down capabilities, export options

### 2. **Statistical Reports**
- Correlation matrices
- Regression coefficients
- Confidence intervals
- P-values and significance tests

### 3. **Investment Recommendations**
- Risk-adjusted company rankings
- Portfolio allocation guidance
- Sector rotation strategies
- Risk management considerations

---

## 🔮 Future Enhancements

### Short-term (v2.0)
- [ ] Add Monte Carlo simulation for risk scenarios
- [ ] Include macroeconomic indicators (interest rates, GDP)
- [ ] Implement real-time data feeds
- [ ] Add peer benchmarking features

### Long-term (v3.0)
- [ ] Machine learning models for return prediction
- [ ] Natural language processing for earnings calls
- [ ] ESG metrics integration
- [ ] API for programmatic access

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards
- PEP 8 compliance for Python code
- Comprehensive docstrings
- Unit tests for new features
- Update documentation

---

## 👤 Author

**Phinidy George**
- 📧 Email: phinidygeorge01@gmail.com
- 🔗 GitHub: [@bigtime5](https://github.com/bigtime5)
- 🌐 Portfolio: [View Project](https://bigtime5.github.io/Hedge-Fund-Investment-Research/)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Financial data modeling best practices from CFA Institute
- Statistical methods inspired by academic finance research
- Visualization techniques from Plotly documentation
- Hedge fund industry insights from practitioner experience

---

## 📞 Contact

For questions, suggestions, or collaboration opportunities:
- Create an [Issue](https://github.com/bigtime5/Hedge-Fund-Investment-Research/issues)
- Email: phinidygeorge01@gmail.com
- LinkedIn: [Connect with me](#)

---

<div align="center">

**⭐ If you found this analysis helpful, please star the repository! ⭐**

*Last Updated: November 2024*

</div>
