def flatten(data):
    i = 0
    while i < len(data):
        if isinstance(data[i], list):
            flatten(data[i])    
            data[i:i+1] = data[i]
        else:
            i += 1

list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten(list_a)
print(list_a)
