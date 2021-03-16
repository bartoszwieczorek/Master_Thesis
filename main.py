"""
Tool for getting metadata of selected videos and comments
"""
__author__ = 'Bartosz Wieczorek'

from MoviesStats import MoviesStats
from CommentStats import CommentStats
from datetime import datetime

API_KEY = 'AIzaSyC72fpF2VCnfok9Ia8VI3iJEA0eX3mGxIU'
COUNTRY = 'PL'
EXEC_TIME = datetime.now().strftime("%y%m%d_%H%M%S")
# DURATION = 'any'/'long'/'medium'/'short'
# ORDER = 'rating'/'viewCount'
# TOPIC = '/m/02vx4'  ->  Football. Full list available in documents/topics.txt
# LICENSE = 'any'/'creativeCommon'/'youtube'


def main():
    MoviesStatsObject = MoviesStats(API_KEY, 'short', 'viewCount', ('/m/02vx4', 'football'), 'youtube', COUNTRY, EXEC_TIME)
    MoviesStatsObject.get_popular_videos()
    MoviesStatsObject.export_to_csv()

    CommentStatsObject = CommentStats(API_KEY, EXEC_TIME)
    CommentStatsObject.get_comment_stats(MoviesStatsObject.video_ids)
    CommentStatsObject.export_to_csv()


if __name__ == '__main__':
    main()


