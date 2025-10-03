# Applying Machine Learning Techniques to a chess data


## possible evaluations:
- how does rating affect winrate vs lower rated players?
- what openings seemed to have won most
  - lower vs higher, higher vs lower rated
  -


## Comments on ...
- Statistics.py > Statistics.mode():
A bit awkward to not use collections.Counter(), but I want to make at least the
basic statistical functions somewhat understandable.
This is not a educational project on statistics, so at some point I will use
more sophisticated methods.


## Progress
- after categorizing the player tiers respective to rating ranges,
the question arises, how i could approach the most "distinctive" ranges
which define the tiers.
Obviously I could just take some established approach from the chess world,
but, it's more appealing to me, to approach that problem with a more sophisticated
approach. -> I have decided for a K-Means algorithmic solution.

## 01 K-Means

Info: K-Means is a **unsupervised** algorithm that finds patterns in data
Goal: Find clusters in player ratings
