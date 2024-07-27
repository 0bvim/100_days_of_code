from prettytable import PrettyTable;

table = PrettyTable() 
table.add_column("Pokename", ["Xipaku", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire Name"])
table.align = "l"

print(table)
