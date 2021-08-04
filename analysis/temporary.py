import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('all_data.csv')

topics = df['topic'].unique()

df['publishedAt'] = pd.to_datetime(df['publishedAt'])

print(df['publishedAt'])