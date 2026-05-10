# =========================================
# STARTUP SUCCESS SCORE PREDICTOR
# Multiple Linear Regression Project
# =========================================

# Install first:
# pip install pandas numpy scikit-learn matplotlib seaborn

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# =========================================
# STEP 1: CREATE SAMPLE DATASET
# =========================================

data = {
    'Funding_Amount': [50, 80, 120, 200, 300, 500, 100, 150, 400, 600],
    'Team_Size': [5, 8, 10, 15, 20, 30, 7, 12, 25, 35],
    'Marketing_Budget': [10, 15, 20, 30, 50, 70, 12, 18, 60, 80],
    'Founder_Experience': [1, 2, 3, 5, 6, 8, 2, 4, 7, 10],
    'Social_Media_Score': [40, 50, 60, 70, 80, 95, 45, 55, 85, 98],
    'Success_Score': [45, 52, 60, 72, 80, 95, 50, 65, 88, 99]
}

df = pd.DataFrame(data)

print("\nDataset:\n")
print(df)

# =========================================
# STEP 2: DEFINE INPUTS AND OUTPUT
# =========================================

X = df[[
    'Funding_Amount',
    'Team_Size',
    'Marketing_Budget',
    'Founder_Experience',
    'Social_Media_Score'
]]

y = df['Success_Score']

# =========================================
# STEP 3: TRAIN TEST SPLIT
# =========================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# =========================================
# STEP 4: TRAIN MODEL
# =========================================

model = LinearRegression()
model.fit(X_train, y_train)

# =========================================
# STEP 5: MAKE PREDICTIONS
# =========================================

y_pred = model.predict(X_test)

print("\nPredicted Values:\n")
print(y_pred)

# =========================================
# STEP 6: MODEL EVALUATION
# =========================================

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# =========================================
# STEP 7: USER INPUT PREDICTION
# =========================================

print("\n===== ENTER STARTUP DETAILS =====")

funding = float(input("Funding Amount: "))
team = int(input("Team Size: "))
marketing = float(input("Marketing Budget: "))
experience = int(input("Founder Experience (Years): "))
social = float(input("Social Media Score: "))

new_data = np.array([[
    funding,
    team,
    marketing,
    experience,
    social
]])

prediction = model.predict(new_data)

print("\nPredicted Startup Success Score:", round(prediction[0], 2))

# =========================================
# STEP 8: VISUALIZATION
# =========================================

plt.figure(figsize=(6,5))

plt.scatter(y_test, y_pred)

plt.xlabel("Actual Success Score")
plt.ylabel("Predicted Success Score")

plt.title("Actual vs Predicted")

plt.grid(True)

plt.show()