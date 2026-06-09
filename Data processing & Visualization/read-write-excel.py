import pandas as pd

df = pd.read_csv(
    r"C:\code\Data processing & Visualization\Read_write_to_excel_resources\Read_write_to_excel_resources\stock_data.csv",
    header=1,
    na_values=['not available', -1, 'n.a.']
)
print(df)



# Correct way with raw string
df_movie = pd.read_excel(
    r"C:\code\Data processing & Visualization\Read_write_to_excel_resources\Read_write_to_excel_resources\movies_db.xlsx",
    "movies"
)
print(df_movie)
print("JAI SHREE RAMM\n")
print(df_movie.head(4))

import pandas as pd

# Correct usage with sheet_name
import pandas as pd

import pandas as pd

df_financials = pd.read_excel(
    r"C:\code\Data processing & Visualization\Read_write_to_excel_resources\Read_write_to_excel_resources\movies_db.xlsx",
    "financials"   # ✅ exact match
)

print(df_financials.head(5))

def standarize_currency(curr):
    if curr == "$$"or curr == "Dollars":
        return "USD"    
    return curr

df_financials = pd.read_excel(
    r"C:\code\Data processing & Visualization\Read_write_to_excel_resources\Read_write_to_excel_resources\movies_db.xlsx",
    "financials" converters={'currency: standardize_currency'
    })
 