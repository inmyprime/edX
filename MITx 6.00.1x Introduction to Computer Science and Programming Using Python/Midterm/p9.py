def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    f = []
    for ele in aList:
        if type(ele) != list:
            f.append(ele)
        else:
            f.extend(flatten(ele))
    return f
