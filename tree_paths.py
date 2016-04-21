"""
Victoria has a tree, TT, consisting of NN nodes numbered from 11 to NN. Each edge from node UiUi to ViVi in tree TT has an integer weight, WiWi.

Let's define the cost, CC, of a path from some node XX to some other node YY as the maximum weight (WW) for any edge in the unique path from node XX to node YY.

Victoria wants your help processing QQ queries on tree TT, where each query contains 22 integers, LL and RR, such that L≤RL≤R. For each query, she wants to print the number of different paths in TT that have a cost, CC, in the inclusive range [L,R][L,R].

It should be noted that path from some node XX to some other node YY is considered same as path from node YY to XX i.e {X,Y}{X,Y} is same as {Y,X}{Y,X}.

Input Format

The first line contains 22 space-separated integers, NN (the number of nodes) and QQ (the number of queries), respectively.
Each of the N−1N−1 subsequent lines contain 33 space-separated integers, UU, VV, and WW, respectively, describing a bidirectional road between nodes UU and VV which has weight WW.
The QQ subsequent lines each contain 22 space-separated integers denoting LL and RR.

Constraints

1≤N,Q≤1051≤N,Q≤105
1≤U,V≤N1≤U,V≤N
1≤W≤1091≤W≤109
1≤L≤R≤1091≤L≤R≤109
Scoring

1≤N,Q≤1031≤N,Q≤103 for 30%30% of the test data.
1≤N,Q≤1051≤N,Q≤105 for 100%100% of the test data.
Output Format

For each of the QQ queries, print the number of paths in TT having cost CC in the inclusive range [L,R][L,R] on a new line.

Sample Input

5 5
1 2 3
1 4 2
2 5 6
3 4 1
1 1
1 2
2 3
2 5
1 6
Sample Output

1
3
5
5
10
Explanation

Q1Q1: {3,4}{3,4}
Q2Q2: {1,3},{3,4},{1,4}{1,3},{3,4},{1,4}
Q3Q3: {1,4},{1,2},{2,4},{1,3},{2,3}{1,4},{1,2},{2,4},{1,3},{2,3}
Q4Q4: {1,4},{1,2},{2,4},{1,3},{2,3}{1,4},{1,2},{2,4},{1,3},{2,3}
...etc.
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node(object):

    def __init__(self, data):
        self.data = data
        self.adj = None

    def add_adj(self, new_adj, weight):
        self.adj = self.adj or []
        self.adj.append((new_adj, weight))


n, q = raw_input().strip().split()
n = int(n)
q = int(q)

nodes = []
for i in range(1, n+1):
    node = Node(i)
    nodes.append(node)

for i in range(n-1):
    start, end, weight = raw_input().strip().split()
    start = int(start)
    end = int(end)
    weight = int(weight)

    first = nodes[start-1]
    second = nodes[end-1]
    first.add_adj(second, weight)
    second.add_adj(first, weight)

queries = []
for j in range(q):
    low, high = raw_input().strip().split()
    low = int(low)
    high = int(high)
    queries.append((low, high))


def print_number_of_paths(node_list, query_list):
    for query in query_list:
        low = query[0]
        high = query[1]
        count = count_number_of_paths(node_list, low, high)
        print count

def count_number_of_paths(node_list, low, high):
    seen = set()
    for node in node_list:
        to_check = []
        for adj in node.adj:
            to_check.append(adj[0])
        while to_check:
            checking = to_check.pop(0)
            for adjacent in checking.adj:
                adjacent_node = adj[0]
                adjacent_weight = adj[1]
                if adjacent_weight >= low and adjacent_weight <= high:
                    to_check.extend(adjacent_node.adj)
                    if (node, checking) not in seen and (checking, node) not in seen:
                        seen.add((node, checking))
    return len(seen)

print_number_of_paths(nodes, queries)
