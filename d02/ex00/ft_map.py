def ft_map(function_to_apply, list_of_inputs):
    """ft_map is implementation for map function"""
    return_map=[]
    len_list = len(list_of_inputs)
    if len_list is 0:
        return None
    for input in list_of_inputs:
        return_map.append(function_to_apply(input))
    return return_map

