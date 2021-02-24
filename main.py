from MoviesStats import MoviesStats
from CommentStats import CommentStats

API_KEY = 'AIzaSyC72fpF2VCnfok9Ia8VI3iJEA0eX3mGxIU'
COUNTRY = 'PL'
#DURATION = 'any'/'long'/'medium'/'short'
#ORDER = 'rating'/'viewCount'
# /m/02vx4  ->  Football
#LICENSE = 'any'/'creativeCommon'/'youtube'


MoviesStats1 = MoviesStats(API_KEY, 'short', 'viewCount', '/m/02vx4', 'youtube', COUNTRY)
MoviesStats1.get_popular_videos()
print(MoviesStats1.chosen_videos)
MoviesStats1.retrieve_ids()
MoviesStats1.get_results()
print(len(MoviesStats1.video_ids))


CommentStats1 = CommentStats(API_KEY)
CommentStats1.get_comment_stats(MoviesStats1.video_ids)
CommentStats1.get_comment_results()
