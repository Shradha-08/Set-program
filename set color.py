color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set of elements: ")
print(color_list_1)
print(color_list_2)
#print(color_list_1 - color_list_2)
for item in color_list_1:
    if item not in color_list_2:
        print("Item: ", item)
