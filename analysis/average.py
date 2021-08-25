import pandas as pd
import matplotlib.pyplot as plt
import csv


df = pd.read_csv('all_data.csv')

topics = df['topic'].unique()

df['publishedAt'] = pd.to_datetime(df['publishedAt'])

topic_c = {'license': 'creative commons'}
topic_y = {'license': 'youtube'}

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['viewCount'], ascending=False)
    youtube = youtube.sort_values(['viewCount'], ascending=False)

    average_c = creative['viewCount'].mean()
    average_y = youtube['viewCount'].mean()

    topic_c[topic] = average_c
    topic_y[topic] = average_y


with open('average.csv', 'w', newline='') as f:
   writer = csv.DictWriter(f, topic_c.keys())
   writer.writeheader()
   writer.writerow(topic_c)
   writer.writerow(topic_y)


