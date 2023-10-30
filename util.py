from nba_api.stats.endpoints import playercareerstats
import pandas as pd

# career dataframe
def lifespan(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    return career.get_data_frames()[0]
    