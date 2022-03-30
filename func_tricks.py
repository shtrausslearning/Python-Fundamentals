# MAP FUNCTION

# map(func, iter)
list(map(lambda x: x[0], ['red', 'green', 'blue'])) 
# Result: ['r', 'g', 'b']

# map(func, i1, ..., ik)
list(map(lambda x, y: str(x) + ' ' + y + 's' , [0, 2, 2], ['apple', 'orange', 'banana']))
# Result: ['0 apples', '2 oranges', '2 bananas']
