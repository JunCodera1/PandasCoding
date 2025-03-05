'''
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.



it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).

Write a solution to find the name, population, and area of the big countries.

Return the result table in any order.

The result format is in the following example.
'''

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Define the conditions for big countries
    area_condition = world['area'] >= 3000000
    population_condition = world['population'] >= 25000000
    
    # Apply the conditions using logical OR and select the required columns
    big_countries_df = world[area_condition | population_condition]
    return big_countries_df[['name', 'population', 'area']]
