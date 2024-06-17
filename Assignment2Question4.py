import csv
import numpy as np

country_info_list = []
with open('countries_info.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        country_info_list.append(row)

def pearson_correlation(x, y):
    n = len(x)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    numerator = sum((x - mean_x) * (y - mean_y))
    denominator = np.sqrt(sum((x - mean_x)**2) * sum((y - mean_y)**2))
    correlation = numerator / denominator
    return correlation

areas = np.array([float(country['Area'].replace(',', '')) for country in country_info_list])
populations = np.array([float(country['Population'].replace(',', '')) for country in country_info_list])
gdps = np.array([float(country['GDP'].replace(',', '').replace('$', '').replace(' trillion', '')) for country in country_info_list])

area_population_correlation = pearson_correlation(areas, populations)
area_gdp_correlation = pearson_correlation(areas, gdps)
population_gdp_correlation = pearson_correlation(populations, gdps)

print(f"Pearson correlation coefficient for (area, population): {area_population_correlation:.4f}")
print(f"Pearson correlation coefficient for (area, GDP): {area_gdp_correlation:.4f}")
print(f"Pearson correlation coefficient for (population, GDP): {population_gdp_correlation:.4f}")
