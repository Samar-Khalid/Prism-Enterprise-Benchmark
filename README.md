# Prism Enterprise Benchmark

> Synthetic Benchmark Dataset for Enterprise AI Research

---

## Overview

A **100% synthetic** benchmark dataset designed to evaluate AI/ML models on enterprise manufacturing scenarios. No real company data is used.

---

## 🎯 Purpose

Provide a realistic, standardized benchmark for:
- NL2SQL model evaluation
- Enterprise anomaly detection
- Manufacturing forecast testing
- BI dashboard validation

---

## 📊 Dataset Characteristics

| Attribute | Value |
|-----------|-------|
| Company | Prism Fertilizers (Fictional) |
| Industry | Fertilizer Manufacturing |
| Records | 100K+ synthetic transactions |
| Tables | 20+ enterprise entities |
| Time Range | 3 years synthetic data |

---

## 📦 Dataset Contents

### Core Entities
- **Customers** — 500 fictional B2B customers
- **Products** — 50 product variants
- **Suppliers** — 100 fictional suppliers
- **Employees** — 200 fictional employees

### Transaction Data
- **Sales Orders** — 50K+ orders
- **Purchase Orders** — 30K+ orders
- **Inventory Movements** — 100K+ transactions
- **Production Records** — 20K+ batches

### Reference Data
- **Warehouses** — 10 locations
- **Price Lists** — Multiple tiers
- **Payment Terms** — Various configurations

---

## 🎯 Benchmark Tasks

### 1. NL2SQL Evaluation
```
Question: "What were the top 5 products by sales last month?"
Expected: Correct SQL query and results
```

### 2. Anomaly Detection
```
Input: 6 months of production data
Task: Identify anomalies in output, defects, downtime
```

### 3. Forecasting
```
Input: 2 years of demand data
Task: Predict next quarter demand by product
```

### 4. Report Generation
```
Input: Raw data tables
Task: Generate executive summary with key insights
```

---

## 📂 Structure

```
Prism-Enterprise-Benchmark/
├── data/
│   ├── raw/              # Generated raw data
│   ├── processed/        # Cleaned data
│   └── synthetic/        # Final benchmark data
├── generators/           # Data generation scripts
├── benchmarks/           # Evaluation tasks
├── results/              # Model evaluation results
└── docs/                 # Documentation
```

---

## 🚀 Quick Start

```bash
# Generate synthetic data
python generators/generate_all.py

# Run benchmark
python benchmarks/evaluate.py --model gpt-4

# View results
python results/visualize.py
```

---

## 📊 Leaderboard

| Model | NL2SQL Accuracy | Anomaly F1 | Forecast MAE |
|-------|----------------|------------|--------------|
| GPT-4 | TBD | TBD | TBD |
| Claude | TBD | TBD | TBD |
| Custom | TBD | TBD | TBD |

---

## ⚠️ Important

> **This dataset is 100% synthetic.** It resembles a fertilizer manufacturing company but does not represent any real company's data.

---

## 📝 License

MIT License — Free for research and commercial use
