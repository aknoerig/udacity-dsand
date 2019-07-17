import math
def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def shortest_path(M, start, goal):
    frontier = [] # the frontier line
    visited = [] # processed intersections
    from_to = {} # shortest path steps on the way
    
    # keep track of costs for all intersections
    F = {}
    G = {}
    H = {}
    
    # start with the start!
    frontier.append(start)
    G[start] = 0
    H[start] = distance(M.intersections[start], M.intersections[goal])
    F[start] = G[start] + H[start]
    
    while len(frontier) > 0:
        # get lowest F
        current = frontier[0]
        for city in frontier:
            if F[city] < F[current]:
                current = city
        
        # when arrived, backtrace the path
        if current == goal:
            path = []
            path.append(goal)
            next = goal
            while next != start:
                next = from_to[next]
                path.append(next)
            path.reverse()
            print("path", path)
            return path
        
        # move current to visited list
        frontier.remove(current)
        visited.append(current)
        
        for city in M.roads[current]:
            if city in visited:
                continue
            
            # check if this city would be an improvement
            g_city = G[current] + distance(M.intersections[current], M.intersections[city])
            if city not in frontier:
                frontier.append(city)
            elif g_city >= G[city]:
                continue
                
            # it is for now, so calculate its costs
            G[city] = g_city
            H[city] = distance(M.intersections[city], M.intersections[goal])
            F[city] = G[city] + H [city]
            from_to[city] = current
            
    return None
