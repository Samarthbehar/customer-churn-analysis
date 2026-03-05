# importing required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# loading dataset
df = pd.read_excel('data/telco_churn.xlsx')

# renaming churn column properly
if 'Churn Value' in df.columns:
    df = df.rename(columns={'Churn Value': 'Churn'})

# removing unnecessary columns (only if they exist)
cols_to_remove = [
    'City',
    'State',
    'Country',
    'CLTV',
    'Churn Score',
    'Count',
    'Churn Label'  # removing to avoid leakage
]

cols_to_remove = [col for col in cols_to_remove if col in df.columns]
df = df.drop(cols_to_remove, axis=1)

# converting Total Charges to numeric
if 'Total Charges' in df.columns:
    df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')

# removing rows where Total Charges is missing
df = df.dropna(subset=['Total Charges'])

# checking churn distribution
print("Churn distribution:")
print(df['Churn'].value_counts())
print("-" * 40)

# selecting categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns

# encoding categorical variables
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# separating features and target
X = df_encoded.drop('Churn', axis=1)
y = df_encoded['Churn']

# splitting data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# building pipeline with scaling + logistic regression
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(
        max_iter=1000,
        class_weight='balanced',
        solver='liblinear'
    ))
])

# training model
pipeline.fit(X_train, y_train)

# making predictions
y_pred = pipeline.predict(X_test)

# printing model performance
print("Classification Report:")
print(classification_report(y_test, y_pred))
