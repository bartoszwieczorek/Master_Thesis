import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
import tikzplotlib


df = pd.read_csv('all_data.csv')

topics = df['topic'].unique()
samples_creative = []
samples_youtube = []

for topic in topics:
    samples_creative = []
    samples_youtube = []

    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['commentCount'], ascending=False)
    youtube = youtube.sort_values(['commentCount'], ascending=False)

    samples_creative.append(creative['likeCount']/(creative['likeCount']+creative['dislikeCount']).fillna(0).values)
    samples_youtube.append(youtube['likeCount']/(youtube['likeCount']+youtube['dislikeCount']).fillna(0).values)

    ecdf_creative = ECDF(samples_creative[0])
    ecdf_youtube = ECDF(samples_youtube[0])
    print(ecdf_creative.x)
    plt.plot(ecdf_creative.x, ecdf_creative.y, 'g', label='Creative Commons')
    plt.plot(ecdf_youtube.x, ecdf_youtube.y, 'r', label='Youtube')
    plt.legend()
    plt.title(topic)
    plt.xlabel('Prawdopodobieństwo polubienia jeśli została dodana reakcja')
    plt.ylabel('Prawdopodobieństwo')
    plt.savefig(f'empirical_dist_percent_line/{topic}')

    plt.close()
