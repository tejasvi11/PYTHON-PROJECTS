# 🦠 COVID-19 Data Analysis (India & Global)

This project explores COVID-19 case data using Python, with an emphasis on data cleaning, transformation, and preliminary analysis. The goal is to visualize confirmed cases, deaths, and recoveries across different regions and time periods.

## 📁 Files Included

- `covid_19_data(in).csv` — Raw dataset containing COVID-19 reports by date, region, and case type.
- `covid19analysis.ipynb` — Jupyter Notebook with all analysis, cleaning, and visualization code.

## 📊 Dataset Overview

The dataset includes:
- **Date-wise** and **location-wise** records of COVID-19 cases
- Fields like:
  - `Confirmed`, `Deaths`, `Recovered`
  - `Country/Region`, `Province/State`, `ObservationDate`

## 🧪 Analysis Performed

- Data preprocessing:
  - Dropped unnecessary columns
  - Renamed for clarity
  - Filled missing values using `SimpleImputer`
- Time series formatting using `pandas.to_datetime()`
- Basic aggregations and visualizations (line plots, bar charts)

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Scikit-learn (for missing value imputation)

## 📌 How to Run

1. Open `covid19analysis.ipynb` in Jupyter Notebook or Google Colab
2. Make sure `covid_19_data(in).csv` is in the same directory
3. Run the notebook cells step-by-step

## 📈 Future Improvements

- Add predictive modeling (e.g., time series forecasting)
- Create interactive dashboards using Plotly or Streamlit
- Visualize country comparisons and recovery rates

## 📚 Acknowledgments

Dataset inspired by early COVID-19 public data sources from John Hopkins University.

