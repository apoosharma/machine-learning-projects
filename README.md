# 🤖 Machine Learning Assignments

End-to-end ML projects covering regression, classification, and model deployment — built as part of my ML learning journey.

---

## 📁 Projects Overview

### 📌 Assignment 1 — Linear Regression (House Price Prediction)
Predicts California housing prices using a Linear Regression model.

- **Dataset:** California Housing Dataset (sklearn)
- **Preprocessing:** Feature scaling with StandardScaler, train-test split (80:20)
- **Evaluation:**
  - R² Score: ~0.60
  - MAE, MSE computed and analyzed
- **Output:** Predicted vs Actual values scatter plot

---

### 📌 Assignment 2 — Classification (Iris Flower Species)
Classifies Iris flower species using two different ML algorithms.

- **Dataset:** Iris Dataset (sklearn)
- **Models:** Logistic Regression & Decision Tree Classifier
- **Split:** 70:30 (train:test)
- **Evaluation:** Accuracy, Precision, Recall, F1-score, Confusion Matrix
- **Output:** Confusion matrix plots for both models with comparison

---

### 📌 Assignment 3 — Flask Deployment (House Price Predictor Web App)
Deployed the Assignment 1 regression model as a live web app using Flask.

- **Model:** Linear Regression trained on California Housing Dataset
- **Features accepted:** Median Income, House Age, Avg Rooms, Avg Bedrooms, Block Population, Avg Occupancy, Latitude, Longitude
- **Output:** Estimated house price in USD
- **Stack:** Flask + Joblib + HTML form

> 🖥️ Sample prediction: Input values for a Los Angeles-area block → **Estimated Price: $397,175.91**

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| scikit-learn | Model training & evaluation |
| pandas & numpy | Data handling |
| matplotlib & seaborn | Visualizations |
| Flask | Web deployment |
| joblib | Model serialization |

---

## 🚀 How to Run

**1. Clone the repo**
```bash
git clone https://github.com/apoosharma/ml-assignments.git
cd ml-assignments
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the notebooks**
Open any `.ipynb` file in Jupyter Notebook or VS Code.

**4. Run the Flask app**
```bash
cd assignment3_flask_deployment
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

> **Note:** Run the Assignment 1 notebook first to generate `model.pkl` before launching the Flask app.

---

## 📂 Folder Structure

```
ml-assignments/
├── assignment1_regression/
│   ├── regression.ipynb
│   └── plots/
├── assignment2_classification/
│   ├── classification.ipynb
│   └── plots/
├── assignment3_flask_deployment/
│   ├── app.py
│   ├── model.pkl
│   └── templates/
│       └── index.html
├── requirements.txt
└── README.md
```

---

## 👩‍💻 Author

**Apoorva** — ECE undergrad @ VIT 
📎 [GitHub](https://github.com/apoosharma) • [LinkedIn](https://www.linkedin.com/in/apoorva-rr)
