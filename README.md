# 🍽️ Zomato Dataset Cleaning and Preprocessing

This repository contains a Jupyter Notebook that performs data cleaning and preprocessing on the **Zomato Restaurant Dataset**. The goal is to prepare the dataset for meaningful analysis by handling missing values, cleaning inconsistent formats, and transforming columns for better usability.

---

## 📁 Files Included

- `zomato_cleaning.ipynb`: The main Jupyter Notebook for cleaning the Zomato dataset.
- `zomato_data_analysis.csv`: Output CSV after cleaning (generated by the notebook).
- `zomato.csv`: Raw input dataset (not included here for size/privacy – please add it manually).

---

## 🧾 Dataset Overview

The dataset includes details about restaurants listed on Zomato, such as:

- Restaurant names and locations
- Cuisines offered
- Cost estimates
- Ratings
- Restaurant types

---

## 🧼 Cleaning & Preprocessing Steps

The notebook performs the following operations:

1. **Import libraries**: Loads required Python packages (`pandas`, `numpy`).
2. **Load the dataset**: Reads `zomato.csv` using `pandas`.
3. **Drop unnecessary columns**: Removes irrelevant fields like `url`, `phone`, `reviews_list`, etc.
4. **Rename columns**: Makes column names more user-friendly (e.g., `approx_cost(for two people)` ➝ `cost_per_person`).
5. **Handle missing values**: Drops rows with missing essential information.
6. **Format cost column**: Removes commas, converts cost to numeric, and computes per person cost.
7. **Clean rating column**: Replaces 'NEW' and '-' with `NaN` and fills missing ratings with the column mean.
8. **Save cleaned data**: Writes the cleaned DataFrame to a new CSV file: `zomato_data_analysis.csv`.

---

## 🚀 How to Run

1. Clone the repository or download the notebook.
2. Place the original `zomato.csv` file in the same directory.
3. Open `zomato_cleaning.ipynb` using Jupyter Notebook or VSCode.
4. Run all cells in sequence.
5. The cleaned CSV will be saved as `zomato_data_analysis.csv`.

---

## 🔧 Requirements

- Python 3.x
- `pandas`
- `numpy`
- Jupyter Notebook (or any IDE that supports `.ipynb`)

Install dependencies (if needed):

```bash
pip install pandas numpy
```

---

## 📬 Contact

For questions or suggestions, feel free to open an issue or contact the author.

---

## 📜 License

This project is shared for educational and analytical purposes. Use it freely and responsibly.
