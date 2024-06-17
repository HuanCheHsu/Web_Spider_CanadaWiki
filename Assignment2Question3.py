country_info_list = []
with open('countries_info.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        country_info_list.append(row)

def find_highest(metric):
    highest_country = None
    highest_value = 0
    
    for country_info in country_info_list:
        value = float(country_info[metric].replace(',', ''))
        if value > highest_value:
            highest_value = value
            highest_country = country_info['Country']
    
    return highest_country, highest_value

highest_population_country, highest_population = find_highest('Population')

highest_area_country, highest_area = find_highest('Area')

highest_gdp_country, highest_gdp = find_highest('GDP')

print(f"Country with the highest population: {highest_population_country} ({highest_population} million)")
print(f"Country with the highest area: {highest_area_country} ({highest_area} square kilometers)")
print(f"Country with the highest GDP: {highest_gdp_country} (${highest_gdp} trillion)")
