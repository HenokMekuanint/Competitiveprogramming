from collections import defaultdict

def parallelCourses(n, prerequisites):

    # Write your code here.
    pass
    adj = defaultdict(list)
    indegree = [0] * (n + 1)
    height = [0] * (n + 1)
    for u, v in prerequisites:
        adj[u].append(v)
        indegree[v] += 1

    q = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            height[i] = 1

    count = 0
    while q:
        node = q.pop(0)
        count += 1
        for v in adj[node]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
                height[v] = 1 + height[node]

    if count != n:
        return -1

    max_height = 0
    for i in range(1, n + 1):
        max_height = max(max_height, height[i])

    return max_height
