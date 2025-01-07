class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connections = set()

        def dfs(city):
            for row in range(len(isConnected)):
                if row not in connections and isConnected[city][row] == 1:
                    connections.add(row)
                    dfs(row)

        provinces = 0
        # get list of connections
        for city in range(len(isConnected)):
            # call dfs on city
            if city not in connections:
                # mark all neighbors
                dfs(city)
                provinces += 1
        
        return provinces