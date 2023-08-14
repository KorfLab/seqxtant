def score_algo(combo):
	# scoring system parameters
	dist_penalty = 0.5
	overlap_penalty = 2
	connect_reward = 20
	# get sum of blast scores
	score = sum(each[6] for each in combo)
	
	# get the distance penalty, by the max projection of the distance onto one coordinate axis
	score -= (dist_penalty * 
		sum(max(combo[i+1][1]-combo[i][2], combo[i+1][3]-combo[i][4]) 
		for i in range(len(combo)-1) 
		if max(combo[i+1][1]-combo[i][2], combo[i+1][3]-combo[i][4]) > 0))

	
	# get the overlap penalty
	score += (overlap_penalty * 
		sum(min(combo[i+1][1]-combo[i][2], combo[i+1][3]-combo[i][4]) 
		for i in range(len(combo)-1) 
		if min(combo[i+1][1]-combo[i][2], combo[i+1][3]-combo[i][4]) < 0))
		

	
	# get connect reward
	score += connect_reward * (len(combo)-1)
	return score



def score_sys(hsps):
	# sort hsps by coordinate and blast score respectively
	hsps.sort(key = lambda x: (x[1], x[3]))
	hsps_order = [each for each in hsps]
	hsps_order.sort(key = lambda x: x[6])
	combos = []

	while hsps != []:
		combo = [hsps_order[-1]]

		idx = hsps.index(hsps_order[-1])
		score = hsps_order[-1][6]
		# forward
		for i in range(len(hsps[idx+1:])):
			new_combo = combo + [hsps[idx+1+i]]
			new_score = score_algo(new_combo)

			if new_score > score:
				combo = new_combo
				score = new_score

		# backward
		# maybe we should design a penalty for backward connection? (first intron
		# intends to be the longest one in plant genome)
		for i in range(len(hsps[:idx])):
			new_combo = [hsps[idx-1-i]] + combo
			new_score = score_algo(new_combo)

			if new_score > score:
				combo = new_combo
				score = new_score

		# delete used alignments

		for each in combo:
			hsps.remove(each)
			hsps_order.remove(each)
			
		combos.append(combo)
	return combos

def score(hsps):
	dic_hsps = {}
	dic_combos = {}
	for hsp in hsps:
		if 	hsp[0]+hsp[5] not in dic_hsps: dic_hsps[hsp[0]+hsp[5]] = [hsp]
		else: dic_hsps[hsp[0]+hsp[5]] += [hsp]
	for sid_st in dic_hsps:
		dic_combos[sid_st] = score_sys(dic_hsps[sid_st])
	return dic_combos

alignments = [["Ⅲ", 1573, 1729, 110912, 111079, "+", 102],
              ["Ⅲ", 625, 802, 789, 999, "+", 95],
		      ["Ⅲ", 100923, 101001, 19995, 20077, "+", 127],
              ["Ⅲ", 625, 802, 110022, 110222, "+", 71],
              ["Ⅲ", 973, 1105, 110439, 110578, "+", 68],
		      ["Ⅲ", 100923, 101001, 589, 661, "+", 119],
	          ["Ⅲ", 100425, 100573, 154, 307, "+", 134],
		      ['Ⅲ', 625, 802, 120022, 120222, '+', 75],
		      ['Ⅲ', 973, 1105, 120439, 120578, '+', 63]
		     ]
			 



score(alignments)