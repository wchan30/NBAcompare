import matplotlib.pyplot as plt
from nba_api.stats.endpoints import playercareerstats
from util import lifespan

def pointslinegraph(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_df = career.get_data_frames()[0]
    points = career_df['PTS']
    season = career_df['SEASON_ID']
    return points