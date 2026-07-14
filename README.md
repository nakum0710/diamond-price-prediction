# 💎 Diamond Price Prediction using Machine Learning

An end-to-end Machine Learning project that predicts diamond prices based on their physical characteristics using **XGBoost Regressor**. The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, hyperparameter tuning, model evaluation, and an interactive **Streamlit** web application.

---

## 📌 Project Overview

The price of a diamond depends on several factors such as its weight, cut, color, clarity, and dimensions. This project uses machine learning to accurately estimate the price of a diamond based on these features.

---

## 🎯 Objectives

- Perform data cleaning and preprocessing
- Conduct Exploratory Data Analysis (EDA)
- Train multiple regression models
- Optimize the best model using hyperparameter tuning
- Evaluate model performance using regression metrics
- Deploy the trained model with Streamlit

---

## 📊 Dataset

**Dataset:** Diamonds Dataset

**Number of Records:** 53,940

### Features

| Feature | Description |
|----------|-------------|
| carat | Weight of the diamond |
| cut | Quality of the cut |
| color | Diamond color grade |
| clarity | Diamond clarity grade |
| depth | Total depth percentage |
| table | Width of the top of the diamond |
| x | Length (mm) |
| y | Width (mm) |
| z | Depth (mm) |
| price | Target variable (Diamond Price) |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit
- Joblib/Pickle

---

## 📂 Project Workflow

```
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Data Preprocessing
        │
        ▼
Train-Test Split
        │
        ▼
Model Training
        │
        ▼
Hyperparameter Tuning
        │
        ▼
Model Evaluation
        │
        ▼
Model Saving
        │
        ▼
Streamlit Deployment
```

---

## 🤖 Machine Learning Model

The final model used is **XGBoost Regressor**, selected after comparing multiple regression algorithms and optimizing it using **RandomizedSearchCV**.

---

## 📈 Model Performance

| Metric | Score |
|---------|-------|
| R² Score | **0.9804** |
| Mean Absolute Error (MAE) | **272.27** |
| Root Mean Squared Error (RMSE) | **546.65** |

The model explains approximately **98% of the variance** in diamond prices, demonstrating excellent predictive performance.

---

## 🚀 Streamlit Application

The web application allows users to:

- Enter diamond characteristics
- Predict the estimated diamond price instantly
- Interact with a simple and user-friendly interface

---

## 📁 Project Structure

```
diamond-price-prediction-ml/
│
├── app7.py
├── diamond_price_project13.ipynb
├── model.pkl
├── columns.pkl
├── diamond_price_dataset.csv
├── requirements.txt
├── README.md
│
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/diamond-price-prediction-ml.git
```

### 2. Navigate to the Project Directory

```bash
cd diamond-price-prediction-ml
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
pandas
numpy
scikit-learn
xgboost
matplotlib
seaborn
joblib
```

---

## 👨‍💻 Author

**Mansi Nakum**
