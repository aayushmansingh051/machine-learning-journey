import pandas as pd

# Use the full path to the CSV file
df = pd.read_csv(r"C:\code\Data processing & Visualization\Dataframe_basics_resources\Dataframe_basics_resources\movies.csv")

print(df.head(3))
print(df.shape)
print(df.columns)
print(df.industry.unique())
print(df['language'].unique())
print(df.studio.unique())
print(df.studio=='Marvel Studios')
print(df.describe())
print(df.imdb_rating==df.imdb_rating.max())
print("A")
print(df[(df.imdb_rating==df.imdb_rating.max())| (df.imdb_rating==df.imdb_rating.min())])

df["age"]=df['release_year'].apply(lambda x:2023-x)
print(df.head(4))