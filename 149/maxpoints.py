import collections
from typing import List

# [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] => 4

def maxPoints(points: List[List[int]]) -> int:
        res = 1
        for i in range(len(points)):
            p1 = points[i]
            count = collections.defaultdict(int)
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p2[0] == p1[0]:
                    slope = float("inf")
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                count[slope] += 1
                res = max(res, count[slope] + 1)
        return res


from collections import Counter

def maxPoints2(points: List[List[int]]) -> int:
        mx = 0
        for i, (x0, y0) in enumerate(points[:-1]):
            cnt = Counter(((x-x0)/(y-y0) if (y-y0) != 0 else None) for x, y in points[i+1:])
            mx = max(mx, max(cnt.values()))
        return mx+1


if __name__ == '__main__':
    ls = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(maxPoints(ls))
    print(maxPoints2(ls))