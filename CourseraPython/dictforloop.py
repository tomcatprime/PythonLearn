file_counts = {"jpg": 10, "txt":14, "csv":2, "py":23,}
for ext in file_counts:
    print(ext)
    
    
for ext, amount in file_counts.items(): #item method return tuple for each element in the dictionary.
    print("There are {} files with the .{} extension.".format(amount, ext))
    

file_counts.keys()
file_counts.values()

for value in file_counts.values():
    print(value)
    
