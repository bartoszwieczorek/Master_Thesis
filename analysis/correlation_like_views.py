import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.stats import pearsonr


df = pd.read_csv('all_data.csv')

topics = df['topic'].unique()

df['publishedAt'] = pd.to_datetime(df['publishedAt'])

creative_correlations = {'licence': 'creative'}
youtube_correlations = {'licence': 'yuotube'}
creative_p_values = ['none']
youtube_p_values = ['none']

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['viewCount'], ascending=False)
    youtube = youtube.sort_values(['viewCount'], ascending=False)

    creative_views = creative['viewCount']
    creative_likes = creative['likeCount']

    youtube_views = youtube['viewCount']
    youtube_likes = youtube['likeCount']

    df_clean_creative = creative[['viewCount', 'likeCount']].dropna()
    correlation_creative, p_creative = pearsonr(df_clean_creative['viewCount'], df_clean_creative['likeCount'])
    creative_p_values.append(p_creative)
    df_clean_youtube = youtube[['viewCount', 'likeCount']].dropna()

    correlation_youtube, p_youtube = pearsonr(df_clean_youtube['viewCount'], df_clean_youtube['likeCount'])
    youtube_p_values.append(p_youtube)

    creative_correlations[topic] = correlation_creative
    youtube_correlations[topic] = correlation_youtube

print(creative_correlations)
print(youtube_correlations)

with open('correlation_likeonviews.csv', 'w', newline='') as f:
   writer = csv.writer(f)
   writer.writerow(creative_correlations.keys())
   writer.writerow(creative_correlations.values())
   writer.writerow(creative_p_values)
   writer.writerow(youtube_correlations.values())
   writer.writerow(youtube_p_values)




