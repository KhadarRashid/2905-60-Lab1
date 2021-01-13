
# Creating an empty list to append to later
classList = []

print("What classes will you be taking this semester?: ")
# Gathering the classes they will be taking
classes = input("Please enter all the classes you are taking this semester (press enter to quit): ")
while classes:
    # Appending the classes to the list
    classList.append(classes)
    classes = input("Please enter all the classes you are taking this semester (press enter to quit): ")

# Showing the classes they will be taking even numbered
print("You will be taking these classes this semester")
for index, c in enumerate(classList):
    print(f"{index+1} {c}")
