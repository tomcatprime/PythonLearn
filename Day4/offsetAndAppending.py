# list - starts always with [] 
# frutis = [item1, item2]
# if index is minus, will start from end of list
states = ["Delaware", "Pennsylvania", "Arizona", "Texas"]
print(states[1])
# if index is minus, will start from end of list
print(states[-1])

# Modify item in list
states[2] = "Ariz"

#add item to the end of the list .append()

states.append("Los Angeles")
print(states)

# adding bunch of items .extend()
states.extend(["Miami", "Florida"])
print(states)