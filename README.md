# 🔍 Security Log Analyzer with Threat Scoring

This project is a Python-based tool that parses system log files, detects suspicious activities, and scores threats using a basic severity model. It supports mapping events to the MITRE ATT&CK framework and visualizes results using a Jupyter Notebook.

## 🚀 Features
- Log file parser supporting standard syslog format
- Threat scoring engine based on severity keywords
- MITRE ATT&CK tactic tagging (basic example implementation)
- Visual summary of top threats and IPs in Jupyter
- Customizable regex pattern matching

## 🛠 Requirements
- Python 3.8+
- pandas
- matplotlib
- re
- json
- Jupyter Notebook

Install using:
```bash
pip install -r requirements.txt
