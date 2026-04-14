import pandas as pd
import matplotlib
matplotlib.use('Agg')  # ADD THIS LINE
import matplotlib.pyplot as plt
import seaborn as sns

# Load results
df = pd.read_csv('results/responses.csv')

print(f"Total responses: {len(df)}")
print(f"\nRatings by model:")
print(df.groupby('model')['auto_rating'].value_counts().unstack(fill_value=0))
print(f"\nAverage rating by category:")
print(df.groupby('category')['auto_rating'].mean().round(2))

# Chart 1: Ratings by model
plt.figure(figsize=(10, 6))
df.groupby('model')['auto_rating'].value_counts().unstack(fill_value=0).plot(
    kind='bar', color=['red', 'orange', 'green']
)
plt.title('Response Ratings by Model (0=Refused, 1=Partial, 2=Answered)')
plt.xlabel('Model')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/chart1_ratings_by_model.png')
print("\nChart 1 saved!")

# Chart 2: Ratings by category
plt.figure(figsize=(10, 6))
df.groupby('category')['auto_rating'].mean().sort_values().plot(
    kind='bar', color='steelblue'
)
plt.title('Average Rating by Attack Category (higher = more answered)')
plt.xlabel('Category')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/chart2_ratings_by_category.png')
print("Chart 2 saved!")