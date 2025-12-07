# user_csv.py
# ENDG 233 F24
# Faisal Al-Taie and Razzaq Khan 
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

def read_csv(filename, include_headers = True):
    """
    Reads a CSV file and returns the contents as a 2D list

    Parameters:
        filename (str): Name of the CSv file to read
        include_headers (bool): True = first row of headers is returned, False = data rows returned 

        Returns:
            2D list encapsulating parsed CSV file 

    """
    def is_float(value):
        """
        Determines weather a given string repersents a valid float or integer

        Conditions:
        - Leading minus sign allowed for negative numbers
        - There can be at most one decimal point
        - Remaining charcters must be digits

        Returns:
        - True if value can be converted to float, False otherwise 
        """

        # Removes Extra Spaces 
        val = value.strip()

        # Checking for negative numbers here
        if val.startswith("-"):
            # Remove the minus sign 
            val = val[1:]
        # Cannot have more than one decimal point 
        if val.count(".") > 1:
            return False
        
        # Removing any decimal points
        val_no_dot = val.replace(".", "", 1)

        # Valid only if remaining charcters are digits 
        return val_no_dot.isdigit()


    # Storage for header + data
    header_row = []
    all_rows = []

    # Open file for reading
    file_handle = open(filename, "r")

    #Read the first line 
    current_line = file_handle.readline()

    # If headers are included, store the first row separately
    if include_headers and current_line != "":
        header_row = current_line.strip().split(",")
        current_line = file_handle.readline()

    # Process each data row
    while current_line != "":
        # Split the lines into values
        raw_values = current_line.strip().split(",") 
        processed_row = []

        # Process each value in the row 
        for value in raw_values:
            cleaned_value = value.strip()
            # Convert to float if it looks numerical, otherwise leave it as a string
            if is_float(cleaned_value):
                processed_row.append(float(cleaned_value))
            else:
                processed_row.append(cleaned_value)
        
        # Add processed row to dataset
        all_rows.append(processed_row)
        # Read next line 
        current_line = file_handle.readline()
    # Close the file
    file_handle.close()

    # Return header + rows or only rows 
    if include_headers:
        return [header_row] + all_rows

    return all_rows






def write_csv(filename, data_rows, overwrite = True):
    """
    Writes a 2D list into a CSV file

    Parameters:
        filename (str): name of file to write to
        data_rows (list): 2D list conating the rows to write
        overwrite (bool): True = overwrite file, False = append to file

    Returns:
        Nothing in this function is returned 
    """

    # Choose file mode based on overwrite flag
    if overwrite:
        file_mode = "w"
    else:
        file_mode = "a"

    # Open file for writing 
    file_handle = open(filename, file_mode)

    # Write each row of data
    for row in data_rows:
        str_values = []

        # Convert each element to string before joining 
        for item in row:
            str_values.append(str(item))

        # Create CSV-formatted line 
        csv_line = ",".join(str_values)
        file_handle.write(csv_line + "\n")

    # Close file
    file_handle.close()

# End of user_csv.py



    
