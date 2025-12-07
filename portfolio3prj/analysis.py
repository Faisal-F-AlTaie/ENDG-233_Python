# analysis.py
# ENDG 233 F25
# Faisal Al-Taie and Razzaq Khan
# Helper functions for data analysis using numpy.
# These functions are used by design_project.py (Stage 4 requirement).

# analysis_utils.py
# ENDG 233 F24
# Faisal Al-Taie and Razzaq Khan
# Helper functions for data analysis using numpy.
# These functions are used by design_project.py (Stage 4 requirement).

import numpy as np


def compute_population_change(pop_values):
    """
    Calculates the change in population from the first year to the last year

    Parameters:
        pop_values (numpy.ndarray): Array of population values for each recorded year

    Returns:
        float: Difference between last value and first value
    """

    # taking the first population and last population so we can compare the change over time
    start_pop = pop_values[0]

    # selecting the last population value in the array to measure final point
    end_pop = pop_values[-1]

    # subtracting first year from last year to show total growth or decline
    change = end_pop - start_pop

    # returning the amount of population change so the main program can print it
    return change





def compute_average_population(pop_values):
    """
    Calculates the average population over all recorded years

    Parameters:
        pop_values (numpy.ndarray): Array of population values for each recorded year

    Returns:
        float: Average population across all values
    """

    # using numpy mean to find the average because it is simple and reduces manual math
    average = np.mean(pop_values)

    # returning the average so it can be used in the population summary
    return average





def compute_total_threatened(numeric_values):
    """
    Calculates the total threatened species for a single country

    Parameters:
        numeric_values (list or array): List of numeric values for threatened mammals birds fish plants

    Returns:
        float: Sum of all threatened species values combined
    """

    # converting every entry into a float so they can be added together safely
    float_values = []
    for value in numeric_values:
        float_values.append(float(value))

    # summing up all categories so we get one total number for threatened species
    total = sum(float_values)

    # returning the total so option 2 can list and compare values
    return total


# End of analysis.py
