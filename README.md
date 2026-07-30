# Prism Enterprise Benchmark

A synthetic benchmark dataset for evaluating AI models on enterprise manufacturing scenarios. All data is 100% fictional.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)

## Dataset

- **500 customers** - fictional B2B companies
- **50 products** - fertilizer categories (Urea, DAP, NPK, etc.)
- **100 suppliers** - raw material providers
- **50K+ orders** - sales transactions with statuses
- **100K+ inventory movements** - stock in/out records
- **20K+ production batches** - manufacturing data

## Quick Start

```bash
git clone https://github.com/Samar-Khalid/Prism-Enterprise-Benchmark.git
cd Prism-Enterprise-Benchmark
pip install -r requirements.txt
python generators/generate_all.py
```

## Benchmark Tasks

| Task | Description |
|------|-------------|
| NL2SQL | Convert natural language questions to SQL |
| Anomaly Detection | Find unusual patterns in production data |
| Forecasting | Predict future demand |
| Report Generation | Summarize data into insights |

## Structure

```
data/synthetic/     # Generated CSV files
generators/         # Data generation scripts
benchmarks/         # Evaluation scripts
configs/            # Generator configuration
```

## License

MIT