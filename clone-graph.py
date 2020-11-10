"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.
"""

# my approach: use DFS twice: once to create a hashmap of the node -> clone pairings, and a second time
# to make the connections


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        table = {}

        def dfs(node, table):
            if not node:
                return
            table[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in table:
                    dfs(neighbor, table)
        dfs(node, table)
        seenNodes = set()

        def makeConnections(node, table, seenNodes):
            if not node:
                return
            seenNodes.add(node)
            lst = table[node].neighbors
            for neighbor in node.neighbors:
                lst.append(table[neighbor])
                if neighbor not in seenNodes:
                    makeConnections(neighbor, table, seenNodes)
        makeConnections(node, table, seenNodes)
        return table[node] if node else node
