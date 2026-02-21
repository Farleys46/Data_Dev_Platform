# Lab 1

Imported pandas.

## Ingestion
I used pandas to read the raw data `lab_1.csv`. Since the separator in the raw csv file is `;` and not a comma, I had to specify that in the python script. 

## Cleaning data 
Started with removing whitespaces for the columns using the `.str.strip()` method. As well as replacing the `;` to `,` to make it look more like a regular csv file. 

Since the data type for the `price` column was string I changed it to float using the pandas `to_numeric` function: 
[StackOverflow: When to apply pd.to_numeric and when to astype in python](https://stackoverflow.com/questions/40095712/when-to-applypd-to-numeric-and-when-to-astypenp-float64-in-python)

For the `created_at` column there were some values in the wrong format. Instead of `2024-03-21` some had `/` between etc. I cleaned it by replacing `/` with `-` and also using the pandas function `to_datetime`: 
[Pandas User Guide: Time series](https://pandas.pydata.org/docs/user_guide/timeseries.html).

## Flagging and rejecting
I decided that the values that should be flagged are any missing values in all columns except the `id` column. As well as high prices in the list that exceed 40000 SEK, because the closest values was a "watch" and a "ring" that makes sense to be a high price.

I also flagged the rows with `0` in price since it would be good to double check if something really should be free. There is one row that says "free" but since it has no `id` or `created_at` columns its hard to check it so I rejected it instead. 

The other values I rejected were products with a negative price (so `< 0`) and those who had a missing `id`.

## Loading in new csv files
All rejected rows was saved in a new csv file called `rejected_products.csv` by using the `.to_csv()` method. 

I then saved the clean version of the file into a csv file called `cleaned_products.csv` with all impossible values removed. 

## Analytics 
I created a new csv file called `analytics_summary.csv` and added the columns `mean_price`, `median_price`, `amount_of_products`, and `missing_price`. Then I made it into a DataFrame called `analytics_df` before loading it in the new csv file.