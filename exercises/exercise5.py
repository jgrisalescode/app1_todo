# 1. prompts the user to enter a new member.
# 2. adds that member to members.txt at the end of the existing members.
# For example, the user here has entered the member Solomon Right.

new_member = input("Add a new member: ")

file = open("members.txt", "r")
members = file.readlines()
members.append(f"{new_member}\n")
file.close()

file = open("members.txt", "w")
file.writelines(members)
file.close()

print(members)

