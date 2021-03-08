import itertools

W = ['St', 'Petersburg', 'USF', 'Campus']

#creating/define iterator
iterators = itertools.cycle(W)

for W in range(12):
    print(next(iterators), end=" ")

