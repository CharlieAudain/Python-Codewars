def count_by(x, n):
    a = []
    iteration = 1
    while iteration <= n:
        a.append(iteration * x)
        iteration += 1
    return a

test = count_by(5, 4)
print(test)