import numpy as np
import pandas as pd

# Sample patient data
np.random.seed(1)
n = 100
ages = np.random.randint(20, 80, size=n)
bp   = np.random.randint(90, 180, size=n)

df = pd.DataFrame({"Age": ages, "BloodPressure": bp})

# 1. Average blood pressure
avg_bp = df["BloodPressure"].mean()
print(f"Average Blood Pressure: {avg_bp:.2f} mmHg")

# 2. High-risk patients (BP > 140)
high_risk = df[df["BloodPressure"] > 140]
print(f"\nHigh-risk patients (BP > 140): {len(high_risk)}")
print(high_risk.head())

# 3. Normalize both columns between 0 and 1
def normalize(series):
    return (series - series.min()) / (series.max() - series.min())

df["Age_norm"] = normalize(df["Age"])
df["BP_norm"]  = normalize(df["BloodPressure"])

print("\nNormalized data (first 5 rows):")
print(df[["Age", "Age_norm", "BloodPressure", "BP_norm"]].head())

# Bonus: Risk category breakdown
df["Risk"] = pd.cut(
    df["BloodPressure"],
    bins=[0, 120, 140, 999],
    labels=["Normal", "Elevated", "High"]
)
print("\nRisk category counts:")
print(df["Risk"].value_counts())