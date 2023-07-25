import itertools

def desc(stuff, level):
	for n1 in range(1, len(stuff) +1):
		for t1 in itertools.combinations(stuff, n1):
			pad = '\t' * level
			print(pad, t1)
			remain = ''
			for c in stuff:
				if c not in t1 and c > t1[-1]: remain += c
			desc(remain, level+1)


s = 'abcd'
desc(s, 0)