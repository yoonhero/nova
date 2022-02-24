def number_generator():
    yield 0
    yield 1
    yield 2

# for i in number_generator():
#     print(i)


g = number_generator()

# print(dir(g))

print(next(g))

print(next(g))

print(next(g))

def one_generator():
    yield 1
    return 'return에 지정한 값'
 
try:
    g = one_generator()
    next(g)
    next(g)
except StopIteration as e:
    print(e)    # return에 지정한 값