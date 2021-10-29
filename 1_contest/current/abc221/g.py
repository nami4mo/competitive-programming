
# from collections import deque
# def main():
#     def bfs(start, g, visited):
#         q = deque([start])
#         visited[start] = 0
#         last_node = 0
#         while q:
#             curr_node = q.popleft()
#             for next_node in g[curr_node]:
#                 if visited[next_node] >= 0: continue
#                 visited[next_node] = visited[curr_node] + 1
#                 q.append(next_node)
#                 last_node = next_node
#         return last_node

#     n = int(input())
#     gl = [ [] for _ in range(n)]
#     visited = [-1] * (n)
#     for i in range(n-1):
#         a, b = map(int, input().split()) 
#         a-=1
#         b-=1
#         gl[a].append(b)
#         gl[b].append(a)


#     node_a = bfs(0, gl, visited)
#     cnts1=0
#     ma=max(visited)
#     for c in visited:
#         if c==ma:cnts1+=1
    

#     visited = [-1] * (n)
#     node_b = bfs(node_a,gl,visited)
#     cnts2=0
#     ma=max(visited)
#     for c in visited:
#         if c==ma:cnts2+=1
#     # print(visited[node_b])
#     print(node_a, node_b)
#     ans=cnts


# if __name__ == "__main__":
#     main()

# def main():
#     pass


# if __name__ == "__main__":
#     main()