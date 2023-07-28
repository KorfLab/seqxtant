import itertools

def desc(stuff, level, alist):
	for n1 in range(1, len(stuff)+1):
	
		for t1 in itertools.combinations(stuff, n1):

			alist.append([level, t1])
			remain = ''
			for c in stuff:
				if c not in t1 and c > t1[-1]: remain += c
			desc(remain, level+1, alist)


def getcombo(desc_combos, level_num):

	for level in range(level_num):
		for i in range(len(desc_combos)-1):
			if desc_combos[i][0] == level:
				for j in range(1, len(desc_combos[i+1:])+1):
					if desc_combos[i+j][0] == level + 1: 
						desc_combos[i+j] = [desc_combos[i+j][0]] + desc_combos[i][1:] + desc_combos[i+j][1:]
#						print("pass")
					if desc_combos[i+j][0] <= level: 
#						print(desc_combos[i], desc_combos[i+j])
						break

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
			 
alignments.sort(key = lambda x: (x[1], x[2], x[3], x[4]))
n = len(alignments)
print(alignments)
s = ''
for i in range(n):
	s += str(i)



result = []
desc(s, 0, result)
#print(result)

getcombo(result, n)



combos = []
for each in result:
	if each[-1][-1] == s[-1]: combos.append(each)


#print(len(result))
#print(result)


#for each in combos:
#	print(each)

#print(len(combos))
#print(combos[-1])

# scoring system
dist_penalty = 0.1
overlap_penalty = 10
connect_reward = 1

score = -100000000
count = 0
for combo in combos:
	count += 1
	new_score = 0
	combo.pop(0)
#	print(combo)
#	break
	for each in combo:
		# sum of algnment scores
		for i in each:
			i = int(i)
#			print(i)
#			print(alignments[i][-1])
			new_score += alignments[i][-1]
			
		# calculate penalty
		for j in range(1, len(each[1:])+1):
#			print(each)
			for x in [0, 2]:
				dist = alignments[int(each[j])][1+x] - alignments[int(each[j-1])][2+x]
				if dist <= 0: new_score += dist * overlap_penalty
				else: new_score -= dist * dist_penalty
		
		# calculate reward
		if len(each) > 1:
			for n in each:
				n = int(n)
				new_score += alignments[n][-1] * connect_reward
#		print(new_score)
	if new_score > score:
		score = new_score
		chosen_combo = combo
		print(chosen_combo, score)
			
#	if count == 3: break			

