import argparse
import sys
import pprint

from util import lifespan
from charts import pointslinegraph
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
   player1_line = pointslinegraph(player1_id)


   pprint.pprint(player1_line)

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

   pprint.pprint(player2_stats)
