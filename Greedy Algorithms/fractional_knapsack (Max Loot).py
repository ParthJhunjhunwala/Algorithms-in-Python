# Uses python3
def get_optimal_value(cap, value_weights):
    tval = 0
    v , w = map(list, zip(*sorted(value_weights, key = lambda x: x[0]/x[1], reverse = True)))
    for i in range(n):
        if cap <= 0:
            return tval
        tweight = min(cap, w[i])
        tval = tval + tweight*(v[i]/w[i])
        cap = cap - w[i]
        w[i] = w[i] - tweight
    return tval


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    value_weights = []
    for i in range(n):
        x, y = map(int, input().split())
        value_weights.append((x, y))
    opt_value = get_optimal_value(capacity, value_weights)
    print("{:.10f}".format(opt_value))