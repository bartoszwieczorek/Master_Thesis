import requests
import json
from pytube import YouTube


class MoviesStats:
    def __init__(self, api_key, duration, views_or_rating, topic, license_type, region_code):
        self.api_key = api_key
        self.duration = duration
        self.views_or_rating = views_or_rating
        self.region_code = region_code
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

    def get_comment_stats(self):
        for video in self.video_ids:
            url = f"https://www.googleapis.com/youtube/v3/commentThreads?key={self.api_key}&videoId={video}&part=snippet&maxResults=100&order=relevance"
            json_url = requests.get(url)
            data = json.loads(json_url.text)
            self.comments = data

    def retrieve_ids(self):
        for video in self.chosen_videos['items']:
            self.video_ids.append(video['id']['videoId'])

    def download_all(self):
        for video in self.video_ids:
            yt = YouTube(f'www.youtube.com/watch?v={video}')
            stream = yt.streams.first()
            stream.download('/movies')

    def check_sentiment(self):
        pass #todo

    def get_results(self):
        print(self.video_ids)

    def get_comment_results(self):
        print(self.comments)



