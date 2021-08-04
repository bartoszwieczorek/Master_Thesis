import pandas as pd
import matplotlib.pyplot as plt
import tikzplotlib


df = pd.read_csv('all_data.csv')

topics = df['topic'].unique()

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['viewCount'])
    youtube = youtube.sort_values(['viewCount'])

    creative['comparison rate'] = creative['likeCount']/(creative['likeCount']+creative['dislikeCount'])
    youtube['comparison rate'] = youtube['likeCount']/(youtube['dislikeCount']+youtube['likeCount'])

    creative = creative.sort_values(['comparison rate'])
    youtube = youtube.sort_values(['comparison rate'])

    creative = creative.sort_values(['viewCount'])
    youtube = youtube.sort_values(['viewCount'])

    plt.figure(figsize=[16, 12])
    plt.plot(youtube['viewCount'], youtube['likeCount']/(youtube['dislikeCount']+youtube['likeCount']), 'r.', label='youtube')
    plt.plot(creative['viewCount'], creative['likeCount']/(creative['likeCount']+creative['dislikeCount']), 'g.', label='creative Common')


    plt.legend()
    plt.title(topic)
    plt.xlabel('Liczba wyświetleń')
    plt.ylabel('Stosunek liczby polubień do ogólnej liczby (nie)polubień')
    plt.xscale('log')
    tikzplotlib.save(f'latex_likePercentage_viewCount/{topic}.tex', encoding='utf-8')
    plt.close()
