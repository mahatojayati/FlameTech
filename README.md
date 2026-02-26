# Team Name - FlameTech

Project Name - Vedic Financial Compute Engine

Project Statement - Fast interest and calculator using Nikhilam Sutra

Track - FinTech & Smart Computing

Team Members - 
1. Sahil Gazi (1230439255)
2. Nishtha Sahani (1230439201)
3. Priyanshu Kumar (1230439224)
4. Jayati Mahato (1230439154)
# 🏦 Vedic Financial Compute Engine  
### Fast EMI & Interest Calculator using Vedic Mathematics (Nikhilam Sutra)

---

## 🚀 Problem Statement

Traditional financial calculators rely on conventional arithmetic methods that can be computationally heavy at scale. In high-frequency financial systems (loan portals, banking apps, micro-finance tools), efficiency and precision matter.

We propose a **Vedic Financial Compute Engine** that applies principles inspired by the **Nikhilam Sutra** from Vedic Mathematics to optimize financial computations such as:

- EMI calculation
- Simple Interest
- Compound Interest

---

## 💡 Solution Overview

The system provides:

- 🧮 EMI Calculator
- 📈 Simple Interest Calculator
- 📊 Compound Interest Calculator
- ⚡ Optimized computational logic
- 🏦 Bank-style interactive UI using Streamlit
- 📦 Deployment-ready structure

The goal is to demonstrate:
- Faster arithmetic operations
- Modular compute architecture
- Clean fintech-style frontend

---

## 🏗️ System Architecture


---

## 🧠 Key Features

- Modular Python package structure
- Clean separation of UI and computation logic
- Efficient EMI formula implementation
- Scalable design
- Ready for deployment (Render/Heroku compatible)

---

## 📂 Project Structure

---

## 🧮 Financial Formulas Used

### EMI Formula

\[
EMI = \frac{P \cdot r (1+r)^n}{(1+r)^n - 1}
\]

Where:
- P = Principal
- r = Monthly Interest Rate
- n = Number of Months

---

### Simple Interest

\[
SI = \frac{P \cdot R \cdot T}{100}
\]

---

### Compound Interest

\[
CI = P \left(1 + \frac{R}{100n} \right)^{nT} - P
\]

---

## ⚙️ Tech Stack

- Python 3.x
- Streamlit
- Modular Package Design
- Custom CSS Styling

---

## 📊 Efficiency Focus

- Reduced redundant recalculations
- Optimized exponentiation logic
- Minimal UI overhead
- Clean compute layer isolation

Future Scope:
- Benchmark vs traditional implementation
- Amortization schedule generator
- PDF report export
- REST API microservice version
- Integration with fintech backends

---

## 🖥️ How to Run Locally

```bash
git clone <repo-url>
cd vedic-financial-engine
pip install -r requirements.txt
streamlit run app.py
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0

