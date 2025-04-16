names=["Keerthy","Kavya","Heama","Deepthi","Divya","Gomathi"]

grouped_names={}
for name in names:
    first_letter=name[0].lower()
    if first_letter in grouped_names:
        grouped_names[first_letter].append(name)
    else:
        grouped_names[first_letter]=[name]
print(grouped_names)
        
