# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_titles.csv")
print(f"Dataframe dimension:{df.shape}")
df.head()

display(df.isna().any())

for col in df.columns:
    if df[col].isna().any():
        df[col] = df[col].fillna(df[col].mode()[0])
display(df.isna().any())

df_year = df['release_year'].value_counts()
df_year

df_year_count = df['release_year'].value_counts().sort_values(ascending=False)
df_year_count

plt.figure(figsize=(8,6))
top_20_years = df_year_count.nlargest(20)
sns.barplot(x=top_20_years.index, y=top_20_years.values, palette="viridis")
plt.xlabel("Release Year")
plt.ylabel("Number of movies produced")
plt.title("Number of Movies Released per Year")
plt.xticks(rotation=90)
plt.show()

content_type = df['type'].value_counts()
colors = sns.color_palette('dark')[0:len(content_type)]
plt.figure(figsize=(8,6))
plt.pie(content_type, labels=content_type.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Content type distribution')
plt.show()

genres = df['listed_in'].value_counts()
top_genre = genres.nlargest(20)
plt.figure(figsize=(10,8))
sns.barplot(y=top_genre.index, x=top_genre.values, palette="viridis")
plt.ylabel("Genres")
plt.xlabel("Count")
plt.title("Top 20 most popular genre on Netflix")
plt.yticks(rotation=0, ha='right')
plt.show()

country_count = df['country'].value_counts()
top_country_count = country_count.nlargest(10)
plt.figure(figsize=(8,6))
sns.barplot(x=top_country_count.index, y=top_country_count.values, palette="viridis")
plt.ylabel("Country")
plt.xlabel("Count")
plt.title("Top 10 most popular countries on Netflix")
plt.xticks(rotation=45, ha='right')
plt.show()

ratings_count = df['rating'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=ratings_count.index, y=ratings_count.values, palette='viridis', hue=ratings_count.index, legend=False)
plt.xlabel("Classification")
plt.ylabel("Titles count")
plt.title("Netflix content rating distribution")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
