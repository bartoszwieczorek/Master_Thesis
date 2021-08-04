import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('all_data.csv')

topics = df['topic'].unique()

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative['percent'] = creative['likeCount']/(creative['likeCount']+creative['dislikeCount'])
    youtube['percent'] = youtube['likeCount']/(youtube['likeCount']+youtube['dislikeCount'])

    creative = creative.sort_values(['percent'], ascending=False)
    youtube = youtube.sort_values(['percent'], ascending=False)   

    print('creative ', topic, creative['viewCount'])
    plt.figure(figsize=[16, 12])
    plt.plot(creative['percent'].values, 'g.', label='Creative Commons')
    plt.plot(youtube['percent'].values, 'r.', label='Youtube')

    line_point = creative['viewCount'].values[0]

    plt.legend()
    plt.title(topic)
    plt.xlabel('Numer filmu w kolejności największej procentowej pozytywnej reakcji')
    plt.ylabel('Procent liczby polubień do ogólnej liczby reakcji')
    plt.savefig(f'likePercent_order_by_likePercent/{topic}')
    plt.close()
