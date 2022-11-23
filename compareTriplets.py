############ Problem
# Alice and Bob each created one problem for HackerRank. A reviewer rates the two
# challenges, awarding points on a scale from 1 to 100 for three categories:
# problem clarity, originality and difficulty.
# We define the rating for Alice's challenge to be the triplet
# a = (a[0], a[1], a[2]) and rating for Bob's challenge to be the triplet
# b = (b[0], b[1], b[2]).
# Compare a[0] with b[0], and continuing for all 3.
#   - If a[i] > b[i], then Alice is awarded 1 point
#   - If a[i] < b[i], then Bob is awarded 1 point
#   - If a[i] = b[i], then neither person receives a point
# example a = [1,2,3] and b = [3,2,1], then it would return [1,1], first being
# Alice score and second being Bob score


def compareTriplets(a,b):
    ab = [cd for cd in [1 if a[index] > b[index] else (-1 if a[index] == b[index] else 0)
          for index, f in enumerate(a)] if cd != -1]
    ba = [0 if ef == 1 else 1 for ef in ab]
    return sum(ab),sum(ba)

if __name__ == "__main__":
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    print(compareTriplets(a,b))
