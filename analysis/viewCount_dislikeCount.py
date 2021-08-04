import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('all_data.csv')

topics = df['topic'].unique()


for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['viewCount'], ascending=False)
    youtube = youtube.sort_values(['viewCount'], ascending=False)

    plt.figure(figsize=[16, 12])

    plt.plot(creative['viewCount'], creative['dislikeCount'], 'g.', label='Creative Commons')
    plt.plot(youtube['viewCount'], youtube['dislikeCount'], 'r.', label='Youtube')
    plt.xscale('log')
    plt.yscale('log')

    plt.legend()
    plt.title(topic)
    plt.xlabel('Liczba wyświetleń')
    plt.ylabel('Liczba niepolubień')
    plt.savefig(f'dislikeCount_viewCount/{topic}')
    plt.close()
