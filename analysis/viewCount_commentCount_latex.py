import pandas as pd
import matplotlib.pyplot as plt
import tikzplotlib


df = pd.read_csv('all_data.csv')

topics = df['topic'].unique()

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['viewCount'], ascending=False)
    youtube = youtube.sort_values(['viewCount'], ascending=False)

    plt.figure(figsize=[16, 12])

    plt.plot(creative['viewCount'], creative['commentCount'], 'g.', label='Creative Commons')
    plt.plot(youtube['viewCount'], youtube['commentCount'], 'r.', label='Youtube')

    plt.xscale('log')
    plt.yscale('log')

    plt.legend()
    plt.title(topic)
    plt.xlabel('Liczba wyświetleń')
    plt.ylabel('Liczba komentarzy')

    tikzplotlib.save(f'latex_viewCount_commentCount/{topic}.tex', encoding='utf-8')
    plt.close()
