# Write a program that will generate files inside files folder with the names of filenames variable
# Each file will have the content of the list contents

contents = [
    "All carrots are to be sliced longitudinally",
    "The carrots were reportedly sliced",
    "The slicing process was well presented"
]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)
