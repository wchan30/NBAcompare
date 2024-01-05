import argparse
import sys
import pprint
import matplotlib as plt

from util import lifespan
from util import threePointAttempt
from util import totalGames
from util import fieldGoalAttempt
from util import freeThrowAttempt
from util import pointsPerGame
from util import assistsPerGame
from util import reboundsPerGame

from charts import pointslinegraph
from charts import assistslinegraph
from charts import reboundslinegraph

from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats


if __name__ == '__main__':
   # parser to get the command line arguments
   parser = argparse.ArgumentParser()

   # sets up a flag argument for the parser
   parser.add_argument('-n1', '--name1', nargs='*', help="name of the player")
   parser.add_argument('-n2','--name2', nargs = '*', help = "name of the player")

   # parses the arguments into a variable
   args = parser.parse_args()
   
   # Use full name
   name1 = args.name1
   name2 = args.name2



if name1 is not None:
   full_name1 = " ".join(name1)

   matching_players1 = players.find_players_by_full_name(full_name1)
   active_list = [x for x in matching_players1 if x['is_active']]
   if len(active_list) > 1:
      active_players = [x['full_name'] for x in active_list ]
      print('Here is what we found')
      print(active_players)
      sys.exit('Please be more specific')
   if len(active_list) == 0:
      sys.exit('We could not find such player. Try again')
   player1 = active_list[0]
   player1_full_name = player1['full_name']
   player1_id = player1['id']

   player1_stats = lifespan(player1_id)
   player1_total_games = totalGames(player1_id)

   player1_avg_three_points_attempt = threePointAttempt(player1_id)/totalGames(player1_id)
   player1_avg_field_goal_attempt = fieldGoalAttempt(player1_id)/totalGames(player1_id)
   player1_avg_free_throw_attempt = freeThrowAttempt(player1_id)/totalGames(player1_id)
   player1_avg_points_per_game = pointsPerGame(player1_id)/totalGames(player1_id)
   player1_avg_assists_per_game = assistsPerGame(player1_id)/totalGames(player1_id)
   player1_avg_rebounds_per_game = reboundsPerGame(player1_id)/totalGames(player1_id)
   
   print(int(player1_avg_three_points_attempt))
   print(int(player1_avg_field_goal_attempt))
   print(int(player1_avg_free_throw_attempt))
   print(int(player1_avg_points_per_game)) # round to nearest tenth
   print(int(player1_avg_assists_per_game)) # round to nearest tenth
   print(int(player1_avg_rebounds_per_game)) # round to nearest tenth

   



if name2 is not None:
   full_name2 = " ".join(name2)
   matching_players2 = players.find_players_by_full_name(full_name2)
   active_list = [x for x in matching_players2 if x['is_active']]
   if len(active_list) > 1:
      active_players = [x['full_name'] for x in active_list ]
      print('Here is what we found')
      print(active_players)
      sys.exit('Please be more specific')
   if len(active_list) == 0:
      sys.exit('We could not find such player. Try again')
   player2= active_list[0]
   player2_full_name = player2['full_name']
   player2_id = player2['id']
   player2_stats = lifespan(player2_id)

   pointslinegraph(player1_id,player2_id)
   assistslinegraph(player1_id,player2_id)
   reboundslinegraph(player1_id,player2_id)
