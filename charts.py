import matplotlib.pyplot as plt
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players

def pointslinegraph(player_id1, player_id2):
    game_log1 = playergamelog.PlayerGameLog(player_id=player_id1)
    game_log2 = playergamelog.PlayerGameLog(player_id=player_id2)
    
    game_df1 = game_log1.get_data_frames()[0]
    game_df2 = game_log2.get_data_frames()[0]
    
    points1 = game_df1['PTS']
    points2 = game_df2['PTS']
    
    games1 = range(1, len(points1)+1)
    games2 = range(1, len(points2)+1)

    name1 = players.find_player_by_id(player_id1)['full_name']
    name2 = players.find_player_by_id(player_id2)['full_name']

    plt.figure(figsize=(10, 6))

    plt.plot(games1, points1, label= name1,  marker='o')
    plt.plot(games2, points2, label= name2, marker='o')

    plt.xlabel('Game Number')
    plt.ylabel('Points')
    plt.title('Points per Game')
    plt.legend()
    plt.grid(True)
    plt.show()


def assistslinegraph(player_id1,player_id2):
    game_log1 = playergamelog.PlayerGameLog(player_id=player_id1)
    game_log2 = playergamelog.PlayerGameLog(player_id=player_id2)
    
    game_df1 = game_log1.get_data_frames()[0]
    game_df2 = game_log2.get_data_frames()[0]
    
    assists1 = game_df1['AST']
    assists2 = game_df2['AST']
    
    games1 = range(1, len(assists1)+1)
    games2 = range(1, len(assists2)+1)

    name1 = players.find_player_by_id(player_id1)['full_name']
    name2 = players.find_player_by_id(player_id2)['full_name']

    plt.figure(figsize=(10, 6))

    plt.plot(games1, assists1, label= name1,  marker='o')
    plt.plot(games2, assists2, label= name2, marker='o')

    plt.xlabel('Game Number')
    plt.ylabel('Assists')
    plt.title('Assists per Game')
    plt.legend()
    plt.grid(True)
    plt.show()

def reboundslinegraph(player_id1,player_id2):
    game_log1 = playergamelog.PlayerGameLog(player_id=player_id1)
    game_log2 = playergamelog.PlayerGameLog(player_id=player_id2)
    
    game_df1 = game_log1.get_data_frames()[0]
    game_df2 = game_log2.get_data_frames()[0]
    
    rebounds1 = game_df1['REB']
    rebounds2 = game_df2['REB']
    
    games1 = range(1, len(rebounds1)+1)
    games2 = range(1, len(rebounds2)+1)

    name1 = players.find_player_by_id(player_id1)['full_name']
    name2 = players.find_player_by_id(player_id2)['full_name']

    plt.figure(figsize=(10, 6))

    plt.plot(games1, rebounds1, label= name1,  marker='o')
    plt.plot(games2, rebounds2, label= name2, marker='o')

    plt.xlabel('Game Number')
    plt.ylabel('Rebounds')
    plt.title('Rebounds per Game')
    plt.legend()
    plt.grid(True)
    plt.show()
