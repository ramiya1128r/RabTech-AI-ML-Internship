CUSTOMER CHURN DATA

customer_id  tenure_months  support_tickets  monthly_spend_inr  last_login_days plan_type  churned
C001         2              4                 499                20               Basic      1
C002         5              3                 599                15               Basic      1
C003         1              5                 499                30               Basic      1
C004         8              2                 799                10               Basic      1
C005         3              4                 599                25               Basic      1
C006         12             1                 999                5                Standard   0
C007         18             0                 1499               2                Pro        0
C008         24             1                 1299               3                Pro        0
C009         30             0                 1499               1                Pro        0
C010         15             2                 999                7                Standard   0
C011         20             1                 1299               4                Pro        0
C012         10             2                 799                8                Standard   0

MODEL ACCURACY:
1.0

CLASSIFICATION REPORT:
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         7
           1       1.00      1.00      1.00         5

    accuracy                           1.00        12
   macro avg       1.00      1.00      1.00        12
weighted avg       1.00      1.00      1.00        12

MAJORITY BASELINE:
0.5833333333333334
