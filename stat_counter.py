# use the stat ranking created from prev program to now count the stats of my mods
import csv

#initializing dict
stat_ranks = {}
file_name = "stat_ranking.csv"
with open(file_name, "r") as file_1:
    csv_read_object = csv.reader(file_1)
    for row in csv_read_object:
        stat_ranks[row[0]] = float(row[1])

# SHowing the ranking
print(f"THe ranking from file:")
for key in stat_ranks:
    print(f"{key}: {stat_ranks[key]}")
print("")

# PROGRAM CALC STARTS
print("\nThe calc begins:")
# getting the 2nd higest ranked stat value
i = 0
for key in stat_ranks:
    i+=1
    if i == 2:
        count_wrt = stat_ranks[key]
        break

# Unit roll amount:
unit_dict = {'enemy_dmg': 0.06, 
             'bounce crit': 0.25, 
             'cr': 0.05, 
             'cd': 0.15, 
             'bounce_chance_1': 0.06, 
             'wp': 0.06, 
             'wk': 0.09, 
             'bounce_wk': 0.15, 
             'bounce': 0.06}

# input mod substats:
list_mod_substats = {"hat":{"cd": 0.15, "wp": 0, "enemy_dmg": 0.06}, 
                     "mask": {"bounce": 0.06, "bounce crit": 0, "bounce_chance_1": 0.048}, 
                     "top":{"cd": 0.12, "wp": 0.06, "enemy_dmg": 0.06}, 
                     "pant":{"cd": 0.12, "wp": 0.024, "enemy_dmg": 0}, 
                     "gloves":{"cd": 0.12, "wp": 0.048, "enemy_dmg": 0.08}, 
                     "shoes":{"cd": 0.15, "wp": 0, "enemy_dmg": 0}, 
                     "weapon": {"bounce": 0.048, "bounce crit": 0.2, "enemy_dmg": 0.08}}

value_dict = {}

# calc
for armor in list_mod_substats:
    value = 0
    dict_armor = list_mod_substats[armor]
    for sub_stat in dict_armor:
        value += dict_armor[sub_stat]/unit_dict[sub_stat] * stat_ranks[sub_stat]
    value_dict[armor] = round(value, 3)

print(f"\n*****---------*****---------*****\n\nThe value dict is:")
for key in value_dict:
    print(f"{key} - value:\t{value_dict[key]}")

count_dict = {}
print(f"\n*****---------*****---------*****\n\nTHe Count obtained is:")
for key in value_dict:
    count_dict[key] = round( value_dict[key]/count_wrt, 1)
    print(f"{key} - count:\t{count_dict[key]}")
print("")