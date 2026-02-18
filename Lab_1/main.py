# Import necessary libraries
import pandas as pd
import json

# Load the CSV file using Pandas. And tell it that the separator is ";" and not ",".
dirty_products = pd.read_csv("Lab_1/lab1_products.csv", sep=";")


#################################
##### Cleaning the CSV file #####
#################################

# Replace all ";" with "," in the DataFrame to make it CSV compliant.
dirty_products = dirty_products.replace(";", ",", regex=True)


# Remove whitespaces from the "name" and "currency" columns.
dirty_products["name"] = dirty_products["name"].str.strip()
dirty_products["currency"] = dirty_products["currency"].str.strip()


# Change data type for "price" column to float instead of string.

dirty_products["price"] = pd.to_numeric(dirty_products["price"], errors="coerce")

# Flag products with missing values in any of the columns or with price less than 0 or greater than 40000.
columns = ["id", "name", "price", "currency", "created_at"]
dirty_products["is_flagged"] = dirty_products[columns].isna().any(axis=1)|(dirty_products["price"] < 0)|(dirty_products["price"] > 40000)



print(dirty_products)

#print(dirty_products.info())

# Check if data type has changed to float. 
print(dirty_products["price"].dtype)

