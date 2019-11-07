def ft_filter(function_to_apply, list_of_inputs):
    """ft_filter is implementation for filter function"""
    return_map=[]
    len_list = len(list_of_inputs)
    if len_list is 0:
        return None
    for input in list_of_inputs:
        if (function_to_apply(input)):
            return_map.append(input)
    return_map

