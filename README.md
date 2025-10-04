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

## Insights from evaluations
- There is a difference between the columns "opening_name" and "opening_eco",
that is, that
opening_eco: 365 -> different openings
opening_name: 1477 -> different openings
```python
print(f"Total unique Openings: {df['opening_name'].unique().__len__()}")
print(f"Total unique Openings: {df['opening_eco'].unique().__len__()}")
```
"opening_name" seems to be more precise.
I have to evaluate how I will proceed with the evaluation of openings.

