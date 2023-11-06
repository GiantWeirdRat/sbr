from sys import argv

def find_optimal_distances(n, k, distances):
    inserts = [1]*n
    new_distances = distances[:]
    
    while k > 0:
        i = new_distances.index(max(new_distances))
        inserts[i] += 1
        new_distances[i] = distances[i] / inserts[i]
        k -= 1
    
    result = []
    for i, d in zip(inserts, new_distances):
        result += [d]*i
    return result

n, k = int(argv[1]), int(argv [2])
distances = list(map(int, argv[3:3+n]))

#n, k, distances = 5, 3, [100, 180, 50, 60, 150]

optimal_distances = find_optimal_distances(n, k, distances)

for d in optimal_distances:
    print(d)