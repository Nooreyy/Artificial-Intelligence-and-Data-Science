import pandas as pd
import numpy as np

# For reproducibility
np.random.seed(42)

n = 100

# 1) Generate column
genders  = np.random.choice(['Male', 'Female'], size=n)
cities   = np.random.choice(['Lahore', 'Karachi', 'Islamabad', 'Peshawar', 'Quetta'], size=n)
subjects = np.random.choice(['Math', 'English', 'Physics', 'Chemistry', 'Biology'], size=n)
# loc = 60 -> mean (average) = 60 , scale = 20 -> standard deviation (spread) = 20
marks    = np.random.normal(loc=60, scale=20, size=n)

# 2) Inject a few extreme outliers
out_idx = np.random.choice(n, size=3, replace=False) #replace = False means don’t pick the same element more than once (no repetition).
marks[out_idx] = [150, -20, 130]  # two high outliers and one negative

# 3) Admission status
admission = np.where(np.random.rand(n) > 0.7, 'Yes', 'No')

# 4) Assemble into DataFrame
# DataFrame is an object in Python
df = pd.DataFrame({
    'Gender'   : genders,
    'City'     : cities,
    'Marks'    : marks,
    'Subject'  : subjects,
    'Admission': admission
})

# 5) Randomly introduce ~7% missing values per column
for col in df.columns:
    missing_count = int(0.07 * n)  # mathematical function to convert % into the numbers

# df.index -> all row indices of the DataFrame.
# np.random.choice(..., size=missing_count, replace=False) -> randomly picks unique row indices equal to missing_count.

# These will be the rows where missing values are introduced.
    missing_indices = np.random.choice(df.index, size=missing_count, replace=False)
    df.loc[missing_indices, col] = np.nan # .loc selects rows (missing_indices) and column (col) and adds NaN in the place of missing values

# 6) Inspect the first few rows
print(df)