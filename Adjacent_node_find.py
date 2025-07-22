def fin_adj_node(my_list,start,visited=None,result=None):
    #always capture the reult outside the loop so we will find next adjecent node while capturing visited node
    if visited is None:
        visited = set()
    
    if result is None:
        result = list()
    
    for val in start:
        if val not in visited:
            visited.add(val) # set stores all the unique values
            result.append(val) # list stores all the values but we are passing only those which are not visited so for first [1,5] it will only append 1

    #recursion loop to find the next adj node which has one of the unique value
    for pair in my_list:
        if pair!=start and (set(pair) & set(start)) and not all(val in visited for val in pair):
            fin_adj_node(my_list,pair,visited,result)
    return result,visited
        


my_list = [[3,5],[4,6],[2,4],[1,2],[1,5]]
result,visited = fin_adj_node(my_list,start=my_list[0])
print(result,visited)
