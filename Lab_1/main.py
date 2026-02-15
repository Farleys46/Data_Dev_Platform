# Import necessary libraries
import pandas as pd
import json

# Load the CSV file using Pandas. 
dirty_products = pd.read_csv("Lab_1/lab1_products.csv", sep=";")


#################################
##### Cleaning the CSV file #####
#################################

# Replace all ";" with "," in the DataFrame to make it CSV compliant.
dirty_products = dirty_products.replace(";", ",", regex=True)


dirty_products["name"] = dirty_products["name"].str.strip()

print(dirty_products.values)