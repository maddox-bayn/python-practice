# python program to help analyze this large amount of data.
# project author: Oduh Emmanuel
# added functionality to allow users to search by country name to see its minimum, maximum, and average life expectancy.

# getting user input for year to analyze
user_input = input("Enter the year or country of interest: ")

# if user input is a yeaer
is_year = user_input.isdigit()

# variable to calculate the average life expectancy for the year of interest
total_life_expectancy = 0.0
count = 0

# unique variables for country search
country_life_expectancy = 0.0
country_count = 0
country_max_life_expectancy = 0.0
country_min_life_expectancy = float('inf')
country_max_life_expectancy_year = ""
country_min_life_expectancy_year = ""

# Initialize variables to track overall max and min life expectancy
max_life_expectancy = 0.0
min_life_expectancy = float('inf')  # Initialize to positive infinity
# year of overall max and min life expectancy 
max_life_expectancy_year = ""
min_life_expectancy_year = ""
# max and min life expectancy for each year in the data set.
current_min_life_expectancy = float('inf')
current_max_life_expectancy = 0.0

# overall max and min countries for life expectancy
max_life_expectancy_country = ""
min_life_expectancy_country = ""

# current year max and min countries for life expectancy
current_max_life_expectancy_country = ""
current_min_life_expectancy_country = ""

# Open the life-expectancy.csv file and read its contents
with open("life-expectancy.csv") as life_file:

    # skip the first line in file
    next(life_file)
    # looping through each line in life_file
    for line in life_file:
        # split each line into parts and retrive parts
        parts = line.split(",")
        entity = parts[0]
        code = parts[1]
        year = parts[2]
        life_expectancy = float(parts[3])

        # Update max and min life expectancy for the current year
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_life_expectancy_country = entity
            max_life_expectancy_year = year
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_life_expectancy_country = entity
            min_life_expectancy_year = year
        if is_year and year == user_input:
            if life_expectancy > current_max_life_expectancy:
                current_max_life_expectancy = life_expectancy
                current_max_life_expectancy_country = entity
            if life_expectancy < current_min_life_expectancy:
                current_min_life_expectancy = life_expectancy
                current_min_life_expectancy_country = entity
            total_life_expectancy += life_expectancy
            count += 1
        elif not is_year and user_input.lower() == entity.lower():
            country_life_expectancy += life_expectancy
            country_count += 1
            if life_expectancy > country_max_life_expectancy:
                country_max_life_expectancy = life_expectancy
                country_max_life_expectancy_year = year
            if life_expectancy < country_min_life_expectancy:
                country_min_life_expectancy = life_expectancy
                country_min_life_expectancy_year = year

# Calculate the average life expectancy for the year of interest
if count > 0:
    average_life_expectancy = total_life_expectancy / count
else:
    average_life_expectancy = 0.0

# Calculate the average life expectancy for the country of interest
if country_count > 0:
    country_average_life_expectancy = country_life_expectancy / country_count
else:
    country_average_life_expectancy = 0.0

print(f"The Overall maximum life expectancy is {max_life_expectancy} from {max_life_expectancy_country} in the year {max_life_expectancy_year}")
print(f"The Overall minimum life expectancy is {min_life_expectancy} from {min_life_expectancy_country} in the year {min_life_expectancy_year}")
print()
if is_year:
    print(f"for the year {user_input}:")
    print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
    print(f"The maximum life expectancy was in {current_max_life_expectancy_country} with {current_max_life_expectancy}")
    print(f"The minimum life expectancy was in {current_min_life_expectancy_country} with {current_min_life_expectancy}")
else:
    print(f"for the country {user_input}:")
    print(f"The average life expectancy was {country_average_life_expectancy:.2f}")
    print(f"The maximum life expectancy was {country_max_life_expectancy} in the year {country_max_life_expectancy_year}")
    print(f"The minimum life expectancy was {country_min_life_expectancy} in the year {country_min_life_expectancy_year}")