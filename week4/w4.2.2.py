import pandas as pd

df = pd.read_csv("C:/Users/msi/MSE800/week4/sample_junk_mail.csv")

print(df.head())

if 'Subject' in df.columns:
    subjects = df['Subject']
    print(subjects)
