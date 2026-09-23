import pandas as pd

df = pd.read_excel("Raisin_Dataset.xlsx")
print(df.sample(5))
print(df.shape)
X = df[["Area", "MajorAxisLength", "MinorAxisLength", "Eccentricity", "ConvexArea", "Extent", "Perimeter"]]
y = df["Class"]
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#scale the data
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

print(X_train_scaled=scaler.transform(X_train))
print(X_test_scaled = scaler.transform(X_test))