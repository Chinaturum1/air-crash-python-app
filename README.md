# ✈️ Aircraft Crash Analysis (1908–2024)

An exploratory data analysis of global aircraft crashes spanning over a century, built with Python and deployed as an interactive dashboard using Streamlit.

> **Note:** This dataset was also used in a separate [Excel-based analysis project](#), where pivot tables and Excel charts were used to explore the same data. This Python project takes the analysis further with programmatic cleaning, visualisation, and an interactive web app.

---

## 📌 Project Overview

This project explores a dataset of 5,035 recorded aircraft crashes from 1908 to 2024. The goal was to clean the data, answer seven research questions through visualisation, and present the findings in an interactive Streamlit dashboard.

---

## 🔬 Research Questions

| # | Question |
|---|----------|
| RQ1 | How have aircraft crashes trended over the years? |
| RQ2 | Which countries recorded the most aircraft crashes? |
| RQ3 | Which operators or airlines were involved in the most crashes? |
| RQ4 | Which aircraft types appeared most in crash records? |
| RQ5 | Which months historically record the most crashes? |
| RQ6 | What is the difference between fatalities in the air, casualties on the ground, and those aboard? |
| RQ7 | What proportion of crashes had zero survivors? |

---

## 📊 Charts Used

| Research Question | Chart Type |
|---|---|
| RQ1 — Crash trend over time | Line Chart |
| RQ2 — Top countries by crashes | Horizontal Bar Chart |
| RQ3 — Top operators by crashes | Horizontal Bar Chart |
| RQ4 — Top aircraft types | Horizontal Bar Chart |
| RQ5 — Crashes by month | Bar Chart |
| RQ6 — Air vs Ground vs Aboard fatalities | Bar Chart |
| RQ7 — Survivor proportion | Pie Chart |

---

## 🧹 Data Cleaning Steps

- Filled missing values in `Country/Region` and `Operator` columns with `"Unknown"`
- Stripped whitespace from all string columns
- Applied title case across all object columns
- Replaced `"'-"` entries with `"Unknown"`
- Mapped US state names in `Country/Region` to `"United States"` for accurate country-level analysis
- Created a derived `Survivors` column calculated as `Aboard - Fatalities (air)`

---

## 🗂️ Project Structure

```
aircrash-analysis/
│
├── AircrashResearch.ipynb        # Jupyter notebook with cleaning and charts
├── app.py                        # Streamlit dashboard app
├── aircrahesFullDataUpdated_2024.csv  # Dataset
└── README.md
```

---

## 🛠️ Tools & Libraries

- **Python**
- **Pandas** — data cleaning and manipulation
- **Matplotlib** — data visualisation
- **Seaborn** — imported for styling support
- **Streamlit** — interactive web dashboard
- **Jupyter Notebook** — exploratory analysis

---

## ▶️ How to Run the Streamlit App

1. Clone the repository
```bash
git clone https://github.com/your-username/aircrash-analysis.git
cd aircrash-analysis
```

2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

3. Install dependencies
```bash
pip install pandas matplotlib seaborn streamlit
```

4. Run the app
```bash
streamlit run app.py
```

---

## 💡 Key Findings

- Crash frequency rose sharply through the mid-20th century as commercial aviation expanded, peaking around the 1970s–1980s before declining steadily.
- The United States recorded the highest number of crashes, largely due to its long aviation history and flight volume.
- Military operators dominated the top 10 operators by crash frequency.
- A significant proportion of crashes resulted in zero survivors, though the share with survivors reflects improving safety standards over time.
- Ground casualties, while smaller in number, highlight the wider community impact of aviation incidents.

---

## ✍️ Author

**Okonkwo Uchechukwu Faith**  
[GitHub](https://github.com/your-username) · [LinkedIn](https://linkedin.com/in/your-link)
