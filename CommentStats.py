import requests
import json


COMMENT_HEADERS = ('videoId', 'id', 'textDisplay', 'likeCount', 'publishedAt', 'totalReplyCount')


class CommentStats:
    def __init__(self, api_key):
        self.api_key = api_key
        self.comments = {}

    def get_comment_stats(self, video_ids):
        for video in video_ids:
            url = f"https://www.googleapis.com/youtube/v3/commentThreads?key={self.api_key}&videoId={video}&part=snippet&maxResults=100&order=relevance"
            json_url = requests.get(url)
            data = json.loads(json_url.text)
            self.comments = data

    def get_comment_results(self):
        print(self.comments)

    def check_sentiment(self):
        pass #todo

    def export_to_excel(self):
        pass #todo