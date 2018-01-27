def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    dot_product = 0
    for i in range(len(listA)):
        dot_product += listA[i] * listB[i]

    return dot_product
