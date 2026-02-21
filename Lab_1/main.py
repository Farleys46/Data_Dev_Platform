# Import necessary libraries
import pandas as pd

# Load the CSV file using Pandas. And tell it that the separator is ";" and not ",".
dirty_products = pd.read_csv("Lab_1/lab1_products.csv", sep=";")


#################################
##### Cleaning the CSV file #####
#################################

# Replace all ";" with "," in the DataFrame to make it look more like CSV file. 
dirty_products = dirty_products.replace(";", ",", regex=False)


# Remove whitespaces from the "name" and "currency" columns.
dirty_products["name"] = dirty_products["name"].str.strip()
dirty_products["currency"] = dirty_products["currency"].str.strip()


# Change data type for "price" column to float instead of string.
dirty_products["price"] = pd.to_numeric(dirty_products["price"], errors="coerce")

# Clean the "created_at" column by converting it to datetime format. And replace "/" with "-".
dirty_products["created_at"] = dirty_products["created_at"].str.replace("/", "-", regex=False)
dirty_products["created_at"] = pd.to_datetime(dirty_products["created_at"], errors="coerce")


################################
#### Flagging and rejecting ####
################################


# Flag products with missing values in any of the columns except "id", or with price less than 0 or greater than 40000.
columns = ["name", "price", "currency", "created_at"]

dirty_products["flag_missing_values"] = dirty_products[columns].isna().any(axis=1)
dirty_products["flag_high_price"] = dirty_products["price"] > 40000
dirty_products["flag_zero_price"] = dirty_products["price"] == 0

# Reject impossible values:
impossible_values = (dirty_products["price"] < 0) | (dirty_products["id"].isna()) 


#print(dirty_products.info())

# Check if data type has changed to float. 
print(dirty_products["price"].dtype)
print(dirty_products["created_at"].dtype)

# Save rejected rows to a new CSV file called "rejected_products.csv".
rejected_products = dirty_products[impossible_values]
rejected_products.to_csv("Lab_1/rejected_products.csv", index=False)


# Save cleaned data to a new DataFrame called "cleaned_products" and rejecting impossible values.
cleaned_products = dirty_products[~impossible_values]


####################################
##### Analytics and Bonus task #####
####################################

mean_price = round(cleaned_products["price"].mean(), 2)
median_price = round(cleaned_products["price"].median(), 2)
amount_of_products = len(cleaned_products)    
missing_price = cleaned_products["price"].isna().sum()

analytics_df = pd.DataFrame({
    "mean_price": [mean_price],
    "median_price": [median_price],
    "amount_of_products": [amount_of_products],
    "missing_price": [missing_price]
})

# Save the analytics summary to a new CSV file called "analytics_summary.csv".
analytics_df.to_csv("Lab_1/analytics_summary.csv", index=False)


print(cleaned_products)
print(amount_of_products)