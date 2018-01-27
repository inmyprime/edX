animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    for ele in aDict.values():
        count += len(ele)
    return count

    # return sum(map(len,aDict.values()))
    # return sum(len(x) for x in animals.values())

print(how_many(animals))

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if not aDict:
        return None
    largest = max(map(len, aDict.values()))
    for ele in aDict:
        if len(aDict[ele]) == largest:
            return ele

print(biggest(animals))
