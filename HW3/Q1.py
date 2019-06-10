import xlrd
from collections import defaultdict

#open xls file
xl_workbook = xlrd.open_workbook("Graph_data.xls")

sheet_names = xl_workbook.sheet_names()

xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])

#breadth first search
def bfs(graph, start):
    queue, path = [start], []

    while queue:
        vertex = queue.pop(0)
        if vertex in path:
            continue
        else:
            path.append(vertex)
        for neighbor in graph[vertex]:
            queue.append(neighbor)

    return path

#depth first search
def dfs(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex not in path:
            path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
      
    return path

#format print
def print_result(arr):
    for i in range(0,len(arr)):
        print(arr[i],"-> ", end='')
    print()

#graph adjacency list
graph = defaultdict(list)

num_rows = xl_sheet.nrows
for i in range (3,num_rows):
    cell_obj_1 = xl_sheet.cell(i, 0)
    cell_obj_2 = xl_sheet.cell(i, 1)
    val1 = int (cell_obj_1.value)
    val2 = int (cell_obj_2.value)
    graph[val1].append(val2)

#tests
print_result(bfs(graph, 1))
print_result(dfs(graph, 1))