# Python program to
# demonstrate reading files
# using for loop

# Writing to file

# Opening file
file1 = open('index.html', 'r', encoding="utf8")

file2 = open('index2.html', 'w', encoding="utf8")

# Using for loop
print("Using for loop")
for line in file1:
    if line != "\n":
        file2.write(line)
    # print("Line{}: {}".format(count, line.strip()))

# Closing files
file1.close()
file2.close()
