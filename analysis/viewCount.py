import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('all_data.csv')

topics = df['topic'].unique()

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['viewCount'], ascending=False)
    youtube = youtube.sort_values(['viewCount'], ascending=False)

    print('creative ', topic, creative['viewCount'])
    plt.figure(figsize=[16, 12])
    plt.plot(creative['viewCount'].values, 'g.', label='Creative Commons')
    plt.plot(youtube['viewCount'].values, 'r.', label='Youtube')

    line_point = creative['viewCount'].values[0]

    plt.axhline(y=line_point, color='green', linestyle='-')

    plt.yscale('log')

    plt.legend()
    plt.title(topic)
    plt.xlabel('Numer filmu w kolejności największej liczby wyświetleń')
    plt.ylabel('Liczba wyświetleń')
    plt.savefig(f'viewCount/{topic}')
    plt.close()
