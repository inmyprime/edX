def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    intersect = {}
    difference = {}
    keys1 = d1.keys()
    keys2 = d2.keys()
    for key in keys1:
        if key in keys2:
            intersect[key] = f(d1[key], d2[key])
        else:
            difference[key] = d1[key]
    for key in keys2:
        if key not in keys1:
            difference[key] = d2[key]

    return (intersect, difference)
