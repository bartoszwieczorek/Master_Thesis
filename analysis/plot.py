import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('all_data.csv')

# Index(['videoId', 'publishedAt', 'channelId', 'title', 'description',
#        'liveBroadcastContent', 'viewCount', 'likeCount', 'dislikeCount',
#        'favoriteCount', 'commentCount', 'videoLicense', 'regionCode', 'order',
#        'licence', 'length', 'topic', 'region', 'time'],
#       dtype='object')

# print(df.head(5))
# print(df['videoId'])
# print(df.columns)
# print(df.iloc[2, 1])
# print(df.iloc[0:4])
# print(df.loc[df['videoLicense'] == 'youtube'])
# print(df.groupby(['videoLicense', 'topic']).count())
# labels = ['creative Commons', 'youtube']

# football_creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == 'Football')]
# football_youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == 'Football')]
#
# plt.plot(football_creative['viewCount'], football_creative['likeCount']/football_creative['viewCount'], 'r.--', label='creative Common')
# plt.plot(football_youtube['viewCount'], football_youtube['likeCount']/football_youtube['viewCount'], 'g.--', label='youtube')
#
# plt.legend()
#
# plt.show()

# business_creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == 'Business')]
# business_youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == 'Business')]
#
# plt.plot(business_creative['viewCount'], business_creative['likeCount']/business_creative['viewCount'], 'r.--', label='creative Common')
# plt.plot(business_youtube['viewCount'], business_youtube['likeCount']/business_youtube['viewCount'], 'g.--', label='youtube')
#
# plt.legend()
#
# plt.show()

#loop
# print(df['topic'].unique())
topics = df['topic'].unique()

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['viewCount'])[20:-20]
    youtube = youtube.sort_values(['viewCount'])[20:-20]

    creative['comparison rate'] = creative['likeCount']/(creative['likeCount']+creative['dislikeCount'])
    youtube['comparison rate'] = youtube['likeCount']/(youtube['dislikeCount']+youtube['likeCount'])

    creative = creative.sort_values(['comparison rate'])[20:-20]
    youtube = youtube.sort_values(['comparison rate'])[20:-20]

    creative = creative.sort_values(['viewCount'])
    youtube = youtube.sort_values(['viewCount'])

    plt.figure(figsize=[16, 12])
    plt.plot(youtube['viewCount'], youtube['likeCount']/(youtube['dislikeCount']+youtube['likeCount']), 'r.--', label='youtube')
    # plt.plot(creative['viewCount'], creative['likeCount']/(creative['likeCount']+creative['dislikeCount']), 'g.--', label='creative Common')


    plt.legend()
    plt.title(topic)
    plt.savefig(f'everything_20/{topic}_youtube')
    plt.close()
    # plt.show()

for topic in topics:
    creative = df.loc[(df['videoLicense'] == 'creativeCommon') & (df['topic'] == topic)]
    youtube = df.loc[(df['videoLicense'] == 'youtube') & (df['topic'] == topic)]

    creative = creative.sort_values(['viewCount'])[20:-20]
    youtube = youtube.sort_values(['viewCount'])[20:-20]

    creative['comparison rate'] = creative['likeCount']/(creative['likeCount']+creative['dislikeCount'])
    youtube['comparison rate'] = youtube['likeCount']/(youtube['dislikeCount']+youtube['likeCount'])

    creative = creative.sort_values(['comparison rate'])[20:-20]
    youtube = youtube.sort_values(['comparison rate'])[20:-20]

    creative = creative.sort_values(['viewCount'])
    youtube = youtube.sort_values(['viewCount'])

    plt.figure(figsize=[16, 12])
    # plt.plot(youtube['viewCount'], youtube['likeCount']/(youtube['dislikeCount']+youtube['likeCount']), 'r.--', label='youtube')
    plt.plot(creative['viewCount'], creative['likeCount']/(creative['likeCount']+creative['dislikeCount']), 'g.--', label='creative Common')


    plt.legend()
    plt.title(topic)
    plt.savefig(f'everything_20/{topic}_creative.png')
    plt.close()
