def get_percentage(aList):
	s = sum(aList)
	return [1.0 * x / s for x in aList]

def round_it(x):
	return round(x,4)

def round_list(aList):
	return list(map(round_it,aList))

def add_to(holdings, stakings, rate, should_round=False):
	new_total = sum(holdings) * (1+rate)
	total_staked = sum(stakings)
	each_stakers_percentage = get_percentage(stakings)
	new_staked = [ 1.0 * sp * new_total for sp in each_stakers_percentage ]
	new_holding = [ max(holding, staking) for holding, staking in zip(holdings,new_staked) ]
	if should_round:
		new_staked = round_list(new_staked)
		new_holding = round_list(new_holding)
	return new_holding, new_staked

i_h = [2,2,1.5,1,1,.5,.25,1]
i_s = [2,2,1.5,1,1,.5,.25,0]
rate = .04
initial_max = round(max(get_percentage(i_h)),5)

new_holding, new_staked = i_h, i_s
hps = get_percentage(new_holding)
print("Year {} Holdings = {}, max % = {}, initial = {}".format(0, round_list(new_holding), round(max(hps),5), initial_max))
for i in range(1, 51):
	hps = get_percentage(new_holding)
	new_holding, new_staked = add_to(new_holding, new_staked, rate)
	print("Year {} Holdings = {}, max % = {}, initial = {}".format(i, round_list(new_holding), round(max(hps),5), initial_max))
