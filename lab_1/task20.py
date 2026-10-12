def flatten(data):
    i = 0
    while i < len(data):
        if isinstance(data[i], list):
            flatten(data[i])    
            data[i:i+1] = data[i]
        else:
            i += 1

def unique_elements(data):
    flatten(data)
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    data[:] = result

list_a = [1, 2, 3, [4], 5, [6, 6, [7, [], 8, [9]]]]
unique_elements(list_a)
print(list_a)
