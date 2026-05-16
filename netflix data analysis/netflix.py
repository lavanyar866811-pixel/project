import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\ELCOT\Downloads\netflix data analysis\data\netflix_titles.csv", encoding='latin1')


print(df.head())

type_count = df['type'].value_counts()

print("\nMovies vs TV Shows:")
print(type_count)


top_countries = df['country'].value_counts().head(10)

print("\nTop 10 Countries:")
print(top_countries)

ratings = df['rating'].value_counts()

print("\nRatings:")
print(ratings)



type_count.plot(kind='bar', figsize=(6,5))

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("netflix_chart.png")

plt.show()



year_count = df['release_year'].value_counts().sort_index()

year_count.plot(kind='line', figsize=(10,5))

plt.title("Netflix Content Release Trend")
plt.xlabel("Year")
plt.ylabel("Number of Shows")

plt.tight_layout()

plt.savefig("release_year_trend.png")

plt.show()
