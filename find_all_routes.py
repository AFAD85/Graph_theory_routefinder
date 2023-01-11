

def find_routes(graph, start, end, routes=None, max_visit=3):

    # initializes the routes list if it isn't already made
    if routes is None:
        routes = []
    
    # checks to see if the start is a node in the graph
    if not start in graph:
        return ValueError("Start town not in routefinder")
    
    route = []
    
    # calls the recursive function, which will find all the routes
    recursive_find(graph, start, end, route, routes, 0, max_visit)
    print(routes)

    return routes
    
def recursive_find(graph, start, end, route, routes, visited, max_visit):
    
    # initializes the route by copying the route
    new_route = route.copy()
    new_route.append(start)
    
    # checks to see if the route is complete, if so adds the new route to the list of routes    
    if start == end and visited > 0:
        routes.append(new_route)
    
    # checks to see if the max number of visits has been reached, if so ends the function call    
    if visited == max_visit:
        return
    
    # keeps track of the number of nodes visited, and feed that number into the next recursive call
    current_visited = visited+1

    # loops through all the nodes connected to the start node, and calls the recursive function on each of them
    for i in range (len(graph[start])):
        recursive_find(graph, graph[start][i], end, new_route , routes, current_visited, max_visit)
    return routes
    

graph = {'A': ['B', 'D', 'E'],
         'B': ['C'],
         'C': ['D','E'],
         'D': ['C','E'],
         'E': ['B']
        }

routes = find_routes(graph, 'C', 'C')





