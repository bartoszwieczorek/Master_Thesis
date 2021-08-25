"""
Tool for getting metadata of selected videos and comments
"""
__author__ = 'Bartosz Wieczorek'

from MoviesStats import MoviesStats
from CommentStats import CommentStats
from datetime import datetime
import pandas as pd

API_KEY = 'AIzaSyASCD8vXy4bUfI9ATiBKT7MaUQpzrpuiFQ'
COUNTRY = 'PL'
EXEC_TIME = datetime.now().strftime("%y%m%d_%H%M%S")
API_KEYS = ['AIzaSyAFM0Ubeuuzo-hDS2WtBNVlNk2npx7DhT8']

# 'AIzaSyDbQD1GdVkT-qIzBUrmbVeV0aonugwTPwU'
# 'AIzaSyC72fpF2VCnfok9Ia8VI3iJEA0eX3mGxIU', 'AIzaSyAt8nDxnYFXtJxRGMxTqhoCl9Rva0pQUzo',
#             'AIzaSyAFgSTQoOTo66ZCfmPjz_ynue-6ZSf3gBo', 'AIzaSyCXWYrkZDK8LbrQF2-Hp3B4MSaMoLlqZLE',
#'AIzaSyBKJDG6Vriq1EvAeVLiOlHuU37SPAWrTGM',      'AIzaSyCneEUuwr6iL74Sse5Ri8bXkmiBGjCsdFQ',
# 'AIzaSyDi39fBbd-DznLKnNaQqqJRqPqTzZFqpWw', 'AIzaSyBUcdxr8XuwcLn7aca8vgcQcEv9UIXnaJo',
# 'AIzaSyAyf-YRXoOtiQgTi0NKpQhfO0XPEBZagd8', 'AIzaSyAr86ILzIW4Pguz3wUsWphud2sEcUsYO2M'
# 'AIzaSyBu0Cf2bxhZemdv-vXdMSsMM5CwCMJf8Bw', 'AIzaSyCGLXREw2Ogp2J_Bf14jkm5Y1hrVR3VqD8'


# AIzaSyCnXIW4l3_NaV9oH3DQ8pbWKq-FdlukHWE, AIzaSyDbQD1GdVkT-qIzBUrmbVeV0aonugwTPwU
# DURATION = 'any'/'long'/'medium'/'short'
# ORDER = 'rating'/'viewCount'/'relevance'
# TOPIC = '/m/02vx4'  ->  Football. Full list available in documents/topics.txt
# LICENSE = 'any'/'creativeCommon'/'youtube'


def get_topics():
    df = pd.read_csv('documents/topics.csv', header=None)#, skiprows=54
    output = dict(df.to_numpy())
    return output


def main():
    topics = get_topics()
    # n_items = take(n, d.items())

    INDEX = 0
    for topic_code, topic_label in topics.items():
        # MoviesStatsObject = MoviesStats(API_KEY, 'short', 'viewCount', ('/m/02vx4', 'Football'), 'youtube', COUNTRY, EXEC_TIME)
        MoviesStatsObject = MoviesStats(API_KEYS, 'short', 'viewCount', (topic_code, topic_label), 'youtube', COUNTRY, EXEC_TIME, INDEX)
        MoviesStatsObject.get_popular_videos()
        MoviesStatsObject.retrieve_ids()
        MoviesStatsObject.export_to_csv()
        INDEX = MoviesStatsObject.INDEX
        print('next')

    # CommentStatsObject = CommentStats(API_KEY, EXEC_TIME)
    # CommentStatsObject.get_comment_stats(MoviesStatsObject.video_ids)
    # CommentStatsObject.export_to_csv()


if __name__ == '__main__':
    main()


