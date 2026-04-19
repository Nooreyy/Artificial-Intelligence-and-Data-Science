import numpy as np
import pandas as pd

# Car counts per hour (24 hours)
np.random.seed(99)
car_counts = np.random.randint(100, 800, size=24)
# Inject a spike to make it interesting
car_counts[8]  = 1500   # morning rush
car_counts[17] = 1800   # evening rush

hours = [f"{h:02d}:00" for h in range(24)]
df = pd.DataFrame({"Hour": hours, "Cars": car_counts})

# 1. Peak traffic hour
peak_idx  = df["Cars"].idxmax()
peak_hour = df.loc[peak_idx, "Hour"]
peak_cars = df.loc[peak_idx, "Cars"]
print(f"Peak traffic hour: {peak_hour} with {peak_cars} cars")

# 2. Total cars per day
total_cars = df["Cars"].sum()
print(f"Total cars today: {total_cars}")

# 3. Detect outliers using Z-score (|z| > 2 = spike)
mean = df["Cars"].mean()
std  = df["Cars"].std()
df["Z_score"] = (df["Cars"] - mean) / std

spikes = df[df["Z_score"].abs() > 2]
print(f"\nAbnormal traffic spikes (|Z| > 2):")
print(spikes[["Hour", "Cars", "Z_score"]].to_string(index=False))

# Bonus: Hourly average
print(f"\nHourly average: {mean:.1f} cars")
print(f"Std deviation:  {std:.1f} cars")
