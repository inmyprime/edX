def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]
applyToEach(testList, abs)
print(testList)

testList = [1, -4, 8, -9]
def addOne(x):
    return x + 1

applyToEach(testList, addOne)
print(testList)

testList = [1, -4, 8, -9]
def square(x):
    return x ** 2

applyToEach(testList, square)
print(testList)

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, square, halve, abs], -3))
print(applyEachTo([inc, square, halve, abs], 3.0))
print(applyEachTo([inc, max, int], -3))
