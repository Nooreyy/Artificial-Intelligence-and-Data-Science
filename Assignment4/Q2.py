import numpy as np

# Simulate 30 days of daily sales (in $)
np.random.seed(7)
sales = np.random.randint(1000, 10000, size=30).astype(float)
days = np.arange(1, 31)

# 1. Total monthly revenue
total_revenue = sales.sum()
print(f"Total monthly revenue: ${total_revenue:,.2f}")

# 2. Best-selling day
best_day_index = np.argmax(sales)
print(f"\nBest-selling day: Day {best_day_index + 1}")
print(f"Sales on best day: ${sales[best_day_index]:,.2f}")

# 3. 7-day moving average (manual with NumPy)
window = 7
moving_avg = np.array([
    sales[i:i+window].mean()
    for i in range(len(sales) - window + 1)
])

print(f"\n7-Day Moving Average (Day 7 onwards):")
for i, avg in enumerate(moving_avg):
    print(f"  Day {i+window}: ${avg:,.2f}")

# Bonus: Days above average
daily_avg = sales.mean()
above_avg = np.where(sales > daily_avg)[0] + 1
print(f"\nAverage daily sales: ${daily_avg:,.2f}")
print(f"Days above average: {above_avg}")