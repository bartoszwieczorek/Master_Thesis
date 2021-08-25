import requests
import json
from pytube import YouTube
import csv


VIDEO_HEADERS = ('videoId', 'publishedAt', 'channelId', 'title', 'description',
                 'liveBroadcastContent', 'viewCount', 'likeCount', 'dislikeCount', 'favoriteCount',
                 'commentCount', 'videoLicense', 'regionCode')


class MoviesStats:
    def __init__(self, api_keys, duration, views_or_rating, topic_and_label, license_type, region_code, EXEC_TIME, INDEX):
        self.api_keys = api_keys
        self.duration = duration
        self.views_or_rating = views_or_rating
        self.region_code = region_code
        self.EXEC_TIME = EXEC_TIME
        self.topic, self.topic_label = topic_and_label
        self.license_type = license_type
        self.video_ids = []
        self.chosen_videos = {}
        self.comments = {}
        self.total_results = None
        self.INDEX = INDEX

    def get_popular_videos(self):
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&key={self.api_keys[self.INDEX]}&maxResults=50&videoDuration={self.duration}&regionCode={self.region_code}&order={self.views_or_rating}&topicId={self.topic}&videoLicense={self.license_type}&type=video"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            if data['error']['code'] == 403:
                self.INDEX += 1
            url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&key={self.api_keys[self.INDEX]}&maxResults=50&videoDuration={self.duration}&regionCode={self.region_code}&order={self.views_or_rating}&topicId={self.topic}&videoLicense={self.license_type}&type=video"
            json_url = requests.get(url)
            data = json.loads(json_url.text)
        except KeyError:
            pass

        self.total_results = data['pageInfo']['totalResults']

        try:
            next_token = data['nextPageToken']
        except KeyError:
            pass

        iterations = 5
        for i in range(iterations):
            try:
                url2 = f"https://www.googleapis.com/youtube/v3/search?part=snippet&key={self.api_keys[self.INDEX]}&maxResults=50&videoDuration={self.duration}&regionCode={self.region_code}&order={self.views_or_rating}&topicId={self.topic}&videoLicense={self.license_type}&type=video&pageToken={next_token}"
                json_url2 = requests.get(url2)
                data2 = json.loads(json_url2.text)
                try:
                    if data2['error']['code'] == 403:
                        self.INDEX += 1
                    url2 = f"https://www.googleapis.com/youtube/v3/search?part=snippet&key={self.api_keys[self.INDEX]}&maxResults=50&videoDuration={self.duration}&regionCode={self.region_code}&order={self.views_or_rating}&topicId={self.topic}&videoLicense={self.license_type}&type=video&pageToken={next_token}"
                    json_url2 = requests.get(url2)
                    data2 = json.loads(json_url2.text)
                except KeyError:
                    pass
                data['items'].extend(data2['items'])
                next_token = data2['nextPageToken']
            except KeyError:
                pass
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
        url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={id}&key={self.api_keys[self.INDEX]}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            if data['error']['code'] == 403:
                self.INDEX += 1
            url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&key={self.api_keys[self.INDEX]}&maxResults=50&videoDuration={self.duration}&regionCode={self.region_code}&order={self.views_or_rating}&topicId={self.topic}&videoLicense={self.license_type}&type=video"
            json_url = requests.get(url)
            data = json.loads(json_url.text)
        except KeyError:
            pass
        return data['items'][0]['statistics']

    def export_to_csv(self):
        with open(f'output/{self.EXEC_TIME}__movies_{self.duration}_{self.views_or_rating}_{self.topic_label}_{self.license_type}_{self.region_code}.csv', 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.DictWriter(file, fieldnames=VIDEO_HEADERS)
            csv_writer.writeheader()

            for element in self.chosen_videos['items']:
                default_value = None
                try:
                    video_stats = self.get_statistics(element['id']['videoId'])
                except KeyError:
                    video_stats = default_value

                try:
                    video_id = element['id']['videoId']
                except KeyError:
                    video_id = default_value

                try:
                    published_at = element['snippet']['publishedAt']
                except KeyError:
                    published_at = default_value

                try:
                    channel_id = element['snippet']['channelId']
                except KeyError:
                    channel_id = default_value

                try:
                    title = element['snippet']['title']
                except KeyError:
                    title = default_value

                try:
                    description = element['snippet']['description']
                except KeyError:
                    description = default_value

                try:
                    live_broadcast_content = element['snippet']['liveBroadcastContent']
                except KeyError:
                    live_broadcast_content = default_value

                try:
                    view_count = video_stats['viewCount']
                except KeyError:
                    view_count = default_value
                except TypeError:
                    view_count = default_value
                    print('typeerror')

                try:
                    like_count = video_stats['likeCount']
                except KeyError:
                    like_count = default_value

                try:
                    dislike_count = video_stats['dislikeCount']
                except KeyError:
                    dislike_count = default_value

                try:
                    favorite_count = video_stats['favoriteCount']
                except KeyError:
                    favorite_count = default_value

                try:
                    comment_count = video_stats['commentCount']
                except KeyError:
                    comment_count = default_value

                csv_writer.writerow({'videoId': video_id, 'publishedAt': published_at,
                                     'channelId': channel_id, 'title': title,
                                     'description': description, 'liveBroadcastContent': live_broadcast_content,
                                     'viewCount': view_count, 'likeCount': like_count,
                                     'dislikeCount': dislike_count, 'favoriteCount': favorite_count,
                                     'commentCount': comment_count, 'videoLicense': self.license_type,
                                     'regionCode': self.region_code
                                     })



