def kokoEatingBananas(piles, h): 
  ''''Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
  The guards have gone and will come back in h hours.Koko can decide her bananas-per-hour eating speed of k. 
  Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
  If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
  Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
  Return the minimum integer k such that she can eat all the bananas within h hours.'''
  def canEatBananas(piles, mid, h): 
    timeTaken = 0 
    for n in piles: 
      timeTaken += n // mid
      if n % mid != 0: 
        timeTaken += 1 
    return timeTaken <= h
  l = 1
  r = max(piles)
  while l < r:
    mid = l + r // 2
    if canEatBananas(piles, mid, h):
      r = mid
    else: 
      l = mid + 1 
  return l 
