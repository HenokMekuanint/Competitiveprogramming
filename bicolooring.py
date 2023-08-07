from collections import defaultdict

while True:
    nodes = int(input())

    if nodes == 0:
        break

    edges = int(input())
    adjacency = defaultdict(list)

    for _ in range(edges):
        node1, node2 = map(int, input().split())

        adjacency[node1].append(node2)
        adjacency[node2].append(node1)


    color = defaultdict(int)
    stack = [1]
    color[1] = 1
    visited = set([1])
    got = False
    while stack:

        cur = stack.pop()

        for neighbour in adjacency[cur]:

            
            
                if color[neighbour] == color[cur]:
                    print('NOT BICOLOURABLE.')
                    got = True
                    break

                elif neighbour not in visited:

                    color[neighbour] = color[cur] * -1
                    visited.add(neighbour)
                    stack.append(neighbour)

        if got:
            break

    else:
        print('BICOLOURABLE.')
