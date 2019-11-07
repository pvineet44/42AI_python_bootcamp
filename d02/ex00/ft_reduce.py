def ft_reduce(function_to_apply, list_of_inputs):
    """ft_reduce is implementation for reduce function"""
    return_map=[]
    len_list = len(list_of_inputs)
    if len_list is 0:
        return None
    return_map=[list_of_inputs[0]]
    for  i in range(1, len_list):
        return_map = function_to_apply(return_map, list_of_inputs[i])
    return return_map

