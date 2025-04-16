def reverse_traverse_with_index(list):
    length=len(list)
    for i in range(length-1,-1,-1):
        print(f"Index{i}:{list[i]}")

original_list=['red','green','white','black']
print("Original list:",original_list)
print("Traverse reverse list with original indexes")
reverse_traverse_with_index(original_list)
