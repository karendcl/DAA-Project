def calc(l,r,unf):
    sum = 0
    for i in range(l,r):
        for j in range(i,r):
            sum += unf[i][j]
    return sum

def calculate_unf(starting_indexes_groups,unf):
    sum = 0
    if len(starting_indexes_groups) == 0:
        return calc(0,len(unf),unf)
    for i in range(len(starting_indexes_groups)):
        if i == 0:
            sum += calc(0,starting_indexes_groups[i],unf)
        else:
            sum += calc(starting_indexes_groups[i-1],starting_indexes_groups[i],unf)
    sum += calc(starting_indexes_groups[-1],len(unf),unf)
    return sum

def brute_solve(n,k,unf):
    import itertools
    min = float('inf')
    groups = [i for i in range(1,n)]
    for i in itertools.combinations(groups, k-1):
        i = list(i)
        sum = calculate_unf(i,unf)
        if sum < min:
            min = sum
    return min







