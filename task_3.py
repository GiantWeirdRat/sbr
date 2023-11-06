from sys import argv

def maxstring(strings):
    buffer = strings[:]
    i = 0
    while i < len(strings[0]):
        current_max = str( max( map( lambda x: int(x[i]), buffer) ) )
        buffer = list(filter(lambda x: x[i] == current_max, buffer))
        if len(buffer) == 1:
            return buffer[0]
        i += 1
    return buffer[0]

def deepsearch(branch, nodes):
    if len(nodes) == 1:
        return [branch + str(nodes[0])]
    else:
        min_node_len = min ( map(len,  nodes) )
        max_car = str( max( map( lambda x: int(x[:min_node_len]), nodes) ) )
        new_branches = []
        for i, n in enumerate(nodes):
            if n[:min_node_len] == max_car:
                new_branches += deepsearch(branch + n, nodes[:i]+nodes[i+1:])
        return new_branches
                
def findmaxnumber(numbers):
    return maxstring(deepsearch('', numbers))

numbers = list(map(str, argv[1:]))
#numbers = ['11', '234', '005', '981', '98', '54', '98', '984']
#numbers = ['11', '234', '005', '89']

print(findmaxnumber(numbers))