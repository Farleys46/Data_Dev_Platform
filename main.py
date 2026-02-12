from fastapi import FastAPI, status

from psycopg_pool import ConnectionPool

from psycopg.types.json import Json # Convert Pydantic to JSON.

from psycopg import Connection




DATABASE_URL = "postgresql://postgres:admin123@localhost:5432/lektion_5"
pool = ConnectionPool(DATABASE_URL)


app = FastAPI(title="lektion5_postgresql_fastapi")

@app.get("/")
def root() -> dict:
    return {"Hello": "World"}

@app.post(
    "/products", 
        status_code=status.HTTP_201_CREATED,
        response_model=ProductSchema,
)
def post_product(product: ProductSchema) -> ProductSchema:
    
    #Query Insert
    with pool.connection() as conn:
        insert_product(conn, product)
        conn.commit()
    
    return product

def insert_product(conn: Connection, product: ProductSchema):
    conn.execute(
        "INSERT INTO products_raw (product) VALUES (%s)",
        (Json(product),)
)