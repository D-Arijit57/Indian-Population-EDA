# 🇮🇳 India Population Growth — Exploratory Data Analysis

## Project Overview

This project performs an Exploratory Data Analysis (EDA) on India's historical population data sourced from the **World Bank API**. It examines population trends, decade-wise growth, and key demographic milestones from **1970 to 2023**.

---

## Table of Contents

- [Data Source](#data-source)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Key Analyses](#key-analyses)
- [Visualizations](#visualizations)
- [Key Findings](#key-findings)
- [How to Run](#how-to-run)

---

## Data Source

Data is fetched live from the **World Bank Open Data API**:

```
https://api.worldbank.org/v2/country/ind/indicator/SP.POP.TOTL?format=json
```

- **Indicator:** `SP.POP.TOTL` — Total Population
- **Country:** India (`IND`)
- **Format:** JSON

---

## Requirements

Install the dependencies using:

```bash
pip install -r requirement.txt
```

**Dependencies (`requirement.txt`):**

| Package | Purpose |
|---------|---------|
| `pandas` | Data manipulation and analysis |
| `requests` | Fetching data from the World Bank API |
| `matplotlib` | Data visualization |

---

## Project Structure

```
├── Population_data.py                        # Main EDA script
├── requirement.txt                           # Python dependencies
├── Population_Growth_by_Decade.png           # Bar chart — decade-wise growth
└── India_Population_Growth_Trend_1980-2020.png  # Line chart — yearly growth trend
```

---

## Key Analyses

### 1. Data Preprocessing
- Fetched and parsed JSON response from the World Bank API
- Constructed a clean DataFrame with columns: `country`, `year`, `population`
- Converted `year` to numeric type and dropped missing values
- Computed **year-over-year population change**

### 2. Growth Statistics
- **Average yearly population change** across the full dataset
- **Total percentage growth** from 1980 to 2023
- **Year with the highest single-year increase**

### 3. Decade-Wise Analysis
- Created a `decade` column by binning years
- Aggregated total population growth per decade
- Identified the **fastest-growing decade**

### 4. Milestone Tracking
Tracked the years India crossed key population thresholds:

| Milestone | Year Crossed |
|-----------|-------------|
| 700 million | — |
| 800 million | — |
| 900 million | — |
| 1 billion | — |
| 1.1 billion | — |
| 1.2 billion | — |
| 1.3 billion | — |
| 1.4 billion | — |

> Exact milestone years are printed at runtime based on live API data.

### 5. Future Projection
- Estimated **years required to add the next 100 million people**, based on average annual growth rate.

---

## Visualizations

### India Population Growth Trend (1980–2020)
![India Population Growth Trend](India_Population_Growth_Trend__1980_-2020_.png)

A line chart showing the **year-over-year population change** between 1980 and 2020. The trend peaked around **2001** (~20 million people added per year) and has since steadily declined, indicating a slowing growth rate — consistent with demographic transition patterns.

---

### Population Growth by Decade
![Population Growth by Decade](Population_Growth_by_Decade.png)

A bar chart showing the **total population added per decade**. The 1990s saw the highest absolute growth (~190 million), while the 2020s show a sharp decline due to fewer years captured in the data and a falling annual growth rate.

---

## Key Findings

- India's population grew by over **90%** between 1980 and 2023.
- The **1990s** were the fastest-growing decade in absolute terms.
- Annual population growth **peaked around 2001** and has been declining since, reflecting falling fertility rates.
- At the current average growth rate, India adds **100 million people approximately every 5–6 years**.
- India crossed the **1 billion milestone** around the year **2000** and reached **1.4 billion** by the early 2020s.

---

## How to Run

```bash
# 1. Clone or download the project files

# 2. Install dependencies
pip install -r requirement.txt

# 3. Run the EDA script
python Population_data.py
```

The script will:
1. Fetch live data from the World Bank API
2. Print statistical summaries and insights to the console
3. Display two matplotlib charts (Growth Trend & Decade Growth)

---

## Author Notes

- The script uses **live API data**, so results may differ slightly as the World Bank updates its records.
- The 2020s decade bar appears shorter in the chart because data collection was still in progress at the time of analysis.
- Missing values are dropped before analysis to ensure data integrity.
