Counties_2 = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in Counties_2:
    print("El Paso is in the list of Counties.")
else:
    print("El Paso is not in the list of Counties.")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county,voters in counties_dict.items():
    print((county) + " county has " + str(voters) + " registered voters.")