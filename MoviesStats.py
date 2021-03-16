import requests
import json
from pytube import YouTube
import csv


VIDEO_HEADERS = ('videoId', 'publishedAt', 'channelId', 'title', 'description',
                 'liveBroadcastContent', 'viewCount', 'likeCount', 'dislikeCount', 'favoriteCount') #, ,
                 # 'commentCount', 'videoLicense', 'type', 'regionCode',


class MoviesStats:
    def __init__(self, api_key, duration, views_or_rating, topic, license_type, region_code, EXEC_TIME):
        self.api_key = api_key
        self.duration = duration
        self.views_or_rating = views_or_rating
        self.region_code = region_code
        self.EXEC_TIME = EXEC_TIME
        self.topic = topic
        self.license_type = license_type
        self.video_ids = []
        self.chosen_videos = {}
        self.comments = {}
        self.total_results = None

    def get_popular_videos(self):
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&key={self.api_key}&maxResults=50&videoDuration={self.duration}&regionCode={self.region_code}&order={self.views_or_rating}&topicId={self.topic}&videoLicense={self.license_type}&type=video"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        self.total_results = data['pageInfo']['totalResults']
        if 'nextPageToken' in data:
            url2 = f"https://www.googleapis.com/youtube/v3/search?part=snippet&key={self.api_key}&maxResults=50&videoDuration={self.duration}&regionCode={self.region_code}&order={self.views_or_rating}&topicId={self.topic}&videoLicense={self.license_type}&type=video&pageToken={data['nextPageToken']}"
            json_url2 = requests.get(url2)
            data2 = json.loads(json_url2.text)
            data['items'].extend(data2['items'])
        self.chosen_videos = data

    def retrieve_ids(self):
        for video in self.chosen_videos['items']:
            self.video_ids.append(video['id']['videoId'])

    def download_all(self):
        for video in self.video_ids:
            yt = YouTube(f'www.youtube.com/watch?v={video}')
            stream = yt.streams.first()
            stream.download('/movies')

    def get_results(self):
        print(self.video_ids)

    def get_statistics(self, id):
        url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={id}&key={self.api_key}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        return data['items'][0]['statistics']

    def export_to_csv(self):
        with open(f'output/{self.EXEC_TIME}__{self.duration}_{self.views_or_rating}_{self.license_type}_{self.region_code}.csv', 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.DictWriter(file, fieldnames=VIDEO_HEADERS)
            csv_writer.writeheader()

            for element in self.chosen_videos['items']:
                try:
                    video_stats = self.get_statistics(element['id']['videoId'])
                    csv_writer.writerow({'videoId': element['id']['videoId'], 'publishedAt': element['snippet']['publishedAt'],
                                         'channelId': element['snippet']['channelId'], 'title': element['snippet']['title'],
                                         'description': element['snippet']['description'], 'liveBroadcastContent': element['snippet']['liveBroadcastContent'],
                                         'viewCount': video_stats['viewCount'], 'likeCount': video_stats['likeCount'],
                                         'dislikeCount': video_stats['dislikeCount'], 'favoriteCount': video_stats['favoriteCount']
                                         })
                except Exception as e:
                    print(f'An exception of type {type(e).__name__} occured. Arguments: {e.args}\n')



'''
features_of_videos = [
    {
        'videoId': '',
        'regionCode': '',
        'publishedAt': '',
        ..
    },
]
'''


