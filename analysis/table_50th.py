import pandas as pd
import matplotlib.pyplot as plt
import csv


df = pd.read_csv('all_data.csv')

topics = df['topic'].unique()

df['publishedAt'] = pd.to_datetime(df['publishedAt'])

table = {}

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['viewCount'], ascending=False)
    youtube = youtube.sort_values(['viewCount'], ascending=False)

    fiftieth = youtube['viewCount'].iloc[49]

    lower_than_fifftieth = len(creative['viewCount'][creative['viewCount'] > fiftieth])
    table[topic] = lower_than_fifftieth

print(table)

with open('larger50th.csv', 'w', newline='') as f:
   writer = csv.DictWriter(f, table.keys())
   writer.writeheader()
   writer.writerow(table)


