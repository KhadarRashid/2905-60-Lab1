
classList = []
print("What classes will you be taking this semester?: ")
classes = input("Please enter all the classes you are taking this semester (press enter to quit): ")
while classes:
    classList.append(classes)
    classes = input("Please enter all the classes you are taking this semester (press enter to quit): ")

print("You will be taking these classes this semester")
for index, c in enumerate(classList):
    print(f"{index+1} {c}")