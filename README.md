## ⚡ Smart Energy Consumption Prediction using Machine Learning & AI

### 📌 Project Overview

This project aims to analyze and predict household energy consumption using historical power usage data combined with external weather parameters.
The model helps users estimate future energy usage based on environmental and calendar factors, enabling smart planning and energy optimization—supporting sustainability and smart energy systems.

---

## 🎯 Objectives

* Perform preprocessing and feature engineering on large energy datasets
* Train machine learning models to predict electricity consumption
* Improve prediction accuracy using Hybrid Ensemble Models
* Integrate real-time prediction using a Flask-based web application
* Build a user-friendly UI for predicting energy usage

---

## 📂 Dataset

| Dataset                                             | Description                                                       |
| --------------------------------------------------- | ----------------------------------------------------------------- |
| **Individual Household Electric Power Consumption** | Time-series dataset of household electricity usage from 2006–2010 |
| **Weather Dataset (Bangalore 2006-2010)**           | Temperature & humidity data merged with energy data               |
| **Merged Dataset**                                  | Combined dataset used for final training                          |

---

## 🧠 Model Pipeline

### ✔ Steps Performed

* Data cleaning & handling missing values
* Timestamp conversion & resampling
* Feature engineering
  ➤ DayOfWeek, IsWeekend
  ➤ PrevDayPower
  ➤ RollingMean_3
* Weather data integration
* Multiple model training & comparison

### 🏆 Models Used

| Model                                 | R² Score  |
| ------------------------------------- | --------- |
| Linear Regression                     | Low       |
| Random Forest                         | Moderate  |
| XGBoost                               | Improved  |
| LightGBM                              | Higher    |
| **Hybrid Ensemble (RF + XGB + LGBM)** | **0.99+** |

---

## 🖥 Flask Web App UI

Users input:

* 🌡 Temperature (°C)
* 💧 Humidity (%)
* 📅 Date

Backend automatically calculates other internal model features and predicts consumption.

### 🔮 Output Example

```
Predicted Energy Consumption: 0.82 kW
```

---

## 📦 Tech Stack

| Category         | Technology                                     |
| ---------------- | ---------------------------------------------- |
| Language         | Python                                         |
| ML Libraries     | Scikit-Learn, XGBoost, LightGBM, Pandas, NumPy |
| Model Deployment | Flask                                          |
| Frontend         | HTML, CSS                                      |
| Notebook         | Google Colab                                   |
| Version Control  | Git & GitHub                                   |

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/MehaBN/SmartEnergyProject.git
cd SmartEnergyProject
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Flask App

```bash
python app.py
```

### 4️⃣ Open Browser

```
http://127.0.0.1:5000/
```

---

## 📌 Project Status

✔ Data preprocessing completed
✔ Dataset merged & feature engineered
✔ ML model training completed
✔ Hybrid model deployed
✔ Web UI ready for prediction

---


## 🏁 Future Enhancements

🔹 Add bill estimation (₹ cost calculation)
🔹 Deploy web app on cloud (Render / Railway / AWS)
🔹 Add graph-based trend visualization
🔹 Train additional deep learning models (LSTM, GRU)

---

## 👩‍💻 Developer

**Meha B N**
BE Computer Science Engineering

📌 Internship: **Edunet Foundation – AI Project**

🔗 GitHub Repository
[https://github.com/MehaBN/SmartEnergyProject.git](https://github.com/MehaBN/SmartEnergyProject.git)

---

### ⭐ If you like this project, please star the repository!

---

