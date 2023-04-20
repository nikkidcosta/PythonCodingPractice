num_elements = int(input("Enter the number of elements: "))
elements = []

for i in range(num_elements):
    element = input("Enter element {}: ".format(i+1))
    elements.append(element)

comp_type = input("Which type of comprehension do you want to create? (List/Dict/Set/Generator): ")

if comp_type.lower() == "list":
    comp = [element for element in elements]
elif comp_type.lower() == "dict":
    comp = {element: len(element) for element in elements}
elif comp_type.lower() == "set":
    comp = {element for element in elements}
elif comp_type.lower() == "generator":
    comp = (element for element in elements)

print("Comprehension:", comp)