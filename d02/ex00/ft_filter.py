def ft_filter(function_to_apply, list_of_inputs):
    """ft_filter is implementation for filter function"""
    return_map=[]
    for input in list_of_inputs:
        if (function_to_apply(input)):
            return_map.append(input)
    return_map

