def keep_only_int(x):
    result = []
    for i in x:
        if isinstance(i, int):
            result.append(i)
    return result
print(keep_only_int([1, 1.5, 2, 'a']))
