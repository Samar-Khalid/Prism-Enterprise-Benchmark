# Prism Enterprise Benchmark

A synthetic benchmark dataset for evaluating AI models on enterprise manufacturing scenarios. All data is 100% fictional.

## Motivation

Finding realistic enterprise data for benchmarking AI models is difficult. Most public datasets are either too simplistic (toy data) or not representative of actual manufacturing systems. Prism Enterprise Benchmark fills this gap by providing a realistic, synthetic manufacturing dataset that captures the complexity of real ERP systems while containing no real company data.

## Dataset Overview

| Dataset | Records | Description |
|---------|---------|-------------|
| Customers | 500 | Fictional B2B manufacturing companies |
| Products | 50 | Fertilizer and chemical product categories |
| Suppliers | 100 | Raw material providers |
| Orders | 50K+ | Sales transactions with full status lifecycle |
| Inventory | 100K+ | Stock movements (in/out/transfer) |
| Production | 20K+ | Manufacturing batch records |

## Benchmark Tasks

| Task | Description | Evaluation Metric |
|------|-------------|-------------------|
| **Text-to-SQL** | Convert natural language questions to SQL queries | Execution Accuracy |
| **Data QA** | Answer questions about manufacturing data | Exact Match + F1 |
| **KPI Generation** | Generate business KPIs from raw data | Precision/Recall |
| **Report Generation** | Summarize data into structured reports | ROUGE + Human Eval |
| **Anomaly Detection** | Identify unusual patterns in production | Precision/Recall/F1 |

## Evaluation Metrics

- **Accuracy** - Overall correctness of model outputs
- **Execution Accuracy** - SQL queries that run without errors AND return correct results
- **Response Quality** - Human evaluation of response relevance and completeness

## Quick Start

```bash
git clone https://github.com/Samar-Khalid/Prism-Enterprise-Benchmark.git
cd Prism-Enterprise-Benchmark
pip install -r requirements.txt
python generators/generate_all.py
```

## Repository Structure

```
data/synthetic/          # Generated CSV datasets
generators/              # Data generation scripts
benchmarks/              # Evaluation scripts (NL2SQL, QA, etc.)
configs/                 # Generator configuration
```

## Limitations

- Data schema is simplified compared to real ERP systems
- Currently focused on fertilizer/manufacturing domain
- No time-series data yet (production schedules, etc.)
- Limited to structured data (no text logs, images, etc.)

## Future Work

- Add time-series production data
- Include maintenance records and quality control data
- Multi-language support (Arabic + English queries)
- Domain expansion to other manufacturing verticals

## License

MIT