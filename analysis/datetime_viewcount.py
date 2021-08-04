import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('all_data.csv')

topics = df['topic'].unique()

df['publishedAt'] = pd.to_datetime(df['publishedAt'])


for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['viewCount'], ascending=False)
    youtube = youtube.sort_values(['viewCount'], ascending=False)

    plt.figure(figsize=[16, 12])

    plt.plot(creative['publishedAt'], creative['viewCount'], 'g.', label='Creative Commons')
    plt.plot(youtube['publishedAt'], youtube['viewCount'], 'r.', label='Youtube')
    plt.yscale('log')

    plt.legend()
    plt.title(topic)
    plt.xlabel('Data')
    plt.ylabel('Liczba wyświetleń')
    plt.savefig(f'viewCount_date/{topic}')
    plt.close()
