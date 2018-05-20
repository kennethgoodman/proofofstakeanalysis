# proofofstakeanalysis
Do the rich get richer?


The expected amount a staker will have in the next block = their stake + their stake / all staked * block reward.

So after 1 blocks:

s = their stake

t = all staked; t(n+1) = t(0) + n * r

r = block reward; r(n) = ~N(r(0),\sigma) 
 
s(0) = initial staked

t(0) = total initial staked

s(1) = s(0) + s(0) / t(0) * r

s(n+1) = s(n) + s(n) / t(n) * r = s(n) + s(n) / (t(0) + n * r) * r;

As n -> infinity, if t(n) != total supply, then t(n)/total supply will converge to 1 and those that did not stake will approach 0% of all coins. For those that are staking their percentage is calculated as:

ts = total supply; ts(n) = ts(0) + n * r

sp(n+1) = s(n+1) / ts(n+1) = ( s(n) + s(n) / t(n) * r ) / ts(n+1) 

Because the wealthier can afford to spend less of their earned through staking coins, we can see the rich getting richer. Especially for any coin that restricts liquidity for stakers, as the poor can not do that with the same percentage of their wealth as compared to the wealthy. We may see pooled investment vehicles similar to PoW mining pools to capitalize on this phenominom.
