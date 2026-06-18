import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())
print(df.columns)
print(df.shape)
print(df["Churn"].value_counts())

print(df.groupby("Contract")["Churn"].value_counts())
print(df.groupby("gender")["Churn"].value_counts())

print("\nInternet Service")
print(df.groupby("InternetService")["Churn"].value_counts())

print("\nTech Support")
print(df.groupby("TechSupport")["Churn"].value_counts())

print("\nPayment Method")
print(df.groupby("PaymentMethod")["Churn"].value_counts())