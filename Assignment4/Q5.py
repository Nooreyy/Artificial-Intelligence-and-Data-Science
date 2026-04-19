import numpy as np
import pandas as pd

# Ratings matrix: 6 users x 5 movies (0 = not rated)
ratings_raw = np.array([
    [5, 3, 0, 1, 4],
    [4, 0, 4, 1, 2],
    [1, 1, 0, 5, 0],
    [0, 0, 5, 4, 0],
    [3, 4, 4, 0, 2],
    [2, 0, 3, 5, 4],
])
movies = ["Inception", "Interstellar", "Avengers", "Parasite", "Dune"]
df = pd.DataFrame(ratings_raw, columns=movies,
                  index=[f"User{i+1}" for i in range(6)])

print("Original ratings (0 = missing):")
print(df)

# 1. Average rating per movie (excluding 0s)
def avg_nonzero(col):
    vals = col[col != 0]
    return vals.mean() if len(vals) > 0 else 0

avg_ratings = df.apply(avg_nonzero)
print("\nAverage rating per movie:")
print(avg_ratings.round(2))

# 2. Most popular movie (highest average)
most_popular = avg_ratings.idxmax()
print(f"\nMost popular movie: {most_popular} "
      f"(avg: {avg_ratings[most_popular]:.2f})")

# 3. Replace 0s with the movie's average rating
df_filled = df.copy()
for movie in movies:
    avg = avg_ratings[movie]
    df_filled[movie] = df_filled[movie].replace(0, round(avg, 2))

print("\nRatings after filling missing values:")
print(df_filled)

# Bonus: Top movie per user (after filling)
df_filled["Favorite"] = df_filled.idxmax(axis=1)
print("\nEach user's top-rated movie:")
print(df_filled["Favorite"])