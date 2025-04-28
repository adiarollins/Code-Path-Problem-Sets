'''Problem 1
def most_endangered(species_list):
    if len(species_list) > 0: 
        minName = species_list[0]["name"]
        minPop = species_list[0]["population"]
    for i in range(1, len(species_list)):
        if species_list[i]["population"] < minPop:
            minName = species_list[i]["name"]
            minPop = species_list[i]["population"]
    return minName

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 74
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))
Problem 2
def count_endangered_species(endangered_species, observed_species):
    dict = {}
    for endangered in observed_species:
        if endangered in endangered_species and endangered in dict:
            dict[endangered] += 1
        elif endangered in endangered_species:
            dict[endangered] = 1
    total = sum(dict.values())
    return total

endangered_species1 = "aA"

observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  

Problem 3
def navigate_research_station(station_layout, observations):
    sum = 0
    i = 0
    j = 0
    station_layout_dict = {}
    station_layout_list = list(station_layout)
    for k in range(len(station_layout_list)):
        station_layout_dict[station_layout_list[k]] = k
    for m in observations:
        j = station_layout_dict.get(m)
        sum = sum + abs(int(i)-int(j))
        i = station_layout_dict.get(m)
    return sum

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))
'''