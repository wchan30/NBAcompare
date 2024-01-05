from nba_api.stats.endpoints import playercareerstats
import pandas as pd

# career dataframe
def lifespan(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    return career.get_data_frames()[0]

def totalGames(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_df = career.get_data_frames()[0]
    total_games = career_df['GP'].sum()
    return total_games

def threePointAttempt(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_df = career.get_data_frames()[0]
    three_points_attempt = career_df['FG3A'].sum()
    return three_points_attempt

def fieldGoalAttempt(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_df = career.get_data_frames()[0]
    field_goal_attempt = career_df['FGA'].sum()
    return field_goal_attempt

def freeThrowAttempt(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_df = career.get_data_frames()[0]
    field_goal_attempt = career_df['FTA'].sum()
    return field_goal_attempt

def pointsPerGame(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_df = career.get_data_frames()[0]
    points_per_game = career_df['PTS'].sum()
    return points_per_game

def assistsPerGame(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_df = career.get_data_frames()[0]
    assists_per_game = career_df['AST'].sum()
    return assists_per_game

def reboundsPerGame(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_df = career.get_data_frames()[0]
    rebounds_per_game = career_df['REB'].sum()
    return rebounds_per_game
    
