# From this list waiting_list = ["sen", "ben", "john"]
# Print like this:
# 1.Ben
# 2.John
# 3.Sen

waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for index, person in enumerate(waiting_list):
    print(f"{index + 1}.{person.title()}")
