<div align="center">

# 📊 Prism Enterprise Benchmark

### Synthetic Benchmark Dataset for Enterprise AI Research

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Synthetic Data](https://img.shields.io/badge/Data-100%25%20Synthetic-brightgreen?style=for-the-badge)](#-dataset-characteristics)

---

A **100% synthetic** benchmark dataset designed to evaluate AI/ML models on enterprise manufacturing scenarios.

[Generate Data](#-quick-start) • [Benchmark Tasks](#-benchmark-tasks) • [Leaderboard](#-leaderboard) • [Contributing](#-contributing)

</div>

---

## 🎯 Purpose

Provide a realistic, standardized benchmark for:

| Task | Description | Status |
|------|-------------|--------|
| 🔍 **NL2SQL** | Evaluate natural language to SQL models | ✅ Ready |
| 🚨 **Anomaly Detection** | Test anomaly detection algorithms | ✅ Ready |
| 📈 **Forecasting** | Validate time series forecasting | ✅ Ready |
| 📊 **Report Generation** | Assess automated report quality | ✅ Ready |

---

## 📊 Dataset Characteristics

| Attribute | Value |
|-----------|-------|
| **Company** | Prism Fertilizers (Fictional) |
| **Industry** | Fertilizer Manufacturing |
| **Records** | 100K+ synthetic transactions |
| **Tables** | 20+ enterprise entities |
| **Time Range** | 3 years synthetic data |
| **File Format** | CSV, JSON, SQL |

---

## 📦 Dataset Contents

### Core Entities

| Entity | Count | Description |
|--------|-------|-------------|
| 👥 **Customers** | 500 | B2B customers across regions |
| 📦 **Products** | 50 | Product variants with categories |
| 🏭 **Suppliers** | 100 | Raw material suppliers |
| 👷 **Employees** | 200 | Staff across departments |

### Transaction Data

| Entity | Count | Description |
|--------|-------|-------------|
| 🛒 **Sales Orders** | 50K+ | Customer orders with statuses |
| 📋 **Purchase Orders** | 30K+ | Supplier purchase orders |
| 📦 **Inventory Movements** | 100K+ | Stock in/out movements |
| ⚙️ **Production Records** | 20K+ | Manufacturing batches |

### Reference Data

| Entity | Count | Description |
|--------|-------|-------------|
| 🏢 **Warehouses** | 10 | Storage locations |
| 💰 **Price Lists** | Multiple | Tiered pricing |
| 💳 **Payment Terms** | Various | Payment configurations |

---

## 🎯 Benchmark Tasks

### 1. NL2SQL Evaluation

Test model's ability to convert natural language questions to SQL queries.

```sql
-- Question: "What were the top 5 products by sales last month?"
-- Expected SQL:
SELECT 
    p.name,
    SUM(oi.quantity * oi.unit_price) as total_sales
FROM order_items oi
JOIN products p ON oi.product_id = p.id
JOIN orders o ON oi.order_id = o.id
WHERE o.order_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
GROUP BY p.name
ORDER BY total_sales DESC
LIMIT 5;
```

### 2. Anomaly Detection

Identify anomalies in production data (output, defects, downtime).

```python
# Input: 6 months of production data
# Task: Detect anomalies
# Metrics: Precision, Recall, F1-Score
```

### 3. Forecasting

Predict future demand based on historical data.

```python
# Input: 2 years of demand data
# Task: Forecast next quarter demand
# Metrics: MAE, RMSE, MAPE
```

### 4. Report Generation

Generate executive summaries from raw data.

```python
# Input: Raw data tables
# Task: Generate insights
# Metrics: Accuracy, Completeness, Clarity
```

---

## 📁 Project Structure

```
Prism-Enterprise-Benchmark/
├── data/
│   ├── raw/                    # Generated raw data
│   ├── processed/              # Cleaned data
│   └── synthetic/              # Final benchmark data
├── generators/
│   ├── generate_all.py         # Main generator
│   └── generators/             # Entity generators
├── benchmarks/
│   ├── nl2sql/                 # NL2SQL evaluation
│   ├── anomaly/                # Anomaly detection
│   └── forecasting/            # Time series forecasting
├── results/                    # Evaluation results
├── configs/                    # Configuration files
└── docs/                       # Documentation
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Samar-Khalid/Prism-Enterprise-Benchmark.git
cd Prism-Enterprise-Benchmark

# Install dependencies
pip install -r requirements.txt
```

### Generate Synthetic Data

```bash
# Generate all synthetic data
python generators/generate_all.py

# Generate specific entity
python generators/generate_all.py --entity customers --count 1000
```

### Run Benchmarks

```bash
# Run NL2SQL benchmark
python benchmarks/nl2sql/evaluate.py --model gpt-4

# Run anomaly detection benchmark
python benchmarks/anomaly/evaluate.py --model isolation_forest

# Run forecasting benchmark
python benchmarks/forecasting/evaluate.py --model prophet
```

---

## 📊 Leaderboard

| Model | NL2SQL Accuracy | Anomaly F1 | Forecast MAE | Rank |
|-------|----------------|------------|--------------|------|
| GPT-4 | - | - | - | - |
| Claude-3 | - | - | - | - |
| Fine-tuned LLaMA | - | - | - | - |
| Custom Transformer | - | - | - | - |

> 🏆 **Submit your results!** See [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [DATA.md](docs/DATA.md) | Dataset documentation |
| [GENERATORS.md](docs/GENERATORS.md) | Generator documentation |
| [BENCHMARKS.md](docs/BENCHMARKS.md) | Benchmark methodology |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guidelines |

---

## ⚠️ Important Notice

> **This dataset is 100% synthetic.** 
> 
> It resembles a fertilizer manufacturing company but **does not represent any real company's data**. All customer names, product names, financial values, and transactions are fictional.

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create your feature branch
3. Add your benchmark results
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### 📊 Repository Stats

![GitHub stars](https://img.shields.io/github/stars/Samar-Khalid/Prism-Enterprise-Benchmark?style=social)
![GitHub forks](https://img.shields.io/github/forks/Samar-Khalid/Prism-Enterprise-Benchmark?style=social)

**Made for AI Research**

</div>
