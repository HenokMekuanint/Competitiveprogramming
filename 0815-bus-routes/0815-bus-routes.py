class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0

        stops_to_buses = {}  # A mapping of stop to the buses that pass through it

        for bus_ind, route in enumerate(routes):
            for stop in route:
                if stop not in stops_to_buses:
                    stops_to_buses[stop] = []
                stops_to_buses[stop].append(bus_ind)

        if target not in stops_to_buses or source not in stops_to_buses:
            return -1

        def bfs(start):
            queue = deque([(start, 0)])
            visited = set([start])

            while queue:
                stop, num_buses = queue.popleft()

                if stop == target:
                    return num_buses

                for bus in stops_to_buses[stop]:
                    for next_stop in routes[bus]:
                        if next_stop not in visited:
                            queue.append((next_stop, num_buses + 1))
                            visited.add(next_stop)

            return -1

        return bfs(source)
            
                