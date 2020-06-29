# python3
def compute_min_refills(distance, tank, stops):
    count, can_reach = 0, 0
    while can_reach < len(stops)-1:
        last_ref = can_reach
        while stops[can_reach + 1] - stops[last_ref] <= tank:
            can_reach += 1
            if can_reach == len(stops) - 1: break
        if can_reach == last_ref:
            return -1
        if stops[can_reach] < distance:
            count += 1
    return count

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    stops = []
    n = int(input())
    stops = list(map(int, input().split()))[:n]
    stops = [0] + stops + [d]
    print(compute_min_refills(d, m, stops))
