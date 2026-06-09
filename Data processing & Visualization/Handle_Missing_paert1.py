import pandas as pd

df = pd.read_csv(
    r"C:\code\Data processing & Visualization\Handling_missing_data_fillna_dropna_interpolate_resources.zip",
    compression='zip'
)

df.fillna(0, inplace=True)   # modifies df directly
print(df)
