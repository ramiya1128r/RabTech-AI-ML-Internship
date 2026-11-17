
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.metrics import accuracy_score, classification_report

data = {
    "customer_id": [
        "C001","C002","C003","C004",
        "C005","C006","C007","C008",
        "C009","C010","C011","C012"
    ],
    "tenure_months": [2,5,1,8,3,12,18,24,30,15,20,10],
    "support_tickets": [4,3,5,2,4,1,0,1,0,2,1,2],
    "monthly_spend_inr": [499,599,499,799,599,999,1499,1299,1499,999,1299,799],
    "last_login_days": [20,15,30,10,25,5,2,3,1,7,4,8],
    "plan_type": [
        "Basic","Basic","Basic","Basic",
        "Basic","Standard","Pro","Pro",
        "Pro","Standard","Pro","Standard"
    ],
    "churned": [1,1,1,1,1,0,0,0,0,0,0,0]
}

df = pd.DataFrame(data)

print("CUSTOMER CHURN DATA")
print(df)


X = df.drop(columns=["customer_id", "churned"])
y = df["churned"]


preprocessor = ColumnTransformer([
    ("num", StandardScaler(), [
        "tenure_months",
        "support_tickets",
        "monthly_spend_inr",
        "last_login_days"
    ]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["plan_type"])
])


model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])


cv = LeaveOneOut()
predictions = cross_val_predict(model, X, y, cv=cv)

print("\nMODEL ACCURACY:")
print(accuracy_score(y, predictions))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y, predictions, zero_division=0))

print("\nMAJORITY BASELINE:")
baseline = DummyClassifier(strategy="most_frequent")
baseline_predictions = cross_val_predict(baseline, X, y, cv=cv)
print(accuracy_score(y, baseline_predictions))
