import json 
import pandas as pd 

products_jsonb = pd.read_csv (
    "workshop_products.csv"
)

#print(products_jsonb.values)


products_jsonb["payload"] = products_jsonb["payload"].apply(json.loads)

payload_df = pd.json_normalize (products_jsonb["payload"])

print(payload_df)