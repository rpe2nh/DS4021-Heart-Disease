import pandas as pd
from sklearn.model_selection import train_test_split

cols = ["age","sex","cp","trestbps","chol","fbs","restecg",
        "thalach","exang","oldpeak","slope","ca","thal","num"]

# Run once by Mark on 11/17/2026 to create the development and reporting sets.
# Teammates do NOT need to run this. Use Data/development_set.csv.
df = pd.read_csv("/Users/markespiritu/Downloads/heart+disease/processed.cleveland.data",
                 header=None, names=cols, na_values="?")

dev, report = train_test_split(
    df, test_size=0.2, random_state=4021, stratify=(df["num"] > 0)
)

dev.to_csv("Data/development_set.csv", index=False)
report.to_csv("Data/reporting_set.csv", index=False)

print(len(dev), len(report))
print("overlap:", len(set(dev.index) & set(report.index)))
