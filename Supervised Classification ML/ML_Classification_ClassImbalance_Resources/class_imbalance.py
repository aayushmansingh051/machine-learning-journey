import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from imblearn.under_sampling import RandomUnderSampler
from collections import Counter

# Step 1: Load dataset
df = pd.read_csv("churn.csv")
print(df.head())

# Step 2: Separate features and target
X = df.drop("Churn", axis=1)   # all columns except 'Churn'
y = df["Churn"]                # target column

print("Original class distribution:", Counter(y))

# Step 3: Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
print("Training set distribution before undersampling:", Counter(y_train))

# Step 4: Train Logistic Regression on imbalanced data
model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("\nClassification report (before undersampling):")
print(classification_report(y_test, y_pred))

# Step 5: Apply RandomUnderSampler
rus = RandomUnderSampler(random_state=42)
X_train_rus, y_train_rus = rus.fit(X_train, y_train)

print(y_train_rus.value_counts())

# Step 6: Train Logistic Regression on balanced data
model_rus = LogisticRegression(max_iter=2000)
model_rus.fit(X_train_rus, y_train_rus)

y_pred_rus = model_rus.predict(X_test)
print("\nClassification report (after undersampling):")
print(classification_report(y_test, y_pred_rus))
