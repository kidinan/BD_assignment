import duckdb
import pandas as pd
from sqlalchemy import create_engine

def process_data_with_duckdb():
    # Load the cleaned e-commerce data using DuckDB
    con = duckdb.connect(database=':memory:')
    ecommerce_data = pd.read_csv('C:/Users/a/Desktop/BD assignment/data/processed/clean_data.csv')

    # Verify that data is loaded
    print("E-commerce data loaded:")
    print(ecommerce_data.head())

    # Create table and process data with DuckDB
    con.execute("""
        CREATE TABLE ecommerce_data AS SELECT * FROM ecommerce_data;
    """)
    processed_data = con.execute("""
        SELECT
            user_id AS customer_id,
            customer_age,
            location,
            account_age_days,
            transaction_id AS order_id,
            transaction_date1 AS order_date,
            transaction_amount AS total_amount,
            quantity,
            transaction_amount AS price,
            merchant_category AS product_category,
            device_type
        FROM
            ecommerce_data
    """).fetchdf()

    # Verify the processed data
    print("Processed data:")
    print(processed_data.head())

    return processed_data

def clean_and_load_data(processed_data):
    # Create a mapping for product categories to integer IDs
    product_categories = processed_data['product_category'].unique()
    product_category_map = {category: idx + 1 for idx, category in enumerate(product_categories)}
    
    # Map product categories to integer IDs
    processed_data['product_id'] = processed_data['product_category'].map(product_category_map)

    # Verify the product category mapping
    print("Product category mapping:")
    print(product_category_map)

    # Remove duplicate customer_id values
    customers_data = processed_data[['customer_id', 'customer_age', 'location', 'account_age_days']].drop_duplicates(subset=['customer_id'])
    
    # Remove duplicates for other tables
    orders_data = processed_data[['order_id', 'customer_id', 'order_date', 'total_amount']].drop_duplicates(subset=['order_id'])
    products_data = pd.DataFrame(product_category_map.items(), columns=['merchant_category', 'product_id'])
    order_items_data = processed_data[['order_id', 'product_id', 'quantity', 'price']].drop_duplicates(subset=['order_id', 'product_id'])

    # Verify the data before loading into PostgreSQL
    print("Customers data:")
    print(customers_data.head())
    print("Orders data:")
    print(orders_data.head())
    print("Products data:")
    print(products_data.head())
    print("Order items data:")
    print(order_items_data.head())

    # Database connection string for PostgreSQL
    engine = create_engine('postgresql+psycopg2://postgres:your_password@localhost:5432/new_ecommerce_db')

    # Insert the data into PostgreSQL tables
    with engine.connect() as conn:
        # Insert cleaned data into PostgreSQL tables
        customers_data.to_sql('customers', conn, if_exists='append', index=False)
        orders_data.to_sql('orders', conn, if_exists='append', index=False)
        products_data.to_sql('products', conn, if_exists='append', index=False)
        order_items_data.to_sql('order_items', conn, if_exists='append', index=False)

    print('Data successfully loaded into PostgreSQL!')

if __name__ == "__main__":
    processed_data = process_data_with_duckdb()
    clean_and_load_data(processed_data)
