# Extraction Plan (10-K / 10-Q)

## Goal
Extract high-quality, structured financial data from filings to support:
1) baseline financial trend analysis, and
2) a GenAI chatbot that answers questions grounded in source documents.

## Key data to extract

### Income Statement (per period)
- Revenue
- Gross profit (if available)
- Operating income
- Net income
- EPS (basic/diluted, if available)

### Balance Sheet (as of period end)
- Total assets
- Total liabilities
- Shareholders’ equity
- Cash & cash equivalents (if available)
- Total debt (short + long-term, if available)

### Cash Flow Statement (per period)
- Net cash from operating activities
- Net cash from investing activities
- Net cash from financing activities
- Free cash flow (derived: OCF - CapEx, if CapEx available)

## Core metrics to compute (trend indicators)
- YoY / QoQ revenue growth
- Net margin = net income / revenue
- Operating margin = operating income / revenue
- Change in cash position (period-over-period)
- Leverage proxy (if debt available): debt / equity

## Data quality checks
- Track units (USD vs other; millions vs billions)
- Preserve signs (losses, negative cash flow)
- Ensure period labeling is correct (FY vs quarter)
- Flag missing fields (do not hallucinate)
- Validate obvious relationships when possible (e.g., margins within reasonable bounds)

## AI-ready structure (output format)
Store extracted values in structured formats:
- `data/processed/financials.csv` (tabular)
- `data/processed/financials.json` (for chatbot/RAG context)
Include fields like:
- company
- filing_type (10-K/10-Q)
- period_end_date
- metric_name
- value
- units
- source_section/page_reference (if available)
