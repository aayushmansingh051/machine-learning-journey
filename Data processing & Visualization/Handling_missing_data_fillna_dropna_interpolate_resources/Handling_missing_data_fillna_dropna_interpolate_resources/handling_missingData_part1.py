import pandas as pd
df = pd.read_csv("weather_data.csv")

new_df = df.fillna(0)   # returns a new DataFrame
print(new_df)
print("next part\n")
new_df=df.fillna({'windspeed': df.windspeed.mean()})
print(new_df)

print("next part\n")
new_df = df.fillna(method="ffill")
print(new_df)