"""
design_project.py

Faisal Al-Taie and Razzaq Khan
ENDG 233 F25
Design-project main program file

This file is basically the main hub for the whole project. It is the part of the
program that brings everything together — loading the data files, showing the
menu, getting user input, running the calculations, and creating the graphs.
All of the actual math and CSV reading happens in the helper modules, and this
file just coordinates everything in a clean and simple way.

The project uses three connected CSV files:
    1. Country_Data.csv – tells us each country's region and sub-region
    2. Population_Data.csv – stores population values across many years
    3. Threatened_Species.csv – lists different threatened species counts per country

From the main menu, the user can choose between two major types of analysis:

    OPTION 1 – Country population summary
        - user enters a country name
        - the program calculates the total change in population between the first
          and last recorded years
        - it also calculates the average population using NumPy
        - the user can choose to see:
              (1) change only
              (2) average only
              (3) or both values together
        - two graphs are created for the chosen country:
              • population trend over time
              • year-to-year population changes

    OPTION 2 – Sub-region threatened species summary
        - user enters a UN sub-region and a minimum threshold value
        - the program finds every country that belongs to that sub-region
        - it sums up all threatened species for each country
        - it prints a clean table showing which countries meet or pass the threshold
        - it also saves a summary CSV file for the user to view outside the program

The menu keeps looping so the user can run as many analyses as they want
Option 0 exits the program cleanly when the user is done
"""



import numpy as np
import matplotlib.pyplot as plt  
from user_csv import read_csv, write_csv
from analysis import (
    compute_population_change,
    compute_average_population,
    compute_total_threatened,)

# storing file paths so the program can load data easily from one place
DATA_FOLDER = "data_files/"
COUNTRY_FILE = DATA_FOLDER + "Country_Data.csv"
POPULATION_FILE = DATA_FOLDER + "Population_Data.csv"
SPECIES_FILE = DATA_FOLDER + "Threatened_Species.csv"

# column index positions for readability
COUNTRY_NAME_COL = 0
COUNTRY_REGION_COL = 1
COUNTRY_SUBREGION_COL = 2

# index values for threatened species dataset
SPECIES_COUNTRY_COL = 0
SPECIES_MAM_COL = 1
SPECIES_BIRDS_COL = 2
SPECIES_FISH_COL = 3
SPECIES_PLANTS_COL = 4





def load_all_datasets():
    """
    Loads all CSV datasets so the main loop can use them throughout the program

    Returns:
        tuple: country_data population_data species_data
    """

    # reading each CSV file using the custom csv reader so formatting stays consistent
    country_data = read_csv(COUNTRY_FILE, True)

    # loading population numbers so we can compute change and averages
    population_data = read_csv(POPULATION_FILE, True)

    # loading species data so we can compute total threatened species per country
    species_data = read_csv(SPECIES_FILE, True)

    # returning all datasets together so they are easy to unpack in main
    return country_data, population_data, species_data





def print_main_menu():
    """
    Displays the menu choices for the user so they know what analysis is available
    """

    # printing menu layout in a readable format for the user to choose options
    print()
    print("\n===Terminal-based data analysis and visualization program in Python===")
    print("\t1. Country population summary")
    print("\t2. Sub-region threatened species summary")
    print("\t0. Exit program")





def get_countries_in_subreigon(country_rows, subregion_name):
    """
    Returns all rows where the subregion matches the one the user entered

    Parameters:
        country_rows (list): list of country records without header
        subregion_name (str): the subregion user wants to analyze

    Returns:
        list: all rows matching the chosen subregion
    """

    # creating a list to store only the rows that belong to the chosen subregion
    matching_rows = []

    # looping through country rows to compare subregion column to user input
    for row in country_rows:

        # converting text to lowercase and trimming spaces so comparisons are reliable
        row_sub = str(row[COUNTRY_SUBREGION_COL]).strip().lower()

        # checking if subregion matches ignoring case differences
        if row_sub == subregion_name.strip().lower():

            # if match found we add the row to results so option 2 can use it
            matching_rows.append(row)

    # returning a list of only the needed rows to reduce workload later
    return matching_rows 





def prompt_for_valid_subregion(country_rows):
    """
    Repeatedly asks for a valid subregion until one is found in the dataset

    Parameters:
        country_rows (list): list of all country rows

    Returns:
        tuple: (subregion_name matching_rows)
    """

    # loop continues until the user enters a subregion that actually exists
    while True:

        # asking the user which subregion they want to analyze
        subregion_input = input("\nEnter a UN sub-region (e.g. Polynesia): ")

        # calling helper function to pull matching country rows
        matches = get_countries_in_subreigon(country_rows, subregion_input)

        # if no matches then user entered something invalid
        if len(matches) == 0:
            print("There were no countries found for that sub-region Please try again")

        # if matches found then return the values so option 2 continues
        else:
            return subregion_input, matches





def prompt_for_country(population_rows):
    """
    Asks the user for a valid country until a match is found in the population dataset

    Parameters:
        population_rows (list): list of population rows

    Returns:
        str: a valid country name exactly as stored in dataset
    """

    # creating a set of country names so we can quickly check if the user entered a real one
    valid_countries = set()
    for row in population_rows:
        country_name = str(row[0]).strip()
        valid_countries.add(country_name)

    # showing five sample countries so the user has an idea of valid entries
    print("\nSome example countries from the dataset")
    example_count = 0
    for name in valid_countries:
        print(" -", name)
        example_count += 1
        if example_count >= 5:
            break

    # loop keeps asking until user enters a valid country that exists in dataset
    while True:
        user_country = input("Enter a country name from the dataset: ").strip()

        # comparing user input to the set of valid country names ignoring case
        for name in valid_countries:
            if user_country.lower() == name.lower():

                # returning the correct dataset version of the name to avoid case issues
                return name

        # user typed something invalid so we ask again
        print("Country not found in the population dataset Please try again")





def propt_for_statistic_choice():
    """
    Asks the user which population statistic they want to see
    """

    # printing list of choices so user understands what each option displays
    print("\nWhich statistic choice would you like to see")
    print("1. Change in population (from first to last year)")
    print("2. Average population over all years")
    print("3. Both the change in population and average population")
    
    # asking repeatedly until the user enters one of the three valid codes
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()

        # checking if choice is valid
        if choice in ["1", "2", "3"]:
            return choice

        # wrong input message shown so user tries again
        else:
            print("Invalid Choice Please enter 1 2 or 3")





def create_population_plots(country_name, header_row, country_row):
    """
    Creates two graphs for the selected country using population data

    Parameters:
        country_name (str): name of the chosen country
        header_row (list): the years stored in dataset header
        country_row (list): population values for the chosen country

    Returns:
        nothing the function saves a PNG plot file
    """

    # extracting the column titles except the first one because it is the country name
    year_labels = header_row[1:]

    # creating a cleaner list of year labels by converting them to strings
    clean_year_labels = []
    for label in year_labels:
        clean_year_labels.append(str(label))

    # converting population row values into numpy format so math is fast and easy
    population_values = np.array(country_row[1:], dtype=float)

    # generating x axis indexes for placement of points in the plot
    x_values = range(len(clean_year_labels))

    # creating a whole figure with two subplots stacked vertically
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)  
    ax2 = fig.add_subplot(2, 1, 2)  

    # plotting total population values so user can see long term population trend
    ax1.plot(x_values, population_values)
    ax1.set_title("Population of " + country_name + " over time")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Population")
    ax1.set_xticks(list(x_values))
    ax1.set_xticklabels(clean_year_labels, rotation=45, fontsize=8)

    # computing year to year changes by subtracting each previous value
    changes = []
    index = 1
    while index < len(population_values):
        change = population_values[index] - population_values[index - 1]
        changes.append(change)
        index = index + 1

    # plotting these yearly changes so user sees increases or decreases each year
    ax2.bar(list(x_values)[1:], changes)
    ax2.set_title("Year-to-year population change for " + country_name)
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Change in population")
    ax2.set_xticks(list(x_values)[1:])
    ax2.set_xticklabels(clean_year_labels[1:], rotation=45, fontsize=8)

    # making sure layout fits nicely and labels do not overlap
    plt.tight_layout()

    # saving the combined figure as PNG so it can be viewed outside the program
    filename = "final_plots/" + country_name.replace(" ", "_") + "_population.png"
    fig.savefig(filename)
    plt.close(fig)

    # letting the user know the plot has been saved
    print("\nPopulation plots saved as:", filename)





def run_country_population_summary(population_data):
    """
    Handles menu option for population summary
    Prompts user for country and statistic choice
    Computes change and average and generates plots
    """

    # removing header row so only actual country data remains
    population_rows = population_data[1:]

    # asking user for a valid country name
    chosen_country = prompt_for_country(population_rows)

    # asking which statistics user wants to see
    start_choice = propt_for_statistic_choice()

    # looping to find the exact row that matches the chosen country
    country_row = None 
    for row in population_rows:
        if str(row[0]).strip().lower() == chosen_country.lower():
            country_row = row
            break

    # converting population row values into numpy array for easy summary calculations
    population_values = np.array(country_row[1:], dtype=float)

    # calling Stage 4 helper functions to compute change and average
    population_change = compute_population_change(population_values)
    average_population = compute_average_population(population_values)

    # printing the results to the user in a clear summary
    print("\n===Population Summary for", chosen_country, "===")
    if start_choice in ["1", "3"]:
        print(f"Change in population from first to last year: {int(population_change)} people")
    if start_choice in ["2", "3"]:
        print(f"Average population over the recorded years: {int(average_population)} people")
        
    # calling plot creator so graphs appear in final_plots folder
    header_row = population_data[0]
    create_population_plots(chosen_country, header_row, country_row)





def run_subregion_threatened_summary(country_data, species_data):
    """
    Handles menu option for sub region threatened species summary
    Based on user chosen sub region and threshold
    Produces printed table and summary CSV file
    """

    # extracting only data rows by skipping header
    country_rows = country_data[1:]
    species_rows = species_data[1:]

    # asking user for a valid sub region name
    subregion_name, subregion_country_rows = prompt_for_valid_subregion(country_rows)

    # asking user for a whole number threshold and validating input
    while True:
        threshold_input = input("\nEnter a minimum total threatened species (integer): ").strip()
        if threshold_input.isdigit():
            threshold_value = int(threshold_input)
            break
        else:
            print("Invalid entry Please enter a whole number like 100")

    # preparing lists to store totals and formatted output rows
    total_in_subregion = []
    country_total = []  

    # looping through each country inside the chosen sub region
    for country_row in subregion_country_rows:

        # storing the name of the country from that row
        country_name = str(country_row[COUNTRY_NAME_COL])

        # setting default value until matched in species dataset
        total_value = None

        # matching country names between datasets ignoring case differences
        for species_row in species_rows:

            # checking if country names are the same across datasets
            if str(species_row[SPECIES_COUNTRY_COL]).strip().lower() == country_name.lower():

                # extracting only numeric columns for species values
                numeric_vals = species_row[1:]

                # computing total using helper function so logic stays consistent
                total_value = compute_total_threatened(numeric_vals)
                break

        # storing totals and data only if species data was found for that country
        if total_value is not None:
            total_in_subregion.append(total_value)

            # adding formatted country and totals to be printed later
            country_total.append([
                str(country_row[COUNTRY_REGION_COL]),
                str(country_row[COUNTRY_SUBREGION_COL]),
                country_name,
                total_value
            ])

    # computing average threatened species in entire sub region
    if len(total_in_subregion) > 0:

        # converting totals into numpy array so average is easy to compute
        threatened_array = np.array(total_in_subregion, dtype=float)

        # finding overall average for this sub region
        average_threatened = np.mean(threatened_array)

        print(f"\nAverage number of threatened species in {subregion_name}: {average_threatened:.1f}")

    else:

        # if no data found then summary cannot continue so we exit function early
        print(f"\nNo threatened species data found for this sub region")
        return

    # printing table header so results appear organized
    print(f"\nCountries in {subregion_name} with at least {threshold_value} threatened species:\n")
    print("{:<10s} {:<15s} {:<15s} {:>10s}".format("UN Reg.", "Sub-Region", "Country", "Total"))

    found_anything = False

    # printing each country that meets or exceeds the threshold
    for region, subreg, name, total in country_total:
        if total >= threshold_value:
            found_anything = True
            print("{:<10s} {:<15s} {:<15s} {:>10.0f}".format(region, subreg, name, total))

    # message shown if no results meet threshold
    if not found_anything:
        print("No countries in this sub region meet or exceed that threshold")

    # creating a CSV file to store all matching countries for external viewing
    summary_rows = [["UN Region", "Sub-Region", "Country", "Total Threatened"]]

    for region, subreg, name, total in country_total:
        if total >= threshold_value:
            summary_rows.append([region, subreg, name, total])

    # writing the summary into a CSV file so user has a saved copy
    write_csv("subregion_summary.csv", summary_rows, overwrite=True)
    print("\nA summary CSV has been saved as 'subregion_summary.csv'")





def main():
    """
    Main program loop
    Loads datasets and waits for user menu choices
    Responds to each option until user exits
    """

    # loading all datasets one time so access is fast during program execution
    country_data, population_data, species_data = load_all_datasets()

    # keeping the program running until user chooses to exit
    while True:

        # printing main menu for user navigation
        print_main_menu()

        # reading user choice from keyboard
        choice = input("Enter your choice: ").strip()

        # if user wants population summary then run appropriate function
        if choice == "1":
            run_country_population_summary(population_data)

        # if user wants sub region summary then run option 2 function
        elif choice == "2":
            run_subregion_threatened_summary(country_data, species_data)

        # if user wants to exit break out of loop and end program
        elif choice == "0":
            print("Exiting program Goodbye")
            break

        # invalid entry message so user tries again
        else:
            print("Invalid menu choice Please enter 0 1 or 2")


# running main only when file is executed directly
if __name__ == "__main__":
    main() 