# Uses python3
'''
Logic: Arrange segments in ascending order of their end points
Select the first end point, remove all segments covering that point.
Append the end point in the list and repeat until all segments are covered.

Note:
segments[:] creates a copy of the segments list and itereates through that
instead of the original list. This is done because segments might change
length in each iteration
'''
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort(key = lambda x: x[1])
    while segments != []:
        point = segments[0].end
        for s in segments[:]:
            if s.start <= point <= s.end:
                segments.remove(s)
        points.append(point)
    return points

if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        a, b = map(int, input().split())
        segments.append(Segment(a, b))
    points = optimal_points(segments)
    print(len(points))
    print(*points)