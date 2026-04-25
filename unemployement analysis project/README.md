# 📊 Unemployment Analysis with Python

A data analysis project that explores unemployment trends in India using Python, with a focus on the impact of COVID-19 on the labour market.

---

## 🗂️ Project Structure

```
unemployment_project/
├── unemployment_analysis.py          ← Main Python script
├── Unemployment in India.csv         ← Dataset 1 (monthly data)
├── Unemployment_Rate_upto_11_2020.csv← Dataset 2 (region-wise data)
└── README.md                         ← This file
```

---

## 📌 About the Project

Unemployment is measured by the **unemployment rate** — the number of people who are unemployed as a percentage of the total labour force.

This project analyzes unemployment data across Indian states from 2019 to 2020, with special focus on the sharp rise in unemployment caused by the **COVID-19 pandemic and lockdowns**.

---

## 📦 Dataset

- **Source:** [Kaggle - Unemployment in India](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india)
- **Files Used:**
  - `Unemployment in India.csv` — Monthly unemployment data by state
  - `Unemployment_Rate_upto_11_2020.csv` — Region-wise data with Urban/Rural split

---

## 🛠️ Libraries Used

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical operations |
| `matplotlib` | Plotting and visualization |
| `seaborn` | Advanced and styled visualizations |

---

## ▶️ How to Run

### Option 1: Run Locally (VS Code / Terminal)

**Step 1:** Install required libraries
```bash
pip install pandas numpy matplotlib seaborn
```

**Step 2:** Place all files in the same folder, then run:
```bash
python unemployment_analysis.py
```

### Option 2: Run on Google Colab (Recommended - No Installation Needed)

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Upload `unemployment_analysis.py`
3. Upload both CSV files using:
```python
from google.colab import files
uploaded = files.upload()
```
4. Run the script — all libraries are pre-installed on Colab

---

## 📊 Visualizations Generated

| Plot | Description |
|------|-------------|
| `plot1_unemployment_over_time.png` | Line chart showing unemployment rate trend over time |
| `plot2_statewise_unemployment.png` | Bar chart of average unemployment rate by state |
| `plot3_covid_impact.png` | Before vs After COVID-19 comparison |
| `plot4_urban_vs_rural.png` | Urban vs Rural unemployment comparison |
| `plot5_heatmap.png` | Heatmap of unemployment across states and months |

---

## 🔍 Key Findings

- Unemployment rate **spiked sharply in April–May 2020** due to COVID-19 lockdowns
- Some states like **Tripura and Haryana** recorded higher unemployment rates
- **Urban areas** showed higher unemployment rates compared to rural areas during lockdown
- Average unemployment nearly **doubled** after COVID-19 compared to pre-COVID levels

---

## 💡 Concepts Covered

- Data Loading and Cleaning with Pandas
- Handling missing values
- Exploratory Data Analysis (EDA)
- Time-series visualization
- Impact analysis (Before vs After COVID)
- Heatmap visualization

---

## 👤 Author

**[Your Name]**
BTech 3rd Year | Internship Project
[Your College Name]

---

## 📄 License

This project is for educational purposes only. Dataset credits go to [Gokulraj KMV on Kaggle](https://www.kaggle.com/gokulrajkmv).
