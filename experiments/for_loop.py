todos = ['Clean', 'Walk', 'Buy']

for index, todo in enumerate(todos):
    print(index, todo)

print("Last variable created in loop iteration", index, todo)

# Use enumerate also for strings
for i, j in enumerate("Hello World"):
    print(i, j)
