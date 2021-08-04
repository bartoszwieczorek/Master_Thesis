import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('all_data2.csv')

topics = df['topic'].unique()

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['commentCount'], ascending=False)
    youtube = youtube.sort_values(['commentCount'], ascending=False)

    plt.figure(figsize=[16, 12])
    plt.plot(creative['commentCount'].values, 'g.', label='Creative Commons')
    plt.plot(youtube['commentCount'].values, 'r.', label='Youtube')

    line_point = creative['commentCount'].values[0]

    plt.axhline(y=line_point, color='green', linestyle='-')

    plt.yscale('log')

    plt.legend()
    plt.title(topic)
    plt.xlabel('Numer filmu w kolejności największej liczby komentarzy')
    plt.ylabel('Liczba komentarzy')
    plt.savefig(f'commentCount2/{topic}')
    plt.close()
