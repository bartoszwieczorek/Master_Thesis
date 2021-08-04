import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('all_data.csv')
topics = df['topic'].unique()

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    plt.figure(figsize=[16, 12])
    plt.plot(youtube['viewCount'], youtube['likeCount']/(youtube['dislikeCount']+youtube['likeCount']), 'r.--', label='youtube')

    plt.legend()
    plt.title(topic)
    plt.savefig(f'output/{topic}_youtube')
    plt.close()

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    plt.figure(figsize=[16, 12])
    
    plt.plot(creative['viewCount'], creative['likeCount']/(creative['likeCount']+creative['dislikeCount']), 'g.--', label='creative Common')

    plt.legend()
    plt.title(topic)
    plt.savefig(f'output/{topic}_creative.png')
    plt.close()
