player_score={}
with open("run.csv", "r") as f:
  for line in f:
        
        player , score = line.split(',')
        score = int(score)
            
        if player in player_score:
            player_score[player].append(score)
             

        else:
            player_score[player] = [score]
            print(player, type(score))


for player, score_list in player_score.items():
            print(player,score_list)