import requests
import json
import csv


COMMENT_HEADERS = ('videoId', 'id', 'textDisplay', 'likeCount', 'publishedAt', 'totalReplyCount')


class CommentStats:
    def __init__(self, api_key, EXEC_TIME):
        self.api_key = api_key
        self.EXEC_TIME = EXEC_TIME
        self.comments = []

    def get_comment_stats(self, video_ids):
        for video in video_ids:
            url = f"https://www.googleapis.com/youtube/v3/commentThreads?key={self.api_key}&videoId={video}&part=snippet&maxResults=100&order=relevance"
            json_url = requests.get(url)
            data = json.loads(json_url.text)
            try:
                self.comments.extend(data['items'])
            except KeyError:
                pass

    def get_comment_results(self):
        print(self.comments)

    def check_sentiment(self):
        pass #todo

    def export_to_csv(self):
        with open(f'output/{self.EXEC_TIME}__comments.csv', 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.DictWriter(file, fieldnames=COMMENT_HEADERS)
            csv_writer.writeheader()

            for element in self.comments:
                try:
                    csv_writer.writerow({'videoId': element['snippet']['videoId'], 'id': element['id'],
                                         'textDisplay': element['snippet']['topLevelComment']['snippet']['textDisplay'],
                                         'likeCount': element['snippet']['topLevelComment']['snippet']['likeCount'],
                                         'publishedAt': element['snippet']['topLevelComment']['snippet']['publishedAt'],
                                         'totalReplyCount': element['snippet']['totalReplyCount']
                                         })
                except Exception as e:
                    print(f'An exception of type {type(e).__name__} occured. Arguments: {e.args}\n')

