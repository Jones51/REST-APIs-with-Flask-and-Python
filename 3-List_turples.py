list = ["Bob", "Carlos", "Joao"]
turples = ("Bob", "Carlos", "Joao") #cant add or remove values
sets = {"Bob", "Carlos", "Joao"} #cant have duplicates, the order can change

print(list[0])
print(turples[0])
print(set[0])

list.append("Kely")

abroad = {"Rodolf, Bob"}
local_friends = abroad.difference(sets)
print(local_friends)