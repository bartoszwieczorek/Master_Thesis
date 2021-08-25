from os import write
import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import ttest_ind


df = pd.read_csv('all_data.csv')

topics = df['topic'].unique()

df['publishedAt'] = pd.to_datetime(df['publishedAt'])

creative_correlations = {'licence': 'creative'}
creative_p_values = ['p-value cc']
youtube_correlations = {'licence': 'yuotube'}
youtube_p_values = ['p-value y']
ttest = ['ttest']
ttest_pvalues = ['ttest pvalue']

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['viewCount'], ascending=False)
    youtube = youtube.sort_values(['viewCount'], ascending=False)

    creative['percent'] = creative['likeCount']/(creative['likeCount']+creative['dislikeCount'])
    youtube['percent'] = youtube['likeCount']/(youtube['likeCount']+youtube['dislikeCount'])

    creative_views = creative['viewCount']
    creative_percent_likes = creative['likeCount']/(creative['likeCount']+creative['dislikeCount'])

    youtube_views = youtube['viewCount']
    youtube_percent_likes = youtube['likeCount']/(youtube['likeCount']+youtube['dislikeCount'])

    df_clean_creative = creative[['viewCount', 'percent']].dropna()

    correlation_creative, p_creative = pearsonr(df_clean_creative['viewCount'], df_clean_creative['percent'])

    creative_p_values.append(p_creative)

    df_clean_youtube = youtube[['viewCount', 'percent']].dropna()

    correlation_youtube, p_youtube = pearsonr(df_clean_youtube['viewCount'], df_clean_youtube['percent'])
    youtube_p_values.append(p_youtube)

    ttest_value, ttest_pvalue = ttest_ind(df_clean_creative['percent'], df_clean_youtube['percent'])
    print(ttest_value)
    ttest.append(ttest_value)
    ttest_pvalues.append(ttest_pvalue)

    creative_correlations[topic] = correlation_creative
    youtube_correlations[topic] = correlation_youtube

print(creative_correlations)
print(youtube_correlations)

with open('viewcount_to_percent_reactions_correlations_ttest.csv', 'w', newline='') as f:
   writer = csv.writer(f)
   writer.writerow(creative_correlations.keys())
   writer.writerow(creative_correlations.values())
   writer.writerow(creative_p_values)
   writer.writerow(youtube_correlations.values())
   writer.writerow(youtube_p_values)
   writer.writerow(ttest)
   writer.writerow(ttest_pvalues)




