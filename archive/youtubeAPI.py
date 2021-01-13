import requests
import json

API_KEY = 'AIzaSyC72fpF2VCnfok9Ia8VI3iJEA0eX3mGxIU'
CHANNEL_ID = 'UCD6Ax9U5erEvD8vwRoXCBGw'
VIDEO_ID = '1pGL60PsfHc'
COUNTRY = 'PL'

# CHANNEL_ID = 'UC8kNdmPH2SoCWNhqUHv2mJg'
# VIDEO_ID = '8IJoGyy_c2M'


class YoutubeStats:
    def __init__(self, api_key, channel_id, video_id, country):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        self.video_id = video_id
        self.country = country

    def get_channel_statistics(self):
        # url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        # print(url)
        url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={self.video_id}&key={self.api_key}"
        # url = f"https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=snippet,id&order=date"
        print(url)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        print(data)

    def get_categories(self):
        url = f'https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode={self.country}&key={self.api_key}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        categories = {}
        for element in data['items']:
            categories.update({element['snippet']['title']: element['id']})

        return categories


yt = YoutubeStats(API_KEY, CHANNEL_ID, VIDEO_ID, COUNTRY)
# yt.get_channel_statistics()
categories = yt.get_categories()
print(categories)

with open('categoriesPL.txt', 'w') as f:
    for key, value in categories.items():
        f.write(key + ': ' + value + '\n')
