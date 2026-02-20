# BCG GenAI Financial Analysis – Forage Simulation

This repository contains my work for the **BCG GenAI Job Simulation (Forage)**.  
The goal of this task was to extract key financial data from 10-K filings and perform programmatic trend analysis to support the future development of an AI-powered financial chatbot.

---

## 🎯 Project Objective

For three companies:

- Microsoft  
- Tesla  
- Apple  

I manually extracted data from their 10-K filings for the **last three fiscal years**, and analyzed:

- **Total Revenue**
- **Net Income**
- **Total Assets**
- **Total Liabilities**
- **Cash Flow from Operating Activities**

Then, using Python and pandas in a Jupyter Notebook, I:

- Computed **year-over-year (YoY) growth** for each metric
- Organized the results by company and year
- Summarized the key financial trends in markdown within the notebook

This workflow simulates how a GenAI-powered assistant could reason over structured financial data as part of a financial chatbot.

---

## 🧱 Tech Stack

- **Python** (pandas)
- **Jupyter Notebook**
- **CSV / Excel** for data storage
- **Git & GitHub** for version control

---

## 📂 Repository Structure

```text
bcg-genai-financial-chatbot/
├── data/
│   └── raw/
│       ├── financial_data_raw.xlsx   # Manually extracted financials (not tracked in git if ignored)
│       └── financial_data_raw.csv    # CSV version used in analysis
├── notebooks/
│   └── BCG_Financial_Analysis.ipynb  # Main notebook for Task 2
├── src/
│   ├── extract.py                    # (Reserved for future automation)
│   ├── clean.py
│   ├── metrics.py
│   └── utils.py
├── EXTRACTION_PLAN.md                # Notes on which metrics to extract and why
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
